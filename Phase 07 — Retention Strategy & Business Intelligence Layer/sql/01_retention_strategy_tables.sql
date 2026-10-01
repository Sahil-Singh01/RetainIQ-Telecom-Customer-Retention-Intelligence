USE retainiq;

CREATE TABLE IF NOT EXISTS retention_strategy_priority (
    priority_id BIGINT NOT NULL AUTO_INCREMENT,
    scope VARCHAR(20) NOT NULL,
    entity_name VARCHAR(220) NOT NULL,
    state VARCHAR(100) NULL,
    city VARCHAR(150) NULL,
    segment_name VARCHAR(120) NULL,
    retention_profile VARCHAR(60) NULL,
    customers INT NOT NULL,
    churn_rate_pct DECIMAL(8,2) NULL,
    avg_cltv DECIMAL(14,2) NULL,
    revenue_at_risk DECIMAL(16,2) NOT NULL,
    ease_of_intervention_score DECIMAL(6,2) NULL,
    priority_score DECIMAL(18,2) NOT NULL,
    priority_basis VARCHAR(120) NOT NULL,
    action_theme VARCHAR(180) NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (priority_id),
    INDEX idx_priority_scope (scope),
    INDEX idx_priority_score (priority_score),
    INDEX idx_priority_revenue (revenue_at_risk)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS retention_impact_scenarios (
    scenario_id BIGINT NOT NULL AUTO_INCREMENT,
    scope VARCHAR(20) NOT NULL,
    entity_name VARCHAR(220) NOT NULL,
    revenue_at_risk DECIMAL(16,2) NOT NULL,
    recovery_rate_pct DECIMAL(8,2) NOT NULL,
    estimated_recovered_revenue DECIMAL(16,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (scenario_id),
    INDEX idx_scenario_scope (scope),
    INDEX idx_scenario_recovery (recovery_rate_pct)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS retention_action_framework (
    segment_id INT NOT NULL,
    segment_name VARCHAR(120) NOT NULL,
    retention_profile VARCHAR(60) NOT NULL,
    customers INT NOT NULL,
    avg_cltv DECIMAL(14,2) NULL,
    churn_rate_pct DECIMAL(8,2) NULL,
    revenue_at_risk DECIMAL(16,2) NOT NULL,
    priority_score DECIMAL(18,2) NOT NULL,
    action_theme VARCHAR(180) NOT NULL,
    action_description TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (segment_id)
) ENGINE=InnoDB;
