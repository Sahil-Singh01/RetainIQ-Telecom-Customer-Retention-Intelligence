# RetainIQ — Phase 3: SQL Data Modeling & Analytical Warehouse Design

**Database: MySQL 8.x**

## Notebooks
1. 01_mysql_schema_design.ipynb
2. 02_mysql_database_build_and_load.ipynb
3. 03_mysql_validation_and_analytics.ipynb
4. 04_mysql_advanced_sql_views_and_performance.ipynb

## SQL
1. 01_database_and_staging.sql
2. 02_star_schema.sql
3. 03_load_data.sql
4. 04_validation_and_analysis.sql
5. 05_views_indexes_performance.sql

## Python
The notebooks connect directly to MySQL with mysql-connector-python. The CSV is loaded into staging with a parameterized MySQL executemany() load, not pandas.to_sql().

## Skills
DDL, DML, DQL, joins, aggregation, CASE, CTEs, window functions, views, indexes, EXPLAIN, keys, validation, reconciliation, Customer 360.
