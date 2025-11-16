# Supply Chain Optimization Dashboard

Brief: Dashboard focused on optimized supply chain KPIs and recommendations.

- Objectives:
  - Highlight opportunities to reduce cost and lead times.
- Scope:
  - Inventory health, lead time variance, carrier performance.
- Key Components:
  - Optimization outputs, supplier SLAs, exception dashboards.
- Technologies:
  - BI tools, optimization engines, data pipelines.
- Deliverables:
  - Dashboard, runbooks, prioritized action list.

# Expanded Source Schemas, ER Diagrams, Facts & Dimensions

This standardized expansion provides five logical sources for the project and a canonical set of artifacts to be appended to project markdown files when a detailed schema is required.

NOTE: The artifacts below are design artifacts created for documentation and implementation planning. They are original work and may be used for internal design and implementation purposes.

Project-specific prefix: `supply_chain_optimization_dashboard` (derived from filename: `supply-chain-optimization-dashboard.md`).

---

### Source A: Ingest & Landing (Source: `supply_chain_optimization_dashboard_ingest`)

Tables (20):
1. supply_chain_optimization_dashboard_stg_raw
2. supply_chain_optimization_dashboard_raw_records
3. supply_chain_optimization_dashboard_dim_source_system
4. supply_chain_optimization_dashboard_dim_data_owner
5. supply_chain_optimization_dashboard_dim_file_type
6. supply_chain_optimization_dashboard_ref_file_schema
7. supply_chain_optimization_dashboard_fact_raw_events
8. supply_chain_optimization_dashboard_stage_enrichments
9. supply_chain_optimization_dashboard_dim_geo
10. supply_chain_optimization_dashboard_dim_business_unit
11. supply_chain_optimization_dashboard_audit_ingest
12. supply_chain_optimization_dashboard_dim_environment
13. supply_chain_optimization_dashboard_ref_parsing_errors
14. supply_chain_optimization_dashboard_stage_cdc
15. supply_chain_optimization_dashboard_dim_schema_version
16. supply_chain_optimization_dashboard_fact_event_counts
17. supply_chain_optimization_dashboard_audit_transforms
18. supply_chain_optimization_dashboard_stage_retries
19. supply_chain_optimization_dashboard_ref_mappings
20. supply_chain_optimization_dashboard_dim_status

ER Diagram (ASCII):

supply_chain_optimization_dashboard_fact_raw_events (event_id, source_system_id, record_key, payload_hash, event_ts)
  |-- source_system_id --> supply_chain_optimization_dashboard_dim_source_system(source_system_id)
  |-- record_key --> supply_chain_optimization_dashboard_raw_records(record_key)

Description: Ingest staging (immutable) → raw normalization → enrichment → audit. `supply_chain_optimization_dashboard_fact_raw_events` is used for throughput and source health monitoring.

---

### Source B: Operational Logs & Metrics (Source: `supply_chain_optimization_dashboard_ops`)

Tables (20):
1. supply_chain_optimization_dashboard_stg_ops_logs
2. supply_chain_optimization_dashboard_raw_ops
3. supply_chain_optimization_dashboard_dim_service
4. supply_chain_optimization_dashboard_dim_instance
5. supply_chain_optimization_dashboard_dim_log_level
6. supply_chain_optimization_dashboard_ref_error_codes
7. supply_chain_optimization_dashboard_fact_logs
8. supply_chain_optimization_dashboard_stage_alerts
9. supply_chain_optimization_dashboard_dim_team
10. supply_chain_optimization_dashboard_dim_region
11. supply_chain_optimization_dashboard_audit_ops_ingest
12. supply_chain_optimization_dashboard_ref_runbooks
13. supply_chain_optimization_dashboard_stage_incidents
14. supply_chain_optimization_dashboard_fact_incident_metrics
15. supply_chain_optimization_dashboard_dim_priority
16. supply_chain_optimization_dashboard_ref_maintenance_windows
17. supply_chain_optimization_dashboard_audit_recon
18. supply_chain_optimization_dashboard_stage_trimmed_logs
19. supply_chain_optimization_dashboard_ref_retention_policy
20. supply_chain_optimization_dashboard_dim_status

ER Diagram (ASCII):

supply_chain_optimization_dashboard_fact_logs (log_id, service_id, instance_id, log_level, message_ts)
  |-- service_id --> supply_chain_optimization_dashboard_dim_service(service_id)
  |-- instance_id --> supply_chain_optimization_dashboard_dim_instance(instance_id)

---

### Source C: Governance & Catalog (Source: `supply_chain_optimization_dashboard_gov`)

