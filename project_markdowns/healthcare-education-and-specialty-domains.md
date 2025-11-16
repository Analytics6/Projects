# Healthcare, Education & Specialty Domains

Brief: Data platforms and analytics tailored to healthcare, education, and specialized domains.

- Objectives:
  - Provide domain-specific data models and compliance.
- Scope:
  - PHI handling, student performance analytics, domain-specific KPIs.
- Key Components:
  - Secure data stores, domain models, reporting.
- Technologies:
  - HIPAA-compliant configurations, Databricks, specialized tools.
- Deliverables:
  - Data models, compliance checklists, dashboards.

# Expanded Source Schemas, ER Diagrams, Facts & Dimensions

This standardized expansion provides five logical sources for the project and a canonical set of artifacts to be appended to project markdown files when a detailed schema is required.

NOTE: The artifacts below are design artifacts created for documentation and implementation planning. They are original work and may be used for internal design and implementation purposes.

Project-specific prefix: `healthcare_education_and_specialty_domains` (derived from filename: `healthcare-education-and-specialty-domains.md`).

---

### Source A: Ingest & Landing (Source: `healthcare_education_and_specialty_domains_ingest`)

Tables (20):
1. healthcare_education_and_specialty_domains_stg_raw
2. healthcare_education_and_specialty_domains_raw_records
3. healthcare_education_and_specialty_domains_dim_source_system
4. healthcare_education_and_specialty_domains_dim_data_owner
5. healthcare_education_and_specialty_domains_dim_file_type
6. healthcare_education_and_specialty_domains_ref_file_schema
7. healthcare_education_and_specialty_domains_fact_raw_events
8. healthcare_education_and_specialty_domains_stage_enrichments
9. healthcare_education_and_specialty_domains_dim_geo
10. healthcare_education_and_specialty_domains_dim_business_unit
11. healthcare_education_and_specialty_domains_audit_ingest
12. healthcare_education_and_specialty_domains_dim_environment
13. healthcare_education_and_specialty_domains_ref_parsing_errors
14. healthcare_education_and_specialty_domains_stage_cdc
15. healthcare_education_and_specialty_domains_dim_schema_version
16. healthcare_education_and_specialty_domains_fact_event_counts
17. healthcare_education_and_specialty_domains_audit_transforms
18. healthcare_education_and_specialty_domains_stage_retries
19. healthcare_education_and_specialty_domains_ref_mappings
20. healthcare_education_and_specialty_domains_dim_status

ER Diagram (ASCII):

healthcare_education_and_specialty_domains_fact_raw_events (event_id, source_system_id, record_key, payload_hash, event_ts)
  |-- source_system_id --> healthcare_education_and_specialty_domains_dim_source_system(source_system_id)
  |-- record_key --> healthcare_education_and_specialty_domains_raw_records(record_key)

Description: Ingest staging (immutable) → raw normalization → enrichment → audit. `healthcare_education_and_specialty_domains_fact_raw_events` is used for throughput and source health monitoring.

---

### Source B: Operational Logs & Metrics (Source: `healthcare_education_and_specialty_domains_ops`)

Tables (20):
1. healthcare_education_and_specialty_domains_stg_ops_logs
2. healthcare_education_and_specialty_domains_raw_ops
3. healthcare_education_and_specialty_domains_dim_service
4. healthcare_education_and_specialty_domains_dim_instance
5. healthcare_education_and_specialty_domains_dim_log_level
6. healthcare_education_and_specialty_domains_ref_error_codes
7. healthcare_education_and_specialty_domains_fact_logs
8. healthcare_education_and_specialty_domains_stage_alerts
9. healthcare_education_and_specialty_domains_dim_team
10. healthcare_education_and_specialty_domains_dim_region
11. healthcare_education_and_specialty_domains_audit_ops_ingest
12. healthcare_education_and_specialty_domains_ref_runbooks
13. healthcare_education_and_specialty_domains_stage_incidents
14. healthcare_education_and_specialty_domains_fact_incident_metrics
15. healthcare_education_and_specialty_domains_dim_priority
16. healthcare_education_and_specialty_domains_ref_maintenance_windows
17. healthcare_education_and_specialty_domains_audit_recon
18. healthcare_education_and_specialty_domains_stage_trimmed_logs
19. healthcare_education_and_specialty_domains_ref_retention_policy
20. healthcare_education_and_specialty_domains_dim_status

ER Diagram (ASCII):

healthcare_education_and_specialty_domains_fact_logs (log_id, service_id, instance_id, log_level, message_ts)
  |-- service_id --> healthcare_education_and_specialty_domains_dim_service(service_id)
  |-- instance_id --> healthcare_education_and_specialty_domains_dim_instance(instance_id)

---

### Source C: Governance & Catalog (Source: `healthcare_education_and_specialty_domains_gov`)

