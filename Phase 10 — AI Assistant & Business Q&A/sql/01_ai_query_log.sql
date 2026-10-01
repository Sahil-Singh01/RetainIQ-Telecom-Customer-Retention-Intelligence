USE retainiq;

CREATE TABLE IF NOT EXISTS ai_query_log (
    query_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    question_text TEXT NOT NULL,
    answer_mode VARCHAR(100) NOT NULL,
    answer_text LONGTEXT,
    evidence_ids TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;
