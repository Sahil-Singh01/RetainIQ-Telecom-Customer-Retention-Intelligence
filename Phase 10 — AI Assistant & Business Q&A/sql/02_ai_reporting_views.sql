USE retainiq;

CREATE OR REPLACE VIEW vw_ai_query_log AS
SELECT query_id, question_text, answer_mode, answer_text, evidence_ids, created_at
FROM ai_query_log;
