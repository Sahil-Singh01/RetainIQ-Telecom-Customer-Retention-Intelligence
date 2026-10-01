# RetainIQ — Phase 10: AI Assistant & Business Q&A

## Objective

I turn the Phase 9 RAG pipeline into a reusable local AI assistant for RetainIQ. The assistant uses a hybrid approach:

- RAG retrieval for definitions, methodology, business context, geography, strategy, and benchmark evidence.
- Structured MySQL queries for questions that require exact portfolio metrics or comparisons.
- Ollama + Qwen3 4B for grounded answer generation.
- Evidence IDs and source metadata in every answer.
- Optional query logging to MySQL.

This phase also addresses the retrieval-completeness issue observed in Phase 9 for comparison questions such as “which segment has the highest revenue at risk?” by using broader candidate retrieval and source-record diversification, with SQL routing for exact comparison queries.

## Notebooks

1. `01_assistant_backend_and_hybrid_query_router.ipynb` — reusable query engine, routing, RAG/SQL evidence preparation, and grounded generation tests.
2. `02_comparison_aware_retrieval_and_evaluation.ipynb` — comparison-aware retrieval and evaluation of questions containing highest/lowest/top/compare language.
3. `03_conversation_history_and_evidence_validation.ipynb` — multi-turn context, citation validation, answer evidence checks, and query-log preparation.
4. `04_streamlit_app_integration_and_testing.ipynb` — end-to-end application smoke tests and deployment readiness checks.

## App

- `app/query_engine.py` — reusable hybrid RAG + SQL backend.
- `app/streamlit_app.py` — local Streamlit chat interface with expandable evidence.

## Run order

1. Complete Phase 9 and confirm its outputs exist.
2. Make sure MySQL has the Phase 3/6/7/8 reporting views used by the engine.
3. Run `ollama list` and confirm `qwen3:4b` exists.
4. Keep Ollama available locally at `http://localhost:11434`.
5. Run the four Phase 10 notebooks in order.
6. Start the app with:

```bash
streamlit run app/streamlit_app.py
```

## Phase 9 location

By default, the app looks for Phase 9 as a sibling directory named:

`Phase 9 — GenAI RAG Knowledge Layer`

You can override this with the environment variable `RETAINIQ_PHASE9_DIR`.

## Important interpretation rule

The assistant must distinguish observed metrics, reproducible calculations, scenario assumptions, and limitations. It must not invent figures when the retrieved or queried evidence is insufficient.
