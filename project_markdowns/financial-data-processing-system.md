# Financial Data Processing System

Brief: High-integrity processing system for financial datasets.

- Objectives:
  - Ensure accurate, timely transformations and lineage for financial reports.
- Scope:
  - Transaction processing, FX normalization, consolidation.
- Key Components:
  - ELT pipelines, QC, lineage, reconciliation.
- Technologies:
  - Databricks, Azure Data Factory, data catalogs.
- Deliverables:
  - Processed ledgers, QC reports, data lineage artifacts.

# Expanded Source Schemas, ER Diagrams, Facts & Dimensions

This standardized expansion provides five logical sources for the project and a canonical set of artifacts to be appended to project markdown files when a detailed schema is required.

NOTE: The artifacts below are design artifacts created for documentation and implementation planning. They are original work and may be used for internal design and implementation purposes.

Project-specific prefix: `financial_data_processing_system` (derived from filename: `financial-data-processing-system.md`).

---

### Source A: Ingest & Landing (Source: `financial_data_processing_system_ingest`)

Tables (20):
1. financial_data_processing_system_stg_raw
2. financial_data_processing_system_raw_records
3. financial_data_processing_system_dim_source_system
4. financial_data_processing_system_dim_data_owner
5. financial_data_processing_system_dim_file_type
6. financial_data_processing_system_ref_file_schema
7. financial_data_processing_system_fact_raw_events
8. financial_data_processing_system_stage_enrichments
9. financial_data_processing_system_dim_geo
10. financial_data_processing_system_dim_business_unit
11. financial_data_processing_system_audit_ingest
12. financial_data_processing_system_dim_environment
13. financial_data_processing_system_ref_parsing_errors
14. financial_data_processing_system_stage_cdc
15. financial_data_processing_system_dim_schema_version
16. financial_data_processing_system_fact_event_counts
17. financial_data_processing_system_audit_transforms
18. financial_data_processing_system_stage_retries
19. financial_data_processing_system_ref_mappings
20. financial_data_processing_system_dim_status

ER Diagram (ASCII):

financial_data_processing_system_fact_raw_events (event_id, source_system_id, record_key, payload_hash, event_ts)
  |-- source_system_id --> financial_data_processing_system_dim_source_system(source_system_id)
  |-- record_key --> financial_data_processing_system_raw_records(record_key)

Description: Ingest staging (immutable) → raw normalization → enrichment → audit. `financial_data_processing_system_fact_raw_events` is used for throughput and source health monitoring.

---

### Source B: Operational Logs & Metrics (Source: `financial_data_processing_system_ops`)

Tables (20):
1. financial_data_processing_system_stg_ops_logs
2. financial_data_processing_system_raw_ops
3. financial_data_processing_system_dim_service
4. financial_data_processing_system_dim_instance
5. financial_data_processing_system_dim_log_level
6. financial_data_processing_system_ref_error_codes
7. financial_data_processing_system_fact_logs
8. financial_data_processing_system_stage_alerts
9. financial_data_processing_system_dim_team
10. financial_data_processing_system_dim_region
11. financial_data_processing_system_audit_ops_ingest
12. financial_data_processing_system_ref_runbooks
13. financial_data_processing_system_stage_incidents
14. financial_data_processing_system_fact_incident_metrics
15. financial_data_processing_system_dim_priority
16. financial_data_processing_system_ref_maintenance_windows
17. financial_data_processing_system_audit_recon
18. financial_data_processing_system_stage_trimmed_logs
19. financial_data_processing_system_ref_retention_policy
20. financial_data_processing_system_dim_status

ER Diagram (ASCII):

financial_data_processing_system_fact_logs (log_id, service_id, instance_id, log_level, message_ts)
  |-- service_id --> financial_data_processing_system_dim_service(service_id)
  |-- instance_id --> financial_data_processing_system_dim_instance(instance_id)

---

### Source C: Governance & Catalog (Source: `financial_data_processing_system_gov`)

