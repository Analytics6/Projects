# Cloud Data Migration

Brief: Projects to migrate data assets to the cloud with minimal disruption.

- Objectives:
  - Move data and workloads while ensuring integrity and continuity.
- Scope:
  - Discovery, pilots, full migrations, cutovers.
- Key Components:
  - Migration tools, validation suites, rollback plans.
- Technologies:
  - Azure Migrate, Data Factory, cloud-native stores.
- Deliverables:
  - Migration plans, validation reports, cutover scripts.

# Expanded Source Schemas, ER Diagrams, Facts & Dimensions

This standardized expansion provides five logical sources for the project and a canonical set of artifacts to be appended to project markdown files when a detailed schema is required.

NOTE: The artifacts below are design artifacts created for documentation and implementation planning. They are original work and may be used for internal design and implementation purposes.

Project-specific prefix: `cloud_data_migration` (derived from filename: `cloud-data-migration.md`).

---

### Source A: Ingest & Landing (Source: `cloud_data_migration_ingest`)

Tables (20):
1. cloud_data_migration_stg_raw
2. cloud_data_migration_raw_records
3. cloud_data_migration_dim_source_system
4. cloud_data_migration_dim_data_owner
5. cloud_data_migration_dim_file_type
6. cloud_data_migration_ref_file_schema
7. cloud_data_migration_fact_raw_events
8. cloud_data_migration_stage_enrichments
9. cloud_data_migration_dim_geo
10. cloud_data_migration_dim_business_unit
11. cloud_data_migration_audit_ingest
12. cloud_data_migration_dim_environment
13. cloud_data_migration_ref_parsing_errors
14. cloud_data_migration_stage_cdc
15. cloud_data_migration_dim_schema_version
16. cloud_data_migration_fact_event_counts
17. cloud_data_migration_audit_transforms
18. cloud_data_migration_stage_retries
19. cloud_data_migration_ref_mappings
20. cloud_data_migration_dim_status

ER Diagram (ASCII):

cloud_data_migration_fact_raw_events (event_id, source_system_id, record_key, payload_hash, event_ts)
  |-- source_system_id --> cloud_data_migration_dim_source_system(source_system_id)
  |-- record_key --> cloud_data_migration_raw_records(record_key)

Description: Ingest staging (immutable) → raw normalization → enrichment → audit. `cloud_data_migration_fact_raw_events` is used for throughput and source health monitoring.

---

### Source B: Operational Logs & Metrics (Source: `cloud_data_migration_ops`)

Tables (20):
1. cloud_data_migration_stg_ops_logs
2. cloud_data_migration_raw_ops
3. cloud_data_migration_dim_service
4. cloud_data_migration_dim_instance
5. cloud_data_migration_dim_log_level
6. cloud_data_migration_ref_error_codes
7. cloud_data_migration_fact_logs
8. cloud_data_migration_stage_alerts
9. cloud_data_migration_dim_team
10. cloud_data_migration_dim_region
11. cloud_data_migration_audit_ops_ingest
12. cloud_data_migration_ref_runbooks
13. cloud_data_migration_stage_incidents
14. cloud_data_migration_fact_incident_metrics
15. cloud_data_migration_dim_priority
16. cloud_data_migration_ref_maintenance_windows
17. cloud_data_migration_audit_recon
18. cloud_data_migration_stage_trimmed_logs
19. cloud_data_migration_ref_retention_policy
20. cloud_data_migration_dim_status

ER Diagram (ASCII):

cloud_data_migration_fact_logs (log_id, service_id, instance_id, log_level, message_ts)
  |-- service_id --> cloud_data_migration_dim_service(service_id)
  |-- instance_id --> cloud_data_migration_dim_instance(instance_id)

---

### Source C: Governance & Catalog (Source: `cloud_data_migration_gov`)

