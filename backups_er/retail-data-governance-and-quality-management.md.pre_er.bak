# Retail Data Governance & Quality Management

Brief: Ongoing management and operationalization of retail data governance.

- Objectives:
  - Operationalize governance, monitoring, and remediation.
- Scope:
  - Workflows for data issues, ownership, and remediation.
- Key Components:
  - Issue tracking, dashboards, automated checks.
- Technologies:
  - Data catalogs, quality tooling, ticketing systems.
- Deliverables:
  - Governance playbook, escalation flows, KPI dashboards.

## Expanded Source Schemas, ER Diagrams, Facts & Dimensions

This standard expansion provides five logical sources for retail data governance, each with 20 tables, ER diagrams, fact/dimension descriptions, reconciliation patterns, and a rights statement that these diagrams are original design artifacts.

Project prefix: `rdgq_` (Retail Data Governance & Quality)

### Source A: Channel Ingest (rdgq_channel)

Tables (20):
1. rdgq_stg_channel_events
2. rdgq_raw_channel_events
3. rdgq_dim_channel
4. rdgq_dim_source
5. rdgq_dim_format
6. rdgq_ref_schema
7. rdgq_fact_channel_events
8. rdgq_stage_enrichments
9. rdgq_dim_geo
10. rdgq_dim_store
11. rdgq_audit_ingest
12. rdgq_ref_event_map
13. rdgq_stage_dedup
14. rdgq_dim_event_type
15. rdgq_ref_error_codes
16. rdgq_fact_event_counts
17. rdgq_audit_recon
18. rdgq_stage_corrections
19. rdgq_ref_retention
20. rdgq_dim_status

ER Diagram (ASCII):

rdgq_fact_channel_events (event_id, channel_id, store_id, customer_id, event_ts)
  |-- channel_id --> rdgq_dim_channel(channel_id)
  |-- store_id --> rdgq_dim_store(store_id)

Rights Statement: I assert the right to author and publish these diagrams and schemas as original design artifacts for platform design and implementation.

---

### Source B: Catalog & Metadata (rdgq_catalog)

Tables (20):
1. rdgq_stg_catalog
2. rdgq_raw_catalog
3. rdgq_dim_dataset
4. rdgq_dim_owner
5. rdgq_dim_tag
6. rdgq_ref_policies
7. rdgq_fact_data_quality
8. rdgq_stage_lineage
9. rdgq_dim_classification
10. rdgq_dim_sensitivity
11. rdgq_audit_policies
12. rdgq_ref_sla
13. rdgq_stage_certifications
14. rdgq_fact_issues
15. rdgq_dim_remediation_team
16. rdgq_ref_controls
17. rdgq_audit_certification
18. rdgq_stage_policy_changes
19. rdgq_ref_standards
20. rdgq_dim_status

ER Diagram (ASCII):

rdgq_fact_data_quality (dq_id, dataset_id, check_name, status, checked_ts)
  |-- dataset_id --> rdgq_dim_dataset(dataset_id)

---

### Source C: Quality Checks & Alerts (rdgq_quality)

Tables (20):
1. rdgq_stg_checks
2. rdgq_raw_checks
3. rdgq_dim_check_type
4. rdgq_dim_dataset
5. rdgq_dim_rule_owner
6. rdgq_ref_thresholds
7. rdgq_fact_check_runs
8. rdgq_stage_alerts
9. rdgq_dim_priority
10. rdgq_dim_channel
11. rdgq_audit_check_ingest
12. rdgq_ref_remediation_steps
13. rdgq_stage_issues
14. rdgq_fact_issue_metrics
15. rdgq_dim_team
16. rdgq_ref_automations
17. rdgq_audit_issues
18. rdgq_stage_corrections
19. rdgq_ref_owner_contacts
20. rdgq_dim_status

---

### Source D: Remediation & Workflows (rdgq_workflow)

Tables (20):
1. rdgq_stg_workflows
2. rdgq_raw_tasks
3. rdgq_dim_workflow_type
4. rdgq_dim_assignee
5. rdgq_dim_priority
6. rdgq_ref_playbooks
7. rdgq_fact_task_metrics
8. rdgq_stage_attachments
9. rdgq_dim_sla
10. rdgq_dim_status
11. rdgq_audit_task_events
12. rdgq_ref_escalation_paths
13. rdgq_stage_comments
14. rdgq_fact_resolution_times
15. rdgq_dim_team
16. rdgq_ref_templates
17. rdgq_audit_workflow_changes
18. rdgq_stage_retries
19. rdgq_ref_automation_rules
20. rdgq_dim_channel

---

### Source E: Reporting & Compliance (rdgq_reporting)

Tables (20):
1. rdgq_stg_reports
2. rdgq_raw_reports
3. rdgq_dim_report_type
4. rdgq_dim_consumer
5. rdgq_dim_dataset
6. rdgq_ref_report_templates
7. rdgq_fact_report_consumption
8. rdgq_stage_exports
9. rdgq_dim_frequency
10. rdgq_dim_region
11. rdgq_audit_report_runs
12. rdgq_ref_compliance_rules
13. rdgq_stage_retention
14. rdgq_fact_compliance_checks
15. rdgq_dim_owner
16. rdgq_ref_signoffs
17. rdgq_audit_signoffs
18. rdgq_stage_distribution
19. rdgq_ref_formats
20. rdgq_dim_status

## Common Patterns
- Use staging (immutable) → raw normalization → enrichment → canonical facts/dimensions → audit & reconciliation.
- Implement SCD2 for slowly-changing dimensions where history is required.
- Use `audit_*` and checksums for reconciliations.

