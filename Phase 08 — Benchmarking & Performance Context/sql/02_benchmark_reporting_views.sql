USE retainiq;

CREATE OR REPLACE VIEW vw_benchmark_reference AS SELECT * FROM benchmark_reference;
CREATE OR REPLACE VIEW vw_segment_benchmark_gap AS SELECT * FROM segment_benchmark_gap;
CREATE OR REPLACE VIEW vw_state_benchmark_gap AS SELECT * FROM state_benchmark_gap;
CREATE OR REPLACE VIEW vw_city_benchmark_gap AS SELECT * FROM city_benchmark_gap;
CREATE OR REPLACE VIEW vw_benchmark_gap_summary AS SELECT * FROM benchmark_gap_summary;
CREATE OR REPLACE VIEW vw_city_benchmark_management AS SELECT * FROM city_benchmark_management_view;
CREATE OR REPLACE VIEW vw_segment_strategy_benchmark AS SELECT * FROM segment_strategy_benchmark_view;
CREATE OR REPLACE VIEW vw_external_benchmark_gap AS SELECT * FROM external_benchmark_gap;
