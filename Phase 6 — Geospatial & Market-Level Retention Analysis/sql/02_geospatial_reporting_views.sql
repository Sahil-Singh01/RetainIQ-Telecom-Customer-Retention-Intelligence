USE retainiq;

CREATE OR REPLACE VIEW vw_market_retention AS
SELECT
    state, city, customers, churned_customers,
    churn_rate_pct, avg_cltv, total_revenue,
    revenue_at_risk, avg_satisfaction, avg_monthly_charge
FROM city_retention_profile;

CREATE OR REPLACE VIEW vw_market_segment_risk AS
SELECT
    state, city, segment_name, customers,
    churned_customers, churn_rate_pct, avg_cltv,
    revenue, revenue_at_risk
FROM market_segment_risk;

CREATE OR REPLACE VIEW vw_geographic_risk_grid AS
SELECT
    lat_grid, lon_grid, customers,
    churned_customers, churn_rate_pct,
    avg_cltv, revenue, revenue_at_risk
FROM geographic_grid_profile;
