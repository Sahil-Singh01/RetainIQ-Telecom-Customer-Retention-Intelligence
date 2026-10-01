# RetainIQ — Phase 3 MySQL Architecture

```text
telco_clean.csv
      ↓
stg_telco_clean
      ↓
fact_customer_status + dimensions
      ↓
validation + analytical SQL
      ↓
views / Power BI / RAG
```

## SQL layers
- DDL
- DML
- DQL
- CASE
- CTEs
- window functions
- views
- indexes
- EXPLAIN
- validation and reconciliation

## Expected final checks
- 7,043 customers
- 1,869 churned
- 26.5% churn
- 0 duplicate fact keys
- 0 orphaned dimension rows
