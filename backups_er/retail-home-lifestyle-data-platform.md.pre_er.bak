# Retail Home & Lifestyle Data Platform

Brief: Data platform for home & lifestyle retail categories to drive merchandising and marketing.

- Objectives:
  - Provide category-specific insights (SKU, trends, returns).
- Scope:
  - Inventory, supplier, sales channels, customer feedback.
- Key Components:
  - Category data marts, demand forecasting pipelines.
- Technologies:
  - Databricks, Azure Synapse, ML frameworks.
- Deliverables:
  - Forecast models, dashboards, KPI definitions.

# Expanded Source Schemas, ER Diagrams, Facts & Dimensions

This standardized expansion provides five logical sources for the project and a canonical set of artifacts to be appended to project markdown files when a detailed schema is required.

NOTE: The artifacts below are design artifacts created for documentation and implementation planning. They are original work and may be used for internal design and implementation purposes.

Project-specific prefix: `retail_home_lifestyle_data_platform` (derived from filename: `retail-home-lifestyle-data-platform.md`).

---

### Source A: Ingest & Landing (Source: `retail_home_lifestyle_data_platform_ingest`)

Tables (20):
1. retail_home_lifestyle_data_platform_stg_raw
2. retail_home_lifestyle_data_platform_raw_records
3. retail_home_lifestyle_data_platform_dim_source_system
4. retail_home_lifestyle_data_platform_dim_data_owner
5. retail_home_lifestyle_data_platform_dim_file_type
6. retail_home_lifestyle_data_platform_ref_file_schema
7. retail_home_lifestyle_data_platform_fact_raw_events
8. retail_home_lifestyle_data_platform_stage_enrichments
9. retail_home_lifestyle_data_platform_dim_geo
10. retail_home_lifestyle_data_platform_dim_business_unit
11. retail_home_lifestyle_data_platform_audit_ingest
12. retail_home_lifestyle_data_platform_dim_environment
13. retail_home_lifestyle_data_platform_ref_parsing_errors
14. retail_home_lifestyle_data_platform_stage_cdc
15. retail_home_lifestyle_data_platform_dim_schema_version
16. retail_home_lifestyle_data_platform_fact_event_counts
17. retail_home_lifestyle_data_platform_audit_transforms
18. retail_home_lifestyle_data_platform_stage_retries
19. retail_home_lifestyle_data_platform_ref_mappings
20. retail_home_lifestyle_data_platform_dim_status

ER Diagram (ASCII):

retail_home_lifestyle_data_platform_fact_raw_events (event_id, source_system_id, record_key, payload_hash, event_ts)
  |-- source_system_id --> retail_home_lifestyle_data_platform_dim_source_system(source_system_id)
  |-- record_key --> retail_home_lifestyle_data_platform_raw_records(record_key)

Description: Ingest staging (immutable) → raw normalization → enrichment → audit. `retail_home_lifestyle_data_platform_fact_raw_events` is used for throughput and source health monitoring.

---

### Source B: Operational Logs & Metrics (Source: `retail_home_lifestyle_data_platform_ops`)

Tables (20):
1. retail_home_lifestyle_data_platform_stg_ops_logs
2. retail_home_lifestyle_data_platform_raw_ops
3. retail_home_lifestyle_data_platform_dim_service
4. retail_home_lifestyle_data_platform_dim_instance
5. retail_home_lifestyle_data_platform_dim_log_level
6. retail_home_lifestyle_data_platform_ref_error_codes
7. retail_home_lifestyle_data_platform_fact_logs
8. retail_home_lifestyle_data_platform_stage_alerts
9. retail_home_lifestyle_data_platform_dim_team
10. retail_home_lifestyle_data_platform_dim_region
11. retail_home_lifestyle_data_platform_audit_ops_ingest
12. retail_home_lifestyle_data_platform_ref_runbooks
13. retail_home_lifestyle_data_platform_stage_incidents
14. retail_home_lifestyle_data_platform_fact_incident_metrics
15. retail_home_lifestyle_data_platform_dim_priority
16. retail_home_lifestyle_data_platform_ref_maintenance_windows
17. retail_home_lifestyle_data_platform_audit_recon
18. retail_home_lifestyle_data_platform_stage_trimmed_logs
19. retail_home_lifestyle_data_platform_ref_retention_policy
20. retail_home_lifestyle_data_platform_dim_status

ER Diagram (ASCII):

retail_home_lifestyle_data_platform_fact_logs (log_id, service_id, instance_id, log_level, message_ts)
  |-- service_id --> retail_home_lifestyle_data_platform_dim_service(service_id)
  |-- instance_id --> retail_home_lifestyle_data_platform_dim_instance(instance_id)

---

### Source C: Governance & Catalog (Source: `retail_home_lifestyle_data_platform_gov`)

