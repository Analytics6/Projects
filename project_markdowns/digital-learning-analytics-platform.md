# Digital Learning Analytics Platform

Brief: Platform for analytics on digital learning content and engagement.

- Objectives:
  - Measure content effectiveness and learner journeys.
- Scope:
  - Content analytics, engagement, completion rates.
- Key Components:
  - Event ingestion, content performance models, dashboards.
- Technologies:
  - Event pipelines, Databricks, BI.
- Deliverables:
  - Content KPIs, cohort analysis, recommendations.

# Expanded Source Schemas, ER Diagrams, Facts & Dimensions

This standardized expansion provides five logical sources for the project and a canonical set of artifacts to be appended to project markdown files when a detailed schema is required.

NOTE: The artifacts below are design artifacts created for documentation and implementation planning. They are original work and may be used for internal design and implementation purposes.

Project-specific prefix: `digital_learning_analytics_platform` (derived from filename: `digital-learning-analytics-platform.md`).

---

### Source A: Ingest & Landing (Source: `digital_learning_analytics_platform_ingest`)

Tables (20):
1. digital_learning_analytics_platform_stg_raw
2. digital_learning_analytics_platform_raw_records
3. digital_learning_analytics_platform_dim_source_system
4. digital_learning_analytics_platform_dim_data_owner
5. digital_learning_analytics_platform_dim_file_type
6. digital_learning_analytics_platform_ref_file_schema
7. digital_learning_analytics_platform_fact_raw_events
8. digital_learning_analytics_platform_stage_enrichments
9. digital_learning_analytics_platform_dim_geo
10. digital_learning_analytics_platform_dim_business_unit
11. digital_learning_analytics_platform_audit_ingest
12. digital_learning_analytics_platform_dim_environment
13. digital_learning_analytics_platform_ref_parsing_errors
14. digital_learning_analytics_platform_stage_cdc
15. digital_learning_analytics_platform_dim_schema_version
16. digital_learning_analytics_platform_fact_event_counts
17. digital_learning_analytics_platform_audit_transforms
18. digital_learning_analytics_platform_stage_retries
19. digital_learning_analytics_platform_ref_mappings
20. digital_learning_analytics_platform_dim_status

ER Diagram (ASCII):

digital_learning_analytics_platform_fact_raw_events (event_id, source_system_id, record_key, payload_hash, event_ts)
  |-- source_system_id --> digital_learning_analytics_platform_dim_source_system(source_system_id)
  |-- record_key --> digital_learning_analytics_platform_raw_records(record_key)

Description: Ingest staging (immutable) → raw normalization → enrichment → audit. `digital_learning_analytics_platform_fact_raw_events` is used for throughput and source health monitoring.

---

### Source B: Operational Logs & Metrics (Source: `digital_learning_analytics_platform_ops`)

Tables (20):
1. digital_learning_analytics_platform_stg_ops_logs
2. digital_learning_analytics_platform_raw_ops
3. digital_learning_analytics_platform_dim_service
4. digital_learning_analytics_platform_dim_instance
5. digital_learning_analytics_platform_dim_log_level
6. digital_learning_analytics_platform_ref_error_codes
7. digital_learning_analytics_platform_fact_logs
8. digital_learning_analytics_platform_stage_alerts
9. digital_learning_analytics_platform_dim_team
10. digital_learning_analytics_platform_dim_region
11. digital_learning_analytics_platform_audit_ops_ingest
12. digital_learning_analytics_platform_ref_runbooks
13. digital_learning_analytics_platform_stage_incidents
14. digital_learning_analytics_platform_fact_incident_metrics
15. digital_learning_analytics_platform_dim_priority
16. digital_learning_analytics_platform_ref_maintenance_windows
17. digital_learning_analytics_platform_audit_recon
18. digital_learning_analytics_platform_stage_trimmed_logs
19. digital_learning_analytics_platform_ref_retention_policy
20. digital_learning_analytics_platform_dim_status

ER Diagram (ASCII):

digital_learning_analytics_platform_fact_logs (log_id, service_id, instance_id, log_level, message_ts)
  |-- service_id --> digital_learning_analytics_platform_dim_service(service_id)
  |-- instance_id --> digital_learning_analytics_platform_dim_instance(instance_id)

---

### Source C: Governance & Catalog (Source: `digital_learning_analytics_platform_gov`)

