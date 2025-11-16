# Retail Sports & Fitness Analytics Platform

Brief: Analytics platform focused on sports & fitness retail performance.

- Objectives:
  - Drive category growth via data-driven decisions.
- Scope:
  - Product, promotion, channel, and customer analytics.
- Key Components:
  - Category dashboards, forecasting, competition analysis.
- Technologies:
  - Data lakehouse, forecasting models, BI.
- Deliverables:
  - Category KPIs, forecast outputs, playbooks.

## Expanded Source Schemas, ER Diagrams, Facts & Dimensions

Adds five logical sources for sports & fitness analytics, each with 20 tables, ER diagrams, detailed fact/dimension descriptions, reconciliation patterns, and a rights statement.

Project prefix: `rsf_` (Retail Sports & Fitness)

### Source A: E-commerce Orders (rsf_orders)

Tables (20):
1. rsf_stg_orders
2. rsf_raw_orders
3. rsf_dim_order
4. rsf_dim_customer
5. rsf_dim_product
6. rsf_ref_status_codes
7. rsf_fact_order_lines
8. rsf_stage_fulfillment
9. rsf_dim_channel
10. rsf_dim_promo
11. rsf_audit_ingest
12. rsf_ref_shipping_rates
13. rsf_stage_returns
14. rsf_fact_returns
15. rsf_dim_time
16. rsf_ref_voucher_rules
17. rsf_audit_recon
18. rsf_stage_pricing
19. rsf_ref_brand
20. rsf_dim_status

ER Diagram (ASCII):

rsf_fact_order_lines (order_line_id, order_id, product_id, qty, net_amount)
  |-- order_id --> rsf_dim_order(order_id)
  |-- product_id --> rsf_dim_product(product_id)

---

### Source B: Inventory & Warehousing (rsf_inventory)

Tables (20):
1. rsf_stg_inventory
2. rsf_raw_inventory
3. rsf_dim_sku
4. rsf_dim_warehouse
5. rsf_dim_supplier
6. rsf_ref_lead_times
7. rsf_fact_stock_levels
8. rsf_stage_replenishments
9. rsf_dim_time
10. rsf_dim_store
11. rsf_audit_inventory_ingest
12. rsf_ref_packaging
13. rsf_stage_movements
14. rsf_fact_turnover
15. rsf_dim_category
16. rsf_ref_units
17. rsf_audit_recon
18. rsf_stage_adjustments
19. rsf_ref_country_codes
20. rsf_dim_status

---

### Source C: Marketing & Campaigns (rsf_marketing)

Tables (20):
1. rsf_stg_campaign_events
2. rsf_raw_campaign_events
3. rsf_dim_campaign
4. rsf_dim_channel
5. rsf_dim_audience
6. rsf_ref_channel_map
7. rsf_fact_campaign_performance
8. rsf_stage_attribution
9. rsf_dim_time
10. rsf_dim_region
11. rsf_audit_campaign_ingest
12. rsf_ref_attribution_rules
13. rsf_stage_experiments
14. rsf_fact_experiment_results
15. rsf_dim_team
16. rsf_ref_costs
17. rsf_audit_recon
18. rsf_stage_creatives
19. rsf_ref_metrics
20. rsf_dim_status

---

### Source D: Product Catalog & Attributes (rsf_catalog)

Tables (20):
1. rsf_stg_catalog
2. rsf_raw_catalog
3. rsf_dim_product
4. rsf_dim_brand
5. rsf_dim_category
6. rsf_ref_attribute_map
7. rsf_fact_product_availability
8. rsf_stage_pricing
9. rsf_dim_supplier
10. rsf_dim_time
11. rsf_audit_catalog_ingest
12. rsf_ref_mappings
13. rsf_stage_sync
14. rsf_fact_catalog_changes
15. rsf_dim_status
16. rsf_ref_taxonomy
17. rsf_audit_recon
18. rsf_stage_media
19. rsf_ref_units
20. rsf_dim_status

---

### Source E: Customer Feedback & Reviews (rsf_feedback)

Tables (20):
1. rsf_stg_feedback
2. rsf_raw_feedback
3. rsf_dim_customer
4. rsf_dim_product
5. rsf_dim_channel
6. rsf_ref_sentiment_codes
7. rsf_fact_feedback
8. rsf_stage_text_analysis
9. rsf_dim_time
10. rsf_dim_region
11. rsf_audit_feedback_ingest
12. rsf_ref_classifiers
13. rsf_stage_enrichments
14. rsf_fact_sentiment_scores
15. rsf_dim_category
16. rsf_ref_tags
17. rsf_audit_recon
18. rsf_stage_moderation
19. rsf_ref_languages
20. rsf_dim_status

## Common Patterns
- Use canonical product and customer dimensions; ensure join keys are stable and hashed when necessary for PII protection.
- Implement reconciliation across sales and inventory facts to support forecasting.

