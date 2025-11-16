# Real-time Retail Performance Dashboard

Brief: Dashboard showing near real-time KPIs for retail operations.

- Objectives:
  - Provide live visibility into sales, traffic, and fulfillment.
- Scope:
  - Streaming data ingestion, low-latency aggregation.
- Key Components:
  - Stream processors, materialized views, dashboarding layer.
- Technologies:
  - Kafka/Event Hubs, ksql/structured streaming, Power BI/Realtime UI.
- Deliverables:
  - Realtime dashboards, SLA definitions, alerting.

# Expanded Source Schemas, ER Diagrams, Facts & Dimensions

This standardized expansion provides five logical sources for the project and a canonical set of artifacts to be appended to project markdown files when a detailed schema is required.

NOTE: The artifacts below are design artifacts created for documentation and implementation planning. They are original work and may be used for internal design and implementation purposes.

Project-specific prefix: `real_time_retail_performance_dashboard` (derived from filename: `real-time-retail-performance-dashboard.md`).

---

### Source A: Ingest & Landing (Source: `real_time_retail_performance_dashboard_ingest`)

Tables (20):
1. real_time_retail_performance_dashboard_stg_raw
2. real_time_retail_performance_dashboard_raw_records
3. real_time_retail_performance_dashboard_dim_source_system
4. real_time_retail_performance_dashboard_dim_data_owner
5. real_time_retail_performance_dashboard_dim_file_type
6. real_time_retail_performance_dashboard_ref_file_schema
7. real_time_retail_performance_dashboard_fact_raw_events
8. real_time_retail_performance_dashboard_stage_enrichments
9. real_time_retail_performance_dashboard_dim_geo
10. real_time_retail_performance_dashboard_dim_business_unit
11. real_time_retail_performance_dashboard_audit_ingest
12. real_time_retail_performance_dashboard_dim_environment
13. real_time_retail_performance_dashboard_ref_parsing_errors
14. real_time_retail_performance_dashboard_stage_cdc
15. real_time_retail_performance_dashboard_dim_schema_version
16. real_time_retail_performance_dashboard_fact_event_counts
17. real_time_retail_performance_dashboard_audit_transforms
18. real_time_retail_performance_dashboard_stage_retries
19. real_time_retail_performance_dashboard_ref_mappings
20. real_time_retail_performance_dashboard_dim_status

ER Diagram (ASCII):

real_time_retail_performance_dashboard_fact_raw_events (event_id, source_system_id, record_key, payload_hash, event_ts)
  |-- source_system_id --> real_time_retail_performance_dashboard_dim_source_system(source_system_id)
  |-- record_key --> real_time_retail_performance_dashboard_raw_records(record_key)

Description: Ingest staging (immutable) → raw normalization → enrichment → audit. `real_time_retail_performance_dashboard_fact_raw_events` is used for throughput and source health monitoring.

---

### Source B: Operational Logs & Metrics (Source: `real_time_retail_performance_dashboard_ops`)

Tables (20):
1. real_time_retail_performance_dashboard_stg_ops_logs
2. real_time_retail_performance_dashboard_raw_ops
3. real_time_retail_performance_dashboard_dim_service
4. real_time_retail_performance_dashboard_dim_instance
5. real_time_retail_performance_dashboard_dim_log_level
6. real_time_retail_performance_dashboard_ref_error_codes
7. real_time_retail_performance_dashboard_fact_logs
8. real_time_retail_performance_dashboard_stage_alerts
9. real_time_retail_performance_dashboard_dim_team
10. real_time_retail_performance_dashboard_dim_region
11. real_time_retail_performance_dashboard_audit_ops_ingest
12. real_time_retail_performance_dashboard_ref_runbooks
13. real_time_retail_performance_dashboard_stage_incidents
14. real_time_retail_performance_dashboard_fact_incident_metrics
15. real_time_retail_performance_dashboard_dim_priority
16. real_time_retail_performance_dashboard_ref_maintenance_windows
17. real_time_retail_performance_dashboard_audit_recon
18. real_time_retail_performance_dashboard_stage_trimmed_logs
19. real_time_retail_performance_dashboard_ref_retention_policy
20. real_time_retail_performance_dashboard_dim_status

ER Diagram (ASCII):

real_time_retail_performance_dashboard_fact_logs (log_id, service_id, instance_id, log_level, message_ts)
  |-- service_id --> real_time_retail_performance_dashboard_dim_service(service_id)
  |-- instance_id --> real_time_retail_performance_dashboard_dim_instance(instance_id)

---

### Source C: Governance & Catalog (Source: `real_time_retail_performance_dashboard_gov`)