Tables (20):
1. healthcare_education_and_specialty_domains_stg_catalog
2. healthcare_education_and_specialty_domains_raw_catalog
3. healthcare_education_and_specialty_domains_dim_dataset
4. healthcare_education_and_specialty_domains_dim_owner
5. healthcare_education_and_specialty_domains_dim_tag
6. healthcare_education_and_specialty_domains_ref_policies
7. healthcare_education_and_specialty_domains_fact_data_quality
8. healthcare_education_and_specialty_domains_stage_lineage
9. healthcare_education_and_specialty_domains_dim_classification
10. healthcare_education_and_specialty_domains_dim_sensitivity
11. healthcare_education_and_specialty_domains_audit_policies
12. healthcare_education_and_specialty_domains_ref_sla
13. healthcare_education_and_specialty_domains_stage_certifications
14. healthcare_education_and_specialty_domains_fact_issues
15. healthcare_education_and_specialty_domains_dim_remediation_team
16. healthcare_education_and_specialty_domains_ref_controls
17. healthcare_education_and_specialty_domains_audit_certification
18. healthcare_education_and_specialty_domains_stage_policy_changes
19. healthcare_education_and_specialty_domains_ref_standards
20. healthcare_education_and_specialty_domains_dim_status

ER Diagram (ASCII):

healthcare_education_and_specialty_domains_fact_data_quality (dq_id, dataset_id, check_name, check_status, checked_ts)
  |-- dataset_id --> healthcare_education_and_specialty_domains_dim_dataset(dataset_id)

---

### Source D: Cost, Billing & Usage (Source: `healthcare_education_and_specialty_domains_cost`)

Tables (20):
1. healthcare_education_and_specialty_domains_stg_billing_records
2. healthcare_education_and_specialty_domains_raw_billing
3. healthcare_education_and_specialty_domains_dim_cost_center
4. healthcare_education_and_specialty_domains_dim_resource_type
5. healthcare_education_and_specialty_domains_dim_region
6. healthcare_education_and_specialty_domains_ref_price_catalog
7. healthcare_education_and_specialty_domains_fact_cost_usage
8. healthcare_education_and_specialty_domains_stage_allocations
9. healthcare_education_and_specialty_domains_dim_tagging
10. healthcare_education_and_specialty_domains_dim_currency
11. healthcare_education_and_specialty_domains_audit_billing_ingest
12. healthcare_education_and_specialty_domains_ref_discounts
13. healthcare_education_and_specialty_domains_stage_corrections
14. healthcare_education_and_specialty_domains_fact_monthly_costs
15. healthcare_education_and_specialty_domains_dim_billing_account
16. healthcare_education_and_specialty_domains_ref_chargeback_rules
17. healthcare_education_and_specialty_domains_audit_allocations
18. healthcare_education_and_specialty_domains_stage_forecasts
19. healthcare_education_and_specialty_domains_ref_rates
20. healthcare_education_and_specialty_domains_dim_status

ER Diagram (ASCII):

healthcare_education_and_specialty_domains_fact_cost_usage (usage_id, resource_id, cost_amount, currency, start_ts, end_ts)
  |-- resource_id --> healthcare_education_and_specialty_domains_dim_resource_type(resource_id)
  |-- cost_center_id --> healthcare_education_and_specialty_domains_dim_cost_center(cost_center_id)

---

### Source E: Canonical Transactions / Facts (Source: `healthcare_education_and_specialty_domains_txn`)

Tables (20):
1. healthcare_education_and_specialty_domains_stg_transactions
2. healthcare_education_and_specialty_domains_raw_transactions
3. healthcare_education_and_specialty_domains_dim_account
4. healthcare_education_and_specialty_domains_dim_customer
5. healthcare_education_and_specialty_domains_dim_product
6. healthcare_education_and_specialty_domains_ref_exchange_rates
7. healthcare_education_and_specialty_domains_fact_transactions
8. healthcare_education_and_specialty_domains_stage_reconciliations
9. healthcare_education_and_specialty_domains_dim_channel
10. healthcare_education_and_specialty_domains_dim_merchant
11. healthcare_education_and_specialty_domains_audit_txn_ingest
12. healthcare_education_and_specialty_domains_ref_fee_schedule
13. healthcare_education_and_specialty_domains_stage_settlements
14. healthcare_education_and_specialty_domains_fact_settlements
15. healthcare_education_and_specialty_domains_dim_status
16. healthcare_education_and_specialty_domains_ref_limits
17. healthcare_education_and_specialty_domains_audit_recon
18. healthcare_education_and_specialty_domains_stage_adjustments
19. healthcare_education_and_specialty_domains_fact_balance_snapshots
20. healthcare_education_and_specialty_domains_dim_time

ER Diagram (ASCII):

healthcare_education_and_specialty_domains_fact_transactions (transaction_id, account_id, amount, currency, txn_type, posted_ts)
  |-- account_id --> healthcare_education_and_specialty_domains_dim_account(account_id)
  |-- customer_id --> healthcare_education_and_specialty_domains_dim_customer(customer_id)
  |-- product_id --> healthcare_education_and_specialty_domains_dim_product(product_id)

Common guidance:
- Always keep an immutable staging/raw zone for auditable ingestion.
- Use `audit_*` tables and checksums for reconciliation between source and target facts.
- Implement SCD patterns for dimensions where history is required.
- Register datasets in a data catalog and apply RBAC and PII protections as required.

