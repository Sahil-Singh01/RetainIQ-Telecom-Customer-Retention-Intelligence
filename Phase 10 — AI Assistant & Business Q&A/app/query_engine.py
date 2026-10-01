from __future__ import annotations

import json
import os
from functools import lru_cache
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

try:
    import requests
except Exception:  # pragma: no cover
    requests = None

try:
    import mysql.connector
except Exception:  # pragma: no cover
    mysql = None


# =====================================================================
# PROJECT PATHS
# =====================================================================
# =====================================================================
# PROJECT PATHS
# =====================================================================

PHASE10_ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = PHASE10_ROOT.parent


def _has_phase9_assets(folder: Path) -> bool:
    """Check whether a folder contains the required Phase 9 RAG assets."""

    output_dir = folder / "outputs"

    required_files = [
        output_dir / "retrieval_chunks.csv",
        output_dir / "retrieval_vectors.npy",
        output_dir / "retrieval_manifest.json",
    ]

    return all(path.exists() for path in required_files)


def _resolve_phase9_dir() -> Path:
    """
    Find the Phase 9 directory without relying on an exact
    Unicode folder name.
    """

    # -------------------------------------------------------------
    # 1. Explicit environment variable
    # -------------------------------------------------------------

    env_path = os.getenv("RETAINIQ_PHASE9_DIR")

    if env_path:
        env_candidate = Path(env_path).expanduser().resolve()

        if _has_phase9_assets(env_candidate):
            return env_candidate

    # -------------------------------------------------------------
    # 2. Search sibling directories of Phase 10
    # -------------------------------------------------------------

    sibling_dirs = [
        path
        for path in PROJECT_ROOT.iterdir()
        if path.is_dir()
        and path.name.lower().startswith("phase 9")
    ]

    for candidate in sibling_dirs:

        if _has_phase9_assets(candidate):
            return candidate

    # -------------------------------------------------------------
    # 3. Search current working directory
    # -------------------------------------------------------------

    cwd = Path.cwd().resolve()

    search_roots = [
        cwd,
        cwd.parent,
        cwd.parent.parent,
    ]

    for root in search_roots:

        if not root.exists():
            continue

        try:
            candidates = [
                path
                for path in root.iterdir()
                if path.is_dir()
                and path.name.lower().startswith("phase 9")
            ]
        except OSError:
            continue

        for candidate in candidates:

            if _has_phase9_assets(candidate):
                return candidate

    # -------------------------------------------------------------
    # 4. Nothing found → provide a clear error
    # -------------------------------------------------------------

    raise FileNotFoundError(
        "Could not locate the Phase 9 RAG assets.\n\n"
        "Expected files:\n"
        "  Phase 9*/outputs/retrieval_chunks.csv\n"
        "  Phase 9*/outputs/retrieval_vectors.npy\n"
        "  Phase 9*/outputs/retrieval_manifest.json\n\n"
        f"Project root searched:\n{PROJECT_ROOT}"
    )


PHASE9_DIR = _resolve_phase9_dir()

OUTPUT_DIR = PHASE9_DIR / "outputs"
CONFIG_DIR = PHASE9_DIR / "config"


# =====================================================================
# CONFIGURATION
# =====================================================================

def _load_parameters() -> dict[str, str]:
    """
    Load Phase 9 RAG parameters.

    The CSV values are normalized to strings and blank/NaN values
    are ignored.
    """

    path = CONFIG_DIR / "rag_parameters.csv"

    defaults = {
        "top_k": "5",
        "comparison_candidate_k": "20",
        "similarity_floor": "0.20",
        "llm_enabled": "true",
        "llm_base_url": "http://localhost:11434/v1",
        "llm_model": "qwen3:4b",
    }

    if not path.exists():
        return defaults

    df = pd.read_csv(path)

    if "parameter" not in df.columns or "value" not in df.columns:
        return defaults

    parameters = defaults.copy()

    for key, value in zip(df["parameter"], df["value"]):
        if pd.isna(value):
            continue

        key = str(key).strip()
        value = str(value).strip()

        if key:
            parameters[key] = value

    return parameters


