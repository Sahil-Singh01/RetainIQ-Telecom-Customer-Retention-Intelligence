# RetainIQ — Phase 4 Methodology

## Source

I use MySQL 8.x as the structured analytical source.

## Population

I use `Stayed` and `Churned` customers for historical churn modeling and exclude `Joined`
customers.

## Statistical testing

I use Welch's independent-samples t-test for selected numeric variables and chi-square tests
for selected categorical variables.

A statistically significant p-value is treated as evidence of association under the test
assumptions, not proof of causation.

## Modeling

I compare Logistic Regression and Random Forest using a stratified split and five-fold stratified
cross-validation.

I track ROC AUC, precision, recall, F1, average precision, and confusion matrices.

## Leakage

I exclude direct outcome fields such as churn label/category/reason. I review `churn_score`
and `CLTV` cautiously because their construction timing is not documented in the source.