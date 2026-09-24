# RetainIQ — Phase 2: Data Cleaning & Transformation

## Notebooks

1. `01_cleaning_scope_and_baseline.ipynb` — baseline and cleaning contract
2. `02_text_and_categorical_standardization.ipynb` — text and semantic standardization
3. `03_customer_flags_and_integrity.ipynb` — new-customer flag and integrity checks
4. `04_cleaning_validation_and_export.ipynb` — final validation and export

## Result

Raw dataset: 7,043 rows × 50 columns  
Clean dataset: 7,043 rows × 51 columns

## Approved transformations

- `Offer`: null → `No Offer`
- `Internet Type`: null → `No Internet Service`
- `Churn Category`: preserve null
- `Churn Reason`: preserve null
- String columns: strip leading/trailing whitespace
- `is_new_customer`: `Customer Status == "Joined"`

## Outputs

- `data/telco_raw.csv`
- `data/telco_clean.csv`
- `outputs/01_clean_schema_profile.csv`
- `outputs/02_missing_values_after_cleaning.csv`
- `outputs/03_transformation_log.csv`
- `outputs/04_validation_snapshot.csv`

## Phase boundary

The raw source is never overwritten. The clean dataset is generated from the raw source and
validated before being approved for downstream work.
