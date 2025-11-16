# Healthcare Data Lake Implementation

Brief: Implement a secure and compliant data lake for healthcare use-cases.

- Objectives:
  - Store and manage health data while complying with regulations.
- Scope:
  - Ingest clinical and operational data, de-identification pipelines.
- Key Components:
  - Secure storage, access auditing, de-identification processes.
- Technologies:
  - Azure with HIPAA controls, encryption, Databricks.
- Deliverables:
  - Secure data lake, compliance documentation, sample pipelines.

# Expanded Source Schemas, ER Diagrams, Facts & Dimensions

This standardized expansion provides five logical sources for the project and a canonical set of artifacts to be appended to project markdown files when a detailed schema is required.

NOTE: The artifacts below are design artifacts created for documentation and implementation planning. They are original work and may be used for internal design and implementation purposes.

Project-specific prefix: `healthcare_data_lake_implementation` (derived from filename: `healthcare-data-lake-implementation.md`).

---

### Source A: Ingest & Landing (Source: `healthcare_data_lake_implementation_ingest`)

Tables (20):
1. healthcare_data_lake_implementation_stg_raw
2. healthcare_data_lake_implementation_raw_records
3. healthcare_data_lake_implementation_dim_source_system
4. healthcare_data_lake_implementation_dim_data_owner
5. healthcare_data_lake_implementation_dim_file_type
6. healthcare_data_lake_implementation_ref_file_schema
7. healthcare_data_lake_implementation_fact_raw_events
8. healthcare_data_lake_implementation_stage_enrichments
9. healthcare_data_lake_implementation_dim_geo
10. healthcare_data_lake_implementation_dim_business_unit
11. healthcare_data_lake_implementation_audit_ingest
12. healthcare_data_lake_implementation_dim_environment
13. healthcare_data_lake_implementation_ref_parsing_errors
14. healthcare_data_lake_implementation_stage_cdc
15. healthcare_data_lake_implementation_dim_schema_version
16. healthcare_data_lake_implementation_fact_event_counts
17. healthcare_data_lake_implementation_audit_transforms
18. healthcare_data_lake_implementation_stage_retries
19. healthcare_data_lake_implementation_ref_mappings
20. healthcare_data_lake_implementation_dim_status

ER Diagram (ASCII):

healthcare_data_lake_implementation_fact_raw_events (event_id, source_system_id, record_key, payload_hash, event_ts)
  |-- source_system_id --> healthcare_data_lake_implementation_dim_source_system(source_system_id)
  |-- record_key --> healthcare_data_lake_implementation_raw_records(record_key)

Description: Ingest staging (immutable) → raw normalization → enrichment → audit. `healthcare_data_lake_implementation_fact_raw_events` is used for throughput and source health monitoring.

---

### Source B: Operational Logs & Metrics (Source: `healthcare_data_lake_implementation_ops`)

Tables (20):
1. healthcare_data_lake_implementation_stg_ops_logs
2. healthcare_data_lake_implementation_raw_ops
3. healthcare_data_lake_implementation_dim_service
4. healthcare_data_lake_implementation_dim_instance
5. healthcare_data_lake_implementation_dim_log_level
6. healthcare_data_lake_implementation_ref_error_codes
7. healthcare_data_lake_implementation_fact_logs
8. healthcare_data_lake_implementation_stage_alerts
9. healthcare_data_lake_implementation_dim_team
10. healthcare_data_lake_implementation_dim_region
11. healthcare_data_lake_implementation_audit_ops_ingest
12. healthcare_data_lake_implementation_ref_runbooks
13. healthcare_data_lake_implementation_stage_incidents
14. healthcare_data_lake_implementation_fact_incident_metrics
15. healthcare_data_lake_implementation_dim_priority
16. healthcare_data_lake_implementation_ref_maintenance_windows
17. healthcare_data_lake_implementation_audit_recon
18. healthcare_data_lake_implementation_stage_trimmed_logs
19. healthcare_data_lake_implementation_ref_retention_policy
20. healthcare_data_lake_implementation_dim_status

ER Diagram (ASCII):

healthcare_data_lake_implementation_fact_logs (log_id, service_id, instance_id, log_level, message_ts)
  |-- service_id --> healthcare_data_lake_implementation_dim_service(service_id)
  |-- instance_id --> healthcare_data_lake_implementation_dim_instance(instance_id)

---

### Source C: Governance & Catalog (Source: `healthcare_data_lake_implementation_gov`)