Tables (20):
1. retail_home_lifestyle_data_platform_stg_catalog
2. retail_home_lifestyle_data_platform_raw_catalog
3. retail_home_lifestyle_data_platform_dim_dataset
4. retail_home_lifestyle_data_platform_dim_owner
5. retail_home_lifestyle_data_platform_dim_tag
6. retail_home_lifestyle_data_platform_ref_policies
7. retail_home_lifestyle_data_platform_fact_data_quality
8. retail_home_lifestyle_data_platform_stage_lineage
9. retail_home_lifestyle_data_platform_dim_classification
10. retail_home_lifestyle_data_platform_dim_sensitivity
11. retail_home_lifestyle_data_platform_audit_policies
12. retail_home_lifestyle_data_platform_ref_sla
13. retail_home_lifestyle_data_platform_stage_certifications
14. retail_home_lifestyle_data_platform_fact_issues
15. retail_home_lifestyle_data_platform_dim_remediation_team
16. retail_home_lifestyle_data_platform_ref_controls
17. retail_home_lifestyle_data_platform_audit_certification
18. retail_home_lifestyle_data_platform_stage_policy_changes
19. retail_home_lifestyle_data_platform_ref_standards
20. retail_home_lifestyle_data_platform_dim_status

ER Diagram (ASCII):

retail_home_lifestyle_data_platform_fact_data_quality (dq_id, dataset_id, check_name, check_status, checked_ts)
  |-- dataset_id --> retail_home_lifestyle_data_platform_dim_dataset(dataset_id)

---

### Source D: Cost, Billing & Usage (Source: `retail_home_lifestyle_data_platform_cost`)

Tables (20):
1. retail_home_lifestyle_data_platform_stg_billing_records
2. retail_home_lifestyle_data_platform_raw_billing
3. retail_home_lifestyle_data_platform_dim_cost_center
4. retail_home_lifestyle_data_platform_dim_resource_type
5. retail_home_lifestyle_data_platform_dim_region
6. retail_home_lifestyle_data_platform_ref_price_catalog
7. retail_home_lifestyle_data_platform_fact_cost_usage
8. retail_home_lifestyle_data_platform_stage_allocations
9. retail_home_lifestyle_data_platform_dim_tagging
10. retail_home_lifestyle_data_platform_dim_currency
11. retail_home_lifestyle_data_platform_audit_billing_ingest
12. retail_home_lifestyle_data_platform_ref_discounts
13. retail_home_lifestyle_data_platform_stage_corrections
14. retail_home_lifestyle_data_platform_fact_monthly_costs
15. retail_home_lifestyle_data_platform_dim_billing_account
16. retail_home_lifestyle_data_platform_ref_chargeback_rules
17. retail_home_lifestyle_data_platform_audit_allocations
18. retail_home_lifestyle_data_platform_stage_forecasts
19. retail_home_lifestyle_data_platform_ref_rates
20. retail_home_lifestyle_data_platform_dim_status

ER Diagram (ASCII):

retail_home_lifestyle_data_platform_fact_cost_usage (usage_id, resource_id, cost_amount, currency, start_ts, end_ts)
  |-- resource_id --> retail_home_lifestyle_data_platform_dim_resource_type(resource_id)
  |-- cost_center_id --> retail_home_lifestyle_data_platform_dim_cost_center(cost_center_id)

---

### Source E: Canonical Transactions / Facts (Source: `retail_home_lifestyle_data_platform_txn`)

Tables (20):
1. retail_home_lifestyle_data_platform_stg_transactions
2. retail_home_lifestyle_data_platform_raw_transactions
3. retail_home_lifestyle_data_platform_dim_account
4. retail_home_lifestyle_data_platform_dim_customer
5. retail_home_lifestyle_data_platform_dim_product
6. retail_home_lifestyle_data_platform_ref_exchange_rates
7. retail_home_lifestyle_data_platform_fact_transactions
8. retail_home_lifestyle_data_platform_stage_reconciliations
9. retail_home_lifestyle_data_platform_dim_channel
10. retail_home_lifestyle_data_platform_dim_merchant
11. retail_home_lifestyle_data_platform_audit_txn_ingest
12. retail_home_lifestyle_data_platform_ref_fee_schedule
13. retail_home_lifestyle_data_platform_stage_settlements
14. retail_home_lifestyle_data_platform_fact_settlements
15. retail_home_lifestyle_data_platform_dim_status
16. retail_home_lifestyle_data_platform_ref_limits
17. retail_home_lifestyle_data_platform_audit_recon
18. retail_home_lifestyle_data_platform_stage_adjustments
19. retail_home_lifestyle_data_platform_fact_balance_snapshots
20. retail_home_lifestyle_data_platform_dim_time

ER Diagram (ASCII):

retail_home_lifestyle_data_platform_fact_transactions (transaction_id, account_id, amount, currency, txn_type, posted_ts)
  |-- account_id --> retail_home_lifestyle_data_platform_dim_account(account_id)
  |-- customer_id --> retail_home_lifestyle_data_platform_dim_customer(customer_id)
  |-- product_id --> retail_home_lifestyle_data_platform_dim_product(product_id)

Common guidance:
- Always keep an immutable staging/raw zone for auditable ingestion.
- Use `audit_*` tables and checksums for reconciliation between source and target facts.
- Implement SCD patterns for dimensions where history is required.
- Register datasets in a data catalog and apply RBAC and PII protections as required.

