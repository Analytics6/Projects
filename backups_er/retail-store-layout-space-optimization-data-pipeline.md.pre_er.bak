# Retail Store Layout & Space Optimization Data Pipeline

Brief: Pipeline to analyze store layout effectiveness and space allocation.

- Objectives:
  - Improve sales per square meter and planogram efficiency.
- Scope:
  - Heatmaps, dwell analytics, planogram experiments.
- Key Components:
  - Customer flow datasets, POS linkages, optimization models.
- Technologies:
  - IoT/footfall data, spatial analytics, optimization solvers.
- Deliverables:
  - Layout recommendations, impact estimates, experiment logs.

## Expanded Source Schemas, ER Diagrams, Facts & Dimensions

Adds five logical sources for layout & space analytics, each with 20 tables, ER diagrams, fact/dimension details, reconciliation guidance, and a rights statement.

Project prefix: `rlso_` (Retail Layout & Space Optimization)

### Source A: Footfall & Sensors (rlso_footfall)

Tables (20):
1. rlso_stg_sensor_events
2. rlso_raw_sensor_events
3. rlso_dim_device
4. rlso_dim_location
5. rlso_dim_floor
6. rlso_ref_device_types
7. rlso_fact_sensor_counts
8. rlso_stage_heatmaps
9. rlso_dim_time
10. rlso_dim_store
11. rlso_audit_ingest
12. rlso_ref_calibration
13. rlso_stage_agg
14. rlso_dim_zone
15. rlso_ref_thresholds
16. rlso_fact_dwell_times
17. rlso_audit_quality
18. rlso_stage_cleaned
19. rlso_ref_epoch
20. rlso_dim_status

ER Diagram (ASCII):

rlso_fact_sensor_counts (count_id, device_id, zone_id, count, measure_ts)
  |-- device_id --> rlso_dim_device(device_id)
  |-- zone_id --> rlso_dim_zone(zone_id)

### Source B: POS & Sales (rlso_sales)

Tables (20):
1. rlso_stg_pos
2. rlso_raw_pos
3. rlso_dim_terminal
4. rlso_dim_product
5. rlso_dim_store
6. rlso_ref_txn_type
7. rlso_fact_sales
8. rlso_stage_promotions
9. rlso_dim_cashier
10. rlso_dim_time
11. rlso_audit_pos_ingest
12. rlso_ref_tax_codes
13. rlso_stage_returns
14. rlso_fact_baskets
15. rlso_dim_channel
16. rlso_ref_price_lists
17. rlso_audit_recon
18. rlso_stage_settlements
19. rlso_ref_discounts
20. rlso_dim_status

### Source C: Experiments & Planograms (rlso_experiments)

Tables (20):
1. rlso_stg_experiments
2. rlso_raw_experiments
3. rlso_dim_experiment
4. rlso_dim_planogram
5. rlso_dim_store
6. rlso_ref_kpis
7. rlso_fact_experiment_results
8. rlso_stage_variations
9. rlso_dim_time
10. rlso_dim_category
11. rlso_audit_experiment_ingest
12. rlso_ref_winner_criteria
13. rlso_stage_segmentations
14. rlso_fact_lift_metrics
15. rlso_dim_team
16. rlso_ref_stat_tests
17. rlso_audit_repro
18. rlso_stage_cleaned
19. rlso_ref_sampling
20. rlso_dim_status

### Source D: Inventory & SKU Flow (rlso_inventory)

Tables (20):
1. rlso_stg_inventory
2. rlso_raw_inventory
3. rlso_dim_sku
4. rlso_dim_location
5. rlso_dim_supplier
6. rlso_ref_lead_times
7. rlso_fact_stock_levels
8. rlso_stage_replenishments
9. rlso_dim_time
10. rlso_dim_store
11. rlso_audit_inventory_ingest
12. rlso_ref_reorder_rules
13. rlso_stage_movements
14. rlso_fact_turnover
15. rlso_dim_category
16. rlso_ref_packaging
17. rlso_audit_recon
18. rlso_stage_adjustments
19. rlso_ref_units
20. rlso_dim_status

### Source E: External Benchmarks & Weather (rlso_external)

Tables (20):
1. rlso_stg_external_feeds
2. rlso_raw_external
3. rlso_dim_source
4. rlso_dim_metric
5. rlso_dim_region
6. rlso_ref_mapping
7. rlso_fact_external_metrics
8. rlso_stage_merged
9. rlso_dim_time
10. rlso_dim_store
11. rlso_audit_external_ingest
12. rlso_ref_units
13. rlso_stage_alignments
14. rlso_fact_correlation
15. rlso_dim_weather_event
16. rlso_ref_thresholds
17. rlso_audit_recon
18. rlso_stage_transforms
19. rlso_ref_codes
20. rlso_dim_status

## Common Guidance
- Use heatmap generation tables and link POS sales to sensor zones to compute sales-per-square-meter.
- Maintain `audit_*` tables for reconciliation and dashboards.

