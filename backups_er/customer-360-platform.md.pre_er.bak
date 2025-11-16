# Customer 360 Platform

Brief: Centralized platform to assemble a unified view of each customer.

- Objectives:
  - Link identities, merge signals, provide accessible 360 profiles.
- Scope:
  - Identity resolution, enrichment, profile APIs.
- Key Components:
  - Identity graph, profile store, access layer.
- Technologies:
  - Graph DB, Cosmos DB/Azure SQL, microservices for APIs.
- Deliverables:
  - Unified profile store, API docs, sample client SDK.

## Expanded Source Schemas, ER Diagrams, Facts & Dimensions

This expansion provides five logical sources to build and operationalize Customer 360 data, each with 20 tables, ER diagrams, fact/dimension descriptions, reconciliation patterns, and a rights statement. Project prefix: `c360_`.

### Source A: CRM & Profile Data (c360_crm)

Tables (20):
1. c360_stg_crm
2. c360_raw_crm
3. c360_dim_customer
4. c360_dim_address
5. c360_dim_contact_method
6. c360_ref_kyc_levels
7. c360_fact_profile_snapshots
8. c360_stage_enrichments
9. c360_dim_time
10. c360_dim_segment
11. c360_audit_crm_ingest
12. c360_ref_matching_rules
13. c360_stage_dedup
14. c360_fact_identity_matches
15. c360_dim_status
16. c360_ref_sources
17. c360_audit_recon
18. c360_stage_history
19. c360_ref_consent_levels
20. c360_dim_owner

ER Diagram (ASCII):

c360_fact_profile_snapshots (profile_id, customer_id, snapshot_ts, attributes_hash)
  |-- customer_id --> c360_dim_customer(customer_id)

Rights Statement: These diagrams and schema designs are original design artifacts created for Customer 360 implementation documentation and may be used for internal design and implementation.

---

### Source B: Transactional Events (c360_txn)

Tables (20):
1. c360_stg_transactions
2. c360_raw_transactions
3. c360_dim_account
4. c360_dim_product
5. c360_dim_channel
6. c360_ref_txn_types
7. c360_fact_transactions
8. c360_stage_enrichments
9. c360_dim_time
10. c360_dim_merchant
11. c360_audit_txn_ingest
12. c360_ref_fx_rates
13. c360_stage_reconciliations
14. c360_fact_balances
15. c360_dim_status
16. c360_ref_fee_types
17. c360_audit_recon
18. c360_stage_adjustments
19. c360_ref_mappings
20. c360_dim_region

---

### Source C: Web & Mobile Events (c360_engagement)

Tables (20):
1. c360_stg_engagement_events
2. c360_raw_events
3. c360_dim_device
4. c360_dim_channel
5. c360_dim_page
6. c360_ref_event_types
7. c360_fact_sessions
8. c360_stage_user_profiles
9. c360_dim_time
10. c360_dim_geo
11. c360_audit_event_ingest
12. c360_ref_attribution_rules
13. c360_stage_dedup
14. c360_fact_engagement_metrics
15. c360_dim_segment
16. c360_ref_event_map
17. c360_audit_recon
18. c360_stage_enrichments
19. c360_ref_botsignals
20. c360_dim_status

---

### Source D: Third-party Enrichments (c360_enrich)

Tables (20):
1. c360_stg_enrich
2. c360_raw_enrich
3. c360_dim_provider
4. c360_dim_attribute
5. c360_dim_country
6. c360_ref_attribute_map
7. c360_fact_enrichments
8. c360_stage_matches
9. c360_dim_time
10. c360_dim_credibility
11. c360_audit_enrich_ingest
12. c360_ref_contracts
13. c360_stage_consents
14. c360_fact_enrichment_counts
15. c360_dim_status
16. c360_ref_rates
17. c360_audit_recon
18. c360_stage_verifications
19. c360_ref_mappings
20. c360_dim_owner

---

### Source E: Analytics & Features (c360_features)

Tables (20):
1. c360_stg_features
2. c360_raw_features
3. c360_dim_feature
4. c360_dim_model_version
5. c360_dim_time
6. c360_ref_feature_defs
7. c360_fact_features_snapshot
8. c360_stage_feature_store
9. c360_dim_segment
10. c360_dim_customer
11. c360_audit_feature_runs
12. c360_ref_usage_policies
13. c360_stage_labeling
14. c360_fact_feature_metrics
15. c360_dim_status
16. c360_ref_access_controls
17. c360_audit_recon
18. c360_stage_exports
19. c360_ref_formats
20. c360_dim_owner

Implementation notes: enforce consent and PII handling, hash or pseudonymize identifiers where appropriate, and use lineage and audit tables for traceability.