Tables (20):
1. real_time_retail_performance_dashboard_stg_catalog
2. real_time_retail_performance_dashboard_raw_catalog
3. real_time_retail_performance_dashboard_dim_dataset
4. real_time_retail_performance_dashboard_dim_owner
5. real_time_retail_performance_dashboard_dim_tag
6. real_time_retail_performance_dashboard_ref_policies
7. real_time_retail_performance_dashboard_fact_data_quality
8. real_time_retail_performance_dashboard_stage_lineage
9. real_time_retail_performance_dashboard_dim_classification
10. real_time_retail_performance_dashboard_dim_sensitivity
11. real_time_retail_performance_dashboard_audit_policies
12. real_time_retail_performance_dashboard_ref_sla
13. real_time_retail_performance_dashboard_stage_certifications
14. real_time_retail_performance_dashboard_fact_issues
15. real_time_retail_performance_dashboard_dim_remediation_team
16. real_time_retail_performance_dashboard_ref_controls
17. real_time_retail_performance_dashboard_audit_certification
18. real_time_retail_performance_dashboard_stage_policy_changes
19. real_time_retail_performance_dashboard_ref_standards
20. real_time_retail_performance_dashboard_dim_status

ER Diagram (ASCII):

real_time_retail_performance_dashboard_fact_data_quality (dq_id, dataset_id, check_name, check_status, checked_ts)
  |-- dataset_id --> real_time_retail_performance_dashboard_dim_dataset(dataset_id)

---

### Source D: Cost, Billing & Usage (Source: `real_time_retail_performance_dashboard_cost`)

Tables (20):
1. real_time_retail_performance_dashboard_stg_billing_records
2. real_time_retail_performance_dashboard_raw_billing
3. real_time_retail_performance_dashboard_dim_cost_center
4. real_time_retail_performance_dashboard_dim_resource_type
5. real_time_retail_performance_dashboard_dim_region
6. real_time_retail_performance_dashboard_ref_price_catalog
7. real_time_retail_performance_dashboard_fact_cost_usage
8. real_time_retail_performance_dashboard_stage_allocations
9. real_time_retail_performance_dashboard_dim_tagging
10. real_time_retail_performance_dashboard_dim_currency
11. real_time_retail_performance_dashboard_audit_billing_ingest
12. real_time_retail_performance_dashboard_ref_discounts
13. real_time_retail_performance_dashboard_stage_corrections
14. real_time_retail_performance_dashboard_fact_monthly_costs
15. real_time_retail_performance_dashboard_dim_billing_account
16. real_time_retail_performance_dashboard_ref_chargeback_rules
17. real_time_retail_performance_dashboard_audit_allocations
18. real_time_retail_performance_dashboard_stage_forecasts
19. real_time_retail_performance_dashboard_ref_rates
20. real_time_retail_performance_dashboard_dim_status

ER Diagram (ASCII):

real_time_retail_performance_dashboard_fact_cost_usage (usage_id, resource_id, cost_amount, currency, start_ts, end_ts)
  |-- resource_id --> real_time_retail_performance_dashboard_dim_resource_type(resource_id)
  |-- cost_center_id --> real_time_retail_performance_dashboard_dim_cost_center(cost_center_id)

---

### Source E: Canonical Transactions / Facts (Source: `real_time_retail_performance_dashboard_txn`)

Tables (20):
1. real_time_retail_performance_dashboard_stg_transactions
2. real_time_retail_performance_dashboard_raw_transactions
3. real_time_retail_performance_dashboard_dim_account
4. real_time_retail_performance_dashboard_dim_customer
5. real_time_retail_performance_dashboard_dim_product
6. real_time_retail_performance_dashboard_ref_exchange_rates
7. real_time_retail_performance_dashboard_fact_transactions
8. real_time_retail_performance_dashboard_stage_reconciliations
9. real_time_retail_performance_dashboard_dim_channel
10. real_time_retail_performance_dashboard_dim_merchant
11. real_time_retail_performance_dashboard_audit_txn_ingest
12. real_time_retail_performance_dashboard_ref_fee_schedule
13. real_time_retail_performance_dashboard_stage_settlements
14. real_time_retail_performance_dashboard_fact_settlements
15. real_time_retail_performance_dashboard_dim_status
16. real_time_retail_performance_dashboard_ref_limits
17. real_time_retail_performance_dashboard_audit_recon
18. real_time_retail_performance_dashboard_stage_adjustments
19. real_time_retail_performance_dashboard_fact_balance_snapshots
20. real_time_retail_performance_dashboard_dim_time

ER Diagram (ASCII):

real_time_retail_performance_dashboard_fact_transactions (transaction_id, account_id, amount, currency, txn_type, posted_ts)
  |-- account_id --> real_time_retail_performance_dashboard_dim_account(account_id)
  |-- customer_id --> real_time_retail_performance_dashboard_dim_customer(customer_id)
  |-- product_id --> real_time_retail_performance_dashboard_dim_product(product_id)

Common guidance:
- Always keep an immutable staging/raw zone for auditable ingestion.
- Use `audit_*` tables and checksums for reconciliation between source and target facts.
- Implement SCD patterns for dimensions where history is required.
- Register datasets in a data catalog and apply RBAC and PII protections as required.

