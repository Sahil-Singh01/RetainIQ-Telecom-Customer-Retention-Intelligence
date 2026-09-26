USE retainiq;

CREATE OR REPLACE VIEW vw_retention_strategy_priority AS
SELECT
    priority_id,
    scope,
    entity_name,
    state,
    city,
    segment_name,
    retention_profile,
    customers,
    churn_rate_pct,
    avg_cltv,
    revenue_at_risk,
    ease_of_intervention_score,
    priority_score,
    priority_basis,
    action_theme,
    created_at
FROM retention_strategy_priority;

CREATE OR REPLACE VIEW vw_retention_impact_scenarios AS
SELECT
    scope,
    entity_name,
    revenue_at_risk,
    recovery_rate_pct,
    estimated_recovered_revenue,
    created_at
FROM retention_impact_scenarios;

CREATE OR REPLACE VIEW vw_retention_action_framework AS
SELECT
    segment_id,
    segment_name,
    retention_profile,
    customers,
    avg_cltv,
    churn_rate_pct,
    revenue_at_risk,
    priority_score,
    action_theme,
    action_description,
    created_at
FROM retention_action_framework;
