# Analytics Lab: Customer Retention Deep Dive

**Project:** RetainIQ — Telecom Customer Retention Intelligence  
**Focus:** SQL, pandas, cohort analysis, and business recommendations  
**Dataset:** `telco.csv` in the repository root

This lab is a reproducible practice task built around the project's telecom customer dataset. It deliberately records questions and methods—not fabricated findings. Run the analysis and document the actual results before drawing conclusions.

## Business question

Which customer groups show the strongest churn signals, and what should a retention team investigate first?

## 1. Data-quality checks (Python)

Use pandas to:

- Load `telco.csv` and inspect shape, column names, data types, and sample rows.
- Check duplicate customer IDs and missing values.
- Convert `TotalCharges` to numeric safely; report values that become null after conversion.
- Validate that churn labels and categorical fields contain expected values.
- Save a short data-quality summary to `outputs/data_quality_summary.csv` (create the folder if needed).

**Deliverable:** A table of each issue, its count, and the treatment chosen. Do not silently drop rows.

## 2. Retention KPIs (SQL or pandas)

Calculate and clearly define:

- Total customers
- Churned customers
- Overall churn rate
- Monthly recurring charges at risk among churned customers
- Average tenure for churned versus retained customers

Use explicit denominators and handle missing values consistently. Label monetary amounts with the appropriate units.

## 3. Segment analysis

Compare churn rate and customer count across:

- Contract type
- Internet service
- Payment method
- Tenure bands (0–12, 13–24, 25–48, and 49+ months)

For each segment, show both its size and churn rate. Avoid ranking tiny segments without noting their sample size.

## 4. SQL practice questions

Write and test queries for the following:

1. What is the churn rate by contract type?
2. Which payment methods have the highest churn rate, and how many customers are in each group?
3. How does average tenure differ between churned and retained customers?
4. Which tenure band contributes the most churned customers?
5. Which customer segments have above-average churn while representing at least 5% of the customer base?

Document your SQL dialect and any column-name/type adjustments required by your database.

## 5. Python analysis

Use pandas to reproduce at least three SQL results and verify that the numbers agree. Create:

- A bar chart of churn rate by contract type
- A tenure distribution comparison for churned and retained customers
- A concise segment table sorted by churn rate, with customer counts included

Prefer readable labels, clear denominators, and charts that answer a business question.

## 6. Turn findings into action

Write a short decision memo containing:

- **Finding:** What the data actually shows, with counts and rates
- **Interpretation:** A plausible explanation, clearly separated from evidence
- **Action:** One retention experiment to test
- **Measurement:** Primary KPI, comparison group, and evaluation window
- **Caveat:** A limitation, confounder, or data-quality concern

Do not claim that a segment *causes* churn based on descriptive analysis alone. Treat recommendations as hypotheses to validate.

## Definition

`Churn rate = churned customers / eligible customers × 100`

State whether your denominator excludes records with missing churn status. Keep that choice consistent throughout the analysis.

## Completion checklist

- [ ] Data-quality issues quantified and documented
- [ ] KPI definitions and denominators stated
- [ ] Segment counts shown alongside rates
- [ ] SQL results cross-checked against pandas
- [ ] Charts include clear labels
- [ ] Business recommendation tied to measured evidence
- [ ] Reproduction steps and environment noted

---
*Practice note: update this file with dated findings only after running the analysis. Never invent metrics to make the project look complete.*
