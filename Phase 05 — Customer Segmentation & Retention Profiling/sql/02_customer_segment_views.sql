USE retainiq;

CREATE OR REPLACE VIEW vw_customer_segments AS
SELECT
    a.customer_id,
    a.segment_id,
    a.segment_name,
    p.retention_profile,
    p.avg_cltv,
    p.churn_rate_pct,
    p.revenue_at_risk,
    a.created_at
FROM customer_segment_assignments a
JOIN segment_profile_summary p
    ON a.segment_id = p.segment_id;

CREATE OR REPLACE VIEW vw_segment_retention_summary AS
SELECT
    segment_id,
    segment_name,
    retention_profile,
    customers,
    share_pct,
    avg_tenure_months,
    avg_monthly_charge,
    avg_cltv,
    avg_satisfaction,
    churned_customers,
    churn_rate_pct,
    revenue_at_risk
FROM segment_profile_summary;