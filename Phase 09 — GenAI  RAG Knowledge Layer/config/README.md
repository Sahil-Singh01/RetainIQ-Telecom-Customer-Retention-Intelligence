# Phase 9 configuration

`rag_parameters.csv` controls chunking, retrieval, embeddings, and the optional LLM endpoint.

`rag_sample_questions.csv` provides repeatable retrieval/evidence checks. The expected topics are used only for lightweight retrieval evaluation; they are not a substitute for human answer-quality review.

The default LLM mode is disabled so the knowledge and retrieval layer can be completed without an API key or hosted model. To enable generation, set `llm_enabled` to `true` and configure an OpenAI-compatible endpoint and model, or set the corresponding environment variables used in Notebook 9.4.
