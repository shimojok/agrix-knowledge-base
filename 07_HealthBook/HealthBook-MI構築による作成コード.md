このスレッド全ての成果物を、新しくマルチAIエージェントに移管するために、AIが利用できる最適なフォーマット（JSONコード、データベースなど）として出力してください。

---


```json
{
  "project": {
    "name": "HealthBook-MI",
    "description": "Metabolic Intelligence OS integrating AcetylCoA, Estrobolome, MBT55, Disease-MI Matrix v2 and HealthBook engines.",
    "version": "2.1"
  },

  "philosophy": {
    "core_definition": "HealthBook-MI is a personal Metabolic Operating System (Metabolic Intelligence OS).",
    "principles": [
      "Track causes (metabolism, microbiome, hormones, mitochondria) rather than only symptoms.",
      "Use AcetylCoA as the central metabolic hub and primary MI index.",
      "Integrate Estrobolome (gut–hormone axis) as a core engine.",
      "Model metabolism as Nutrition × Microbiome × Hormones × Mitochondria × Lifestyle.",
      "Output interpretable metabolic deviations and intervention suggestions instead of disease labels."
    ]
  },

  "mi_core_engines": {
    "acetylcoa": {
      "id": "MI-AcetylCoA",
      "role": "Central metabolic hub index (AcetylCoA Availability).",
      "inputs": [
        "carbohydrate_metabolism",
        "lipid_quality_intake",
        "protein_intake",
        "minerals_Mg_Mn_B",
        "microbiome_scfa",
        "hormone_status",
        "processed_food_load",
        "drug_effects",
        "cold_stress"
      ],
      "outputs": [
        "energy_production_capacity",
        "tissue_repair_capacity",
        "hormone_synthesis_capacity",
        "inflammation_resolution_potential"
      ]
    },
    "estrobolome": {
      "id": "MI-Estrobolome",
      "role": "Gut–hormone metabolism engine (Estrogen recycling and SCFA-linked effects).",
      "inputs": [
        "fiber_intake",
        "fermented_food_intake",
        "bowel_movement",
        "processed_food_load",
        "dysbiosis_risk"
      ],
      "outputs": [
        "estrogen_recycling_efficiency",
        "gut_hormone_balance",
        "mitochondrial_estrogen_support"
      ]
    },
    "mitochondria": {
      "id": "MI-Mitochondria",
      "role": "ATP generation capacity.",
      "inputs": [
        "Mg_Mn_status",
        "estrogen_status",
        "cold_sensitivity",
        "processed_food_load",
        "stress_level"
      ],
      "outputs": [
        "atp_generation_score",
        "fatigue_risk",
        "repair_energy_availability"
      ]
    },
    "mbt55": {
      "id": "MI-MBT55",
      "role": "Microbial-metabolic modular engine (SCFA, bile acids, aromatic amino acids).",
      "inputs": [
        "microbiome_diversity",
        "scfa_production",
        "bile_acid_balance",
        "diet_pattern"
      ],
      "outputs": [
        "immune_modulation_score",
        "anti_inflammatory_potential",
        "metabolic_flux_stability"
      ]
    },
    "inflammation": {
      "id": "MI-Inflammation",
      "role": "Inflammatory load index.",
      "inputs": [
        "processed_food_load",
        "gut_status",
        "stress_level",
        "sleep_quality",
        "hormone_deficit"
      ],
      "outputs": [
        "chronic_inflammation_risk",
        "flare_up_likelihood"
      ]
    },
    "neuro_endocrine": {
      "id": "MI-Neuro-Endocrine",
      "role": "Stress–hormone–autonomic balance.",
      "inputs": [
        "stress_level",
        "sleep_quality",
        "menopausal_stage",
        "mood_state"
      ],
      "outputs": [
        "neuroendocrine_balance_score",
        "stress_reactivity"
      ]
    },
    "musculo_fascial": {
      "id": "MI-Musculo-Fascial",
      "role": "Muscle–fascia load and pain linkage.",
      "inputs": [
        "shoulder_stiffness",
        "forearm_tension",
        "hand_palm_tension",
        "posture",
        "rehab_minutes"
      ],
      "outputs": [
        "musculo_fascial_load_index",
        "mechanical_pain_risk"
      ]
    }
  },

  "metabolic_snapshot_schema": {
    "version": "v2",
    "sections": {
      "nutrition": [
        "total_protein_grams",
        "omega3_intake_score",
        "saturated_fat_quality_score",
        "magnesium_source_count",
        "manganese_source_count",
        "fiber_intake_grams",
        "fermented_food_servings",
        "processed_food_score",
        "plastic_contact_score",
        "high_fat_diet",
        "sugar_high"
      ],
      "gut_status": [
        "bowel_movement_count",
        "stool_form_score",
        "bloating_score",
        "gas",
        "stool_color_change",
        "floating_stool",
        "stool_irregular",
        "abdominal_pain_score"
      ],
      "hormone_state": [
        "menopausal_stage",
        "hot_flash_score",
        "sleep_quality_score",
        "basal_body_temp",
        "cold_sensitivity_score",
        "stress_level_score",
        "insulin_resistance"
      ],
      "microbiome": [
        "dysbiosis",
        "scfa_low"
      ],
      "musculo_fascial": [
        "shoulder_stiffness_score",
        "forearm_tension_score",
        "hand_palm_tension_score",
        "range_of_motion_limit_flag"
      ],
      "symptoms": [
        "thumb_pain_score",
        "thumb_numbness_score",
        "morning_stiffness_minutes",
        "fatigue",
        "odor_change",
        "abdominal_pain"
      ],
      "interventions": [
        "antihypertensive_taken",
        "antihypertensive_type",
        "nsaid_taken",
        "magnesium_supplement_mg",
        "manganese_supplement_mg",
        "thumb_splint_use_flag",
        "rehab_minutes_thumb",
        "rehab_minutes_shoulder_scapula",
        "aerobic_exercise_minutes",
        "hip_pelvis_exercise_minutes"
      ]
    }
  },

  "derived_indices": {
    "estro_support_score": {
      "inputs": [
        "fiber_intake_grams",
        "fermented_food_servings",
        "bowel_movement_count",
        "processed_food_score"
      ],
      "purpose": "Estimate Estrobolome support and SCFA-based hormone metabolism."
    },
    "mineral_index": {
      "inputs": [
        "magnesium_source_count",
        "manganese_source_count",
        "magnesium_supplement_mg",
        "manganese_supplement_mg",
        "processed_food_score",
        "antihypertensive_taken"
      ],
      "purpose": "Assess mineral sufficiency for ATP and enzyme activity."
    },
    "inflammation_load": {
      "inputs": [
        "processed_food_score",
        "stool_form_score",
        "stress_level_score",
        "sleep_quality_score",
        "cold_sensitivity_score"
      ],
      "purpose": "Daily inflammatory environment index."
    },
    "muscle_load": {
      "inputs": [
        "shoulder_stiffness_score",
        "forearm_tension_score",
        "hand_palm_tension_score",
        "rehab_minutes_shoulder_scapula"
      ],
      "purpose": "Musculo-fascial load level along shoulder–arm–hand line."
    },
    "mi_acetylcoa_score": {
      "inputs": [
        "nutrition",
        "microbiome_scfa",
        "minerals_Mg_Mn_B",
        "hormone_state",
        "processed_food_score",
        "drug_effects",
        "cold_sensitivity_score"
      ],
      "purpose": "Central AcetylCoA availability index."
    }
  },

  "disease_mi_matrix_v2": {
    "schema": {
      "fields": [
        "disease_id",
        "name",
        "name_en",
        "category",
        "description",
        "core_pathways",
        "deviation_codes",
        "snapshot_markers",
        "related_mi_engines",
        "intervention_focus"
      ],
      "core_pathways_allowed_values": [
        "high",
        "moderate",
        "low",
        "normal"
      ],
      "mi_engines_allowed": [
        "MI-AcetylCoA",
        "MI-Estrobolome",
        "MI-MBT55",
        "MI-Mitochondria",
        "MI-Inflammation",
        "MI-Neuro-Endocrine",
        "MI-Musculo-Fascial"
      ]
    },
    "batches": {
      "completed_batches": [
        "Batch 1 (D002–D011)",
        "Batch 2 (D012–D021)",
        "Batch 3 (D022–D031)",
        "Batch 4 (D032–D041)",
        "Batch 5 (D042–D051)",
        "Batch 6 (D052–D061)",
        "Batch 7 (D062–D071)",
        "Batch 8 (D072–D081)",
        "Batch 9 (D082–D091)",
        "Batch 10 (D092–D101)",
        "Batch 11 (D102–D111)",
        "Batch 12 (D112–D121)",
        "Batch 13 (D122–D131)",
        "Batch 14 (D132–D141)",
        "Batch 15 (D142–D151)",
        "Batch 16 (D152–D161)",
        "Batch 17 (D162–D171)",
        "Batch 18 (D172–D181)",
        "Batch 19 (D182–D191)",
        "Batch 20 (D192–D201)",
        "Batch 21 (D202–D211)",
        "Batch 22 (D212–D221)",
        "Batch 23 (D222–D231)",
        "Batch 24 (D232–D241)",
        "Batch 25 (D242–D251)",
        "Batch 26 (D252–D261)",
        "Batch 27 (D262–D271)",
        "Batch 28 (D272–D281)",
        "Batch 29 (D282–D291)",
        "Batch 30 (D292–D301)"
      ],
      "pending_work": [
        "D091–D100 unified list (integration format v2).",
        "Batches 31+ (D302–D311 and beyond) under new AcetylCoA/Estrobolome design."
      ],
      "sample_batch_30": [
        "D292: Stress-Triggered Color Shift",
        "D293: Hormone-Linked Stool Color Shift",
        "D294: Bile-Linked Stool Color Shift",
        "D295: Lipid-Driven Stool Color Shift",
        "D296: Fermentation-Driven Color Shift",
        "D297: Transit-Dependent Color Shift",
        "D298: Endotoxin-Linked Color Shift",
        "D299: Immune-Driven Color Shift",
        "D300: Multi-Factor Stool Color Shift",
        "D301: Chronic Stool Color Variability"
      ]
    }
  },

  "consistency_check_spec": {
    "target_file": "disease_mi_matrix_v2.json",
    "checks": [
      "core_pathways values must be in {high, moderate, low, normal}.",
      "disease_id must match ^D[0-9]+$ and be unique.",
      "if core_pathways.acetylcoa != normal then related_mi_engines must contain MI-AcetylCoA.",
      "if core_pathways.estrobolome != normal then related_mi_engines must contain MI-Estrobolome.",
      "related_mi_engines values must be in allowed MI engine list.",
      "core_pathways must contain keys: acetylcoa, estrobolome, mitochondria, mbt55, inflammation."
    ],
    "auto_fix_rules": [
      "Add MI-AcetylCoA when acetylcoa is high/moderate/low and missing.",
      "Add MI-Estrobolome when estrobolome is high/moderate/low and missing.",
      "Do not auto-fix invalid core_pathways values; report as errors."
    ]
  },

  "healthbook_mi_api": {
    "endpoint": "/api/healthbook/mi/evaluate",
    "method": "POST",
    "request": {
      "fields": [
        "user_id",
        "snapshot",
        "options"
      ],
      "options": [
        "include_raw_matches",
        "max_triggers_per_axis"
      ]
    },
    "response": {
      "fields": [
        "mi_scores",
        "axis_triggers",
        "recommended_interventions",
        "meta"
      ],
      "mi_scores_axes": [
        "acetylcoa",
        "estrobolome",
        "mbt55",
        "mitochondria",
        "inflammation",
        "neuro_endocrine"
      ],
      "intervention_categories": [
        "diet",
        "lifestyle",
        "kampo"
      ]
    },
    "error_handling": {
      "400": [
        "INVALID_JSON",
        "MISSING_FIELD",
        "INVALID_FIELD_TYPE"
      ],
      "500": [
        "INTERNAL_ERROR"
      ],
      "empty_snapshot_behavior": "Return all MI scores as 0, no interventions, meta.warnings explaining defaulting."
    }
  },

  "migration_prompt_core": {
    "purpose": "Transfer full HealthBook-MI context to a new multi-agent system.",
    "threads": [
      "🗃️HealthBook-MI repository construction (Disease-MI Matrix v2, schemas, engines).",
      "🏢HealthBook-MI case-based redesign (Estrobolome, AcetylCoA, MBT55 integration, philosophy)."
    ],
    "agent_roles": [
      "matrix_engine: continue Disease-MI Matrix v2 generation and consistency.",
      "design_engine: evolve MI engines, indices, and architecture (AcetylCoA/Estrobolome-centric).",
      "api_engine: maintain and extend HealthBook-MI API and snapshot schema.",
      "analysis_engine: run case-based inference and correlation (e.g., thumb CM joint pain scenarios)."
    ],
    "key_pending_tasks": [
      "Generate D091–D100 unified list under v2 format.",
      "Extend Disease-MI Matrix v2 beyond D301 with new AcetylCoA/Estrobolome design.",
      "Formalize MI-AcetylCoA Index and MI-Estrobolome Score equations.",
      "Integrate MBT55 functional mapping into MI engines.",
      "Finalize HealthBook-MI Architecture v3 (Metabolic OS)."
    ]
  }
}
```