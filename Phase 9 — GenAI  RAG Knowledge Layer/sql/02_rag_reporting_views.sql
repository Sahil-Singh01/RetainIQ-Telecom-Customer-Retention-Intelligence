USE retainiq;

CREATE OR REPLACE VIEW vw_rag_knowledge_catalog AS
SELECT chunk_id, document_id, source_name, source_type, topic, chunk_number, chunk_text
FROM rag_knowledge_documents;

CREATE OR REPLACE VIEW vw_rag_query_log AS
SELECT query_id, question_id, question_text, answer_mode, answer_text, evidence_ids, top_sources, created_at
FROM rag_query_log;
