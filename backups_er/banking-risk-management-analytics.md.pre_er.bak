# Banking Risk Management Analytics

Brief: Analytics to detect, quantify, and monitor banking risks.

- Objectives:
  - Implement measurement and monitoring for credit, market, and operational risk.
- Scope:
  - Exposure calculations, stress testing, dashboards.
- Key Components:
  - Risk data mart, model pipelines, reporting layer.
- Technologies:
  - Python, R, Databricks, secure data stores.
- Deliverables:
  - Risk reports, dashboards, model validation docs.

# Expanded Source Schemas, ER Diagrams, Facts & Dimensions

This standardized expansion provides five logical sources for the project and a canonical set of artifacts to be appended to project markdown files when a detailed schema is required.

NOTE: The artifacts below are design artifacts created for documentation and implementation planning. They are original work and may be used for internal design and implementation purposes.

Project-specific prefix: `banking_risk_management_analytics` (derived from filename: `banking-risk-management-analytics.md`).

---

### Source A: Ingest & Landing (Source: `banking_risk_management_analytics_ingest`)

Tables (20):
1. banking_risk_management_analytics_stg_raw
2. banking_risk_management_analytics_raw_records
3. banking_risk_management_analytics_dim_source_system
4. banking_risk_management_analytics_dim_data_owner
5. banking_risk_management_analytics_dim_file_type
6. banking_risk_management_analytics_ref_file_schema
7. banking_risk_management_analytics_fact_raw_events
8. banking_risk_management_analytics_stage_enrichments
9. banking_risk_management_analytics_dim_geo
10. banking_risk_management_analytics_dim_business_unit
11. banking_risk_management_analytics_audit_ingest
12. banking_risk_management_analytics_dim_environment
13. banking_risk_management_analytics_ref_parsing_errors
14. banking_risk_management_analytics_stage_cdc
15. banking_risk_management_analytics_dim_schema_version
16. banking_risk_management_analytics_fact_event_counts
17. banking_risk_management_analytics_audit_transforms
18. banking_risk_management_analytics_stage_retries
19. banking_risk_management_analytics_ref_mappings
20. banking_risk_management_analytics_dim_status

ER Diagram (ASCII):

banking_risk_management_analytics_fact_raw_events (event_id, source_system_id, record_key, payload_hash, event_ts)
  |-- source_system_id --> banking_risk_management_analytics_dim_source_system(source_system_id)
  |-- record_key --> banking_risk_management_analytics_raw_records(record_key)

Description: Ingest staging (immutable) → raw normalization → enrichment → audit. `banking_risk_management_analytics_fact_raw_events` is used for throughput and source health monitoring.

---

### Source B: Operational Logs & Metrics (Source: `banking_risk_management_analytics_ops`)

Tables (20):
1. banking_risk_management_analytics_stg_ops_logs
2. banking_risk_management_analytics_raw_ops
3. banking_risk_management_analytics_dim_service
4. banking_risk_management_analytics_dim_instance
5. banking_risk_management_analytics_dim_log_level
6. banking_risk_management_analytics_ref_error_codes
7. banking_risk_management_analytics_fact_logs
8. banking_risk_management_analytics_stage_alerts
9. banking_risk_management_analytics_dim_team
10. banking_risk_management_analytics_dim_region
11. banking_risk_management_analytics_audit_ops_ingest
12. banking_risk_management_analytics_ref_runbooks
13. banking_risk_management_analytics_stage_incidents
14. banking_risk_management_analytics_fact_incident_metrics
15. banking_risk_management_analytics_dim_priority
16. banking_risk_management_analytics_ref_maintenance_windows
17. banking_risk_management_analytics_audit_recon
18. banking_risk_management_analytics_stage_trimmed_logs
19. banking_risk_management_analytics_ref_retention_policy
20. banking_risk_management_analytics_dim_status

ER Diagram (ASCII):

banking_risk_management_analytics_fact_logs (log_id, service_id, instance_id, log_level, message_ts)
  |-- service_id --> banking_risk_management_analytics_dim_service(service_id)
  |-- instance_id --> banking_risk_management_analytics_dim_instance(instance_id)

---

### Source C: Governance & Catalog (Source: `banking_risk_management_analytics_gov`)

