# RetainIQ — Phase 9: GenAI / RAG Knowledge Layer

## Objective

I turn the Phase 6–8 analytical outputs into a grounded retrieval-augmented knowledge layer. The purpose is to make the RetainIQ project queryable in natural language without losing the traceability of the underlying business evidence.

## Notebook sequence

1. `01_knowledge_source_inventory_and_corpus.ipynb`
2. `02_chunking_and_embedding_index.ipynb`
3. `03_retrieval_evaluation_and_grounded_context.ipynb`
4. `04_rag_answer_generation_and_mysql_publishing.ipynb`

## What Phase 9 adds

### 9.1 — Knowledge source inventory & corpus
I collect project evidence from Phase 6–8 MySQL reporting views and add a curated project-methodology reference. Every knowledge record keeps source and topic metadata.

### 9.2 — Chunking & embedding index
I split the corpus into overlapping chunks and build a semantic index with SentenceTransformers when available. A TF-IDF fallback keeps the pipeline executable when semantic embeddings are unavailable.

### 9.3 — Retrieval evaluation & grounded context
I test representative RetainIQ questions against the actual saved retrieval index, calculate lightweight retrieval diagnostics, and generate an evidence context pack with traceable chunk identifiers.

### 9.4 — RAG answer generation & MySQL publishing
I connect retrieval to an optional OpenAI-compatible generation endpoint. Answers are instructed to stay within retrieved project evidence and cite evidence identifiers. When no LLM is configured, the notebook returns transparent retrieval-only evidence. Knowledge metadata and query logs are published to MySQL.

## Core RAG flow

`Question → Retrieval → Grounded Context → Optional LLM → Evidence-cited Answer`

## Main outputs

- `knowledge_documents.csv`
- `knowledge_source_inventory.csv`
- `retrieval_chunks.csv`
- `retrieval_vectors.npy`
- `retrieval_manifest.json`
- `retrieval_evaluation.csv`
- `sample_retrieval_results.csv`
- `grounded_context_example.md`
- `rag_demo_answers.csv`
- `tfidf_vectorizer.joblib` when the TF-IDF fallback is used

## MySQL outputs

- `rag_knowledge_documents`
- `rag_query_log`
- `vw_rag_knowledge_catalog`
- `vw_rag_query_log`

## Execution order

1. Complete Phase 7.
2. Complete Phase 8.
3. Run Notebook 9.1.
4. Run Notebook 9.2.
5. Run Notebook 9.3.
6. Run Notebook 9.4.

## LLM configuration

The default `llm_enabled` value is `false`. This means the complete knowledge and retrieval layer can be built without a hosted LLM.

To enable generation, configure an OpenAI-compatible endpoint using the environment variables read by Notebook 9.4:

- `RETAINIQ_RAG_LLM_ENABLED=true`
- `RETAINIQ_RAG_LLM_BASE_URL=<endpoint>/v1`
- `RETAINIQ_RAG_LLM_MODEL=<model name>`

The notebook treats generation as optional and falls back to retrieved evidence when the endpoint is disabled or unavailable.

## Important interpretation rules

- Revenue at risk remains a historical exposure proxy, not a forecast.
- Priority scores depend on explicit business assumptions.
- Benchmark gaps are descriptive comparisons.
- Geographic patterns are descriptive and do not establish causation.
- External benchmark comparisons require explicit comparable source metadata.
- The RAG assistant should say when the retrieved evidence is insufficient.

## Requirements

- pandas
- numpy
- scikit-learn
- sentence-transformers
- joblib
- requests
- mysql-connector-python
- jupyter
