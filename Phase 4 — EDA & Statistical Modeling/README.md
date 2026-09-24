# RetainIQ — Phase 4: EDA & Statistical Modeling

I use the MySQL analytical layer to perform exploratory data analysis, statistical testing,
baseline churn modeling, and model interpretation.

## Notebooks

1. `01_analytical_dataset_and_eda.ipynb`
2. `02_hypothesis_testing_and_churn_drivers.ipynb`
3. `03_baseline_churn_modeling.ipynb`
4. `04_model_evaluation_and_findings.ipynb`

## MySQL integration

I pull analytical data directly from MySQL with `mysql-connector-python`.

## Statistical methods

- Welch's independent-samples t-tests
- chi-square tests of independence
- descriptive statistics
- correlation analysis

## Modeling

- Logistic Regression
- Random Forest
- stratified train/test split
- 5-fold stratified cross-validation
- ROC AUC
- precision
- recall
- F1
- average precision
- confusion matrix
- feature importance
- coefficient interpretation
- churn probability bands

## Modeling population

I use `Stayed` and `Churned` customers for historical churn modeling and keep `Joined`
customers outside the training population.

I exclude direct outcome fields and document leakage considerations for supplied metrics such as
`churn_score` and `CLTV`.