Tables (20):
1. financial_data_processing_system_stg_catalog
2. financial_data_processing_system_raw_catalog
3. financial_data_processing_system_dim_dataset
4. financial_data_processing_system_dim_owner
5. financial_data_processing_system_dim_tag
6. financial_data_processing_system_ref_policies
7. financial_data_processing_system_fact_data_quality
8. financial_data_processing_system_stage_lineage
9. financial_data_processing_system_dim_classification
10. financial_data_processing_system_dim_sensitivity
11. financial_data_processing_system_audit_policies
12. financial_data_processing_system_ref_sla
13. financial_data_processing_system_stage_certifications
14. financial_data_processing_system_fact_issues
15. financial_data_processing_system_dim_remediation_team
16. financial_data_processing_system_ref_controls
17. financial_data_processing_system_audit_certification
18. financial_data_processing_system_stage_policy_changes
19. financial_data_processing_system_ref_standards
20. financial_data_processing_system_dim_status

ER Diagram (ASCII):

financial_data_processing_system_fact_data_quality (dq_id, dataset_id, check_name, check_status, checked_ts)
  |-- dataset_id --> financial_data_processing_system_dim_dataset(dataset_id)

---

### Source D: Cost, Billing & Usage (Source: `financial_data_processing_system_cost`)

Tables (20):
1. financial_data_processing_system_stg_billing_records
2. financial_data_processing_system_raw_billing
3. financial_data_processing_system_dim_cost_center
4. financial_data_processing_system_dim_resource_type
5. financial_data_processing_system_dim_region
6. financial_data_processing_system_ref_price_catalog
7. financial_data_processing_system_fact_cost_usage
8. financial_data_processing_system_stage_allocations
9. financial_data_processing_system_dim_tagging
10. financial_data_processing_system_dim_currency
11. financial_data_processing_system_audit_billing_ingest
12. financial_data_processing_system_ref_discounts
13. financial_data_processing_system_stage_corrections
14. financial_data_processing_system_fact_monthly_costs
15. financial_data_processing_system_dim_billing_account
16. financial_data_processing_system_ref_chargeback_rules
17. financial_data_processing_system_audit_allocations
18. financial_data_processing_system_stage_forecasts
19. financial_data_processing_system_ref_rates
20. financial_data_processing_system_dim_status

ER Diagram (ASCII):

financial_data_processing_system_fact_cost_usage (usage_id, resource_id, cost_amount, currency, start_ts, end_ts)
  |-- resource_id --> financial_data_processing_system_dim_resource_type(resource_id)
  |-- cost_center_id --> financial_data_processing_system_dim_cost_center(cost_center_id)

---

### Source E: Canonical Transactions / Facts (Source: `financial_data_processing_system_txn`)

Tables (20):
1. financial_data_processing_system_stg_transactions
2. financial_data_processing_system_raw_transactions
3. financial_data_processing_system_dim_account
4. financial_data_processing_system_dim_customer
5. financial_data_processing_system_dim_product
6. financial_data_processing_system_ref_exchange_rates
7. financial_data_processing_system_fact_transactions
8. financial_data_processing_system_stage_reconciliations
9. financial_data_processing_system_dim_channel
10. financial_data_processing_system_dim_merchant
11. financial_data_processing_system_audit_txn_ingest
12. financial_data_processing_system_ref_fee_schedule
13. financial_data_processing_system_stage_settlements
14. financial_data_processing_system_fact_settlements
15. financial_data_processing_system_dim_status
16. financial_data_processing_system_ref_limits
17. financial_data_processing_system_audit_recon
18. financial_data_processing_system_stage_adjustments
19. financial_data_processing_system_fact_balance_snapshots
20. financial_data_processing_system_dim_time

ER Diagram (ASCII):

financial_data_processing_system_fact_transactions (transaction_id, account_id, amount, currency, txn_type, posted_ts)
  |-- account_id --> financial_data_processing_system_dim_account(account_id)
  |-- customer_id --> financial_data_processing_system_dim_customer(customer_id)
  |-- product_id --> financial_data_processing_system_dim_product(product_id)

Common guidance:
- Always keep an immutable staging/raw zone for auditable ingestion.
- Use `audit_*` tables and checksums for reconciliation between source and target facts.
- Implement SCD patterns for dimensions where history is required.
- Register datasets in a data catalog and apply RBAC and PII protections as required.

