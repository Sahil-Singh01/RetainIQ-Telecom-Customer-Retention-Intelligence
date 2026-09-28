# RetainIQ — Phase 8 Methodology

## Objective

I add benchmark context to the Phase 7 retention strategy layer. The purpose is to show whether segment and market churn patterns sit above, within, or below explicit reference points.

## Internal benchmarks

### Portfolio benchmark

`portfolio_churn_rate = total churned customers / total customers × 100`

The calculation is weighted by customer counts across the Phase 7 segment table.

### Peer-city benchmark

I calculate the median churn rate across cities with at least 25 customers. The minimum market size is configurable in `config/benchmark_parameters.csv`.

## Benchmark gaps

`churn_gap_pp = observed churn rate − benchmark churn rate`

Positive values mean the observed churn rate is above the reference point. Negative values mean it is below the reference point.

For value context I also calculate the percentage gap between average CLTV or historical revenue-at-risk per customer and the portfolio reference.

## Tolerance

I classify churn gaps using an explicit tolerance of ±1.0 percentage point by default:

- Above benchmark: gap > +1.0 pp
- Within benchmark: -1.0 pp ≤ gap ≤ +1.0 pp
- Below benchmark: gap < -1.0 pp

This is a reporting convention, not a statistical significance test. The parameter is editable.

## External benchmarking

External benchmarks are optional. I only use them when a value is supplied with a directly comparable metric definition, period, population, unit, source, and source date. The notebooks do not invent or infer external benchmark values.

## Revenue at risk

The underlying revenue-at-risk measure remains the Phase 7 historical exposure proxy: historical total revenue associated with customers already recorded as churned. It is not a forecast.

## Interpretation

Benchmark gaps describe observed differences relative to an explicit reference. They do not establish causality, and they should not be interpreted as predictions of future churn.

## Downstream use

Phase 8 outputs support:

- Power BI benchmark cards and gap views
- MySQL reporting
- Executive reporting
- Phase 9 GenAI synthesis
- Phase 10 RAG retrieval
