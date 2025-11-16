# Customer Purchase Behavior Insights

Brief: Generate insights on purchase drivers, basket composition, and repeat behavior.

- Objectives:
  - Identify purchase patterns and drivers to improve conversions.
- Scope:
  - Transactions, returns, promotions, cross-sell signals.
- Key Components:
  - Basket analysis, cohort analysis, uplift studies.
- Technologies:
  - SQL/Analytics engine, Python for modeling, BI tools.
- Deliverables:
  - Insight reports, recommended interventions, dashboards.

# Expanded Source Schemas, ER Diagrams, Facts & Dimensions

This standardized expansion provides five logical sources for the project and a canonical set of artifacts to be appended to project markdown files when a detailed schema is required.

NOTE: The artifacts below are design artifacts created for documentation and implementation planning. They are original work and may be used for internal design and implementation purposes.

Project-specific prefix: `customer_purchase_behavior_insights` (derived from filename: `customer-purchase-behavior-insights.md`).

---

### Source A: Ingest & Landing (Source: `customer_purchase_behavior_insights_ingest`)

Tables (20):
1. customer_purchase_behavior_insights_stg_raw
2. customer_purchase_behavior_insights_raw_records
3. customer_purchase_behavior_insights_dim_source_system
4. customer_purchase_behavior_insights_dim_data_owner
5. customer_purchase_behavior_insights_dim_file_type
6. customer_purchase_behavior_insights_ref_file_schema
7. customer_purchase_behavior_insights_fact_raw_events
8. customer_purchase_behavior_insights_stage_enrichments
9. customer_purchase_behavior_insights_dim_geo
10. customer_purchase_behavior_insights_dim_business_unit
11. customer_purchase_behavior_insights_audit_ingest
12. customer_purchase_behavior_insights_dim_environment
13. customer_purchase_behavior_insights_ref_parsing_errors
14. customer_purchase_behavior_insights_stage_cdc
15. customer_purchase_behavior_insights_dim_schema_version
16. customer_purchase_behavior_insights_fact_event_counts
17. customer_purchase_behavior_insights_audit_transforms
18. customer_purchase_behavior_insights_stage_retries
19. customer_purchase_behavior_insights_ref_mappings
20. customer_purchase_behavior_insights_dim_status

ER Diagram (ASCII):

customer_purchase_behavior_insights_fact_raw_events (event_id, source_system_id, record_key, payload_hash, event_ts)
  |-- source_system_id --> customer_purchase_behavior_insights_dim_source_system(source_system_id)
  |-- record_key --> customer_purchase_behavior_insights_raw_records(record_key)

Description: Ingest staging (immutable) → raw normalization → enrichment → audit. `customer_purchase_behavior_insights_fact_raw_events` is used for throughput and source health monitoring.

---

### Source B: Operational Logs & Metrics (Source: `customer_purchase_behavior_insights_ops`)

Tables (20):
1. customer_purchase_behavior_insights_stg_ops_logs
2. customer_purchase_behavior_insights_raw_ops
3. customer_purchase_behavior_insights_dim_service
4. customer_purchase_behavior_insights_dim_instance
5. customer_purchase_behavior_insights_dim_log_level
6. customer_purchase_behavior_insights_ref_error_codes
7. customer_purchase_behavior_insights_fact_logs
8. customer_purchase_behavior_insights_stage_alerts
9. customer_purchase_behavior_insights_dim_team
10. customer_purchase_behavior_insights_dim_region
11. customer_purchase_behavior_insights_audit_ops_ingest
12. customer_purchase_behavior_insights_ref_runbooks
13. customer_purchase_behavior_insights_stage_incidents
14. customer_purchase_behavior_insights_fact_incident_metrics
15. customer_purchase_behavior_insights_dim_priority
16. customer_purchase_behavior_insights_ref_maintenance_windows
17. customer_purchase_behavior_insights_audit_recon
18. customer_purchase_behavior_insights_stage_trimmed_logs
19. customer_purchase_behavior_insights_ref_retention_policy
20. customer_purchase_behavior_insights_dim_status

ER Diagram (ASCII):

customer_purchase_behavior_insights_fact_logs (log_id, service_id, instance_id, log_level, message_ts)
  |-- service_id --> customer_purchase_behavior_insights_dim_service(service_id)
  |-- instance_id --> customer_purchase_behavior_insights_dim_instance(instance_id)

---

### Source C: Governance & Catalog (Source: `customer_purchase_behavior_insights_gov`)