PARAMETERS = _load_parameters()


# =====================================================================
# PHASE 9 ASSET LOADING
# =====================================================================

def _load_phase9_assets() -> tuple[pd.DataFrame, np.ndarray, dict[str, Any]]:
    """
    Load the Phase 9 retrieval artifacts.

    Required:
        outputs/retrieval_chunks.csv
        outputs/retrieval_vectors.npy
        outputs/retrieval_manifest.json
    """

    chunks_path = OUTPUT_DIR / "retrieval_chunks.csv"
    vectors_path = OUTPUT_DIR / "retrieval_vectors.npy"
    manifest_path = OUTPUT_DIR / "retrieval_manifest.json"

    missing_files = [
        str(path)
        for path in [
            chunks_path,
            vectors_path,
            manifest_path,
        ]
        if not path.exists()
    ]

    if missing_files:
        raise FileNotFoundError(
            "RetainIQ could not locate the required Phase 9 retrieval assets.\n\n"
            f"Resolved Phase 9 directory:\n{PHASE9_DIR}\n\n"
            f"Resolved outputs directory:\n{OUTPUT_DIR}\n\n"
            "Missing files:\n"
            + "\n".join(missing_files)
            + "\n\n"
            "Expected structure:\n"
            f"{PHASE9_DIR}\\outputs\\retrieval_chunks.csv\n"
            f"{PHASE9_DIR}\\outputs\\retrieval_vectors.npy\n"
            f"{PHASE9_DIR}\\outputs\\retrieval_manifest.json"
        )

    chunks = pd.read_csv(chunks_path)
    vectors = np.load(vectors_path)

    manifest = json.loads(
        manifest_path.read_text(encoding="utf-8")
    )

    if len(chunks) != len(vectors):
        raise ValueError(
            "Chunk/vector mismatch: "
            f"{len(chunks)} chunks vs {len(vectors)} vectors."
        )

    required_columns = {
        "chunk_text",
        "document_id",
        "source_name",
        "topic",
    }

    missing_columns = required_columns.difference(chunks.columns)

    if missing_columns:
        raise ValueError(
            "retrieval_chunks.csv is missing required columns: "
            + ", ".join(sorted(missing_columns))
        )

    return chunks, vectors, manifest


CHUNKS_DF, VECTORS, MANIFEST = _load_phase9_assets()


# =====================================================================
# QUERY VECTORISATION
# =====================================================================

@lru_cache(maxsize=1)
def _load_embedding_model():
    """
    Load the SentenceTransformer model once and reuse it.

    This avoids reloading the model for every user question.
    """

    from sentence_transformers import SentenceTransformer

    model_name = MANIFEST.get(
        "embedding_model",
        PARAMETERS.get(
            "embedding_model",
            "all-MiniLM-L6-v2",
        ),
    )

    return SentenceTransformer(model_name)


@lru_cache(maxsize=1)
def _load_tfidf_vectorizer():
    """
    Load the Phase 9 TF-IDF vectorizer when TF-IDF is being used.
    """

    import joblib

    vectorizer_path = OUTPUT_DIR / "tfidf_vectorizer.joblib"

    if not vectorizer_path.exists():
        raise FileNotFoundError(
            f"TF-IDF vectorizer not found at: {vectorizer_path}"
        )

    return joblib.load(vectorizer_path)


def _vectorize_query(query: str) -> np.ndarray:
    """
    Convert a query into the same vector space used by Phase 9.
    """

    query = str(query).strip()

    if not query:
        raise ValueError("Query cannot be empty.")

    backend = str(
        MANIFEST.get("backend", "")
    ).strip().lower()

    if backend == "sentence_transformers":
        model = _load_embedding_model()

        vector = model.encode(
            [query],
            normalize_embeddings=True,
            show_progress_bar=False,
        )[0]

        return np.asarray(
            vector,
            dtype=np.float32,
        )

    if backend == "tfidf":
        vectorizer = _load_tfidf_vectorizer()

        vector = vectorizer.transform(
            [query]
        ).toarray()[0]

        return np.asarray(
            vector,
            dtype=np.float32,
        )

    raise ValueError(
        f"Unsupported retrieval backend: {backend}"
    )


