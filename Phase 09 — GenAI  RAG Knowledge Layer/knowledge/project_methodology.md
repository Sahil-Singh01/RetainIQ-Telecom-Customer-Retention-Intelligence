# RetainIQ — Project Knowledge Reference

## Project purpose
RetainIQ is a telecom customer-retention analytics project. I move from customer-level data quality and warehouse modeling through churn analysis, segmentation, geographic analysis, retention strategy, and benchmark context. This reference is intended to give the GenAI/RAG layer stable definitions and interpretation rules.

## Phase map
1. Business Understanding & Data Quality Audit
2. Data Cleaning & Transformation
3. MySQL Data Modeling & Analytical Warehouse Design
4. EDA & Statistical Modeling
5. Customer Segmentation & Retention Profiling
6. Geospatial & Market-Level Retention Analysis
7. Retention Strategy & Business Intelligence Layer
8. Benchmarking & Performance Context
9. GenAI / RAG Knowledge Layer

## Core definitions

### Churn rate
`Churn Rate = Churned Customers / Total Customers × 100`

### Revenue at risk
Revenue at risk is a **historical exposure proxy**. It is the sum of `total_revenue` associated with customers already recorded as churned. It is not a forecast of future lost revenue.

### Priority score
`Priority Score = Revenue at Risk × Ease-of-Intervention Score`

The ease-of-intervention score is a **subjective 1–5 business input**. The score is not inferred from churn, CLTV, or any other model output.

### Impact scenario
`Estimated Recovered Revenue = Revenue at Risk × Recovery Rate`

Default scenarios used in Phase 7 are 5%, 10%, 20%, and 30%. They are scenario assumptions, not predictions.

### Benchmark gap
`Benchmark Gap = Observed Churn Rate − Benchmark Churn Rate`

The Phase 8 default status tolerance is ±1.0 percentage point. This is a reporting convention, not a statistical significance test.

### Peer-city benchmark
The peer-city benchmark is the median churn rate among cities meeting the Phase 8 minimum market-size requirement of 25 customers.

## Interpretation rules
- Geographic patterns are descriptive and do not prove that geography causes churn.
- Benchmark gaps are descriptive comparisons and are not predictive forecasts.
- Priority scores depend on explicit business assumptions.
- External benchmarks are used only when a directly comparable source, period, population, unit, and notes are available.
- RAG answers should distinguish observed values from calculations, assumptions, and interpretations.
- When the retrieved evidence is insufficient, the assistant should say that the available project evidence is insufficient rather than inventing a value.

## RAG grounding rule
Every generated answer should be traceable to retrieved project evidence. The answer should cite evidence identifiers such as `[1]`, `[2]`, etc. in the notebook output. These identifiers map back to stored knowledge chunks.