Tables (20):
1. supply_chain_optimization_dashboard_stg_catalog
2. supply_chain_optimization_dashboard_raw_catalog
3. supply_chain_optimization_dashboard_dim_dataset
4. supply_chain_optimization_dashboard_dim_owner
5. supply_chain_optimization_dashboard_dim_tag
6. supply_chain_optimization_dashboard_ref_policies
7. supply_chain_optimization_dashboard_fact_data_quality
8. supply_chain_optimization_dashboard_stage_lineage
9. supply_chain_optimization_dashboard_dim_classification
10. supply_chain_optimization_dashboard_dim_sensitivity
11. supply_chain_optimization_dashboard_audit_policies
12. supply_chain_optimization_dashboard_ref_sla
13. supply_chain_optimization_dashboard_stage_certifications
14. supply_chain_optimization_dashboard_fact_issues
15. supply_chain_optimization_dashboard_dim_remediation_team
16. supply_chain_optimization_dashboard_ref_controls
17. supply_chain_optimization_dashboard_audit_certification
18. supply_chain_optimization_dashboard_stage_policy_changes
19. supply_chain_optimization_dashboard_ref_standards
20. supply_chain_optimization_dashboard_dim_status

ER Diagram (ASCII):

supply_chain_optimization_dashboard_fact_data_quality (dq_id, dataset_id, check_name, check_status, checked_ts)
  |-- dataset_id --> supply_chain_optimization_dashboard_dim_dataset(dataset_id)

---

### Source D: Cost, Billing & Usage (Source: `supply_chain_optimization_dashboard_cost`)

Tables (20):
1. supply_chain_optimization_dashboard_stg_billing_records
2. supply_chain_optimization_dashboard_raw_billing
3. supply_chain_optimization_dashboard_dim_cost_center
4. supply_chain_optimization_dashboard_dim_resource_type
5. supply_chain_optimization_dashboard_dim_region
6. supply_chain_optimization_dashboard_ref_price_catalog
7. supply_chain_optimization_dashboard_fact_cost_usage
8. supply_chain_optimization_dashboard_stage_allocations
9. supply_chain_optimization_dashboard_dim_tagging
10. supply_chain_optimization_dashboard_dim_currency
11. supply_chain_optimization_dashboard_audit_billing_ingest
12. supply_chain_optimization_dashboard_ref_discounts
13. supply_chain_optimization_dashboard_stage_corrections
14. supply_chain_optimization_dashboard_fact_monthly_costs
15. supply_chain_optimization_dashboard_dim_billing_account
16. supply_chain_optimization_dashboard_ref_chargeback_rules
17. supply_chain_optimization_dashboard_audit_allocations
18. supply_chain_optimization_dashboard_stage_forecasts
19. supply_chain_optimization_dashboard_ref_rates
20. supply_chain_optimization_dashboard_dim_status

ER Diagram (ASCII):

supply_chain_optimization_dashboard_fact_cost_usage (usage_id, resource_id, cost_amount, currency, start_ts, end_ts)
  |-- resource_id --> supply_chain_optimization_dashboard_dim_resource_type(resource_id)
  |-- cost_center_id --> supply_chain_optimization_dashboard_dim_cost_center(cost_center_id)

---

### Source E: Canonical Transactions / Facts (Source: `supply_chain_optimization_dashboard_txn`)

Tables (20):
1. supply_chain_optimization_dashboard_stg_transactions
2. supply_chain_optimization_dashboard_raw_transactions
3. supply_chain_optimization_dashboard_dim_account
4. supply_chain_optimization_dashboard_dim_customer
5. supply_chain_optimization_dashboard_dim_product
6. supply_chain_optimization_dashboard_ref_exchange_rates
7. supply_chain_optimization_dashboard_fact_transactions
8. supply_chain_optimization_dashboard_stage_reconciliations
9. supply_chain_optimization_dashboard_dim_channel
10. supply_chain_optimization_dashboard_dim_merchant
11. supply_chain_optimization_dashboard_audit_txn_ingest
12. supply_chain_optimization_dashboard_ref_fee_schedule
13. supply_chain_optimization_dashboard_stage_settlements
14. supply_chain_optimization_dashboard_fact_settlements
15. supply_chain_optimization_dashboard_dim_status
16. supply_chain_optimization_dashboard_ref_limits
17. supply_chain_optimization_dashboard_audit_recon
18. supply_chain_optimization_dashboard_stage_adjustments
19. supply_chain_optimization_dashboard_fact_balance_snapshots
20. supply_chain_optimization_dashboard_dim_time

ER Diagram (ASCII):

supply_chain_optimization_dashboard_fact_transactions (transaction_id, account_id, amount, currency, txn_type, posted_ts)
  |-- account_id --> supply_chain_optimization_dashboard_dim_account(account_id)
  |-- customer_id --> supply_chain_optimization_dashboard_dim_customer(customer_id)
  |-- product_id --> supply_chain_optimization_dashboard_dim_product(product_id)

Common guidance:
- Always keep an immutable staging/raw zone for auditable ingestion.
- Use `audit_*` tables and checksums for reconciliation between source and target facts.
- Implement SCD patterns for dimensions where history is required.
- Register datasets in a data catalog and apply RBAC and PII protections as required.