# =====================================================================
# SIMILARITY
# =====================================================================

def _cosine_scores(
    query_vector: np.ndarray,
) -> np.ndarray:
    """
    Calculate cosine similarity between the query vector
    and every stored retrieval vector.
    """

    query_vector = np.asarray(
        query_vector,
        dtype=np.float32,
    )

    vectors = np.asarray(
        VECTORS,
        dtype=np.float32,
    )

    if vectors.ndim != 2:
        raise ValueError(
            f"Expected a 2D vector matrix, got shape {vectors.shape}."
        )

    if vectors.shape[1] != query_vector.shape[0]:
        raise ValueError(
            "Query/vector dimensionality mismatch: "
            f"query={query_vector.shape[0]}, "
            f"vectors={vectors.shape[1]}"
        )

    denominator = (
        np.linalg.norm(vectors, axis=1)
        * np.linalg.norm(query_vector)
    )

    denominator = np.where(
        denominator == 0,
        1.0,
        denominator,
    )

    return (
        vectors @ query_vector
    ) / denominator


# =====================================================================
# QUERY TYPE DETECTION
# =====================================================================

def is_comparison_query(query: str) -> bool:
    """
    Identify questions that benefit from broader/diversified retrieval.
    """

    q = str(query).lower()

    markers = [
        "highest",
        "lowest",
        "largest",
        "smallest",
        "top ",
        "bottom ",
        "compare",
        "versus",
        " vs ",
        "difference",
        "more than",
        "less than",
    ]

    return any(
        marker in q
        for marker in markers
    )


# =====================================================================
# RETRIEVAL
# =====================================================================

def retrieve(
    query: str,
    top_k: int | None = None,
) -> pd.DataFrame:
    """
    Retrieve relevant evidence.

    Normal question:
        top_k → direct semantic retrieval

    Comparison question:
        broader candidate pool → diversified evidence
    """

    query = str(query).strip()

    if not query:
        raise ValueError("Query cannot be empty.")

    top_k = int(
        top_k
        or PARAMETERS.get("top_k", "5")
    )

    if top_k <= 0:
        raise ValueError(
            "top_k must be greater than zero."
        )

    comparison = is_comparison_query(query)

    comparison_candidate_k = int(
        PARAMETERS.get(
            "comparison_candidate_k",
            "20",
        )
    )

    candidate_k = (
        max(top_k, comparison_candidate_k)
        if comparison
        else top_k
    )

    # Convert query to the stored vector space.
    query_vector = _vectorize_query(query)

    # Similarity against every stored vector.
    scores = _cosine_scores(query_vector)

    # Select the highest-scoring candidates.
    candidate_k = min(
        candidate_k,
        len(CHUNKS_DF),
    )

    order = np.argsort(
        -scores
    )[:candidate_k]

    candidates = CHUNKS_DF.iloc[
        order
    ].copy()

    candidates["similarity"] = scores[
        order
    ]

    candidates["rank"] = np.arange(
        1,
        len(candidates) + 1,
    )

    # Remove extremely weak matches.
    similarity_floor = float(
        PARAMETERS.get(
            "similarity_floor",
            "0.20",
        )
    )

    candidates = candidates[
        candidates["similarity"] >= similarity_floor
    ].copy()

    # -------------------------------------------------------------
    # Comparison-aware diversification
    # -------------------------------------------------------------

    if comparison:
        candidates = candidates.reset_index(
            drop=False
        )

        original_index_column = "index"

        selected_indices: list[int] = []
        seen_documents: set[str] = set()

        # Highest similarity first.
        candidates = candidates.sort_values(
            "similarity",
            ascending=False,
        )

        for _, row in candidates.iterrows():
            document_id = str(
                row["document_id"]
            )

            if document_id in seen_documents:
                continue

            selected_indices.append(
                int(row[original_index_column])
            )

            seen_documents.add(
                document_id
            )

            if len(selected_indices) >= top_k:
                break

        # If enough unique documents are not available,
        # fill the remaining slots with the best candidates.
        if len(selected_indices) < top_k:
            selected_set = set(selected_indices)

            for idx in candidates[
                original_index_column
            ].tolist():
                idx = int(idx)

                if idx in selected_set:
                    continue

                selected_indices.append(idx)

                if len(selected_indices) >= top_k:
                    break

        if selected_indices:
            result = CHUNKS_DF.iloc[
                selected_indices
            ].copy()

            # Recalculate similarity/rank in the final output.
            result["similarity"] = [
                float(
                    _cosine_scores(query_vector)[
                        idx
                    ]
                )
                for idx in selected_indices
            ]

            result = result.sort_values(
                "similarity",
                ascending=False,
            ).head(top_k)

        else:
            result = CHUNKS_DF.iloc[
                order[:top_k]
            ].copy()

            result["similarity"] = scores[
                order[:top_k]
            ]

    else:
        result = candidates.head(
            top_k
        ).copy()

    # Final rank after all filtering/diversification.
    result = result.reset_index(
        drop=True
    )

    result["rank"] = np.arange(
        1,
        len(result) + 1,
    )

    result["evidence_id"] = [
        f"[{i}]"
        for i in range(
            1,
            len(result) + 1,
        )
    ]

    return result


