USE retainiq;

CREATE TABLE IF NOT EXISTS customer_segment_assignments (
    customer_id VARCHAR(20) NOT NULL,
    segment_id INT NOT NULL,
    segment_name VARCHAR(120) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (customer_id),
    CONSTRAINT fk_segment_customer
        FOREIGN KEY (customer_id)
        REFERENCES fact_customer_status(customer_id)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS segment_profile_summary (
    segment_id INT NOT NULL,
    segment_name VARCHAR(120) NOT NULL,
    retention_profile VARCHAR(60) NOT NULL,
    customers INT NOT NULL,
    share_pct DECIMAL(8,2) NOT NULL,
    avg_tenure_months DECIMAL(10,2),
    avg_monthly_charge DECIMAL(12,2),
    avg_cltv DECIMAL(14,2),
    avg_satisfaction DECIMAL(8,2),
    churned_customers INT,
    churn_rate_pct DECIMAL(8,2),
    revenue_at_risk DECIMAL(16,2),
    PRIMARY KEY (segment_id)
) ENGINE=InnoDB;