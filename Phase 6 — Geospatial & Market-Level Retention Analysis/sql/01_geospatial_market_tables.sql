USE retainiq;

CREATE TABLE IF NOT EXISTS state_retention_profile (
    state VARCHAR(100) NOT NULL,
    customers INT NOT NULL,
    churned_customers INT NOT NULL,
    avg_cltv DECIMAL(14,2),
    total_revenue DECIMAL(16,2),
    avg_monthly_charge DECIMAL(12,2),
    avg_satisfaction DECIMAL(8,2),
    churn_rate_pct DECIMAL(8,2),
    revenue_at_risk DECIMAL(16,2),
    share_of_customers_pct DECIMAL(8,2),
    PRIMARY KEY (state)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS city_retention_profile (
    state VARCHAR(100),
    city VARCHAR(150),
    customers INT NOT NULL,
    churned_customers INT NOT NULL,
    avg_cltv DECIMAL(14,2),
    total_revenue DECIMAL(16,2),
    avg_monthly_charge DECIMAL(12,2),
    avg_satisfaction DECIMAL(8,2),
    churn_rate_pct DECIMAL(8,2),
    revenue_at_risk DECIMAL(16,2),
    PRIMARY KEY (state, city)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS market_segment_risk (
    state VARCHAR(100),
    city VARCHAR(150),
    segment_name VARCHAR(120),
    customers INT NOT NULL,
    churned_customers INT NOT NULL,
    avg_cltv DECIMAL(14,2),
    revenue DECIMAL(16,2),
    churn_rate_pct DECIMAL(8,2),
    revenue_at_risk DECIMAL(16,2)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS geographic_grid_profile (
    lat_grid DECIMAL(8,4),
    lon_grid DECIMAL(8,4),
    customers INT NOT NULL,
    churned_customers INT NOT NULL,
    avg_cltv DECIMAL(14,2),
    revenue DECIMAL(16,2),
    churn_rate_pct DECIMAL(8,2),
    revenue_at_risk DECIMAL(16,2),
    PRIMARY KEY (lat_grid, lon_grid)
) ENGINE=InnoDB;