Tables (20):
1. cloud_data_migration_stg_catalog
2. cloud_data_migration_raw_catalog
3. cloud_data_migration_dim_dataset
4. cloud_data_migration_dim_owner
5. cloud_data_migration_dim_tag
6. cloud_data_migration_ref_policies
7. cloud_data_migration_fact_data_quality
8. cloud_data_migration_stage_lineage
9. cloud_data_migration_dim_classification
10. cloud_data_migration_dim_sensitivity
11. cloud_data_migration_audit_policies
12. cloud_data_migration_ref_sla
13. cloud_data_migration_stage_certifications
14. cloud_data_migration_fact_issues
15. cloud_data_migration_dim_remediation_team
16. cloud_data_migration_ref_controls
17. cloud_data_migration_audit_certification
18. cloud_data_migration_stage_policy_changes
19. cloud_data_migration_ref_standards
20. cloud_data_migration_dim_status

ER Diagram (ASCII):

cloud_data_migration_fact_data_quality (dq_id, dataset_id, check_name, check_status, checked_ts)
  |-- dataset_id --> cloud_data_migration_dim_dataset(dataset_id)

---

### Source D: Cost, Billing & Usage (Source: `cloud_data_migration_cost`)

Tables (20):
1. cloud_data_migration_stg_billing_records
2. cloud_data_migration_raw_billing
3. cloud_data_migration_dim_cost_center
4. cloud_data_migration_dim_resource_type
5. cloud_data_migration_dim_region
6. cloud_data_migration_ref_price_catalog
7. cloud_data_migration_fact_cost_usage
8. cloud_data_migration_stage_allocations
9. cloud_data_migration_dim_tagging
10. cloud_data_migration_dim_currency
11. cloud_data_migration_audit_billing_ingest
12. cloud_data_migration_ref_discounts
13. cloud_data_migration_stage_corrections
14. cloud_data_migration_fact_monthly_costs
15. cloud_data_migration_dim_billing_account
16. cloud_data_migration_ref_chargeback_rules
17. cloud_data_migration_audit_allocations
18. cloud_data_migration_stage_forecasts
19. cloud_data_migration_ref_rates
20. cloud_data_migration_dim_status

ER Diagram (ASCII):

cloud_data_migration_fact_cost_usage (usage_id, resource_id, cost_amount, currency, start_ts, end_ts)
  |-- resource_id --> cloud_data_migration_dim_resource_type(resource_id)
  |-- cost_center_id --> cloud_data_migration_dim_cost_center(cost_center_id)

---

### Source E: Canonical Transactions / Facts (Source: `cloud_data_migration_txn`)

Tables (20):
1. cloud_data_migration_stg_transactions
2. cloud_data_migration_raw_transactions
3. cloud_data_migration_dim_account
4. cloud_data_migration_dim_customer
5. cloud_data_migration_dim_product
6. cloud_data_migration_ref_exchange_rates
7. cloud_data_migration_fact_transactions
8. cloud_data_migration_stage_reconciliations
9. cloud_data_migration_dim_channel
10. cloud_data_migration_dim_merchant
11. cloud_data_migration_audit_txn_ingest
12. cloud_data_migration_ref_fee_schedule
13. cloud_data_migration_stage_settlements
14. cloud_data_migration_fact_settlements
15. cloud_data_migration_dim_status
16. cloud_data_migration_ref_limits
17. cloud_data_migration_audit_recon
18. cloud_data_migration_stage_adjustments
19. cloud_data_migration_fact_balance_snapshots
20. cloud_data_migration_dim_time

ER Diagram (ASCII):

cloud_data_migration_fact_transactions (transaction_id, account_id, amount, currency, txn_type, posted_ts)
  |-- account_id --> cloud_data_migration_dim_account(account_id)
  |-- customer_id --> cloud_data_migration_dim_customer(customer_id)
  |-- product_id --> cloud_data_migration_dim_product(product_id)

Common guidance:
- Always keep an immutable staging/raw zone for auditable ingestion.
- Use `audit_*` tables and checksums for reconciliation between source and target facts.
- Implement SCD patterns for dimensions where history is required.
- Register datasets in a data catalog and apply RBAC and PII protections as required.

