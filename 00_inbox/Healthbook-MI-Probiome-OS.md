```
healthbook-mi-probiome-os/
│
├── README.md
├── LICENSE
├── .env.example
│
├── docs/
│   ├── architecture/
│   │   ├── metabolic_os.md
│   │   ├── estrobolome.md
│   │   ├── mbt55.md
│   │   ├── ai_agents.md
│   │   └── disease_matrix.md
│   ├── api/
│   │   ├── medical_api.md
│   │   ├── insurance_api.md
│   │   └── snapshot_api.md
│   └── engines/
│       ├── acetylcoa_engine.md
│       ├── estrobolome_engine.md
│       ├── mbt55_engine.md
│       ├── phenotyping_engine.md
│       ├── inflammation_engine.md
│       └── oriental_medicine_engine.md
│
├── engines/
│   ├── probiotics_screening/
│   │   ├── mks_engine.py
│   │   ├── metabolite_predictor.py
│   │   └── synergy_mapper.py
│   ├── phenotyping/
│   │   ├── questionnaire_engine.py
│   │   ├── deviation_codes.py
│   │   └── phenotype_classifier.py
│   ├── estrobolome/
│   │   ├── estrobolome_engine.py
│   │   ├── beta_glucuronidase_model.py
│   │   └── hormone_balance.py
│   ├── endocrine_axis/
│   │   ├── hpa_axis.py
│   │   ├── hpg_axis.py
│   │   └── hpt_axis.py
│   ├── acetylcoa_atp/
│   │   ├── acetylcoa_engine.py
│   │   ├── substrate_flux.py
│   │   └── atp_model.py
│   ├── inflammation_immune/
│   │   ├── inflammation_engine.py
│   │   ├── immune_pattern.py
│   │   └── scfa_bileacid_model.py
│   └── oriental_medicine/
│       ├── kampo_engine.py
│       ├── meridian_model.py
│       └── formula_recommender.py
│
├── ai_agents/
│   ├── triage_agent/
│   │   ├── triage_agent.py
│   │   └── prompts/
│   ├── risk_explainer/
│   │   ├── explainer_agent.py
│   │   └── prompts/
│   ├── insurance_underwriting/
│   │   ├── underwriting_agent.py
│   │   └── rules/
│   └── medical_assistant/
│       ├── clinical_agent.py
│       └── prompts/
│
├── data/
│   ├── pathways/
│   │   ├── master_pathways.json
│   │   └── animal_metabolic_library.json
│   ├── mbt/
│   │   ├── probiotic_matrix.json
│   │   └── mbt55_profiles.json
│   ├── questionnaire/
│   │   ├── questionnaire_200_en.json
│   │   └── questionnaire_200_jp.json
│   ├── disease/
│   │   ├── disease_matrix_137.json
│   │   └── disease_mi_matrix_v2.json
│   └── kampo/
│       ├── kampo_metabolic_library.json
│       └── formula_index.json
│
├── schemas/
│   ├── metabolic_snapshot_v2.schema.json
│   ├── disease_mi_matrix_v2.schema.json
│   ├── phenotype.schema.json
│   ├── mbt55.schema.json
│   └── kampo.schema.json
│
├── interfaces/
│   ├── medical/
│   │   ├── api/
│   │   ├── ui/
│   │   └── reports/
│   ├── insurance/
│   │   ├── api/
│   │   ├── underwriting_rules/
│   │   └── risk_models/
│   └── marketplace/
│       ├── registry/
│       └── kpis/
│
├── platform/
│   ├── orchestrator/
│   │   ├── engine_orchestrator.py
│   │   └── snapshot_builder.py
│   ├── pipelines/
│   │   ├── medical_pipeline.py
│   │   ├── insurance_pipeline.py
│   │   └── probiotics_pipeline.py
│   └── utils/
│       ├── validators.py
│       ├── loaders.py
│       └── converters.py
│
└── tests/
    ├── unit/
    ├── integration/
    └── e2e/
```


```
engines/acetylcoa_atp/acetylcoa_engine.py
engines/estrobolome/estrobolome_engine.py
engines/probiotics_screening/mks_engine.py
```


