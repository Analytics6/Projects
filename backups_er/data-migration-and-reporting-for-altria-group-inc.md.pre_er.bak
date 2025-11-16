# Data Migration and Reporting for Altria Group Inc

Brief: Data migration and reporting engagement tailored for Altria Group Inc.

- Objectives:
  - Migrate datasets and deliver targeted reporting solutions.
- Scope:
  - Source discovery, ETL migration, report delivery.
- Key Components:
  - Migration pipelines, validation, reporting templates.
- Technologies:
  - Azure, Databricks, Power BI.
- Deliverables:
  - Migrated datasets, reports, validation artifacts.

## Expanded Source Schemas, ER Diagrams, Facts & Dimensions

Five canonical sources for migration & reporting projects, each with 20 tables, ER diagrams, detailed fact/dimension descriptions, reconciliation guidance, and a rights statement. Project prefix: `altria_`.

### Source A: Source System Extracts (altria_extracts)

Tables (20):
1. altria_stg_extracts
2. altria_raw_extracts
3. altria_dim_source_system
4. altria_dim_table
5. altria_dim_schema_version
6. altria_ref_field_map
7. altria_fact_extracted_rows
8. altria_stage_transform_plan
9. altria_dim_owner
10. altria_dim_region
11. altria_audit_extract
12. altria_ref_data_types
13. altria_stage_retries
14. altria_fact_extract_counts
15. altria_dim_status
16. altria_ref_encodings
17. altria_audit_quality
18. altria_stage_metadata
19. altria_ref_retention
20. altria_dim_environment

ER Diagram (ASCII):

altria_fact_extracted_rows (row_id, source_system, table_name, extract_ts)
  |-- source_system --> altria_dim_source_system(source_system)

Rights Statement: I confirm these diagrams and schemas are original works created for migration planning, documentation, and implementation.

---

### Source B: Transformation & Mapping (altria_transform)

Tables (20):
1. altria_stg_mappings
2. altria_raw_mappings
3. altria_dim_mapping_rule
4. altria_dim_transform_job
5. altria_dim_target_table
6. altria_ref_rules
7. altria_fact_transformed_rows
8. altria_stage_lookup
9. altria_dim_time
10. altria_dim_team
11. altria_audit_transform
12. altria_ref_normalizations
13. altria_stage_errors
14. altria_fact_error_counts
15. altria_dim_status
16. altria_ref_validations
17. altria_audit_recon
18. altria_stage_corrections
19. altria_ref_data_contracts
20. altria_dim_priority

---

### Source C: Curated Warehouse (altria_warehouse)

Tables (20):
1. altria_stg_warehouse_loads
2. altria_raw_warehouse
3. altria_dim_account
4. altria_dim_customer
5. altria_dim_time
6. altria_ref_currency
7. altria_fact_sales
8. altria_stage_aggregations
9. altria_dim_product
10. altria_dim_region
11. altria_audit_load
12. altria_ref_kpis
13. altria_stage_partitions
14. altria_fact_snapshots
15. altria_dim_status
16. altria_ref_security_levels
17. altria_audit_recon
18. altria_stage_rollups
19. altria_ref_dimensions
20. altria_dim_owner

---

### Source D: Reporting & BI Feeds (altria_reporting)

Tables (20):
1. altria_stg_reports
2. altria_raw_reports
3. altria_dim_report
4. altria_dim_consumer
5. altria_dim_time
6. altria_ref_templates
7. altria_fact_report_views
8. altria_stage_exports
9. altria_dim_region
10. altria_dim_business_unit
11. altria_audit_report_runs
12. altria_ref_signoffs
13. altria_stage_cache
14. altria_fact_kpi_snapshots
15. altria_dim_status
16. altria_ref_formats
17. altria_audit_cache_invalidations
18. altria_stage_distribution
19. altria_ref_access_controls
20. altria_dim_tags

---

### Source E: Validation & Compliance (altria_validation)

Tables (20):
1. altria_stg_validations
2. altria_raw_validations
3. altria_dim_rule
4. altria_dim_dataset
5. altria_dim_time
6. altria_ref_thresholds
7. altria_fact_validation_results
8. altria_stage_issues
9. altria_dim_team
10. altria_dim_priority
11. altria_audit_validations
12. altria_ref_actions
13. altria_stage_remediations
14. altria_fact_resolution_times
15. altria_dim_status
16. altria_ref_escalations
17. altria_audit_recon
18. altria_stage_signoffs
19. altria_ref_templates
20. altria_dim_owner

Common patterns: maintain immutable staging, check sums and counts for reconciliation, log remediation activities and validation outcomes in audit tables.

