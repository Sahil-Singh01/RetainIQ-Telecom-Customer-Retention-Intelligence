# Phase 6 methodology

## Purpose
I analyze how customer retention patterns vary across geography and how those patterns intersect with the customer segments created in Phase 5.

## Data grain
The analytical customer dataset remains one row per customer. State, city, and coordinate-level outputs are aggregations of that customer grain.

## Retention metrics
- Churn rate = churned customers / total customers in the market.
- Revenue at risk is used as a historical proxy: total recorded revenue associated with customers already labeled as churned.

## Market size controls
City comparisons use a minimum market size of 25 customers. Segment-market comparisons use a minimum group size of 10 customers. These thresholds reduce instability in small groups.

## Geographic grid
Valid latitude and longitude pairs are rounded to 2 decimal places to create descriptive geographic cells. The grid is intended for exploratory concentration analysis, not precise spatial inference.

## Interpretation limits
Geographic patterns are descriptive. A high churn rate in a market or coordinate cluster does not establish that geography causes churn.

## Notebook presentation
Relevant analytical code cells are followed by a **Result & conclusion** markdown cell. Analytical code also prints a compact result statement so the observed output and interpretation appear together in a Jupyter run.
