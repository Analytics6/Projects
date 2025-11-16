# Sales & Content Performance Analytics

Brief: Analytics combining sales performance with content and marketing effectiveness.

- Objectives:
  - Measure how content drives conversions and sales.
- Scope:
  - Campaign attribution, content A/B testing, conversion funnels.
- Key Components:
  - Attribution pipelines, experiment analytics, dashboards.
- Technologies:
  - Event processing, Databricks, attribution libraries.
- Deliverables:
  - Attribution reports, conversion dashboards, experiment results.

## Expanded Source Schemas, ER Diagrams, Facts & Dimensions

Five standardized sources for sales and content analytics, each with 20 tables, ER diagrams, fact/dimension details, reconciliation notes, and a rights statement. Project prefix: `scpa_`.

### Source A: Content Interactions (scpa_content)

Tables (20):
1. scpa_stg_content_events
2. scpa_raw_content
3. scpa_dim_content
4. scpa_dim_channel
5. scpa_dim_campaign
6. scpa_ref_event_map
7. scpa_fact_content_events
8. scpa_stage_personalization
9. scpa_dim_time
10. scpa_dim_user
11. scpa_audit_ingest
12. scpa_ref_content_taxonomy
13. scpa_stage_dedup
14. scpa_fact_engagement_scores
15. scpa_dim_region
16. scpa_ref_sentiment
17. scpa_audit_recon
18. scpa_stage_enrich
19. scpa_ref_metrics
20. scpa_dim_status

ER Diagram (ASCII):

scpa_fact_content_events (event_id, content_id, user_id, channel_id, ts)
  |-- content_id --> scpa_dim_content(content_id)
  |-- user_id --> scpa_dim_user(user_id)

Rights Statement: These diagrams are original designs created for analytics implementation and documentation.

---

### Source B: Sales Transactions (scpa_sales)

Tables (20):
1. scpa_stg_sales
2. scpa_raw_sales
3. scpa_dim_order
4. scpa_dim_customer
5. scpa_dim_product
6. scpa_ref_txn_type
7. scpa_fact_order_lines
8. scpa_stage_returns
9. scpa_dim_channel
10. scpa_dim_time
11. scpa_audit_sales_ingest
12. scpa_ref_pricing
13. scpa_stage_promotions
14. scpa_fact_revenue_by_content
15. scpa_dim_region
16. scpa_ref_discounts
17. scpa_audit_recon
18. scpa_stage_settlements
19. scpa_ref_tax_codes
20. scpa_dim_status

---

### Source C: Campaigns & Ads (scpa_campaign)

Tables (20):
1. scpa_stg_campaign_events
2. scpa_raw_campaigns
3. scpa_dim_campaign
4. scpa_dim_channel
5. scpa_dim_audience
6. scpa_ref_costs
7. scpa_fact_campaign_performance
8. scpa_stage_attribution
9. scpa_dim_time
10. scpa_dim_region
11. scpa_audit_campaign_ingest
12. scpa_ref_attribution_rules
13. scpa_stage_experiments
14. scpa_fact_experiment_results
15. scpa_dim_team
16. scpa_ref_cost_models
17. scpa_audit_recon
18. scpa_stage_creatives
19. scpa_ref_metrics
20. scpa_dim_status

---

### Source D: Recommendations & Personalization (scpa_personalization)

Tables (20):
1. scpa_stg_recs
2. scpa_raw_recs
3. scpa_dim_model_version
4. scpa_dim_feature
5. scpa_dim_user
6. scpa_ref_feature_defs
7. scpa_fact_recommendation_events
8. scpa_stage_feature_store
9. scpa_dim_time
10. scpa_dim_channel
11. scpa_audit_model_runs
12. scpa_ref_hyperparams
13. scpa_stage_feedback
14. scpa_fact_model_performance
15. scpa_dim_segment
16. scpa_ref_decisioning_rules
17. scpa_audit_recon
18. scpa_stage_experiments
19. scpa_ref_metrics
20. scpa_dim_status

---

### Source E: Reporting & Dashboards (scpa_reporting)

Tables (20):
1. scpa_stg_reports
2. scpa_raw_reports
3. scpa_dim_report
4. scpa_dim_consumer
5. scpa_dim_time
6. scpa_ref_templates
7. scpa_fact_report_views
8. scpa_stage_exports
9. scpa_dim_region
10. scpa_dim_business_unit
11. scpa_audit_report_runs
12. scpa_ref_signoffs
13. scpa_stage_cache
14. scpa_fact_kpi_snapshots
15. scpa_dim_status
16. scpa_ref_formats
17. scpa_audit_cache_invalidations
18. scpa_stage_distribution
19. scpa_ref_access_controls
20. scpa_dim_tags

Common patterns: Ensure join keys across content and sales are stable and use `audit_*` tables to reconcile content-driven revenue attribution.