# =====================================================================
# MYSQL CONNECTION
# =====================================================================

def get_mysql_connection(
    password: str | None = None,
):
    """
    Connect to the RetainIQ MySQL database.

    Password can be supplied directly or through:
        RETAINIQ_MYSQL_PASSWORD
    """

    if mysql is None:
        raise RuntimeError(
            "mysql-connector-python is not installed."
        )

    resolved_password = (
        password
        if password is not None
        else os.getenv(
            "RETAINIQ_MYSQL_PASSWORD"
        )
    )

    if resolved_password is None:
        raise RuntimeError(
            "Set RETAINIQ_MYSQL_PASSWORD "
            "or provide a MySQL password explicitly."
        )

    return mysql.connector.connect(
        host=os.getenv(
            "RETAINIQ_MYSQL_HOST",
            "localhost",
        ),
        port=int(
            os.getenv(
                "RETAINIQ_MYSQL_PORT",
                "3306",
            )
        ),
        user=os.getenv(
            "RETAINIQ_MYSQL_USER",
            "retainiq_user",
        ),
        password=resolved_password,
        database=os.getenv(
            "RETAINIQ_MYSQL_DATABASE",
            "retainiq",
        ),
    )


# =====================================================================
# SQL EVIDENCE ROUTING
# =====================================================================

