# RetainIQ — Phase 6: Geospatial & Market-Level Retention Analysis

## Objective
I analyze where customers are located, how retention metrics vary across geographic markets, and how customer segments behave within those markets.

## Notebook sequence
1. `01_geospatial_dataset_and_location_quality.ipynb`
2. `02_market_level_retention_and_revenue_analysis.ipynb`
3. `03_geospatial_risk_patterns_and_segment_geography.ipynb`
4. `04_geospatial_reporting_and_mysql_publishing.ipynb`

## Notebook presentation rule
Every **relevant analytical code cell** is followed by a `Result & conclusion` markdown cell. The code also prints a concise, data-driven `Result:` line after the calculation or visualization. Setup-only cells are not padded with unnecessary conclusions.

## Analysis coverage
- customer-level geographic data validation
- location completeness and coordinate validity
- state and city customer concentration
- state and city retention profiles
- market-size controlled churn comparison
- historical revenue exposure from churned customers
- segment × market retention profiling
- geographic grid concentration and churn
- MySQL reporting tables and views

## MySQL outputs
- `state_retention_profile`
- `city_retention_profile`
- `market_segment_risk`
- `geographic_grid_profile`
- `vw_market_retention`
- `vw_market_segment_risk`
- `vw_geographic_risk_grid`

## Requirements
- pandas
- numpy
- matplotlib
- mysql-connector-python
- jupyter

## Important interpretation note
Geography is treated as a descriptive dimension. A market-level churn pattern does not demonstrate that geography causes churn.

## Next
Phase 7 — Retention Strategy & Business Intelligence Layer
