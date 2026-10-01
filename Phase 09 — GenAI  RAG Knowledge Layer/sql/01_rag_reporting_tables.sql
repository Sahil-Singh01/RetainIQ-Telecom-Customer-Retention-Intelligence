USE retainiq;

CREATE TABLE IF NOT EXISTS rag_knowledge_documents (
    chunk_id VARCHAR(255) PRIMARY KEY,
    document_id VARCHAR(255) NOT NULL,
    source_name VARCHAR(255) NOT NULL,
    source_type VARCHAR(120) NOT NULL,
    topic VARCHAR(80) NOT NULL,
    chunk_number INT NOT NULL,
    chunk_text MEDIUMTEXT NOT NULL
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS rag_query_log (
    query_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    question_id VARCHAR(40) NULL,
    question_text TEXT NOT NULL,
    answer_mode VARCHAR(80) NOT NULL,
    answer_text MEDIUMTEXT NOT NULL,
    evidence_ids VARCHAR(1000) NULL,
    top_sources VARCHAR(2000) NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;
