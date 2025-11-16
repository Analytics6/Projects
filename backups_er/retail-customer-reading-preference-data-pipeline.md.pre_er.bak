# Retail Customer Reading Preference Data Pipeline

Brief: Pipeline to capture and analyze customer reading preferences for personalized recommendations.

- Objectives:
  - Build preference signals for personalization and marketing.
- Scope:
  - Content interactions, ratings, dwell time, purchases.
- Key Components:
  - Event collectors, feature extraction, feature store.
- Technologies:
  - Stream processing, Databricks, feature store frameworks.
- Deliverables:
  - Preference features, sample recommender integration.

## Expanded Source Schemas, ER Diagrams, Facts & Dimensions

Five sources focused on content consumption, preferences, metadata, personalization experiments, and feedback, each with 20 tables, ER diagrams, facts/dimensions, reconciliation patterns, and a rights statement. Project prefix: `rcrp_`.

### Source A: Content Interaction Events (rcrp_events)

Tables (20):
1. rcrp_stg_events
2. rcrp_raw_events
3. rcrp_dim_content
4. rcrp_dim_user
5. rcrp_dim_device
6. rcrp_ref_event_types
7. rcrp_fact_content_views
8. rcrp_stage_sessionization
9. rcrp_dim_time
10. rcrp_dim_channel
11. rcrp_audit_ingest
12. rcrp_ref_sampling
13. rcrp_stage_dedup
14. rcrp_fact_engagement_scores
15. rcrp_dim_region
16. rcrp_ref_events_map
17. rcrp_audit_recon
18. rcrp_stage_enrich
19. rcrp_ref_retention
20. rcrp_dim_status

ER Diagram (ASCII):

rcrp_fact_content_views (view_id, content_id, user_id, device_id, view_ts)
  |-- content_id --> rcrp_dim_content(content_id)
  |-- user_id --> rcrp_dim_user(user_id)

Rights Statement: I confirm these flow diagrams and schema designs are authored as original artifacts for personalization pipeline design and documentation.

---

### Source B: Content Catalog & Metadata (rcrp_catalog)

Tables (20):
1. rcrp_stg_catalog
2. rcrp_raw_catalog
3. rcrp_dim_content
4. rcrp_dim_author
5. rcrp_dim_category
6. rcrp_ref_taxonomy
7. rcrp_fact_content_attributes
8. rcrp_stage_media
9. rcrp_dim_format
10. rcrp_dim_time
11. rcrp_audit_catalog_ingest
12. rcrp_ref_mappings
13. rcrp_stage_sync
14. rcrp_fact_catalog_changes
15. rcrp_dim_status
16. rcrp_ref_languages
17. rcrp_audit_recon
18. rcrp_stage_enrich
19. rcrp_ref_classifiers
20. rcrp_dim_owner

---

### Source C: Personalization Features (rcrp_features)

Tables (20):
1. rcrp_stg_features
2. rcrp_raw_features
3. rcrp_dim_feature
4. rcrp_dim_model_version
5. rcrp_dim_user
6. rcrp_ref_feature_defs
7. rcrp_fact_feature_snapshots
8. rcrp_stage_feature_store
9. rcrp_dim_time
10. rcrp_dim_segment
11. rcrp_audit_feature_runs
12. rcrp_ref_labeling_rules
13. rcrp_stage_labeling
14. rcrp_fact_model_performance
15. rcrp_dim_status
16. rcrp_ref_access_controls
17. rcrp_audit_recon
18. rcrp_stage_exports
19. rcrp_ref_formats
20. rcrp_dim_owner

---

### Source D: Experiments & A/B Testing (rcrp_experiments)

Tables (20):
1. rcrp_stg_experiments
2. rcrp_raw_experiments
3. rcrp_dim_experiment
4. rcrp_dim_variation
5. rcrp_dim_audience
6. rcrp_ref_metrics
7. rcrp_fact_experiment_results
8. rcrp_stage_assignments
9. rcrp_dim_time
10. rcrp_dim_region
11. rcrp_audit_experiment_ingest
12. rcrp_ref_winner_criteria
13. rcrp_stage_segmentations
14. rcrp_fact_lift_metrics
15. rcrp_dim_team
16. rcrp_ref_stat_tests
17. rcrp_audit_repro
18. rcrp_stage_cleaned
19. rcrp_ref_sampling
20. rcrp_dim_status

---

### Source E: Feedback & Ratings (rcrp_feedback)

Tables (20):
1. rcrp_stg_feedback
2. rcrp_raw_feedback
3. rcrp_dim_user
4. rcrp_dim_content
5. rcrp_dim_channel
6. rcrp_ref_sentiment_codes
7. rcrp_fact_feedback
8. rcrp_stage_text_analysis
9. rcrp_dim_time
10. rcrp_dim_region
11. rcrp_audit_feedback_ingest
12. rcrp_ref_classifiers
13. rcrp_stage_enrichments
14. rcrp_fact_sentiment_scores
15. rcrp_dim_category
16. rcrp_ref_tags
17. rcrp_audit_recon
18. rcrp_stage_moderation
19. rcrp_ref_languages
20. rcrp_dim_status

Implementation tips: derive preference features from dwell time, completion, ratings, and purchases; store features in a feature store for low-latency serving and batch training.