def sql_evidence(
    query: str,
    password: str | None = None,
) -> pd.DataFrame | None:
    """
    Route selected exact-metric/comparison questions to MySQL.

    Returns:
        DataFrame with SQL evidence,
        or None if the question does not match a supported SQL route.
    """

    q = str(query).lower().strip()

    sql = None
    topic = None

    # -------------------------------------------------------------
    # Overall churn
    # -------------------------------------------------------------

    if (
        "overall churn" in q
        or (
            "churn rate" in q
            and "city" not in q
            and "segment" not in q
        )
    ):
        sql = """
            SELECT
                COUNT(*) AS customers,
                SUM(
                    CASE
                        WHEN churn_label = 'Yes'
                        THEN 1
                        ELSE 0
                    END
                ) AS churned_customers,
                ROUND(
                    SUM(
                        CASE
                            WHEN churn_label = 'Yes'
                            THEN 1
                            ELSE 0
                        END
                    ) / COUNT(*) * 100,
                    2
                ) AS churn_rate_pct
            FROM fact_customer_status
        """

        topic = "sql_portfolio_metric"

    # -------------------------------------------------------------
    # Highest segment revenue at risk
    # -------------------------------------------------------------

    elif (
        "highest" in q
        and "revenue at risk" in q
        and "segment" in q
    ):
        sql = """
            SELECT
                segment_name,
                customers,
                churned_customers,
                avg_cltv,
                revenue_at_risk,
                churn_rate_pct
            FROM vw_segment_retention_summary
            ORDER BY revenue_at_risk DESC
            LIMIT 10
        """

        topic = "sql_segment_comparison"

    # -------------------------------------------------------------
    # Highest market revenue at risk
    # -------------------------------------------------------------

    elif (
        "highest" in q
        and "revenue at risk" in q
    ):
        sql = """
            SELECT
                state,
                city,
                customers,
                churned_customers,
                churn_rate_pct,
                avg_cltv,
                revenue_at_risk
            FROM vw_market_retention
            WHERE customers >= 25
            ORDER BY revenue_at_risk DESC
            LIMIT 10
        """

        topic = "sql_market_comparison"

    # No SQL route available.
    if sql is None:
        return None

    conn = get_mysql_connection(
        password
    )

    cursor = conn.cursor(
        dictionary=True
    )

    try:
        cursor.execute(sql)

        rows = cursor.fetchall()

        df = pd.DataFrame(rows)

        if df.empty:
            return None

        df["source_name"] = topic
        df["topic"] = topic

        df["evidence_id"] = [
            f"[SQL{i}]"
            for i in range(
                1,
                len(df) + 1,
            )
        ]

        return df

    finally:
        cursor.close()
        conn.close()


# =====================================================================
# GROUNDED CONTEXT
# =====================================================================

def build_grounded_context(
    retrieved: pd.DataFrame,
    sql_df: pd.DataFrame | None = None,
) -> str:
    """
    Build the evidence block passed to the LLM.

    SQL evidence is placed first because it is directly computed
    from structured MySQL reporting data.
    """

    blocks: list[str] = []

    # -------------------------------------------------------------
    # SQL evidence
    # -------------------------------------------------------------

    if (
        sql_df is not None
        and not sql_df.empty
    ):
        for row in sql_df.itertuples(
            index=False
        ):
            payload = row._asdict()

            blocks.append(
                f"{payload['evidence_id']} "
                f"Source={payload['source_name']} | "
                f"Topic={payload['topic']}\n"
                f"{payload}"
            )

    # -------------------------------------------------------------
    # Semantic retrieval evidence
    # -------------------------------------------------------------

    if (
        retrieved is not None
        and not retrieved.empty
    ):
        for row in retrieved.itertuples(
            index=False
        ):
            blocks.append(
                f"{row.evidence_id} "
                f"Source={row.source_name} | "
                f"Topic={row.topic} | "
                f"Similarity={row.similarity:.3f}\n"
                f"{row.chunk_text}"
            )

    return "\n\n".join(
        blocks
    )


# =====================================================================
# LLM CALL
# =====================================================================

