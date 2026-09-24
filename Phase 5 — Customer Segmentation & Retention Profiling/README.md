# RetainIQ — Phase 5: Customer Segmentation & Retention Profiling

## Objective

I use the MySQL analytical layer to discover customer segments based on behavior, value, service
adoption, and account characteristics.

## Notebook sequence

1. `01_segmentation_dataset_and_feature_engineering.ipynb`
2. `02_clustering_and_segment_model_selection.ipynb`
3. `03_segment_profiling_and_customer_behavior.ipynb`
4. `04_retention_profiles_and_mysql_publishing.ipynb`

## Methods

- feature engineering
- one-hot encoding
- standardization
- K-Means
- elbow / inertia analysis
- silhouette analysis
- cluster-size checks
- adjusted Rand stability checks
- PCA visualization
- segment profiling
- retention profiling

## Important rule

I do not use churn outcome fields to create the clusters. Churn, value, and revenue are brought
back after the clusters are formed.

## MySQL outputs

- `customer_segment_assignments`
- `segment_profile_summary`
- `vw_customer_segments`
- `vw_segment_retention_summary`

## Generated outputs

- `customer_segment_assignments.csv`
- `segment_profile_summary.csv`
- `segment_retention_profiles.csv`
- `segment_pca_coordinates.csv`
- `cluster_selection_metrics.csv`
- `cluster_stability_metrics.csv`

## Next

Phase 6 — Geospatial & Market-Level Retention Analysis