# RetainIQ — Phase 7 Methodology

## Objective

I convert the segment and market retention outputs from Phases 5 and 6 into a business-analysis and reporting layer.

## Source grains

- `segment_profile_summary`: one row per customer segment.
- `state_retention_profile`: one row per state.
- `city_retention_profile`: one row per state/city market.

I keep these grains separate because the same underlying customers can appear in multiple dimensional summaries. I do not add segment, state, and city revenue-at-risk totals together.

## Revenue at risk

For Phase 7, revenue at risk is a historical exposure proxy carried forward from Phase 6: the sum of `total_revenue` associated with customers recorded as churned.

It is not a forecast of future revenue loss.

## Intervention scoring

The roadmap calls for a subjective 1–5 ease-of-intervention score per segment. I treat this as an explicit business input rather than a statistic inferred from the dataset.

For segments:

`priority_score = revenue_at_risk × ease_of_intervention_score`

For geography, I do not automatically apply a segment score. I provide an optional geography-specific scoring template. When geography scores are missing, geography priority remains `revenue_at_risk` only.

## Action framework

I map the segment retention profiles created in Phase 5 to operational themes. This is a business framework, not a causal model and not a guarantee that a particular action will reduce churn.

## Impact scenarios

I model simple recovery scenarios at 5%, 10%, 20%, and 30%:

`estimated_recovered_revenue = revenue_at_risk × recovery_rate`

These values are scenario estimates controlled by explicit assumptions.

## Executive memo

The memo follows the requested structure:

- Problem
- Key Finding
- Recommendation
- Expected Impact
- Limitations

The expected-impact sentence is labeled as a scenario so that historical exposure is not misrepresented as a forecast.

## Downstream use

Phase 7 outputs are designed for:

- Power BI / BI reporting
- MySQL SQL analysis
- Phase 8 benchmarking
- Phase 9 GenAI synthesis
- Phase 10 RAG retrieval
