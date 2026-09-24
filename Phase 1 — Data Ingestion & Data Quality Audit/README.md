# RetainIQ — Phase 1: Data Audit

This phase establishes the analytical foundation for the RetainIQ telecom retention intelligence platform.

## Notebook sequence

1. `01_dataset_overview.ipynb`
   - Dataset ingestion and profiling
   - Schema inventory
   - Analytical grain
   - Customer ID validation
   - Numeric / categorical inventory

2. `02_data_quality_audit.ipynb`
   - Duplicate-row audit
   - Missingness
   - Key integrity
   - Financial integrity
   - Plausibility ranges
   - Whitespace and empty-string checks

3. `03_business_field_audit.ipynb`
   - Customer outcome consistency
   - Churn-detail applicability
   - Offer / Internet Type semantics
   - Customer-service fields
   - CLTV / satisfaction / churn-score interpretation
   - New-customer modeling eligibility
   - Business decision log

4. `04_audit_summary.ipynb`
   - Executive snapshot
   - Churn distribution
   - Data-quality decisions
   - Validation gates
   - Formal Phase 2 handoff

## Source dataset

The supplied source file contains 7,043 rows and 50 columns.

Key audit results:
- Churned customers: 1,869
- Stayed customers: 5,174
- Joined customers: 454
- Overall churn rate: 26.5%
- Duplicate Customer IDs: 0
- Missing Customer IDs: 0
- Negative audited financial values: 0
- Detected leading/trailing whitespace issues: 0

## Phase boundary

Phase 1 does **not** modify the source data. Approved transformations are documented and
implemented only in Phase 2.
