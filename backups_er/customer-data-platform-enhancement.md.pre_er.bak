# Customer Data Platform Enhancement

Brief: Enhancements to an existing customer data platform to add new capabilities.

- Objectives:
  - Expand features, improve latency, and add governance.
- Scope:
  - Feature store, API layer, privacy controls.
- Key Components:
  - Enrichment services, access controls, lineage.
- Technologies:
  - Feature store tooling, Databricks, Purview.
- Deliverables:
  - Enhanced pipelines, API docs, governance artifacts.

# Expanded Source Schemas, ER Diagrams, Facts & Dimensions

This standardized expansion provides five logical sources for the project and a canonical set of artifacts to be appended to project markdown files when a detailed schema is required.

NOTE: The artifacts below are design artifacts created for documentation and implementation planning. They are original work and may be used for internal design and implementation purposes.

Project-specific prefix: `customer_data_platform_enhancement` (derived from filename: `customer-data-platform-enhancement.md`).

---

### Source A: Ingest & Landing (Source: `customer_data_platform_enhancement_ingest`)

Tables (20):
1. customer_data_platform_enhancement_stg_raw
2. customer_data_platform_enhancement_raw_records
3. customer_data_platform_enhancement_dim_source_system
4. customer_data_platform_enhancement_dim_data_owner
5. customer_data_platform_enhancement_dim_file_type
6. customer_data_platform_enhancement_ref_file_schema
7. customer_data_platform_enhancement_fact_raw_events
8. customer_data_platform_enhancement_stage_enrichments
9. customer_data_platform_enhancement_dim_geo
10. customer_data_platform_enhancement_dim_business_unit
11. customer_data_platform_enhancement_audit_ingest
12. customer_data_platform_enhancement_dim_environment
13. customer_data_platform_enhancement_ref_parsing_errors
14. customer_data_platform_enhancement_stage_cdc
15. customer_data_platform_enhancement_dim_schema_version
16. customer_data_platform_enhancement_fact_event_counts
17. customer_data_platform_enhancement_audit_transforms
18. customer_data_platform_enhancement_stage_retries
19. customer_data_platform_enhancement_ref_mappings
20. customer_data_platform_enhancement_dim_status

ER Diagram (ASCII):

customer_data_platform_enhancement_fact_raw_events (event_id, source_system_id, record_key, payload_hash, event_ts)
  |-- source_system_id --> customer_data_platform_enhancement_dim_source_system(source_system_id)
  |-- record_key --> customer_data_platform_enhancement_raw_records(record_key)

Description: Ingest staging (immutable) → raw normalization → enrichment → audit. `customer_data_platform_enhancement_fact_raw_events` is used for throughput and source health monitoring.

---

### Source B: Operational Logs & Metrics (Source: `customer_data_platform_enhancement_ops`)

Tables (20):
1. customer_data_platform_enhancement_stg_ops_logs
2. customer_data_platform_enhancement_raw_ops
3. customer_data_platform_enhancement_dim_service
4. customer_data_platform_enhancement_dim_instance
5. customer_data_platform_enhancement_dim_log_level
6. customer_data_platform_enhancement_ref_error_codes
7. customer_data_platform_enhancement_fact_logs
8. customer_data_platform_enhancement_stage_alerts
9. customer_data_platform_enhancement_dim_team
10. customer_data_platform_enhancement_dim_region
11. customer_data_platform_enhancement_audit_ops_ingest
12. customer_data_platform_enhancement_ref_runbooks
13. customer_data_platform_enhancement_stage_incidents
14. customer_data_platform_enhancement_fact_incident_metrics
15. customer_data_platform_enhancement_dim_priority
16. customer_data_platform_enhancement_ref_maintenance_windows
17. customer_data_platform_enhancement_audit_recon
18. customer_data_platform_enhancement_stage_trimmed_logs
19. customer_data_platform_enhancement_ref_retention_policy
20. customer_data_platform_enhancement_dim_status

ER Diagram (ASCII):

customer_data_platform_enhancement_fact_logs (log_id, service_id, instance_id, log_level, message_ts)
  |-- service_id --> customer_data_platform_enhancement_dim_service(service_id)
  |-- instance_id --> customer_data_platform_enhancement_dim_instance(instance_id)

---

### Source C: Governance & Catalog (Source: `customer_data_platform_enhancement_gov`)