Tables (20):
1. customer_purchase_behavior_insights_stg_catalog
2. customer_purchase_behavior_insights_raw_catalog
3. customer_purchase_behavior_insights_dim_dataset
4. customer_purchase_behavior_insights_dim_owner
5. customer_purchase_behavior_insights_dim_tag
6. customer_purchase_behavior_insights_ref_policies
7. customer_purchase_behavior_insights_fact_data_quality
8. customer_purchase_behavior_insights_stage_lineage
9. customer_purchase_behavior_insights_dim_classification
10. customer_purchase_behavior_insights_dim_sensitivity
11. customer_purchase_behavior_insights_audit_policies
12. customer_purchase_behavior_insights_ref_sla
13. customer_purchase_behavior_insights_stage_certifications
14. customer_purchase_behavior_insights_fact_issues
15. customer_purchase_behavior_insights_dim_remediation_team
16. customer_purchase_behavior_insights_ref_controls
17. customer_purchase_behavior_insights_audit_certification
18. customer_purchase_behavior_insights_stage_policy_changes
19. customer_purchase_behavior_insights_ref_standards
20. customer_purchase_behavior_insights_dim_status

ER Diagram (ASCII):

customer_purchase_behavior_insights_fact_data_quality (dq_id, dataset_id, check_name, check_status, checked_ts)
  |-- dataset_id --> customer_purchase_behavior_insights_dim_dataset(dataset_id)

---

### Source D: Cost, Billing & Usage (Source: `customer_purchase_behavior_insights_cost`)

Tables (20):
1. customer_purchase_behavior_insights_stg_billing_records
2. customer_purchase_behavior_insights_raw_billing
3. customer_purchase_behavior_insights_dim_cost_center
4. customer_purchase_behavior_insights_dim_resource_type
5. customer_purchase_behavior_insights_dim_region
6. customer_purchase_behavior_insights_ref_price_catalog
7. customer_purchase_behavior_insights_fact_cost_usage
8. customer_purchase_behavior_insights_stage_allocations
9. customer_purchase_behavior_insights_dim_tagging
10. customer_purchase_behavior_insights_dim_currency
11. customer_purchase_behavior_insights_audit_billing_ingest
12. customer_purchase_behavior_insights_ref_discounts
13. customer_purchase_behavior_insights_stage_corrections
14. customer_purchase_behavior_insights_fact_monthly_costs
15. customer_purchase_behavior_insights_dim_billing_account
16. customer_purchase_behavior_insights_ref_chargeback_rules
17. customer_purchase_behavior_insights_audit_allocations
18. customer_purchase_behavior_insights_stage_forecasts
19. customer_purchase_behavior_insights_ref_rates
20. customer_purchase_behavior_insights_dim_status

ER Diagram (ASCII):

customer_purchase_behavior_insights_fact_cost_usage (usage_id, resource_id, cost_amount, currency, start_ts, end_ts)
  |-- resource_id --> customer_purchase_behavior_insights_dim_resource_type(resource_id)
  |-- cost_center_id --> customer_purchase_behavior_insights_dim_cost_center(cost_center_id)

---

### Source E: Canonical Transactions / Facts (Source: `customer_purchase_behavior_insights_txn`)

Tables (20):
1. customer_purchase_behavior_insights_stg_transactions
2. customer_purchase_behavior_insights_raw_transactions
3. customer_purchase_behavior_insights_dim_account
4. customer_purchase_behavior_insights_dim_customer
5. customer_purchase_behavior_insights_dim_product
6. customer_purchase_behavior_insights_ref_exchange_rates
7. customer_purchase_behavior_insights_fact_transactions
8. customer_purchase_behavior_insights_stage_reconciliations
9. customer_purchase_behavior_insights_dim_channel
10. customer_purchase_behavior_insights_dim_merchant
11. customer_purchase_behavior_insights_audit_txn_ingest
12. customer_purchase_behavior_insights_ref_fee_schedule
13. customer_purchase_behavior_insights_stage_settlements
14. customer_purchase_behavior_insights_fact_settlements
15. customer_purchase_behavior_insights_dim_status
16. customer_purchase_behavior_insights_ref_limits
17. customer_purchase_behavior_insights_audit_recon
18. customer_purchase_behavior_insights_stage_adjustments
19. customer_purchase_behavior_insights_fact_balance_snapshots
20. customer_purchase_behavior_insights_dim_time

ER Diagram (ASCII):

customer_purchase_behavior_insights_fact_transactions (transaction_id, account_id, amount, currency, txn_type, posted_ts)
  |-- account_id --> customer_purchase_behavior_insights_dim_account(account_id)
  |-- customer_id --> customer_purchase_behavior_insights_dim_customer(customer_id)
  |-- product_id --> customer_purchase_behavior_insights_dim_product(product_id)

Common guidance:
- Always keep an immutable staging/raw zone for auditable ingestion.
- Use `audit_*` tables and checksums for reconciliation between source and target facts.
- Implement SCD patterns for dimensions where history is required.
- Register datasets in a data catalog and apply RBAC and PII protections as required.