Tables (20):
1. healthcare_data_lake_implementation_stg_catalog
2. healthcare_data_lake_implementation_raw_catalog
3. healthcare_data_lake_implementation_dim_dataset
4. healthcare_data_lake_implementation_dim_owner
5. healthcare_data_lake_implementation_dim_tag
6. healthcare_data_lake_implementation_ref_policies
7. healthcare_data_lake_implementation_fact_data_quality
8. healthcare_data_lake_implementation_stage_lineage
9. healthcare_data_lake_implementation_dim_classification
10. healthcare_data_lake_implementation_dim_sensitivity
11. healthcare_data_lake_implementation_audit_policies
12. healthcare_data_lake_implementation_ref_sla
13. healthcare_data_lake_implementation_stage_certifications
14. healthcare_data_lake_implementation_fact_issues
15. healthcare_data_lake_implementation_dim_remediation_team
16. healthcare_data_lake_implementation_ref_controls
17. healthcare_data_lake_implementation_audit_certification
18. healthcare_data_lake_implementation_stage_policy_changes
19. healthcare_data_lake_implementation_ref_standards
20. healthcare_data_lake_implementation_dim_status

ER Diagram (ASCII):

healthcare_data_lake_implementation_fact_data_quality (dq_id, dataset_id, check_name, check_status, checked_ts)
  |-- dataset_id --> healthcare_data_lake_implementation_dim_dataset(dataset_id)

---

### Source D: Cost, Billing & Usage (Source: `healthcare_data_lake_implementation_cost`)

Tables (20):
1. healthcare_data_lake_implementation_stg_billing_records
2. healthcare_data_lake_implementation_raw_billing
3. healthcare_data_lake_implementation_dim_cost_center
4. healthcare_data_lake_implementation_dim_resource_type
5. healthcare_data_lake_implementation_dim_region
6. healthcare_data_lake_implementation_ref_price_catalog
7. healthcare_data_lake_implementation_fact_cost_usage
8. healthcare_data_lake_implementation_stage_allocations
9. healthcare_data_lake_implementation_dim_tagging
10. healthcare_data_lake_implementation_dim_currency
11. healthcare_data_lake_implementation_audit_billing_ingest
12. healthcare_data_lake_implementation_ref_discounts
13. healthcare_data_lake_implementation_stage_corrections
14. healthcare_data_lake_implementation_fact_monthly_costs
15. healthcare_data_lake_implementation_dim_billing_account
16. healthcare_data_lake_implementation_ref_chargeback_rules
17. healthcare_data_lake_implementation_audit_allocations
18. healthcare_data_lake_implementation_stage_forecasts
19. healthcare_data_lake_implementation_ref_rates
20. healthcare_data_lake_implementation_dim_status

ER Diagram (ASCII):

healthcare_data_lake_implementation_fact_cost_usage (usage_id, resource_id, cost_amount, currency, start_ts, end_ts)
  |-- resource_id --> healthcare_data_lake_implementation_dim_resource_type(resource_id)
  |-- cost_center_id --> healthcare_data_lake_implementation_dim_cost_center(cost_center_id)

---

### Source E: Canonical Transactions / Facts (Source: `healthcare_data_lake_implementation_txn`)

Tables (20):
1. healthcare_data_lake_implementation_stg_transactions
2. healthcare_data_lake_implementation_raw_transactions
3. healthcare_data_lake_implementation_dim_account
4. healthcare_data_lake_implementation_dim_customer
5. healthcare_data_lake_implementation_dim_product
6. healthcare_data_lake_implementation_ref_exchange_rates
7. healthcare_data_lake_implementation_fact_transactions
8. healthcare_data_lake_implementation_stage_reconciliations
9. healthcare_data_lake_implementation_dim_channel
10. healthcare_data_lake_implementation_dim_merchant
11. healthcare_data_lake_implementation_audit_txn_ingest
12. healthcare_data_lake_implementation_ref_fee_schedule
13. healthcare_data_lake_implementation_stage_settlements
14. healthcare_data_lake_implementation_fact_settlements
15. healthcare_data_lake_implementation_dim_status
16. healthcare_data_lake_implementation_ref_limits
17. healthcare_data_lake_implementation_audit_recon
18. healthcare_data_lake_implementation_stage_adjustments
19. healthcare_data_lake_implementation_fact_balance_snapshots
20. healthcare_data_lake_implementation_dim_time

ER Diagram (ASCII):

healthcare_data_lake_implementation_fact_transactions (transaction_id, account_id, amount, currency, txn_type, posted_ts)
  |-- account_id --> healthcare_data_lake_implementation_dim_account(account_id)
  |-- customer_id --> healthcare_data_lake_implementation_dim_customer(customer_id)
  |-- product_id --> healthcare_data_lake_implementation_dim_product(product_id)

Common guidance:
- Always keep an immutable staging/raw zone for auditable ingestion.
- Use `audit_*` tables and checksums for reconciliation between source and target facts.
- Implement SCD patterns for dimensions where history is required.
- Register datasets in a data catalog and apply RBAC and PII protections as required.