Tables (20):
1. banking_risk_management_analytics_stg_catalog
2. banking_risk_management_analytics_raw_catalog
3. banking_risk_management_analytics_dim_dataset
4. banking_risk_management_analytics_dim_owner
5. banking_risk_management_analytics_dim_tag
6. banking_risk_management_analytics_ref_policies
7. banking_risk_management_analytics_fact_data_quality
8. banking_risk_management_analytics_stage_lineage
9. banking_risk_management_analytics_dim_classification
10. banking_risk_management_analytics_dim_sensitivity
11. banking_risk_management_analytics_audit_policies
12. banking_risk_management_analytics_ref_sla
13. banking_risk_management_analytics_stage_certifications
14. banking_risk_management_analytics_fact_issues
15. banking_risk_management_analytics_dim_remediation_team
16. banking_risk_management_analytics_ref_controls
17. banking_risk_management_analytics_audit_certification
18. banking_risk_management_analytics_stage_policy_changes
19. banking_risk_management_analytics_ref_standards
20. banking_risk_management_analytics_dim_status

ER Diagram (ASCII):

banking_risk_management_analytics_fact_data_quality (dq_id, dataset_id, check_name, check_status, checked_ts)
  |-- dataset_id --> banking_risk_management_analytics_dim_dataset(dataset_id)

---

### Source D: Cost, Billing & Usage (Source: `banking_risk_management_analytics_cost`)

Tables (20):
1. banking_risk_management_analytics_stg_billing_records
2. banking_risk_management_analytics_raw_billing
3. banking_risk_management_analytics_dim_cost_center
4. banking_risk_management_analytics_dim_resource_type
5. banking_risk_management_analytics_dim_region
6. banking_risk_management_analytics_ref_price_catalog
7. banking_risk_management_analytics_fact_cost_usage
8. banking_risk_management_analytics_stage_allocations
9. banking_risk_management_analytics_dim_tagging
10. banking_risk_management_analytics_dim_currency
11. banking_risk_management_analytics_audit_billing_ingest
12. banking_risk_management_analytics_ref_discounts
13. banking_risk_management_analytics_stage_corrections
14. banking_risk_management_analytics_fact_monthly_costs
15. banking_risk_management_analytics_dim_billing_account
16. banking_risk_management_analytics_ref_chargeback_rules
17. banking_risk_management_analytics_audit_allocations
18. banking_risk_management_analytics_stage_forecasts
19. banking_risk_management_analytics_ref_rates
20. banking_risk_management_analytics_dim_status

ER Diagram (ASCII):

banking_risk_management_analytics_fact_cost_usage (usage_id, resource_id, cost_amount, currency, start_ts, end_ts)
  |-- resource_id --> banking_risk_management_analytics_dim_resource_type(resource_id)
  |-- cost_center_id --> banking_risk_management_analytics_dim_cost_center(cost_center_id)

---

### Source E: Canonical Transactions / Facts (Source: `banking_risk_management_analytics_txn`)

Tables (20):
1. banking_risk_management_analytics_stg_transactions
2. banking_risk_management_analytics_raw_transactions
3. banking_risk_management_analytics_dim_account
4. banking_risk_management_analytics_dim_customer
5. banking_risk_management_analytics_dim_product
6. banking_risk_management_analytics_ref_exchange_rates
7. banking_risk_management_analytics_fact_transactions
8. banking_risk_management_analytics_stage_reconciliations
9. banking_risk_management_analytics_dim_channel
10. banking_risk_management_analytics_dim_merchant
11. banking_risk_management_analytics_audit_txn_ingest
12. banking_risk_management_analytics_ref_fee_schedule
13. banking_risk_management_analytics_stage_settlements
14. banking_risk_management_analytics_fact_settlements
15. banking_risk_management_analytics_dim_status
16. banking_risk_management_analytics_ref_limits
17. banking_risk_management_analytics_audit_recon
18. banking_risk_management_analytics_stage_adjustments
19. banking_risk_management_analytics_fact_balance_snapshots
20. banking_risk_management_analytics_dim_time

ER Diagram (ASCII):

banking_risk_management_analytics_fact_transactions (transaction_id, account_id, amount, currency, txn_type, posted_ts)
  |-- account_id --> banking_risk_management_analytics_dim_account(account_id)
  |-- customer_id --> banking_risk_management_analytics_dim_customer(customer_id)
  |-- product_id --> banking_risk_management_analytics_dim_product(product_id)

Common guidance:
- Always keep an immutable staging/raw zone for auditable ingestion.
- Use `audit_*` tables and checksums for reconciliation between source and target facts.
- Implement SCD patterns for dimensions where history is required.
- Register datasets in a data catalog and apply RBAC and PII protections as required.

