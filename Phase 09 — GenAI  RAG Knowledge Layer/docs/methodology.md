# Phase 9 methodology

## 1. Knowledge corpus
The corpus is assembled from the reporting views created in Phases 6–8 and from a curated RetainIQ methodology reference. Every record retains source and topic metadata.

## 2. Chunking
Long records are normalized and divided into overlapping chunks. Default configuration is 900 characters with 150 characters of overlap.

## 3. Retrieval
The preferred backend is SentenceTransformers with `all-MiniLM-L6-v2`. A TF-IDF fallback is available so the pipeline can still be executed when the embedding dependency or model is unavailable. The active backend is recorded in `retrieval_manifest.json`.

## 4. Retrieval evaluation
Sample questions are checked using expected topic labels. Hit@5 and mean reciprocal rank indicate whether relevant evidence types are being surfaced. This is a lightweight retrieval diagnostic, not a complete answer-quality benchmark.

## 5. Grounded generation
Retrieved chunks are passed to an optional OpenAI-compatible chat-completions endpoint. The prompt instructs the model to use only supplied project evidence, avoid invented values, distinguish assumptions from observed values, and cite evidence identifiers.

## 6. Fallback behavior
When generation is disabled or unavailable, the notebook returns the retrieved evidence directly. This keeps the pipeline transparent and prevents fabricated answers from being treated as project findings.

## 7. MySQL publishing
Chunk metadata and demo query logs are persisted in MySQL. Embedding vectors remain local file artifacts because they are intended for retrieval rather than BI aggregation.

## 8. Interpretation safeguards
The RAG layer must preserve prior-phase definitions: revenue at risk is historical exposure, priority scores depend on subjective intervention assumptions, benchmark gaps are descriptive, and geography does not establish causation.
