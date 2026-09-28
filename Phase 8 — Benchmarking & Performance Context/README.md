# RetainIQ — Phase 8: Benchmarking & Performance Context

## Objective

I add benchmark context to the RetainIQ retention strategy layer. After Phase 7 translates churn and revenue exposure into business priorities, Phase 8 measures those patterns against explicit internal reference points and optional external benchmarks.

## Notebook sequence

1. `01_benchmark_dataset_and_benchmark_inputs.ipynb`
2. `02_churn_and_revenue_benchmarking.ipynb`
3. `03_benchmark_gap_analysis_and_management_views.ipynb`
4. `04_benchmark_reporting_and_mysql_publishing.ipynb`

## Core logic

### Portfolio churn benchmark

`total churned customers / total customers × 100`

### Peer-city benchmark

Median churn rate across cities with at least 25 customers.

### Benchmark gap

`observed churn rate − benchmark churn rate`

### Status convention

The default tolerance is ±1.0 percentage point. This is a reporting convention, not a statistical significance test.

## External benchmark policy

`config/external_benchmark_inputs.csv` is optional. I only populate it when I have a directly comparable benchmark and retain the source, period, population, unit, and notes. Phase 8 remains complete using internal benchmarks alone.

## Main outputs

- `benchmark_reference.csv`
- `segment_benchmark_gap.csv`
- `state_benchmark_gap.csv`
- `city_benchmark_gap.csv`
- `segment_benchmark_status_summary.csv`
- `city_benchmark_management_view.csv`
- `segment_strategy_benchmark_view.csv`
- `external_benchmark_gap.csv`
- `benchmark_gap_summary.csv`

## MySQL outputs

- `benchmark_reference`
- `segment_benchmark_gap`
- `state_benchmark_gap`
- `city_benchmark_gap`
- `benchmark_gap_summary`
- `city_benchmark_management_view`
- `segment_strategy_benchmark_view`
- `external_benchmark_gap`
- matching `vw_*` reporting views

## Execution order

1. Complete Phase 7.1–7.4.
2. Run Notebook 8.1.
3. Review the benchmark configuration and populate external benchmarks only when comparable evidence is available.
4. Run Notebook 8.2.
5. Run Notebook 8.3.
6. Run Notebook 8.4.

## Important interpretation notes

Benchmark gaps are descriptive. They do not prove causation and are not predictive forecasts. Revenue at risk remains a historical exposure proxy inherited from Phase 7.

## Requirements

- pandas
- numpy
- matplotlib
- mysql-connector-python
- jupyter
