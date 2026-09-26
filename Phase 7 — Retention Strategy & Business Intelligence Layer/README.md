# RetainIQ — Phase 7: Retention Strategy & Business Intelligence Layer

## Objective

I translate the customer-segment and market-retention analysis into a business-facing strategy layer.

Phase 7 connects:

**Phase 5 — Customer Segmentation & Retention Profiling**
→ **Phase 6 — Geospatial & Market-Level Retention Analysis**
→ **Phase 7 — Business Analysis & Retention Strategy**

## Notebook sequence

1. `01_business_analysis_dataset_and_intervention_input.ipynb`
2. `02_revenue_at_risk_prioritization.ipynb`
3. `03_retention_action_framework_and_impact_scenarios.ipynb`
4. `04_executive_memo_and_mysql_publishing.ipynb`

## Notebook presentation rule

Every **relevant analytical code cell** is followed immediately by a `Result & conclusion` markdown cell. The analytical code also prints a concise `Result:` line based on the executed data. Setup-only cells are not padded with artificial conclusions.

## Core business logic

### Segment priority

`Priority Score = Revenue at Risk × Ease-of-Intervention Score`

The ease-of-intervention score is a **subjective 1–5 input** that I enter in `config/ease_of_intervention_scores.csv` after Notebook 7.1 creates the template.

### Geography priority

The original roadmap specifies subjective scores per segment. I therefore do not silently apply segment scores to cities/states. Geography can optionally receive its own 1–5 score through `config/geography_ease_of_intervention_scores.csv`; otherwise the geography view uses revenue at risk alone.

### Impact scenarios

`Estimated Recovered Revenue = Revenue at Risk × Recovery Rate`

The default scenarios are 5%, 10%, 20%, and 30%. These are scenario assumptions, not forecasts.

## Main outputs

- `segment_priority.csv`
- `state_priority.csv`
- `city_priority.csv`
- `retention_strategy_priority.csv`
- `retention_action_framework.csv`
- `retention_impact_scenarios.csv`
- `retention_impact_scenario_summary.csv`
- `phase_07_executive_memo.md`
- `phase_07_business_summary.json`

## MySQL outputs

- `retention_strategy_priority`
- `retention_impact_scenarios`
- `retention_action_framework`
- `vw_retention_strategy_priority`
- `vw_retention_impact_scenarios`
- `vw_retention_action_framework`

## Execution order

1. Complete Phase 5 publishing.
2. Complete Phase 6 publishing.
3. Run Notebook 7.1.
4. Fill in the segment intervention scores.
5. Run Notebook 7.2.
6. Run Notebook 7.3.
7. Run Notebook 7.4.

## Important interpretation notes

Revenue at risk is a historical exposure proxy based on customers already recorded as churned. It is not a forecast.

The intervention score is a business assumption. The priority order changes if the assumption changes.

Geographic patterns are descriptive and do not prove that geography causes churn.

## Requirements

- pandas
- numpy
- matplotlib
- mysql-connector-python
- jupyter