def call_llm(
    query: str,
    context: str,
) -> str:
    """
    Send the grounded context to the configured LLM endpoint.
    """

    if requests is None:
        raise RuntimeError(
            "The requests package is not installed."
        )

    base_url = os.getenv(
        "RETAINIQ_RAG_LLM_BASE_URL"
    )

    if not base_url:
        base_url = PARAMETERS.get(
            "llm_base_url",
            "http://localhost:11434/v1",
        )

    base_url = (
        str(base_url)
        .strip()
        .rstrip("/")
    )

    model = os.getenv(
        "RETAINIQ_RAG_LLM_MODEL"
    )

    if not model:
        model = PARAMETERS.get(
            "llm_model",
            "qwen3:4b",
        )

    if pd.isna(model):
        model = ""

    model = str(
        model
    ).strip()

    if not model:
        raise RuntimeError(
            "No LLM model is configured."
        )

    system_prompt = (
        "You are the RetainIQ business analytics assistant. "
        "Answer only from the supplied evidence. "
        "Distinguish observed metrics, calculations, and assumptions. "
        "Do not invent missing values. "
        "Cite evidence IDs exactly as supplied. "
        "For comparison questions, only claim a winner when "
        "the evidence contains a comparable set. "
        "If the evidence is insufficient, say so clearly. "
        "Do not present scenario assumptions as forecasts."
    )

    user_prompt = (
        f"Question:\n{query}\n\n"
        f"Evidence:\n{context}"
    )

    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": user_prompt,
            },
        ],
        "temperature": 0.2,
        "stream": False,
    }

    response = requests.post(
        f"{base_url}/chat/completions",
        json=payload,
        timeout=180,
    )

    if not response.ok:
        raise RuntimeError(
            f"LLM HTTP {response.status_code}: "
            f"{response.text}"
        )

    data = response.json()

    try:
        return data[
            "choices"
        ][0][
            "message"
        ][
            "content"
        ]

    except (
        KeyError,
        IndexError,
        TypeError,
    ) as exc:
        raise RuntimeError(
            f"Unexpected LLM response format: {data}"
        ) from exc


# =====================================================================
# MAIN QUERY FUNCTION
# =====================================================================

def answer_query(
    query: str,
    mysql_password: str | None = None,
    top_k: int | None = None,
) -> dict[str, Any]:
    """
    Main RetainIQ query pipeline.

    Flow:
        User question
            ↓
        Semantic retrieval
            ↓
        Optional SQL evidence
            ↓
        Grounded context
            ↓
        Qwen / configured LLM
            ↓
        Answer + evidence
    """

    query = str(query).strip()

    if not query:
        raise ValueError(
            "Query cannot be empty."
        )

    # -------------------------------------------------------------
    # Retrieval
    # -------------------------------------------------------------

    retrieved = retrieve(
        query,
        top_k=top_k,
    )

    # -------------------------------------------------------------
    # Structured SQL evidence
    # -------------------------------------------------------------

    sql_df = None

    try:
        sql_df = sql_evidence(
            query,
            mysql_password,
        )
    except Exception:
        # SQL evidence is supplementary.
        # Retrieval should continue even if MySQL
        # credentials are not supplied.
        sql_df = None

    # -------------------------------------------------------------
    # Grounded context
    # -------------------------------------------------------------

    context = build_grounded_context(
        retrieved,
        sql_df,
    )

    if not context.strip():
        raise RuntimeError(
            "No evidence was retrieved for this question."
        )

    # -------------------------------------------------------------
    # LLM configuration
    # -------------------------------------------------------------

    llm_enabled = (
        str(
            os.getenv(
                "RETAINIQ_RAG_LLM_ENABLED",
                PARAMETERS.get(
                    "llm_enabled",
                    "true",
                ),
            )
        )
        .strip()
        .lower()
        == "true"
    )

    model = os.getenv(
        "RETAINIQ_RAG_LLM_MODEL"
    )

    if not model:
        model = PARAMETERS.get(
            "llm_model",
            "qwen3:4b",
        )

    if pd.isna(model):
        model = ""

    model = str(
        model
    ).strip()

    # -------------------------------------------------------------
    # LLM generation
    # -------------------------------------------------------------

    mode = "retrieval_only"

    if llm_enabled and model:
        try:
            answer = call_llm(
                query,
                context,
            )

            mode = "llm"

        except Exception as exc:
            answer = (
                "I could not generate a model answer "
                "from the available evidence.\n\n"
                f"Generation error: {type(exc).__name__}\n\n"
                f"Retrieved evidence:\n{context}"
            )

            mode = (
                f"retrieval_fallback_"
                f"{type(exc).__name__}"
            )

    else:
        answer = context

    # -------------------------------------------------------------
    # Final response object
    # -------------------------------------------------------------

    return {
        "question": query,
        "answer": answer,
        "mode": mode,
        "retrieved": retrieved,
        "sql_evidence": sql_df,
        "context": context,
    }