Tables (20):
1. customer_data_platform_enhancement_stg_catalog
2. customer_data_platform_enhancement_raw_catalog
3. customer_data_platform_enhancement_dim_dataset
4. customer_data_platform_enhancement_dim_owner
5. customer_data_platform_enhancement_dim_tag
6. customer_data_platform_enhancement_ref_policies
7. customer_data_platform_enhancement_fact_data_quality
8. customer_data_platform_enhancement_stage_lineage
9. customer_data_platform_enhancement_dim_classification
10. customer_data_platform_enhancement_dim_sensitivity
11. customer_data_platform_enhancement_audit_policies
12. customer_data_platform_enhancement_ref_sla
13. customer_data_platform_enhancement_stage_certifications
14. customer_data_platform_enhancement_fact_issues
15. customer_data_platform_enhancement_dim_remediation_team
16. customer_data_platform_enhancement_ref_controls
17. customer_data_platform_enhancement_audit_certification
18. customer_data_platform_enhancement_stage_policy_changes
19. customer_data_platform_enhancement_ref_standards
20. customer_data_platform_enhancement_dim_status

ER Diagram (ASCII):

customer_data_platform_enhancement_fact_data_quality (dq_id, dataset_id, check_name, check_status, checked_ts)
  |-- dataset_id --> customer_data_platform_enhancement_dim_dataset(dataset_id)

---

### Source D: Cost, Billing & Usage (Source: `customer_data_platform_enhancement_cost`)

Tables (20):
1. customer_data_platform_enhancement_stg_billing_records
2. customer_data_platform_enhancement_raw_billing
3. customer_data_platform_enhancement_dim_cost_center
4. customer_data_platform_enhancement_dim_resource_type
5. customer_data_platform_enhancement_dim_region
6. customer_data_platform_enhancement_ref_price_catalog
7. customer_data_platform_enhancement_fact_cost_usage
8. customer_data_platform_enhancement_stage_allocations
9. customer_data_platform_enhancement_dim_tagging
10. customer_data_platform_enhancement_dim_currency
11. customer_data_platform_enhancement_audit_billing_ingest
12. customer_data_platform_enhancement_ref_discounts
13. customer_data_platform_enhancement_stage_corrections
14. customer_data_platform_enhancement_fact_monthly_costs
15. customer_data_platform_enhancement_dim_billing_account
16. customer_data_platform_enhancement_ref_chargeback_rules
17. customer_data_platform_enhancement_audit_allocations
18. customer_data_platform_enhancement_stage_forecasts
19. customer_data_platform_enhancement_ref_rates
20. customer_data_platform_enhancement_dim_status

ER Diagram (ASCII):

customer_data_platform_enhancement_fact_cost_usage (usage_id, resource_id, cost_amount, currency, start_ts, end_ts)
  |-- resource_id --> customer_data_platform_enhancement_dim_resource_type(resource_id)
  |-- cost_center_id --> customer_data_platform_enhancement_dim_cost_center(cost_center_id)

---

### Source E: Canonical Transactions / Facts (Source: `customer_data_platform_enhancement_txn`)

Tables (20):
1. customer_data_platform_enhancement_stg_transactions
2. customer_data_platform_enhancement_raw_transactions
3. customer_data_platform_enhancement_dim_account
4. customer_data_platform_enhancement_dim_customer
5. customer_data_platform_enhancement_dim_product
6. customer_data_platform_enhancement_ref_exchange_rates
7. customer_data_platform_enhancement_fact_transactions
8. customer_data_platform_enhancement_stage_reconciliations
9. customer_data_platform_enhancement_dim_channel
10. customer_data_platform_enhancement_dim_merchant
11. customer_data_platform_enhancement_audit_txn_ingest
12. customer_data_platform_enhancement_ref_fee_schedule
13. customer_data_platform_enhancement_stage_settlements
14. customer_data_platform_enhancement_fact_settlements
15. customer_data_platform_enhancement_dim_status
16. customer_data_platform_enhancement_ref_limits
17. customer_data_platform_enhancement_audit_recon
18. customer_data_platform_enhancement_stage_adjustments
19. customer_data_platform_enhancement_fact_balance_snapshots
20. customer_data_platform_enhancement_dim_time

ER Diagram (ASCII):

customer_data_platform_enhancement_fact_transactions (transaction_id, account_id, amount, currency, txn_type, posted_ts)
  |-- account_id --> customer_data_platform_enhancement_dim_account(account_id)
  |-- customer_id --> customer_data_platform_enhancement_dim_customer(customer_id)
  |-- product_id --> customer_data_platform_enhancement_dim_product(product_id)

Common guidance:
- Always keep an immutable staging/raw zone for auditable ingestion.
- Use `audit_*` tables and checksums for reconciliation between source and target facts.
- Implement SCD patterns for dimensions where history is required.
- Register datasets in a data catalog and apply RBAC and PII protections as required.

