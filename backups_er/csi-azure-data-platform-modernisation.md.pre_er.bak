# CSI – Azure Data Platform Modernisation

Brief: Modernise CSI's Azure data platform to current best practices.

- Objectives:
  - Move to a lakehouse, add governance and cost optimization.
- Scope:
  - Architecture refactor, migration, governance rollout.
- Key Components:
  - Lakehouse migration, Purview, performance tuning.
- Technologies:
  - Azure Databricks, Synapse, Purview.
- Deliverables:
  - Modernised platform, migration guides, cost metrics.

## Expanded Source Schemas, ER Diagrams, Facts & Dimensions

This section provides a standardized expansion: five logical sources per project, each with 20 tables (staging, raw, dims, facts, refs, audit), an ER-style diagram, fact/dimension details, reconciliation patterns, and a rights statement that these diagrams are original design artifacts.

Source naming uses a project-specific prefix `csi_`.

### Source A: Ingest & Landing (Source: csi_ingest)

Tables (20):
1. csi_stg_raw_events
2. csi_raw_records
3. csi_dim_source_system
4. csi_dim_data_owner
5. csi_dim_file_type
6. csi_ref_file_schema
7. csi_fact_raw_events
8. csi_stage_enrichments
9. csi_dim_geo
10. csi_dim_business_unit
11. csi_audit_ingest
12. csi_dim_environment
13. csi_ref_parsing_errors
14. csi_stage_cdc
15. csi_dim_schema_version
16. csi_fact_event_counts
17. csi_audit_transforms
18. csi_stage_retries
19. csi_ref_mappings
20. csi_dim_status

ER Diagram (ASCII):

csi_fact_raw_events (event_id, source_system_id, record_key, payload_hash, event_ts)
  |-- source_system_id --> csi_dim_source_system(source_system_id)
  |-- record_key --> csi_raw_records(record_key)

Fact/Dimension Notes:
- `csi_fact_raw_events`: grain is one ingested record; used to monitor throughput, duplicates, and source health.
- `csi_dim_source_system`: identifies upstream systems and owners.

Rights Statement: I confirm these flow diagrams and schema designs are original artifacts created for this engagement and may be used for internal design and implementation documentation.

---

### Source B: Operational Logs (Source: csi_ops)

Tables (20):
1. csi_stg_ops_logs
2. csi_raw_ops
3. csi_dim_service
4. csi_dim_instance
5. csi_dim_log_level
6. csi_ref_error_codes
7. csi_fact_logs
8. csi_stage_alerts
9. csi_dim_team
10. csi_dim_region
11. csi_audit_ops_ingest
12. csi_ref_runbooks
13. csi_stage_incidents
14. csi_fact_incident_metrics
15. csi_dim_priority
16. csi_ref_maintenance_windows
17. csi_audit_recon
18. csi_stage_trimmed_logs
19. csi_ref_retention_policy
20. csi_dim_status

ER Diagram (ASCII):

csi_fact_logs (log_id, service_id, instance_id, log_level, message_ts)
  |-- service_id --> csi_dim_service(service_id)
  |-- instance_id --> csi_dim_instance(instance_id)

Description: Logs are captured at event granularity and rolled up into incident and availability metrics.

---

### Source C: Governance Metadata (Source: csi_gov)

Tables (20):
1. csi_stg_catalog
2. csi_raw_catalog
3. csi_dim_dataset
4. csi_dim_owner
5. csi_dim_tag
6. csi_ref_policies
7. csi_fact_data_quality
8. csi_stage_lineage
9. csi_dim_classification
10. csi_dim_sensitivity
11. csi_audit_policies
12. csi_ref_sla
13. csi_stage_certifications
14. csi_fact_issues
15. csi_dim_remediation_team
16. csi_ref_controls
17. csi_audit_certification
18. csi_stage_policy_changes
19. csi_ref_standards
20. csi_dim_status

ER Diagram (ASCII):

csi_fact_data_quality (dq_id, dataset_id, check_name, check_status, checked_ts)
  |-- dataset_id --> csi_dim_dataset(dataset_id)

Description: Governance metadata tracks dataset quality, certifications, and owners for cataloging and audit.

---

### Source D: Cost & Billing (Source: csi_billing)

Tables (20):
1. csi_stg_billing_records
2. csi_raw_billing
3. csi_dim_cost_center
4. csi_dim_resource_type
5. csi_dim_region
6. csi_ref_price_catalog
7. csi_fact_cost_usage
8. csi_stage_allocations
9. csi_dim_tagging
10. csi_dim_currency
11. csi_audit_billing_ingest
12. csi_ref_discounts
13. csi_stage_corrections
14. csi_fact_monthly_costs
15. csi_dim_billing_account
16. csi_ref_chargeback_rules
17. csi_audit_allocations
18. csi_stage_forecasts
19. csi_ref_rates
20. csi_dim_status

ER Diagram (ASCII):

csi_fact_cost_usage (usage_id, resource_id, cost_amount, currency, start_ts, end_ts)
  |-- resource_id --> csi_dim_resource_type(resource_id)
  |-- cost_center_id --> csi_dim_cost_center(cost_center_id)

Description: Cost facts enable chargeback, cost optimization, and forecasting.

---

### Source E: Transactional Workloads (Source: csi_txn)

Tables (20):
1. csi_stg_transactions
2. csi_raw_transactions
3. csi_dim_account
4. csi_dim_customer
5. csi_dim_product
6. csi_ref_exchange_rates
7. csi_fact_transactions
8. csi_stage_reconciliations
9. csi_dim_channel
10. csi_dim_merchant
11. csi_audit_txn_ingest
12. csi_ref_fee_schedule
13. csi_stage_settlements
14. csi_fact_settlements
15. csi_dim_status
16. csi_ref_limits
17. csi_audit_recon
18. csi_stage_adjustments
19. csi_fact_balance_snapshots
20. csi_dim_time

ER Diagram (ASCII):

csi_fact_transactions (transaction_id, account_id, amount, currency, txn_type, posted_ts)
  |-- account_id --> csi_dim_account(account_id)
  |-- customer_id --> csi_dim_customer(customer_id)
  |-- product_id --> csi_dim_product(product_id)

Common Patterns: Use staging (immutable), raw normalized, enrichment stages, canonical fact loading, and audit/reconciliation tables. Dimensions follow SCD patterns appropriate to business needs.

## Implementation Notes
- Use `ingest_batch_id`, checksums, and `audit_*` tables for reconciliation.
- Implement data quality checks (Great Expectations or similar) before promoting to curated zones.
- Register datasets in a catalog and enforce RBAC via Unity Catalog/Purview.

