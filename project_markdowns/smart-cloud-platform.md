# Sm@rt Cloud Platform

Brief: Modern, automated cloud platform (Smart Cloud) for data and analytics workloads.

- Objectives:
  - Provide managed infrastructure with automation and observability.
- Scope:
  - IaC, CI/CD, tenant provisioning, cost controls.
- Key Components:
  - Landing zones, automation pipelines, observability.
- Technologies:
  - Terraform, Azure Policy, monitoring tools.
- Deliverables:
  - Platform repo, onboarding guide, cost management policies.

## Expanded Source Schemas, ER Diagrams, Facts & Dimensions

Standardized expansion for platform-level monitoring and automation: five logical sources each with 20 tables, ER diagrams, facts/dimensions, reconciliation patterns, and a rights statement.

Project prefix: `scp_` (Sm@rt Cloud Platform)

### Source A: Provisioning Events (scp_provision)

Tables (20):
1. scp_stg_provision_requests
2. scp_raw_provision
3. scp_dim_requester
4. scp_dim_template
5. scp_dim_environment
6. scp_ref_templates
7. scp_fact_provision_events
8. scp_stage_approvals
9. scp_dim_region
10. scp_dim_tenant
11. scp_audit_provision
12. scp_ref_policy
13. scp_stage_rollbacks
14. scp_fact_provision_time
15. scp_dim_status
16. scp_ref_cost_estimates
17. scp_audit_errors
18. scp_stage_metadata
19. scp_ref_dependencies
20. scp_dim_team

ER Diagram (ASCII):

scp_fact_provision_events (prov_id, template_id, requester_id, tenant_id, created_ts)
  |-- template_id --> scp_dim_template(template_id)
  |-- requester_id --> scp_dim_requester(requester_id)

Rights Statement: I confirm these diagrams and schema designs are original artifacts created to model platform flows and may be used internally for implementation.

---

### Source B: Observability Metrics (scp_obs)

Tables (20):
1. scp_stg_metrics
2. scp_raw_metrics
3. scp_dim_resource
4. scp_dim_metric_type
5. scp_dim_instance
6. scp_ref_thresholds
7. scp_fact_metrics
8. scp_stage_alerts
9. scp_dim_region
10. scp_dim_service
11. scp_audit_metrics_ingest
12. scp_ref_dashboards
13. scp_stage_aggregations
14. scp_fact_anomalies
15. scp_dim_time
16. scp_ref_slo
17. scp_audit_alerts
18. scp_stage_enrichments
19. scp_ref_tags
20. scp_dim_status

---

### Source C: CI/CD Pipelines (scp_cicd)

Tables (20):
1. scp_stg_build_events
2. scp_raw_builds
3. scp_dim_pipeline
4. scp_dim_repo
5. scp_dim_branch
6. scp_ref_build_status
7. scp_fact_builds
8. scp_stage_deploys
9. scp_dim_env
10. scp_dim_team
11. scp_audit_builds
12. scp_ref_artifacts
13. scp_stage_rollbacks
14. scp_fact_deploy_metrics
15. scp_dim_time
16. scp_ref_test_coverage
17. scp_audit_tests
18. scp_stage_results
19. scp_ref_approvals
20. scp_dim_status

---

### Source D: Cost & Billing (scp_billing)

Tables (20):
1. scp_stg_billing
2. scp_raw_billing
3. scp_dim_cost_center
4. scp_dim_resource_type
5. scp_dim_region
6. scp_ref_price_catalog
7. scp_fact_cost_usage
8. scp_stage_allocations
9. scp_dim_tagging
10. scp_dim_currency
11. scp_audit_billing
12. scp_ref_discounts
13. scp_stage_corrections
14. scp_fact_monthly_costs
15. scp_dim_billing_account
16. scp_ref_chargeback_rules
17. scp_audit_allocations
18. scp_stage_forecasts
19. scp_ref_rates
20. scp_dim_status

---

### Source E: Governance & Policies (scp_gov)

Tables (20):
1. scp_stg_policies
2. scp_raw_policies
3. scp_dim_policy
4. scp_dim_owner
5. scp_dim_scope
6. scp_ref_controls
7. scp_fact_policy_violations
8. scp_stage_remediations
9. scp_dim_time
10. scp_dim_region
11. scp_audit_policies
12. scp_ref_slas
13. scp_stage_exceptions
14. scp_fact_exception_metrics
15. scp_dim_team
16. scp_ref_workflows
17. scp_audit_actions
18. scp_stage_changes
19. scp_ref_templates
20. scp_dim_status

Common guidance: use audit logs, checksums, and reconciliation to validate provisioning and cost flows. Register all datasets in catalog and enforce RBAC.

