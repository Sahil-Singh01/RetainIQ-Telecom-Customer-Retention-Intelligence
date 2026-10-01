USE retainiq;

CREATE TABLE IF NOT EXISTS benchmark_reference (
    benchmark_scope VARCHAR(30) NOT NULL,
    benchmark_name VARCHAR(160) NOT NULL,
    metric VARCHAR(80) NOT NULL,
    benchmark_value DECIMAL(18,6) NULL,
    unit VARCHAR(80) NULL,
    source VARCHAR(255) NULL,
    source_date VARCHAR(50) NULL,
    population BIGINT NULL,
    notes TEXT NULL,
    PRIMARY KEY (benchmark_scope, benchmark_name, metric)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS segment_benchmark_gap (
    segment_id INT PRIMARY KEY,
    segment_name VARCHAR(120) NOT NULL,
    retention_profile VARCHAR(80) NULL,
    customers INT NOT NULL,
    churned_customers INT NOT NULL,
    churn_rate_pct DECIMAL(8,2) NULL,
    avg_cltv DECIMAL(14,2) NULL,
    revenue_at_risk DECIMAL(16,2) NOT NULL,
    revenue_at_risk_per_customer DECIMAL(16,4) NULL,
    churn_gap_pp DECIMAL(10,4) NULL,
    cltv_gap_pct DECIMAL(12,4) NULL,
    revenue_risk_per_customer_gap_pct DECIMAL(12,4) NULL,
    benchmark_status VARCHAR(40) NULL
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS state_benchmark_gap (
    state VARCHAR(100) PRIMARY KEY,
    customers INT NOT NULL,
    churned_customers INT NOT NULL,
    churn_rate_pct DECIMAL(8,2) NULL,
    avg_cltv DECIMAL(14,2) NULL,
    revenue_at_risk DECIMAL(16,2) NOT NULL,
    revenue_at_risk_per_customer DECIMAL(16,4) NULL,
    churn_gap_pp DECIMAL(10,4) NULL,
    cltv_gap_pct DECIMAL(12,4) NULL,
    revenue_risk_per_customer_gap_pct DECIMAL(12,4) NULL,
    benchmark_status VARCHAR(40) NULL
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS city_benchmark_gap (
    state VARCHAR(100) NOT NULL,
    city VARCHAR(150) NOT NULL,
    customers INT NOT NULL,
    churned_customers INT NOT NULL,
    churn_rate_pct DECIMAL(8,2) NULL,
    avg_cltv DECIMAL(14,2) NULL,
    revenue_at_risk DECIMAL(16,2) NOT NULL,
    revenue_at_risk_per_customer DECIMAL(16,4) NULL,
    churn_gap_to_portfolio_pp DECIMAL(10,4) NULL,
    churn_gap_to_peer_city_pp DECIMAL(10,4) NULL,
    cltv_gap_pct DECIMAL(12,4) NULL,
    revenue_risk_per_customer_gap_pct DECIMAL(12,4) NULL,
    benchmark_status VARCHAR(50) NULL,
    PRIMARY KEY (state, city)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS benchmark_gap_summary (
    entity_type VARCHAR(30) PRIMARY KEY,
    entities INT NOT NULL,
    above_benchmark INT NOT NULL,
    within_benchmark INT NOT NULL,
    below_benchmark INT NOT NULL
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS city_benchmark_management_view (
    state VARCHAR(100) NOT NULL,
    city VARCHAR(150) NOT NULL,
    customers INT NOT NULL,
    churn_rate_pct DECIMAL(8,2) NULL,
    revenue_at_risk DECIMAL(16,2) NOT NULL,
    churn_gap_to_portfolio_pp DECIMAL(10,4) NULL,
    churn_gap_to_peer_city_pp DECIMAL(10,4) NULL,
    revenue_at_risk_per_customer DECIMAL(16,4) NULL,
    exposure_band VARCHAR(40) NULL,
    benchmark_exposure_flag VARCHAR(80) NULL,
    PRIMARY KEY (state, city)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS segment_strategy_benchmark_view (
    segment_id INT PRIMARY KEY,
    segment_name VARCHAR(120) NOT NULL,
    retention_profile VARCHAR(80) NULL,
    customers INT NOT NULL,
    churn_rate_pct DECIMAL(8,2) NULL,
    avg_cltv DECIMAL(14,2) NULL,
    revenue_at_risk DECIMAL(16,2) NOT NULL,
    priority_score DECIMAL(18,2) NOT NULL,
    ease_of_intervention_score DECIMAL(6,2) NULL,
    priority_share_of_total_pct DECIMAL(10,4) NULL,
    churn_gap_pp DECIMAL(10,4) NULL,
    benchmark_status VARCHAR(40) NULL,
    revenue_risk_per_customer_gap_pct DECIMAL(12,4) NULL,
    cltv_gap_pct DECIMAL(12,4) NULL
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS external_benchmark_gap (
    metric VARCHAR(80) NOT NULL,
    benchmark_name VARCHAR(160) NOT NULL,
    benchmark_value DECIMAL(18,6) NOT NULL,
    unit VARCHAR(80) NULL,
    source VARCHAR(255) NULL,
    source_date VARCHAR(50) NULL,
    population VARCHAR(255) NULL,
    notes TEXT NULL,
    internal_reference DECIMAL(18,6) NULL,
    gap DECIMAL(18,6) NULL,
    gap_definition VARCHAR(255) NULL
) ENGINE=InnoDB;
