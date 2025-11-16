# Retail Inventory Management System with Azure Databricks

Brief: Implement inventory processing and analytics using Databricks.

- Objectives:
  - Improve inventory visibility and forecasting accuracy.
- Scope:
  - Stock levels, replenishment signals, supplier lead-times.
- Key Components:
  - Inventory ETL, forecasting notebooks, dashboards.
- Technologies:
  - Databricks, Delta Lake, Azure Data Factory.
- Deliverables:
  - Inventory datasets, forecasting model, runbooks.

## Expanded Source Schemas, ER Diagrams, Facts & Dimensions

Five inventory-focused sources (POS, Warehouse, Suppliers, Forecasting, Replenishment), each with 20 tables, ER diagrams, fact/dimension descriptions, reconciliation patterns, and a rights statement. Project prefix: `rim_`.

### Source A: POS Sales Feed (rim_pos)

Tables (20):
1. rim_stg_pos
2. rim_raw_pos
3. rim_dim_terminal
4. rim_dim_product
5. rim_dim_store
6. rim_ref_txn_types
7. rim_fact_sales
8. rim_stage_returns
9. rim_dim_time
10. rim_dim_channel
11. rim_audit_pos_ingest
12. rim_ref_pricing
13. rim_stage_promotions
14. rim_fact_basket
15. rim_dim_cashier
16. rim_ref_tax_codes
17. rim_audit_recon
18. rim_stage_settlements
19. rim_ref_discounts
20. rim_dim_status

ER Diagram (ASCII):

rim_fact_sales (sale_id, order_id, product_id, qty, net_amount, store_id)
  |-- product_id --> rim_dim_product(product_id)
  |-- store_id --> rim_dim_store(store_id)

---

### Source B: Warehouse & Stock (rim_warehouse)

Tables (20):
1. rim_stg_stock_movements
2. rim_raw_warehouse
3. rim_dim_sku
4. rim_dim_warehouse
5. rim_dim_location
6. rim_ref_storage_types
7. rim_fact_stock_levels
8. rim_stage_replenishments
9. rim_dim_time
10. rim_dim_supplier
11. rim_audit_inventory_ingest
12. rim_ref_lead_times
13. rim_stage_transfers
14. rim_fact_turnover
15. rim_dim_status
16. rim_ref_units
17. rim_audit_recon
18. rim_stage_adjustments
19. rim_ref_packaging
20. rim_dim_owner

---

### Source C: Supplier & PO (rim_supplier)

Tables (20):
1. rim_stg_po
2. rim_raw_supplier_feeds
3. rim_dim_supplier
4. rim_dim_product
5. rim_dim_lead_time_bucket
6. rim_ref_incoterms
7. rim_fact_po_lines
8. rim_stage_goods_receipt
9. rim_dim_time
10. rim_dim_currency
11. rim_audit_supplier_ingest
12. rim_ref_payment_terms
13. rim_stage_invoices
14. rim_fact_costs
15. rim_dim_status
16. rim_ref_uis
17. rim_audit_recon
18. rim_stage_returns
19. rim_ref_quality_codes
20. rim_dim_owner

---

### Source D: Forecasts & Demand Signals (rim_forecast)

Tables (20):
1. rim_stg_forecasts
2. rim_raw_forecast_runs
3. rim_dim_model_version
4. rim_dim_sku
5. rim_dim_store
6. rim_ref_forecast_params
7. rim_fact_forecasts
8. rim_stage_inputs
9. rim_dim_time
10. rim_dim_segment
11. rim_audit_forecast_runs
12. rim_ref_feature_defs
13. rim_stage_backtests
14. rim_fact_forecast_accuracy
15. rim_dim_status
16. rim_ref_seasonality_profiles
17. rim_audit_recon
18. rim_stage_enrichments
19. rim_ref_metrics
20. rim_dim_owner

---

### Source E: Replenishment & Orders (rim_replenish)

Tables (20):
1. rim_stg_replenish_orders
2. rim_raw_replenish
3. rim_dim_supplier
4. rim_dim_sku
5. rim_dim_store
6. rim_ref_reorder_rules
7. rim_fact_replenishment_instructions
8. rim_stage_allocations
9. rim_dim_time
10. rim_dim_priority
11. rim_audit_replenish_ingest
12. rim_ref_costs
13. rim_stage_confirmations
14. rim_fact_fill_rates
15. rim_dim_status
16. rim_ref_lead_times
17. rim_audit_recon
18. rim_stage_corrections
19. rim_ref_units
20. rim_dim_owner

Implementation notes: use daily balance snapshots for inventory visibility, implement reconciliation between POS, warehouse, and replenishment facts, and expose forecasting outputs into the curated zone for downstream consumers.