Tables (20):
1. digital_learning_analytics_platform_stg_catalog
2. digital_learning_analytics_platform_raw_catalog
3. digital_learning_analytics_platform_dim_dataset
4. digital_learning_analytics_platform_dim_owner
5. digital_learning_analytics_platform_dim_tag
6. digital_learning_analytics_platform_ref_policies
7. digital_learning_analytics_platform_fact_data_quality
8. digital_learning_analytics_platform_stage_lineage
9. digital_learning_analytics_platform_dim_classification
10. digital_learning_analytics_platform_dim_sensitivity
11. digital_learning_analytics_platform_audit_policies
12. digital_learning_analytics_platform_ref_sla
13. digital_learning_analytics_platform_stage_certifications
14. digital_learning_analytics_platform_fact_issues
15. digital_learning_analytics_platform_dim_remediation_team
16. digital_learning_analytics_platform_ref_controls
17. digital_learning_analytics_platform_audit_certification
18. digital_learning_analytics_platform_stage_policy_changes
19. digital_learning_analytics_platform_ref_standards
20. digital_learning_analytics_platform_dim_status

ER Diagram (ASCII):

digital_learning_analytics_platform_fact_data_quality (dq_id, dataset_id, check_name, check_status, checked_ts)
  |-- dataset_id --> digital_learning_analytics_platform_dim_dataset(dataset_id)

---

### Source D: Cost, Billing & Usage (Source: `digital_learning_analytics_platform_cost`)

Tables (20):
1. digital_learning_analytics_platform_stg_billing_records
2. digital_learning_analytics_platform_raw_billing
3. digital_learning_analytics_platform_dim_cost_center
4. digital_learning_analytics_platform_dim_resource_type
5. digital_learning_analytics_platform_dim_region
6. digital_learning_analytics_platform_ref_price_catalog
7. digital_learning_analytics_platform_fact_cost_usage
8. digital_learning_analytics_platform_stage_allocations
9. digital_learning_analytics_platform_dim_tagging
10. digital_learning_analytics_platform_dim_currency
11. digital_learning_analytics_platform_audit_billing_ingest
12. digital_learning_analytics_platform_ref_discounts
13. digital_learning_analytics_platform_stage_corrections
14. digital_learning_analytics_platform_fact_monthly_costs
15. digital_learning_analytics_platform_dim_billing_account
16. digital_learning_analytics_platform_ref_chargeback_rules
17. digital_learning_analytics_platform_audit_allocations
18. digital_learning_analytics_platform_stage_forecasts
19. digital_learning_analytics_platform_ref_rates
20. digital_learning_analytics_platform_dim_status

ER Diagram (ASCII):

digital_learning_analytics_platform_fact_cost_usage (usage_id, resource_id, cost_amount, currency, start_ts, end_ts)
  |-- resource_id --> digital_learning_analytics_platform_dim_resource_type(resource_id)
  |-- cost_center_id --> digital_learning_analytics_platform_dim_cost_center(cost_center_id)

---

### Source E: Canonical Transactions / Facts (Source: `digital_learning_analytics_platform_txn`)

Tables (20):
1. digital_learning_analytics_platform_stg_transactions
2. digital_learning_analytics_platform_raw_transactions
3. digital_learning_analytics_platform_dim_account
4. digital_learning_analytics_platform_dim_customer
5. digital_learning_analytics_platform_dim_product
6. digital_learning_analytics_platform_ref_exchange_rates
7. digital_learning_analytics_platform_fact_transactions
8. digital_learning_analytics_platform_stage_reconciliations
9. digital_learning_analytics_platform_dim_channel
10. digital_learning_analytics_platform_dim_merchant
11. digital_learning_analytics_platform_audit_txn_ingest
12. digital_learning_analytics_platform_ref_fee_schedule
13. digital_learning_analytics_platform_stage_settlements
14. digital_learning_analytics_platform_fact_settlements
15. digital_learning_analytics_platform_dim_status
16. digital_learning_analytics_platform_ref_limits
17. digital_learning_analytics_platform_audit_recon
18. digital_learning_analytics_platform_stage_adjustments
19. digital_learning_analytics_platform_fact_balance_snapshots
20. digital_learning_analytics_platform_dim_time

ER Diagram (ASCII):

digital_learning_analytics_platform_fact_transactions (transaction_id, account_id, amount, currency, txn_type, posted_ts)
  |-- account_id --> digital_learning_analytics_platform_dim_account(account_id)
  |-- customer_id --> digital_learning_analytics_platform_dim_customer(customer_id)
  |-- product_id --> digital_learning_analytics_platform_dim_product(product_id)

Common guidance:
- Always keep an immutable staging/raw zone for auditable ingestion.
- Use `audit_*` tables and checksums for reconciliation between source and target facts.
- Implement SCD patterns for dimensions where history is required.
- Register datasets in a data catalog and apply RBAC and PII protections as required.

