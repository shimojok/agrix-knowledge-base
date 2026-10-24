## ✅ ステータス確認

GitHubリポジトリ **M3-BioSynergy** を確認しました。

**現状**:
- 存在する: ✅ https://github.com/shimojok/M3-BioSynergy
- 最終コミット: 2026-04-01（昨日）
- 内容: `src/core/hypercycle.py` などのコア実装あり
- 言語: Python 100%

**不足している要素**:
- ❌ HealthBook統合エンジン（推論エンジン）
- ❌ MBT漢方代謝ライブラリーのJSON
- ❌ 200項目問診＋137疾病マトリックスの完全英語化データ
- ❌ Game3連携デモ

---

## 🚀 本スレッドでの実装計画

### フェーズ1: データの完全英語化（JSON）

以下の3つのJSONファイルを生成します：

1. **`data/questionnaire_200_en.json`** - 200項目問診（英語）
2. **`data/disease_matrix_137_en.json`** - 137疾病マトリックス（英語）
3. **`data/kampo_metabolic_library_en.json`** - MBT漢方代謝ライブラリー（英語）

### フェーズ2: HealthBook推論エンジンの実装

4. **`src/healthbook/engine.py`** - 統合推論エンジン
5. **`src/healthbook/disease_risk.py`** - 疾病リスク予測
6. **`src/healthbook/phytochemical_recommender.py`** - ファイトケミカル推奨

### フェーズ3: デモシステム

7. **`examples/healthbook_demo.py`** - 統合ヘルスケアシミュレーション
8. **`examples/mbt_probiotics_screening.py`** - MBT Probioticsスクリーニング
9. **`examples/game3_integration.py`** - Game3連携デモ

---

## 実行

**データの英語化から開始します。** 各JSONファイルを順次生成します。

### フェーズ1-1: 問診200項目（英語版）生成開始

`questionnaire_full.json`（日本語）を英語化します。まずID 1-10のサンプルを生成します。

```json
{
  "version": "1.0",
  "total_questions": 200,
  "categories": {
    "eating_habits": [1, 50],
    "lifestyle": [51, 100],
    "environment_constitution": [101, 150],
    "symptoms": [151, 200]
  },
  "questions": {
    "1": {
      "id": 1,
      "category": "eating_habits",
      "question": "Meal times are irregular",
      "risk_factors": ["irregular"],
      "metabolic_impact": "Disrupted digestive rhythm → autonomic nervous system load",
      "related_diseases": ["gastritis", "obesity", "diabetes_mellitus"],
      "weight": 0.70
    },
    "2": {
      "id": 2,
      "category": "eating_habits",
      "question": "Often skip breakfast",
      "risk_factors": ["breakfast_skipping"],
      "metabolic_impact": "Disrupted gluconeogenesis rhythm → morning hypoglycemia tendency",
      "related_diseases": ["diabetes_mellitus", "obesity", "chronic_fatigue"],
      "weight": 0.85
    },
    "3": {
      "id": 3,
      "category": "eating_habits",
      "question": "Often eat late-night snacks before bed",
      "risk_factors": ["late_night_meal"],
      "metabolic_impact": "Gastrointestinal burden → reduced lipid metabolism → poor sleep quality",
      "related_diseases": ["chronic_gastritis", "obesity", "diabetes_mellitus"],
      "weight": 0.80
    },
    "4": {
      "id": 4,
      "category": "eating_habits",
      "question": "Eat quickly",
      "risk_factors": ["fast_eating"],
      "metabolic_impact": "Insufficient chewing → reduced digestive enzyme secretion → glucose metabolism load",
      "related_diseases": ["gastritis", "obesity", "diabetes_mellitus"],
      "weight": 0.75
    },
    "5": {
      "id": 5,
      "category": "eating_habits",
      "question": "Eat until full",
      "risk_factors": ["overeating"],
      "metabolic_impact": "Gastric distension → rapid insulin spike → fat accumulation",
      "related_diseases": ["obesity", "fatty_liver", "diabetes_mellitus"],
      "weight": 0.78
    },
    "6": {
      "id": 6,
      "category": "eating_habits",
      "question": "Always finish everything served",
      "risk_factors": ["overeating_tendency"],
      "metabolic_impact": "Blunted satiety center → excessive intake",
      "related_diseases": ["obesity", "fatty_liver"],
      "weight": 0.60
    },
    "7": {
      "id": 7,
      "category": "eating_habits",
      "question": "Large portion of rice with small amount of side dishes",
      "risk_factors": ["carb_overload"],
      "metabolic_impact": "Rapid blood glucose spike → insulin resistance",
      "related_diseases": ["diabetes_mellitus", "obesity"],
      "weight": 0.82
    },
    "8": {
      "id": 8,
      "category": "eating_habits",
      "question": "Snack frequently",
      "risk_factors": ["frequent_snacking"],
      "metabolic_impact": "Increased blood glucose fluctuation → pancreatic load",
      "related_diseases": ["diabetes_mellitus", "obesity"],
      "weight": 0.88
    },
    "9": {
      "id": 9,
      "category": "eating_habits",
      "question": "Prefer salty foods",
      "risk_factors": ["high_salt"],
      "metabolic_impact": "Excess sodium → elevated blood pressure",
      "related_diseases": ["hypertension", "stomach_cancer", "nephritis"],
      "weight": 0.90
    },
    "10": {
      "id": 10,
      "category": "eating_habits",
      "question": "Eat many meat dishes",
      "risk_factors": ["high_fat", "high_meat"],
      "metabolic_impact": "Excess saturated fatty acids → lipid metabolism load",
      "related_diseases": ["hyperlipidemia", "atherosclerosis", "fatty_liver"],
      "weight": 0.80
    }
  }
}
```

この形式で全200項目を生成します。

続いてID 11-30、31-50、51-100、101-150、151-200と進めます。

**ID 11-30（食習慣カテゴリ）を生成します。**

```json
{
  "11": {
    "id": 11,
    "category": "eating_habits",
    "question": "Eat out frequently",
    "risk_factors": ["frequent_dining_out"],
    "metabolic_impact": "Excess fat, salt, and carbohydrates → increased metabolic load",
    "related_diseases": ["hypertension", "hyperlipidemia", "obesity"],
    "weight": 0.82
  },
  "12": {
    "id": 12,
    "category": "eating_habits",
    "question": "Often have simple meals",
    "risk_factors": ["nutritional_deficiency", "simple_meal_centric"],
    "metabolic_impact": "Vitamin and mineral deficiency → reduced enzyme activity",
    "related_diseases": ["anemia", "chronic_fatigue", "immunodeficiency"],
    "weight": 0.70
  },
  "13": {
    "id": 13,
    "category": "eating_habits",
    "question": "Diet is Western-style",
    "risk_factors": ["high_fat", "high_animal_food"],
    "metabolic_impact": "Excess saturated fatty acids → lipid metabolism load",
    "related_diseases": ["hyperlipidemia", "atherosclerosis"],
    "weight": 0.75
  },
  "14": {
    "id": 14,
    "category": "eating_habits",
    "question": "Have many food preferences",
    "risk_factors": ["picky_eating"],
    "metabolic_impact": "Nutritional imbalance → metabolic dysregulation",
    "related_diseases": ["anemia", "immunodeficiency"],
    "weight": 0.72
  },
  "15": {
    "id": 15,
    "category": "eating_habits",
    "question": "Use strong spices",
    "risk_factors": ["high_spice"],
    "metabolic_impact": "Gastric mucosal irritation → increased gastritis risk",
    "related_diseases": ["gastritis", "gastric_ulcer"],
    "weight": 0.68
  },
  "16": {
    "id": 16,
    "category": "eating_habits",
    "question": "Dislike fish",
    "risk_factors": ["insufficient_fish", "EPA_DHA_deficiency"],
    "metabolic_impact": "Deficiency of anti-inflammatory fatty acids → inflammatory tendency",
    "related_diseases": ["atherosclerosis", "hyperlipidemia"],
    "weight": 0.78
  },
  "17": {
    "id": 17,
    "category": "eating_habits",
    "question": "Dislike meat",
    "risk_factors": ["protein_deficiency"],
    "metabolic_impact": "Reduced muscle mass → decreased basal metabolism",
    "related_diseases": ["anemia", "muscle_weakness"],
    "weight": 0.65
  },
  "18": {
    "id": 18,
    "category": "eating_habits",
    "question": "Dislike dark-colored vegetables",
    "risk_factors": ["antioxidant_deficiency"],
    "metabolic_impact": "Phytochemical deficiency → increased oxidative stress",
    "related_diseases": ["atherosclerosis", "immunodeficiency"],
    "weight": 0.80
  },
  "19": {
    "id": 19,
    "category": "eating_habits",
    "question": "Dislike milk and dairy products",
    "risk_factors": ["calcium_deficiency"],
    "metabolic_impact": "Reduced bone metabolism → decreased bone density",
    "related_diseases": ["osteoporosis"],
    "weight": 0.70
  },
  "20": {
    "id": 20,
    "category": "eating_habits",
    "question": "Dislike fruit",
    "risk_factors": ["vitamin_deficiency"],
    "metabolic_impact": "Antioxidant vitamin deficiency → reduced immunity",
    "related_diseases": ["common_cold", "fatigue"],
    "weight": 0.68
  },
  "21": {
    "id": 21,
    "category": "eating_habits",
    "question": "Prefer fatty foods",
    "risk_factors": ["high_fat"],
    "metabolic_impact": "Elevated triglycerides → lipid metabolism load",
    "related_diseases": ["hyperlipidemia", "fatty_liver"],
    "weight": 0.88
  },
  "22": {
    "id": 22,
    "category": "eating_habits",
    "question": "Eat 2 or more eggs daily",
    "risk_factors": ["high_cholesterol_intake"],
    "metabolic_impact": "Lipid metabolism load → tendency for LDL elevation",
    "related_diseases": ["hyperlipidemia"],
    "weight": 0.65
  },
  "23": {
    "id": 23,
    "category": "eating_habits",
    "question": "Often feel thirsty and sweat heavily",
    "risk_factors": ["fluid_deficiency", "high_salt"],
    "metabolic_impact": "Dehydration tendency → blood concentration → circulatory load",
    "related_diseases": ["heat_stroke", "renal_burden"],
    "weight": 0.72
  },
  "24": {
    "id": 24,
    "category": "eating_habits",
    "question": "Like sugary drinks and sweets",
    "risk_factors": ["high_sugar"],
    "metabolic_impact": "Rapid blood glucose spike → insulin resistance",
    "related_diseases": ["diabetes_mellitus", "obesity"],
    "weight": 0.92
  },
  "25": {
    "id": 25,
    "category": "eating_habits",
    "question": "Drink alcohol daily",
    "risk_factors": ["chronic_alcohol"],
    "metabolic_impact": "Hepatic metabolic load → fatty liver risk",
    "related_diseases": ["liver_disease", "hypertension"],
    "weight": 0.90
  },
  "26": {
    "id": 26,
    "category": "eating_habits",
    "question": "Drink heavily once starting",
    "risk_factors": ["binge_drinking_tendency"],
    "metabolic_impact": "Acute hepatic load → lipid metabolism disorder",
    "related_diseases": ["liver_disease", "pancreatitis"],
    "weight": 0.88
  },
  "27": {
    "id": 27,
    "category": "eating_habits",
    "question": "Skip meals when drinking alcohol",
    "risk_factors": ["nutritional_deficiency", "alcohol_dependence_tendency"],
    "metabolic_impact": "Malnutrition → hepatic metabolic disorder",
    "related_diseases": ["liver_disease", "anemia"],
    "weight": 0.75
  },
  "28": {
    "id": 28,
    "category": "eating_habits",
    "question": "Drink 5 or more cups of coffee daily",
    "risk_factors": ["excess_caffeine"],
    "metabolic_impact": "Sympathetic stimulation → elevated blood pressure and sleep disturbance",
    "related_diseases": ["hypertension", "insomnia"],
    "weight": 0.70
  },
  "29": {
    "id": 29,
    "category": "eating_habits",
    "question": "Dislike mushrooms and seaweed",
    "risk_factors": ["fiber_deficiency", "mineral_deficiency"],
    "metabolic_impact": "Gut environment deterioration → constipation, inflammatory tendency",
    "related_diseases": ["constipation", "gut_dysbiosis"],
    "weight": 0.78
  },
  "30": {
    "id": 30,
    "category": "eating_habits",
    "question": "Prefer hot foods and drinks",
    "risk_factors": ["high_temperature_intake"],
    "metabolic_impact": "Esophageal mucosal irritation → inflammation risk",
    "related_diseases": ["esophagitis"],
    "weight": 0.60
  }
}
```

**ID 31-50（食習慣カテゴリ・後半）を生成します。**

```json
{
  "31": {
    "id": 31,
    "category": "eating_habits",
    "question": "Frequently drink cold beverages",
    "risk_factors": ["excessive_cold_beverages"],
    "metabolic_impact": "Gastrointestinal cooling → reduced digestive enzyme activity → metabolic decline",
    "related_diseases": ["gastrointestinal_weakness", "diarrhea"],
    "weight": 0.72
  },
  "32": {
    "id": 32,
    "category": "eating_habits",
    "question": "Frequently eat instant foods",
    "risk_factors": ["high_processed_food"],
    "metabolic_impact": "Additive load → increased hepatic metabolic burden",
    "related_diseases": ["hepatic_dysfunction", "hypertension"],
    "weight": 0.85
  },
  "33": {
    "id": 33,
    "category": "eating_habits",
    "question": "Frequently eat fried foods",
    "risk_factors": ["high_fat", "oxidized_oil_intake"],
    "metabolic_impact": "Increased oxidative stress → lipid metabolism disorder",
    "related_diseases": ["hyperlipidemia", "atherosclerosis"],
    "weight": 0.90
  },
  "34": {
    "id": 34,
    "category": "eating_habits",
    "question": "Frequently eat salty pickled vegetables",
    "risk_factors": ["high_salt"],
    "metabolic_impact": "Excess sodium → elevated blood pressure",
    "related_diseases": ["hypertension", "stomach_cancer"],
    "weight": 0.88
  },
  "35": {
    "id": 35,
    "category": "eating_habits",
    "question": "Frequently eat sweets and pastries",
    "risk_factors": ["high_sugar"],
    "metabolic_impact": "Blood glucose fluctuations → insulin resistance",
    "related_diseases": ["diabetes_mellitus", "obesity"],
    "weight": 0.92
  },
  "36": {
    "id": 36,
    "category": "eating_habits",
    "question": "Frequently eat bread and noodles",
    "risk_factors": ["high_refined_carb"],
    "metabolic_impact": "Rapid blood glucose spike → pancreatic load",
    "related_diseases": ["diabetes_mellitus", "obesity"],
    "weight": 0.80
  },
  "37": {
    "id": 37,
    "category": "eating_habits",
    "question": "Prefer strongly flavored dishes",
    "risk_factors": ["high_salt"],
    "metabolic_impact": "Increased renal burden → elevated blood pressure",
    "related_diseases": ["hypertension", "renal_dysfunction"],
    "weight": 0.85
  },
  "38": {
    "id": 38,
    "category": "eating_habits",
    "question": "Meal time is short (fast eating)",
    "risk_factors": ["fast_eating"],
    "metabolic_impact": "Insufficient chewing → indigestion → rapid blood glucose spike",
    "related_diseases": ["obesity", "gastritis"],
    "weight": 0.78
  },
  "39": {
    "id": 39,
    "category": "eating_habits",
    "question": "Do not chew much during meals",
    "risk_factors": ["insufficient_chewing"],
    "metabolic_impact": "Reduced digestive enzyme secretion → decreased nutrient absorption",
    "related_diseases": ["gastrointestinal_disorders", "obesity"],
    "weight": 0.75
  },
  "40": {
    "id": 40,
    "category": "eating_habits",
    "question": "Meal portions vary greatly day to day",
    "risk_factors": ["unstable_meal_rhythm"],
    "metabolic_impact": "Unstable glycemic regulation → autonomic nervous system load",
    "related_diseases": ["hypoglycemia", "fatigue"],
    "weight": 0.70
  },
  "41": {
    "id": 41,
    "category": "eating_habits",
    "question": "Often eat late at night",
    "risk_factors": ["late_night_meal", "delayed_meal"],
    "metabolic_impact": "Reduced lipid metabolism → fat accumulation",
    "related_diseases": ["obesity", "dyspepsia"],
    "weight": 0.88
  },
  "42": {
    "id": 42,
    "category": "eating_habits",
    "question": "Have a light breakfast",
    "risk_factors": ["insufficient_breakfast"],
    "metabolic_impact": "Morning hypoglycemia → reduced concentration",
    "related_diseases": ["hypoglycemia", "fatigue"],
    "weight": 0.68
  },
  "43": {
    "id": 43,
    "category": "eating_habits",
    "question": "Often eat out for lunch",
    "risk_factors": ["frequent_dining_out"],
    "metabolic_impact": "Excess fat and salt → metabolic load",
    "related_diseases": ["hypertension", "hyperlipidemia"],
    "weight": 0.80
  },
  "44": {
    "id": 44,
    "category": "eating_habits",
    "question": "Dinner is often late",
    "risk_factors": ["delayed_meal"],
    "metabolic_impact": "Digestive burden → reduced sleep quality",
    "related_diseases": ["dyspepsia", "insomnia"],
    "weight": 0.75
  },
  "45": {
    "id": 45,
    "category": "eating_habits",
    "question": "Large dinner portions",
    "risk_factors": ["overeating"],
    "metabolic_impact": "Fat accumulation → blood glucose elevation",
    "related_diseases": ["obesity", "fatty_liver"],
    "weight": 0.85
  },
  "46": {
    "id": 46,
    "category": "eating_habits",
    "question": "Often lie down immediately after meals",
    "risk_factors": ["gastric_stasis"],
    "metabolic_impact": "Gastric content reflux → increased GERD risk",
    "related_diseases": ["gerd"],
    "weight": 0.70
  },
  "47": {
    "id": 47,
    "category": "eating_habits",
    "question": "Always have something sweet after meals",
    "risk_factors": ["high_sugar"],
    "metabolic_impact": "Rapid blood glucose spike → pancreatic load",
    "related_diseases": ["diabetes_mellitus", "obesity"],
    "weight": 0.90
  },
  "48": {
    "id": 48,
    "category": "eating_habits",
    "question": "Drink plenty of fluids during meals",
    "risk_factors": ["gastric_acid_dilution"],
    "metabolic_impact": "Reduced digestive capacity → decreased nutrient absorption",
    "related_diseases": ["gastrointestinal_disorders"],
    "weight": 0.65
  },
  "49": {
    "id": 49,
    "category": "eating_habits",
    "question": "Watch TV or use smartphone during meals",
    "risk_factors": ["distracted_eating"],
    "metabolic_impact": "Blunted satiety center → overeating",
    "related_diseases": ["obesity"],
    "weight": 0.72
  },
  "50": {
    "id": 50,
    "category": "eating_habits",
    "question": "Meal times vary daily",
    "risk_factors": ["unstable_meal_rhythm"],
    "metabolic_impact": "Disrupted metabolic rhythm → unstable glycemic regulation",
    "related_diseases": ["hypoglycemia", "fatigue"],
    "weight": 0.78
  }
}
```

**ID 51-70（生活習慣カテゴリ）を生成します。**

```json
{
  "51": {
    "id": 51,
    "category": "lifestyle",
    "question": "Sleep hours are irregular",
    "risk_factors": ["irregular_sleep_rhythm"],
    "metabolic_impact": "Autonomic nervous system disruption → reduced metabolic rhythm",
    "related_diseases": ["insomnia", "chronic_fatigue", "hypertension"],
    "weight": 0.85
  },
  "52": {
    "id": 52,
    "category": "lifestyle",
    "question": "Difficulty falling asleep",
    "risk_factors": ["sleep_onset_disorder"],
    "metabolic_impact": "Sympathetic dominance → poor sleep quality",
    "related_diseases": ["insomnia", "autonomic_dysfunction"],
    "weight": 0.78
  },
  "53": {
    "id": 53,
    "category": "lifestyle",
    "question": "Often wake up during the night",
    "risk_factors": ["midnight_awakening"],
    "metabolic_impact": "Sleep fragmentation → hormonal imbalance",
    "related_diseases": ["insomnia", "chronic_fatigue"],
    "weight": 0.80
  },
  "54": {
    "id": 54,
    "category": "lifestyle",
    "question": "Difficulty waking up in the morning",
    "risk_factors": ["sleep_deficiency"],
    "metabolic_impact": "Adrenal fatigue → reduced metabolism",
    "related_diseases": ["chronic_fatigue", "hypotension"],
    "weight": 0.75
  },
  "55": {
    "id": 55,
    "category": "lifestyle",
    "question": "Lack of exercise",
    "risk_factors": ["physical_inactivity"],
    "metabolic_impact": "Reduced muscle mass → decreased basal metabolism",
    "related_diseases": ["obesity", "diabetes_mellitus", "hypertension"],
    "weight": 0.92
  },
  "56": {
    "id": 56,
    "category": "lifestyle",
    "question": "Sit for long periods",
    "risk_factors": ["prolonged_sitting"],
    "metabolic_impact": "Blood stasis → increased insulin resistance",
    "related_diseases": ["diabetes_mellitus", "obesity"],
    "weight": 0.85
  },
  "57": {
    "id": 57,
    "category": "lifestyle",
    "question": "Walking speed is slow",
    "risk_factors": ["muscle_weakness"],
    "metabolic_impact": "Reduced lower limb muscle strength → decreased metabolic efficiency",
    "related_diseases": ["sarcopenia", "locomotive_syndrome"],
    "weight": 0.70
  },
  "58": {
    "id": 58,
    "category": "lifestyle",
    "question": "Often avoid stairs",
    "risk_factors": ["low_physical_activity"],
    "metabolic_impact": "Reduced cardiorespiratory function → metabolic decline",
    "related_diseases": ["obesity", "hypertension"],
    "weight": 0.72
  },
  "59": {
    "id": 59,
    "category": "lifestyle",
    "question": "Spend most holidays at home",
    "risk_factors": ["insufficient_activity"],
    "metabolic_impact": "Reduced energy expenditure → weight gain",
    "related_diseases": ["obesity", "depressive_tendency"],
    "weight": 0.68
  },
  "60": {
    "id": 60,
    "category": "lifestyle",
    "question": "Prone to stress",
    "risk_factors": ["high_stress"],
    "metabolic_impact": "Elevated cortisol → fat accumulation and blood glucose elevation",
    "related_diseases": ["hypertension", "diabetes_mellitus", "insomnia"],
    "weight": 0.90
  },
  "61": {
    "id": 61,
    "category": "lifestyle",
    "question": "Easily irritable",
    "risk_factors": ["emotional_stress", "sympathetic_dominance"],
    "metabolic_impact": "Elevated cortisol → blood glucose elevation and fat accumulation",
    "related_diseases": ["hypertension", "diabetes_mellitus", "insomnia"],
    "weight": 0.85
  },
  "62": {
    "id": 62,
    "category": "lifestyle",
    "question": "Poor concentration",
    "risk_factors": ["brain_fatigue", "sleep_deficiency"],
    "metabolic_impact": "Reduced neural metabolism → cognitive decline",
    "related_diseases": ["chronic_fatigue", "attention_deficit"],
    "weight": 0.72
  },
  "63": {
    "id": 63,
    "category": "lifestyle",
    "question": "Severe shoulder stiffness",
    "risk_factors": ["poor_blood_flow", "poor_posture"],
    "metabolic_impact": "Muscle tension → reduced peripheral circulation",
    "related_diseases": ["tension_headache", "autonomic_dysfunction"],
    "weight": 0.70
  },
  "64": {
    "id": 64,
    "category": "lifestyle",
    "question": "Frequent headaches",
    "risk_factors": ["poor_blood_flow", "stress"],
    "metabolic_impact": "Reduced cerebral blood flow → oxygen deficiency",
    "related_diseases": ["migraine", "tension_headache"],
    "weight": 0.78
  },
  "65": {
    "id": 65,
    "category": "lifestyle",
    "question": "Eyes tire easily",
    "risk_factors": ["vdT_work", "poor_blood_flow"],
    "metabolic_impact": "Eye muscle fatigue → increased oxidative stress",
    "related_diseases": ["eye_strain", "headache"],
    "weight": 0.68
  },
  "66": {
    "id": 66,
    "category": "lifestyle",
    "question": "Hands and feet tend to be cold",
    "risk_factors": ["poor_peripheral_circulation"],
    "metabolic_impact": "Reduced blood flow → metabolic decline",
    "related_diseases": ["cold_sensitivity", "hypotension"],
    "weight": 0.80
  },
  "67": {
    "id": 67,
    "category": "lifestyle",
    "question": "Difficulty sweating",
    "risk_factors": ["autonomic_dysfunction"],
    "metabolic_impact": "Impaired thermoregulation → reduced metabolic efficiency",
    "related_diseases": ["autonomic_dysfunction", "heat_stroke_risk"],
    "weight": 0.75
  },
  "68": {
    "id": 68,
    "category": "lifestyle",
    "question": "Prone to constipation",
    "risk_factors": ["gut_dysbiosis", "fiber_deficiency"],
    "metabolic_impact": "Reduced intestinal metabolism → toxin reabsorption",
    "related_diseases": ["constipation", "skin_issues", "fatigue"],
    "weight": 0.92
  },
  "69": {
    "id": 69,
    "category": "lifestyle",
    "question": "Prone to diarrhea",
    "risk_factors": ["intestinal_hyperactivity", "indigestion"],
    "metabolic_impact": "Reduced nutrient absorption → metabolic decline",
    "related_diseases": ["irritable_bowel_syndrome"],
    "weight": 0.78
  },
  "70": {
    "id": 70,
    "category": "lifestyle",
    "question": "Catch colds easily",
    "risk_factors": ["immunodeficiency"],
    "metabolic_impact": "Reduced immune metabolism → increased infection risk",
    "related_diseases": ["common_cold", "infectious_diseases"],
    "weight": 0.88
  }
}
```

**ID 71-90（生活習慣カテゴリ・続き）を生成します。**

```json
{
  "71": {
    "id": 71,
    "category": "lifestyle",
    "question": "Easily fatigued",
    "risk_factors": ["chronic_fatigue", "reduced_metabolism"],
    "metabolic_impact": "Reduced ATP production → decreased systemic metabolic efficiency",
    "related_diseases": ["chronic_fatigue_syndrome", "anemia"],
    "weight": 0.88
  },
  "72": {
    "id": 72,
    "category": "lifestyle",
    "question": "Often feel sluggish",
    "risk_factors": ["autonomic_dysfunction", "sleep_deficiency"],
    "metabolic_impact": "Disrupted metabolic rhythm → energy deficiency",
    "related_diseases": ["autonomic_dysfunction", "chronic_fatigue"],
    "weight": 0.80
  },
  "73": {
    "id": 73,
    "category": "lifestyle",
    "question": "Prone to low mood",
    "risk_factors": ["emotional_stress", "neurotransmitter_deficiency"],
    "metabolic_impact": "Reduced serotonin metabolism → emotional instability",
    "related_diseases": ["depressive_tendency", "anxiety_disorder"],
    "weight": 0.82
  },
  "74": {
    "id": 74,
    "category": "lifestyle",
    "question": "Often lack motivation",
    "risk_factors": ["dopamine_deficiency", "chronic_fatigue"],
    "metabolic_impact": "Reduced neural metabolism → decreased motivation",
    "related_diseases": ["depressive_tendency", "chronic_fatigue"],
    "weight": 0.78
  },
  "75": {
    "id": 75,
    "category": "lifestyle",
    "question": "Gain weight easily",
    "risk_factors": ["reduced_lipid_metabolism", "physical_inactivity"],
    "metabolic_impact": "Decreased basal metabolism → fat accumulation",
    "related_diseases": ["obesity", "fatty_liver"],
    "weight": 0.92
  },
  "76": {
    "id": 76,
    "category": "lifestyle",
    "question": "Lose weight easily",
    "risk_factors": ["malabsorption", "hyperthyroidism"],
    "metabolic_impact": "Excessive metabolism or malabsorption → weight loss",
    "related_diseases": ["thyroid_disorders", "digestive_absorption_disorders"],
    "weight": 0.75
  },
  "77": {
    "id": 77,
    "category": "lifestyle",
    "question": "Prone to swelling",
    "risk_factors": ["reduced_fluid_metabolism", "renal_dysfunction"],
    "metabolic_impact": "Impaired fluid regulation → edema",
    "related_diseases": ["renal_dysfunction", "early_heart_failure"],
    "weight": 0.85
  },
  "78": {
    "id": 78,
    "category": "lifestyle",
    "question": "Skin prone to roughness",
    "risk_factors": ["vitamin_deficiency", "gut_dysbiosis"],
    "metabolic_impact": "Reduced skin metabolism → barrier dysfunction",
    "related_diseases": ["dermatitis", "allergies"],
    "weight": 0.80
  },
  "79": {
    "id": 79,
    "category": "lifestyle",
    "question": "Hair loss",
    "risk_factors": ["nutritional_deficiency", "hormonal_imbalance"],
    "metabolic_impact": "Reduced hair follicle metabolism → alopecia",
    "related_diseases": ["alopecia", "thyroid_disorders"],
    "weight": 0.78
  },
  "80": {
    "id": 80,
    "category": "lifestyle",
    "question": "Nails break easily",
    "risk_factors": ["mineral_deficiency", "protein_deficiency"],
    "metabolic_impact": "Reduced keratin metabolism → nail fragility",
    "related_diseases": ["nutritional_deficiency", "thyroid_disorders"],
    "weight": 0.72
  },
  "81": {
    "id": 81,
    "category": "lifestyle",
    "question": "Shortness of breath",
    "risk_factors": ["reduced_cardiorespiratory_function", "physical_inactivity"],
    "metabolic_impact": "Insufficient oxygen supply → reduced energy metabolism",
    "related_diseases": ["early_heart_failure", "anemia"],
    "weight": 0.82
  },
  "82": {
    "id": 82,
    "category": "lifestyle",
    "question": "Sometimes feel palpitations",
    "risk_factors": ["autonomic_instability", "stress"],
    "metabolic_impact": "Sympathetic overactivity → elevated heart rate",
    "related_diseases": ["arrhythmia", "panic_symptoms"],
    "weight": 0.80
  },
  "83": {
    "id": 83,
    "category": "lifestyle",
    "question": "Prone to hot flashes",
    "risk_factors": ["poor_blood_flow_regulation"],
    "metabolic_impact": "Impaired thermoregulation → autonomic load",
    "related_diseases": ["menopause_symptoms", "autonomic_dysfunction"],
    "weight": 0.72
  },
  "84": {
    "id": 84,
    "category": "lifestyle",
    "question": "Experience dizziness when standing up",
    "risk_factors": ["hypotension", "anemia"],
    "metabolic_impact": "Reduced cerebral blood flow → oxygen deficiency",
    "related_diseases": ["orthostatic_hypotension", "anemia"],
    "weight": 0.78
  },
  "85": {
    "id": 85,
    "category": "lifestyle",
    "question": "Sometimes experience numbness in limbs",
    "risk_factors": ["poor_peripheral_circulation", "reduced_neural_metabolism"],
    "metabolic_impact": "Reduced peripheral nerve metabolism → sensory abnormalities",
    "related_diseases": ["peripheral_neuropathy", "early_diabetes"],
    "weight": 0.80
  },
  "86": {
    "id": 86,
    "category": "lifestyle",
    "question": "Yawn frequently",
    "risk_factors": ["brain_fatigue", "oxygen_deficiency"],
    "metabolic_impact": "Reduced brain metabolism → increased oxygen demand",
    "related_diseases": ["chronic_fatigue", "sleep_deficiency"],
    "weight": 0.65
  },
  "87": {
    "id": 87,
    "category": "lifestyle",
    "question": "Shoulders and neck stiffen when concentrating",
    "risk_factors": ["poor_posture", "muscle_tension"],
    "metabolic_impact": "Localized reduced blood flow → lactate accumulation",
    "related_diseases": ["tension_headache"],
    "weight": 0.70
  },
  "88": {
    "id": 88,
    "category": "lifestyle",
    "question": "Sometimes experience night sweats",
    "risk_factors": ["autonomic_instability", "hormonal_fluctuations"],
    "metabolic_impact": "Impaired thermoregulation → reduced sleep quality",
    "related_diseases": ["menopause_symptoms", "autonomic_dysfunction"],
    "weight": 0.75
  },
  "89": {
    "id": 89,
    "category": "lifestyle",
    "question": "Sigh frequently",
    "risk_factors": ["mental_stress", "shallow_breathing"],
    "metabolic_impact": "Insufficient oxygen supply → reduced metabolic efficiency",
    "related_diseases": ["anxiety_symptoms", "chronic_fatigue"],
    "weight": 0.68
  },
  "90": {
    "id": 90,
    "category": "lifestyle",
    "question": "Still tired after sleeping",
    "risk_factors": ["poor_sleep_quality", "adrenal_fatigue"],
    "metabolic_impact": "Reduced recovery metabolism → chronic fatigue",
    "related_diseases": ["chronic_fatigue_syndrome", "autonomic_dysfunction"],
    "weight": 0.92
  }
}
```

**ID 91-100（生活習慣カテゴリ・最終）を生成します。**

```json
{
  "91": {
    "id": 91,
    "category": "lifestyle",
    "question": "Body tends to feel hot",
    "risk_factors": ["autonomic_instability", "hormonal_fluctuations"],
    "metabolic_impact": "Impaired thermoregulation → disrupted metabolic rhythm",
    "related_diseases": ["menopause_symptoms", "autonomic_dysfunction"],
    "weight": 0.75
  },
  "92": {
    "id": 92,
    "category": "lifestyle",
    "question": "Often feel heaviness in limbs",
    "risk_factors": ["poor_blood_flow", "muscle_weakness"],
    "metabolic_impact": "Reduced peripheral metabolism → fatigue accumulation",
    "related_diseases": ["chronic_fatigue", "anemia"],
    "weight": 0.72
  },
  "93": {
    "id": 93,
    "category": "lifestyle",
    "question": "Bruise easily",
    "risk_factors": ["vascular_fragility", "vitamin_deficiency"],
    "metabolic_impact": "Reduced vascular metabolism → capillary damage",
    "related_diseases": ["vitamin_c_deficiency", "thrombocytopenia"],
    "weight": 0.70
  },
  "94": {
    "id": 94,
    "category": "lifestyle",
    "question": "Sometimes feel breathless",
    "risk_factors": ["shallow_breathing", "stress"],
    "metabolic_impact": "Insufficient oxygen supply → reduced energy metabolism",
    "related_diseases": ["anxiety_symptoms", "hyperventilation_syndrome"],
    "weight": 0.78
  },
  "95": {
    "id": 95,
    "category": "lifestyle",
    "question": "Often feel thirsty",
    "risk_factors": ["dehydration_tendency", "high_salt"],
    "metabolic_impact": "Impaired fluid balance → circulatory load",
    "related_diseases": ["hypertension", "renal_dysfunction"],
    "weight": 0.68
  },
  "96": {
    "id": 96,
    "category": "lifestyle",
    "question": "Sweat easily",
    "risk_factors": ["sympathetic_dominance"],
    "metabolic_impact": "Excessive thermoregulation → electrolyte depletion",
    "related_diseases": ["autonomic_dysfunction", "dehydration"],
    "weight": 0.70
  },
  "97": {
    "id": 97,
    "category": "lifestyle",
    "question": "Body prone to swelling",
    "risk_factors": ["reduced_fluid_metabolism", "renal_dysfunction"],
    "metabolic_impact": "Impaired fluid regulation → edema",
    "related_diseases": ["renal_dysfunction", "early_heart_failure"],
    "weight": 0.85
  },
  "98": {
    "id": 98,
    "category": "lifestyle",
    "question": "Feel unwell with weather pressure changes",
    "risk_factors": ["autonomic_instability"],
    "metabolic_impact": "Atmospheric pressure stress → impaired blood flow regulation",
    "related_diseases": ["migraine", "autonomic_dysfunction"],
    "weight": 0.78
  },
  "99": {
    "id": 99,
    "category": "lifestyle",
    "question": "Prone to illness during seasonal transitions",
    "risk_factors": ["immunodeficiency", "autonomic_instability"],
    "metabolic_impact": "Environmental change stress → impaired metabolic adjustment",
    "related_diseases": ["common_cold", "allergies"],
    "weight": 0.80
  },
  "100": {
    "id": 100,
    "category": "lifestyle",
    "question": "Low body temperature (hypothermia)",
    "risk_factors": ["reduced_basal_metabolism"],
    "metabolic_impact": "Reduced enzyme activity → systemic metabolic decline",
    "related_diseases": ["hypothermia", "chronic_fatigue"],
    "weight": 0.90
  }
}
```

**ID 101-120（症状カテゴリ）を生成します。**

```json
{
  "101": {
    "id": 101,
    "category": "symptoms",
    "question": "Head feels heavy",
    "risk_factors": ["brain_fatigue", "poor_blood_flow"],
    "metabolic_impact": "Reduced cerebral blood flow → oxygen deficiency",
    "related_diseases": ["tension_headache", "autonomic_dysfunction"],
    "weight": 0.78
  },
  "102": {
    "id": 102,
    "category": "symptoms",
    "question": "Sometimes experience dizziness",
    "risk_factors": ["hypotension", "anemia", "autonomic_instability"],
    "metabolic_impact": "Sudden changes in cerebral blood flow → oxygen deficiency",
    "related_diseases": ["orthostatic_hypotension", "anemia"],
    "weight": 0.85
  },
  "103": {
    "id": 103,
    "category": "symptoms",
    "question": "Experience tinnitus (ringing in ears)",
    "risk_factors": ["poor_blood_flow", "stress"],
    "metabolic_impact": "Reduced inner ear metabolism → sensory abnormalities",
    "related_diseases": ["tinnitus", "autonomic_dysfunction"],
    "weight": 0.72
  },
  "104": {
    "id": 104,
    "category": "symptoms",
    "question": "Sometimes vision becomes blurry",
    "risk_factors": ["eye_strain", "poor_blood_flow"],
    "metabolic_impact": "Reduced ocular metabolism → visual impairment",
    "related_diseases": ["eye_strain", "hypotension"],
    "weight": 0.70
  },
  "105": {
    "id": 105,
    "category": "symptoms",
    "question": "Sensation of chest tightness",
    "risk_factors": ["stress", "autonomic_instability"],
    "metabolic_impact": "Chest muscle tension → reduced respiratory metabolism",
    "related_diseases": ["anxiety_symptoms", "gerd"],
    "weight": 0.75
  },
  "106": {
    "id": 106,
    "category": "symptoms",
    "question": "Sometimes experience chest pain",
    "risk_factors": ["muscle_tension", "stress"],
    "metabolic_impact": "Reduced chest blood flow → oxygen deficiency",
    "related_diseases": ["intercostal_neuralgia", "anxiety_symptoms"],
    "weight": 0.80
  },
  "107": {
    "id": 107,
    "category": "symptoms",
    "question": "Feel short of breath",
    "risk_factors": ["shallow_breathing", "stress"],
    "metabolic_impact": "Insufficient oxygen supply → reduced energy metabolism",
    "related_diseases": ["hyperventilation_syndrome", "anxiety_symptoms"],
    "weight": 0.82
  },
  "108": {
    "id": 108,
    "category": "symptoms",
    "question": "Stomach feels heavy or bloated",
    "risk_factors": ["reduced_gastrointestinal_function", "overeating"],
    "metabolic_impact": "Reduced digestive metabolism → impaired nutrient absorption",
    "related_diseases": ["gastritis", "dyspepsia"],
    "weight": 0.88
  },
  "109": {
    "id": 109,
    "category": "symptoms",
    "question": "Experience heartburn",
    "risk_factors": ["reflux", "excess_stomach_acid"],
    "metabolic_impact": "Esophageal mucosal irritation → inflammation",
    "related_diseases": ["gerd"],
    "weight": 0.85
  },
  "110": {
    "id": 110,
    "category": "symptoms",
    "question": "Abdomen feels bloated",
    "risk_factors": ["gut_dysbiosis", "excess_gas_production"],
    "metabolic_impact": "Reduced intestinal metabolism → fermentation abnormalities",
    "related_diseases": ["irritable_bowel_syndrome"],
    "weight": 0.80
  },
  "111": {
    "id": 111,
    "category": "symptoms",
    "question": "Excessive gas accumulation",
    "risk_factors": ["intestinal_fermentation_abnormalities", "fiber_deficiency"],
    "metabolic_impact": "Disrupted intestinal metabolism → increased gas production",
    "related_diseases": ["irritable_bowel_syndrome", "gut_dysbiosis"],
    "weight": 0.80
  },
  "112": {
    "id": 112,
    "category": "symptoms",
    "question": "Hard stool or difficulty passing",
    "risk_factors": ["reduced_intestinal_motility", "fluid_deficiency"],
    "metabolic_impact": "Reduced intestinal metabolism → difficulty defecating",
    "related_diseases": ["constipation", "hemorrhoids"],
    "weight": 0.88
  },
  "113": {
    "id": 113,
    "category": "symptoms",
    "question": "Loose stool or prone to diarrhea",
    "risk_factors": ["intestinal_hyperactivity", "indigestion"],
    "metabolic_impact": "Malabsorption → reduced nutrient metabolism",
    "related_diseases": ["irritable_bowel_syndrome"],
    "weight": 0.82
  },
  "114": {
    "id": 114,
    "category": "symptoms",
    "question": "Feel sleepy after meals",
    "risk_factors": ["rapid_blood_glucose_spike", "excess_insulin_response"],
    "metabolic_impact": "Blood glucose fluctuations → unstable energy metabolism",
    "related_diseases": ["prediabetes", "hypoglycemia"],
    "weight": 0.90
  },
  "115": {
    "id": 115,
    "category": "symptoms",
    "question": "Palpitations after meals",
    "risk_factors": ["blood_glucose_fluctuations", "autonomic_instability"],
    "metabolic_impact": "Sympathetic stimulation → elevated heart rate",
    "related_diseases": ["hypoglycemia", "anxiety_symptoms"],
    "weight": 0.78
  },
  "116": {
    "id": 116,
    "category": "symptoms",
    "question": "Stomach feels distended after meals",
    "risk_factors": ["reduced_gastrointestinal_function", "indigestion"],
    "metabolic_impact": "Reduced gastric metabolism → digestive stasis",
    "related_diseases": ["gastritis", "dyspepsia"],
    "weight": 0.85
  },
  "117": {
    "id": 117,
    "category": "symptoms",
    "question": "Heartburn after meals",
    "risk_factors": ["reflux", "excess_stomach_acid"],
    "metabolic_impact": "Esophageal mucosal irritation → inflammation",
    "related_diseases": ["gerd"],
    "weight": 0.88
  },
  "118": {
    "id": 118,
    "category": "symptoms",
    "question": "Stomach growling after meals",
    "risk_factors": ["excess_intestinal_fermentation", "indigestion"],
    "metabolic_impact": "Disrupted intestinal metabolism → increased gas production",
    "related_diseases": ["gut_dysbiosis"],
    "weight": 0.72
  },
  "119": {
    "id": 119,
    "category": "symptoms",
    "question": "Feel sluggish after meals",
    "risk_factors": ["blood_glucose_fluctuations", "adrenal_fatigue"],
    "metabolic_impact": "Reduced energy metabolism → fatigue",
    "related_diseases": ["hypoglycemia", "chronic_fatigue"],
    "weight": 0.82
  },
  "120": {
    "id": 120,
    "category": "symptoms",
    "question": "Loss of concentration after meals",
    "risk_factors": ["blood_glucose_fluctuations", "reduced_brain_metabolism"],
    "metabolic_impact": "Insufficient brain energy → cognitive decline",
    "related_diseases": ["hypoglycemia", "chronic_fatigue"],
    "weight": 0.78
  }
}
```

**ID 121-140（症状カテゴリ・続き）を生成します。**

```json
{
  "121": {
    "id": 121,
    "category": "symptoms",
    "question": "Often have poor appetite",
    "risk_factors": ["reduced_gastrointestinal_function", "stress"],
    "metabolic_impact": "Reduced digestive metabolism → insufficient nutrient absorption",
    "related_diseases": ["gastritis", "autonomic_dysfunction"],
    "weight": 0.82
  },
  "122": {
    "id": 122,
    "category": "symptoms",
    "question": "Sometimes have abnormally increased appetite",
    "risk_factors": ["blood_glucose_fluctuations", "stress_eating"],
    "metabolic_impact": "Excessive insulin response → fat accumulation",
    "related_diseases": ["prediabetes", "obesity"],
    "weight": 0.88
  },
  "123": {
    "id": 123,
    "category": "symptoms",
    "question": "Mouth feels dry",
    "risk_factors": ["dehydration_tendency", "high_salt"],
    "metabolic_impact": "Impaired fluid balance → circulatory load",
    "related_diseases": ["hypertension", "diabetes_mellitus"],
    "weight": 0.75
  },
  "124": {
    "id": 124,
    "category": "symptoms",
    "question": "Mouth feels bitter or sticky",
    "risk_factors": ["reduced_liver_function", "indigestion"],
    "metabolic_impact": "Bile metabolism disruption → reduced digestive function",
    "related_diseases": ["gallbladder_disorders", "gastrointestinal_disorders"],
    "weight": 0.78
  },
  "125": {
    "id": 125,
    "category": "symptoms",
    "question": "Tongue tends to be coated white (tongue coating)",
    "risk_factors": ["reduced_gastrointestinal_function", "gut_dysbiosis"],
    "metabolic_impact": "Reduced digestive metabolism → oral bacterial balance changes",
    "related_diseases": ["gastritis", "gut_dysbiosis"],
    "weight": 0.82
  },
  "126": {
    "id": 126,
    "category": "symptoms",
    "question": "Concerned about bad breath",
    "risk_factors": ["gut_dysbiosis", "poor_oral_bacterial_balance"],
    "metabolic_impact": "Intestinal metabolism abnormalities → increased volatile substances",
    "related_diseases": ["gastrointestinal_disorders", "periodontal_disease"],
    "weight": 0.80
  },
  "127": {
    "id": 127,
    "category": "symptoms",
    "question": "Sometimes heart pounds",
    "risk_factors": ["stress", "blood_glucose_fluctuations"],
    "metabolic_impact": "Sympathetic stimulation → elevated heart rate",
    "related_diseases": ["anxiety_symptoms", "hypoglycemia"],
    "weight": 0.78
  },
  "128": {
    "id": 128,
    "category": "symptoms",
    "question": "Sometimes hands tremble",
    "risk_factors": ["hypoglycemia", "autonomic_instability"],
    "metabolic_impact": "Insufficient blood glucose → reduced neural metabolism",
    "related_diseases": ["hypoglycemia", "anxiety_symptoms"],
    "weight": 0.85
  },
  "129": {
    "id": 129,
    "category": "symptoms",
    "question": "Body feels hot / flushing",
    "risk_factors": ["autonomic_instability", "hormonal_fluctuations"],
    "metabolic_impact": "Impaired thermoregulation → disrupted metabolic rhythm",
    "related_diseases": ["menopause_symptoms", "autonomic_dysfunction"],
    "weight": 0.75
  },
  "130": {
    "id": 130,
    "category": "symptoms",
    "question": "Body tends to feel cold",
    "risk_factors": ["poor_peripheral_circulation", "reduced_basal_metabolism"],
    "metabolic_impact": "Reduced enzyme activity → systemic metabolic decline",
    "related_diseases": ["cold_sensitivity", "hypotension"],
    "weight": 0.88
  },
  "131": {
    "id": 131,
    "category": "symptoms",
    "question": "Difficulty falling asleep",
    "risk_factors": ["sleep_onset_disorder", "stress"],
    "metabolic_impact": "Sympathetic dominance → reduced sleep metabolism",
    "related_diseases": ["insomnia", "autonomic_dysfunction"],
    "weight": 0.85
  },
  "132": {
    "id": 132,
    "category": "symptoms",
    "question": "Wake up multiple times during the night",
    "risk_factors": ["midnight_awakening", "hormonal_fluctuations"],
    "metabolic_impact": "Sleep fragmentation → reduced recovery metabolism",
    "related_diseases": ["insomnia", "chronic_fatigue"],
    "weight": 0.88
  },
  "133": {
    "id": 133,
    "category": "symptoms",
    "question": "Still tired even after waking up",
    "risk_factors": ["poor_sleep_quality", "adrenal_fatigue"],
    "metabolic_impact": "Reduced recovery metabolism → chronic fatigue",
    "related_diseases": ["chronic_fatigue_syndrome"],
    "weight": 0.92
  },
  "134": {
    "id": 134,
    "category": "symptoms",
    "question": "Dream frequently or have nightmares",
    "risk_factors": ["excessive_rem_sleep", "stress"],
    "metabolic_impact": "Reduced sleep quality → unstable brain metabolism",
    "related_diseases": ["insomnia", "anxiety_symptoms"],
    "weight": 0.70
  },
  "135": {
    "id": 135,
    "category": "symptoms",
    "question": "Experience night sweats",
    "risk_factors": ["autonomic_instability", "hormonal_fluctuations"],
    "metabolic_impact": "Impaired thermoregulation → reduced sleep quality",
    "related_diseases": ["menopause_symptoms", "autonomic_dysfunction"],
    "weight": 0.75
  },
  "136": {
    "id": 136,
    "category": "symptoms",
    "question": "Grind teeth while sleeping",
    "risk_factors": ["stress", "jaw_clenching_habit"],
    "metabolic_impact": "Muscle tension → temporomandibular joint load",
    "related_diseases": ["temporomandibular_disorder", "headache"],
    "weight": 0.78
  },
  "137": {
    "id": 137,
    "category": "symptoms",
    "question": "Morning headaches",
    "risk_factors": ["poor_sleep_quality", "teeth_grinding"],
    "metabolic_impact": "Reduced cerebral blood flow → oxygen deficiency",
    "related_diseases": ["tension_headache", "sleep_apnea"],
    "weight": 0.82
  },
  "138": {
    "id": 138,
    "category": "symptoms",
    "question": "Body feels stiff in the morning",
    "risk_factors": ["poor_blood_flow", "poor_sleep_posture"],
    "metabolic_impact": "Reduced muscle metabolism → stiffness",
    "related_diseases": ["muscle_tension", "autonomic_dysfunction"],
    "weight": 0.75
  },
  "139": {
    "id": 139,
    "category": "symptoms",
    "question": "Stomach feels heavy in the morning",
    "risk_factors": ["late_night_meal", "indigestion"],
    "metabolic_impact": "Reduced gastric metabolism → digestive stasis",
    "related_diseases": ["gastritis", "dyspepsia"],
    "weight": 0.80
  },
  "140": {
    "id": 140,
    "category": "symptoms",
    "question": "Swelling in the morning",
    "risk_factors": ["reduced_fluid_metabolism", "renal_dysfunction"],
    "metabolic_impact": "Impaired fluid regulation → edema",
    "related_diseases": ["renal_dysfunction", "early_heart_failure"],
    "weight": 0.85
  }
}
```

**ID 141-160（症状カテゴリ・続き）を生成します。**

```json
{
  "141": {
    "id": 141,
    "category": "symptoms",
    "question": "Body feels sluggish and unmotivated to move",
    "risk_factors": ["chronic_fatigue", "reduced_metabolism"],
    "metabolic_impact": "Reduced ATP production → decreased physical activity",
    "related_diseases": ["chronic_fatigue_syndrome", "autonomic_dysfunction"],
    "weight": 0.88
  },
  "142": {
    "id": 142,
    "category": "symptoms",
    "question": "Body feels heavy",
    "risk_factors": ["poor_blood_flow", "reduced_metabolism"],
    "metabolic_impact": "Reduced muscle metabolism → fatigue",
    "related_diseases": ["anemia", "chronic_fatigue"],
    "weight": 0.80
  },
  "143": {
    "id": 143,
    "category": "symptoms",
    "question": "Body often feels stiff",
    "risk_factors": ["muscle_tension", "poor_blood_flow"],
    "metabolic_impact": "Reduced muscle metabolism → stiffness",
    "related_diseases": ["muscle_tension_disorder", "autonomic_dysfunction"],
    "weight": 0.75
  },
  "144": {
    "id": 144,
    "category": "symptoms",
    "question": "Limbs feel heavy",
    "risk_factors": ["poor_peripheral_circulation", "muscle_weakness"],
    "metabolic_impact": "Reduced peripheral metabolism → fatigue accumulation",
    "related_diseases": ["anemia", "chronic_fatigue"],
    "weight": 0.78
  },
  "145": {
    "id": 145,
    "category": "symptoms",
    "question": "Body prone to swelling",
    "risk_factors": ["reduced_fluid_metabolism", "renal_dysfunction"],
    "metabolic_impact": "Impaired fluid regulation → edema",
    "related_diseases": ["renal_dysfunction", "early_heart_failure"],
    "weight": 0.85
  },
  "146": {
    "id": 146,
    "category": "symptoms",
    "question": "Body tends to feel cold",
    "risk_factors": ["poor_peripheral_circulation", "reduced_basal_metabolism"],
    "metabolic_impact": "Reduced enzyme activity → systemic metabolic decline",
    "related_diseases": ["cold_sensitivity", "hypotension"],
    "weight": 0.88
  },
  "147": {
    "id": 147,
    "category": "symptoms",
    "question": "Body tends to feel hot",
    "risk_factors": ["autonomic_instability", "hormonal_fluctuations"],
    "metabolic_impact": "Impaired thermoregulation → disrupted metabolic rhythm",
    "related_diseases": ["menopause_symptoms", "autonomic_dysfunction"],
    "weight": 0.75
  },
  "148": {
    "id": 148,
    "category": "symptoms",
    "question": "Sometimes experience numbness in body",
    "risk_factors": ["reduced_peripheral_nerve_metabolism", "poor_blood_flow"],
    "metabolic_impact": "Reduced nerve metabolism → sensory abnormalities",
    "related_diseases": ["peripheral_neuropathy", "early_diabetes"],
    "weight": 0.82
  },
  "149": {
    "id": 149,
    "category": "symptoms",
    "question": "Sometimes body trembles",
    "risk_factors": ["hypoglycemia", "autonomic_instability"],
    "metabolic_impact": "Insufficient blood glucose → reduced neural metabolism",
    "related_diseases": ["hypoglycemia", "anxiety_symptoms"],
    "weight": 0.85
  },
  "150": {
    "id": 150,
    "category": "symptoms",
    "question": "Body feels feverish",
    "risk_factors": ["inflammatory_response", "immune_activation"],
    "metabolic_impact": "Increased immune metabolism → elevated body temperature",
    "related_diseases": ["infectious_diseases", "inflammatory_diseases"],
    "weight": 0.80
  },
  "151": {
    "id": 151,
    "category": "symptoms",
    "question": "Body feels sluggish and unable to concentrate",
    "risk_factors": ["chronic_fatigue", "reduced_brain_metabolism"],
    "metabolic_impact": "Insufficient brain energy → cognitive decline",
    "related_diseases": ["chronic_fatigue_syndrome", "autonomic_dysfunction"],
    "weight": 0.88
  },
  "152": {
    "id": 152,
    "category": "symptoms",
    "question": "Body feels heavy and movements are slow",
    "risk_factors": ["reduced_metabolism", "muscle_weakness"],
    "metabolic_impact": "Reduced ATP production → decreased physical activity",
    "related_diseases": ["hypothyroidism", "chronic_fatigue"],
    "weight": 0.82
  },
  "153": {
    "id": 153,
    "category": "symptoms",
    "question": "Body feels exhausted and wants to lie down",
    "risk_factors": ["adrenal_fatigue", "sleep_deficiency"],
    "metabolic_impact": "Reduced recovery metabolism → increased fatigue",
    "related_diseases": ["chronic_fatigue_syndrome"],
    "weight": 0.85
  },
  "154": {
    "id": 154,
    "category": "symptoms",
    "question": "Body feels sluggish and unable to wake up in the morning",
    "risk_factors": ["poor_sleep_quality", "hormonal_rhythm_disruption"],
    "metabolic_impact": "Reduced recovery metabolism → morning fatigue",
    "related_diseases": ["sleep_disorders", "adrenal_fatigue"],
    "weight": 0.90
  },
  "155": {
    "id": 155,
    "category": "symptoms",
    "question": "Body feels sluggish and unable to concentrate at work",
    "risk_factors": ["brain_fatigue", "blood_glucose_fluctuations"],
    "metabolic_impact": "Reduced brain metabolism → cognitive decline",
    "related_diseases": ["chronic_fatigue", "hypoglycemia"],
    "weight": 0.88
  },
  "156": {
    "id": 156,
    "category": "symptoms",
    "question": "Body feels sluggish and lacks motivation",
    "risk_factors": ["dopamine_deficiency", "chronic_fatigue"],
    "metabolic_impact": "Reduced neural metabolism → decreased motivation",
    "related_diseases": ["depressive_tendency", "chronic_fatigue"],
    "weight": 0.82
  },
  "157": {
    "id": 157,
    "category": "symptoms",
    "question": "Body feels sluggish and standing is difficult",
    "risk_factors": ["muscle_weakness", "poor_blood_flow"],
    "metabolic_impact": "Reduced peripheral metabolism → fatigue accumulation",
    "related_diseases": ["anemia", "autonomic_dysfunction"],
    "weight": 0.80
  },
  "158": {
    "id": 158,
    "category": "symptoms",
    "question": "Body feels sluggish with palpitations",
    "risk_factors": ["blood_glucose_fluctuations", "autonomic_instability"],
    "metabolic_impact": "Sympathetic stimulation → elevated heart rate",
    "related_diseases": ["hypoglycemia", "anxiety_symptoms"],
    "weight": 0.85
  },
  "159": {
    "id": 159,
    "category": "symptoms",
    "question": "Body feels sluggish with shortness of breath",
    "risk_factors": ["shallow_breathing", "stress"],
    "metabolic_impact": "Insufficient oxygen supply → reduced energy metabolism",
    "related_diseases": ["hyperventilation_syndrome", "anxiety_symptoms"],
    "weight": 0.82
  },
  "160": {
    "id": 160,
    "category": "symptoms",
    "question": "Body feels sluggish with poor appetite",
    "risk_factors": ["reduced_gastrointestinal_function", "adrenal_fatigue"],
    "metabolic_impact": "Reduced digestive metabolism → insufficient nutrient absorption",
    "related_diseases": ["gastritis", "chronic_fatigue"],
    "weight": 0.85
  }
}
```

**ID 161-180（症状カテゴリ・続き）を生成します。**

```json
{
  "161": {
    "id": 161,
    "category": "symptoms",
    "question": "Body feels sluggish with brain fog",
    "risk_factors": ["reduced_brain_metabolism", "sleep_deficiency"],
    "metabolic_impact": "Insufficient brain energy → cognitive decline",
    "related_diseases": ["chronic_fatigue", "autonomic_dysfunction"],
    "weight": 0.88
  },
  "162": {
    "id": 162,
    "category": "symptoms",
    "question": "Body feels sluggish with irritability",
    "risk_factors": ["stress", "blood_glucose_fluctuations"],
    "metabolic_impact": "Unstable neural metabolism → emotional instability",
    "related_diseases": ["anxiety_symptoms", "chronic_fatigue"],
    "weight": 0.82
  },
  "163": {
    "id": 163,
    "category": "symptoms",
    "question": "Body feels sluggish with low mood",
    "risk_factors": ["dopamine_deficiency", "chronic_fatigue"],
    "metabolic_impact": "Neurotransmitter deficiency → decreased motivation",
    "related_diseases": ["depressive_tendency", "chronic_fatigue"],
    "weight": 0.85
  },
  "164": {
    "id": 164,
    "category": "symptoms",
    "question": "Body feels sluggish with palpitations",
    "risk_factors": ["blood_glucose_fluctuations", "autonomic_instability"],
    "metabolic_impact": "Sympathetic stimulation → elevated heart rate",
    "related_diseases": ["hypoglycemia", "anxiety_symptoms"],
    "weight": 0.85
  },
  "165": {
    "id": 165,
    "category": "symptoms",
    "question": "Body feels sluggish with shortness of breath",
    "risk_factors": ["shallow_breathing", "stress"],
    "metabolic_impact": "Insufficient oxygen supply → reduced energy metabolism",
    "related_diseases": ["hyperventilation_syndrome", "anxiety_symptoms"],
    "weight": 0.82
  },
  "166": {
    "id": 166,
    "category": "symptoms",
    "question": "Body feels sluggish with cold extremities",
    "risk_factors": ["poor_peripheral_circulation", "reduced_basal_metabolism"],
    "metabolic_impact": "Reduced enzyme activity → systemic metabolic decline",
    "related_diseases": ["cold_sensitivity", "hypotension"],
    "weight": 0.88
  },
  "167": {
    "id": 167,
    "category": "symptoms",
    "question": "Body feels sluggish with numbness in extremities",
    "risk_factors": ["reduced_peripheral_nerve_metabolism", "poor_blood_flow"],
    "metabolic_impact": "Reduced nerve metabolism → sensory abnormalities",
    "related_diseases": ["peripheral_neuropathy", "early_diabetes"],
    "weight": 0.82
  },
  "168": {
    "id": 168,
    "category": "symptoms",
    "question": "Body feels sluggish with nausea",
    "risk_factors": ["autonomic_instability", "reduced_gastrointestinal_function"],
    "metabolic_impact": "Reduced digestive metabolism → gastrointestinal discomfort",
    "related_diseases": ["gastritis", "autonomic_dysfunction"],
    "weight": 0.80
  },
  "169": {
    "id": 169,
    "category": "symptoms",
    "question": "Body feels sluggish with dizziness",
    "risk_factors": ["hypotension", "anemia"],
    "metabolic_impact": "Reduced cerebral blood flow → oxygen deficiency",
    "related_diseases": ["orthostatic_hypotension", "anemia"],
    "weight": 0.85
  },
  "170": {
    "id": 170,
    "category": "symptoms",
    "question": "Body feels sluggish with lightheadedness when standing",
    "risk_factors": ["hypotension", "poor_blood_flow_regulation"],
    "metabolic_impact": "Sudden changes in cerebral blood flow → oxygen deficiency",
    "related_diseases": ["orthostatic_hypotension", "autonomic_dysfunction"],
    "weight": 0.85
  },
  "171": {
    "id": 171,
    "category": "symptoms",
    "question": "Body feels sluggish with headache",
    "risk_factors": ["reduced_cerebral_blood_flow", "muscle_tension"],
    "metabolic_impact": "Reduced brain metabolism → oxygen deficiency",
    "related_diseases": ["tension_headache", "autonomic_dysfunction"],
    "weight": 0.82
  },
  "172": {
    "id": 172,
    "category": "symptoms",
    "question": "Body feels sluggish with shoulder stiffness",
    "risk_factors": ["muscle_tension", "poor_blood_flow"],
    "metabolic_impact": "Reduced local metabolism → lactate accumulation",
    "related_diseases": ["shoulder_stiffness", "tension_headache"],
    "weight": 0.78
  },
  "173": {
    "id": 173,
    "category": "symptoms",
    "question": "Body feels sluggish with heavy lower back",
    "risk_factors": ["muscle_weakness", "poor_blood_flow"],
    "metabolic_impact": "Reduced muscle metabolism → fatigue accumulation",
    "related_diseases": ["low_back_pain", "muscle_tension"],
    "weight": 0.75
  },
  "174": {
    "id": 174,
    "category": "symptoms",
    "question": "Body feels sluggish with joint pain",
    "risk_factors": ["inflammatory_response", "immune_activation"],
    "metabolic_impact": "Increased inflammatory metabolism → pain",
    "related_diseases": ["arthritis", "early_infection"],
    "weight": 0.80
  },
  "175": {
    "id": 175,
    "category": "symptoms",
    "question": "Body feels sluggish with eye strain",
    "risk_factors": ["eye_fatigue", "brain_fatigue"],
    "metabolic_impact": "Reduced ocular metabolism → visual load",
    "related_diseases": ["eye_strain", "headache"],
    "weight": 0.72
  },
  "176": {
    "id": 176,
    "category": "symptoms",
    "question": "Body feels sluggish with tinnitus",
    "risk_factors": ["poor_blood_flow", "autonomic_instability"],
    "metabolic_impact": "Reduced inner ear metabolism → sensory abnormalities",
    "related_diseases": ["tinnitus", "autonomic_dysfunction"],
    "weight": 0.75
  },
  "177": {
    "id": 177,
    "category": "symptoms",
    "question": "Body feels sluggish with sensation of throat tightness",
    "risk_factors": ["stress", "autonomic_instability"],
    "metabolic_impact": "Pharyngeal muscle tension → reduced respiratory metabolism",
    "related_diseases": ["globus_hystericus", "anxiety_symptoms"],
    "weight": 0.78
  },
  "178": {
    "id": 178,
    "category": "symptoms",
    "question": "Body feels sluggish with stomach upset",
    "risk_factors": ["reduced_gastrointestinal_function", "stress"],
    "metabolic_impact": "Reduced digestive metabolism → gastric discomfort",
    "related_diseases": ["gastritis", "autonomic_dysfunction"],
    "weight": 0.82
  },
  "179": {
    "id": 179,
    "category": "symptoms",
    "question": "Body feels sluggish with post-meal sleepiness",
    "risk_factors": ["blood_glucose_fluctuations", "excess_insulin_response"],
    "metabolic_impact": "Blood glucose fluctuations → unstable brain metabolism",
    "related_diseases": ["hypoglycemia", "prediabetes"],
    "weight": 0.90
  },
  "180": {
    "id": 180,
    "category": "symptoms",
    "question": "Body feels sluggish with poor concentration",
    "risk_factors": ["brain_fatigue", "blood_glucose_fluctuations"],
    "metabolic_impact": "Insufficient brain energy → cognitive decline",
    "related_diseases": ["chronic_fatigue", "hypoglycemia"],
    "weight": 0.88
  }
}
```

**ID 181-200（症状カテゴリ・最終）を生成します。**

```json
{
  "181": {
    "id": 181,
    "category": "symptoms",
    "question": "Body feels sluggish and lacks energy",
    "risk_factors": ["dopamine_deficiency", "chronic_fatigue"],
    "metabolic_impact": "Reduced neural metabolism → decreased motivation",
    "related_diseases": ["depressive_tendency", "chronic_fatigue_syndrome"],
    "weight": 0.85
  },
  "182": {
    "id": 182,
    "category": "symptoms",
    "question": "Body feels sluggish and cannot focus on work",
    "risk_factors": ["brain_fatigue", "blood_glucose_fluctuations"],
    "metabolic_impact": "Insufficient brain energy → cognitive decline",
    "related_diseases": ["chronic_fatigue", "hypoglycemia"],
    "weight": 0.88
  },
  "183": {
    "id": 183,
    "category": "symptoms",
    "question": "Body feels sluggish and wants to lie down",
    "risk_factors": ["adrenal_fatigue", "sleep_deficiency"],
    "metabolic_impact": "Reduced recovery metabolism → increased fatigue",
    "related_diseases": ["chronic_fatigue_syndrome"],
    "weight": 0.85
  },
  "184": {
    "id": 184,
    "category": "symptoms",
    "question": "Body feels sluggish and short of breath when moving",
    "risk_factors": ["reduced_cardiorespiratory_function", "anemia"],
    "metabolic_impact": "Insufficient oxygen supply → reduced energy metabolism",
    "related_diseases": ["early_heart_failure", "anemia"],
    "weight": 0.82
  },
  "185": {
    "id": 185,
    "category": "symptoms",
    "question": "Body feels sluggish and dizzy when moving",
    "risk_factors": ["hypotension", "poor_blood_flow_regulation"],
    "metabolic_impact": "Reduced cerebral blood flow → oxygen deficiency",
    "related_diseases": ["orthostatic_hypotension", "anemia"],
    "weight": 0.85
  },
  "186": {
    "id": 186,
    "category": "symptoms",
    "question": "Body feels sluggish and heart pounds when moving",
    "risk_factors": ["blood_glucose_fluctuations", "autonomic_instability"],
    "metabolic_impact": "Sympathetic stimulation → elevated heart rate",
    "related_diseases": ["hypoglycemia", "anxiety_symptoms"],
    "weight": 0.85
  },
  "187": {
    "id": 187,
    "category": "symptoms",
    "question": "Body feels sluggish and nauseous when moving",
    "risk_factors": ["autonomic_instability", "reduced_gastrointestinal_function"],
    "metabolic_impact": "Reduced digestive metabolism → gastrointestinal discomfort",
    "related_diseases": ["gastritis", "autonomic_dysfunction"],
    "weight": 0.80
  },
  "188": {
    "id": 188,
    "category": "symptoms",
    "question": "Body feels sluggish and headache when moving",
    "risk_factors": ["reduced_cerebral_blood_flow", "muscle_tension"],
    "metabolic_impact": "Reduced brain metabolism → oxygen deficiency",
    "related_diseases": ["tension_headache", "autonomic_dysfunction"],
    "weight": 0.82
  },
  "189": {
    "id": 189,
    "category": "symptoms",
    "question": "Body feels sluggish and joint pain when moving",
    "risk_factors": ["inflammatory_response", "immune_activation"],
    "metabolic_impact": "Increased inflammatory metabolism → pain",
    "related_diseases": ["arthritis", "early_infection"],
    "weight": 0.80
  },
  "190": {
    "id": 190,
    "category": "symptoms",
    "question": "Body feels sluggish and fatigue worsens with movement",
    "risk_factors": ["reduced_muscle_metabolism", "energy_deficiency"],
    "metabolic_impact": "Reduced ATP production → increased fatigue",
    "related_diseases": ["chronic_fatigue_syndrome", "anemia"],
    "weight": 0.88
  },
  "191": {
    "id": 191,
    "category": "symptoms",
    "question": "Body feels sluggish and wants to do nothing",
    "risk_factors": ["chronic_fatigue", "reduced_neural_metabolism"],
    "metabolic_impact": "Neurotransmitter deficiency → decreased motivation",
    "related_diseases": ["depressive_tendency", "chronic_fatigue_syndrome"],
    "weight": 0.88
  },
  "192": {
    "id": 192,
    "category": "symptoms",
    "question": "Body feels sluggish and mood becomes unstable",
    "risk_factors": ["stress", "blood_glucose_fluctuations"],
    "metabolic_impact": "Unstable neural metabolism → emotional fluctuations",
    "related_diseases": ["anxiety_symptoms", "autonomic_dysfunction"],
    "weight": 0.82
  },
  "193": {
    "id": 193,
    "category": "symptoms",
    "question": "Body feels sluggish with strong drowsiness",
    "risk_factors": ["sleep_deficiency", "blood_glucose_fluctuations"],
    "metabolic_impact": "Reduced brain metabolism → difficulty maintaining wakefulness",
    "related_diseases": ["sleep_disorders", "hypoglycemia"],
    "weight": 0.85
  },
  "194": {
    "id": 194,
    "category": "symptoms",
    "question": "Body feels sluggish and concentration does not last",
    "risk_factors": ["brain_fatigue", "blood_glucose_fluctuations"],
    "metabolic_impact": "Insufficient brain energy → cognitive decline",
    "related_diseases": ["chronic_fatigue", "hypoglycemia"],
    "weight": 0.88
  },
  "195": {
    "id": 195,
    "category": "symptoms",
    "question": "Body feels sluggish and standing is difficult",
    "risk_factors": ["muscle_weakness", "poor_blood_flow"],
    "metabolic_impact": "Reduced peripheral metabolism → fatigue accumulation",
    "related_diseases": ["anemia", "autonomic_dysfunction"],
    "weight": 0.80
  },
  "196": {
    "id": 196,
    "category": "symptoms",
    "question": "Body feels sluggish and walking is difficult",
    "risk_factors": ["reduced_muscle_metabolism", "reduced_cardiorespiratory_function"],
    "metabolic_impact": "Insufficient oxygen supply → reduced energy metabolism",
    "related_diseases": ["early_heart_failure", "anemia"],
    "weight": 0.82
  },
  "197": {
    "id": 197,
    "category": "symptoms",
    "question": "Body feels sluggish and cannot do housework",
    "risk_factors": ["chronic_fatigue", "adrenal_fatigue"],
    "metabolic_impact": "Reduced recovery metabolism → decreased activity level",
    "related_diseases": ["chronic_fatigue_syndrome"],
    "weight": 0.85
  },
  "198": {
    "id": 198,
    "category": "symptoms",
    "question": "Body feels sluggish and does not want to go out",
    "risk_factors": ["decreased_motivation", "reduced_neural_metabolism"],
    "metabolic_impact": "Neurotransmitter deficiency → reduced activity",
    "related_diseases": ["depressive_tendency", "chronic_fatigue"],
    "weight": 0.82
  },
  "199": {
    "id": 199,
    "category": "comprehensive",
    "question": "Recently, overall health feels poor",
    "risk_factors": ["chronic_fatigue", "reduced_metabolism"],
    "metabolic_impact": "Systemic metabolic decline → multi-system impact",
    "related_diseases": ["autonomic_dysfunction", "chronic_fatigue_syndrome"],
    "weight": 0.92
  },
  "200": {
    "id": 200,
    "category": "comprehensive",
    "question": "Feel like improving health condition",
    "risk_factors": ["poor_lifestyle", "chronic_fatigue"],
    "metabolic_impact": "Motivation for improvement → starting point for behavioral change",
    "related_diseases": ["lifestyle_related_diseases"],
    "weight": 1.00
  }
}
```

---

## ✅ フェーズ1-1完了：問診200項目（英語版）生成完了

JSONファイルの内容は上記の通りです。これらを一つのファイル `data/questionnaire_200_en.json` として保存できます。

**次のステップ**：
1. **フェーズ1-2**: 137疾病マトリックスJSON（英語版）生成
2. **フェーズ1-3**: MBT漢方代謝ライブラリーJSON（英語版）生成

続いて **137疾病マトリックス** の英語化に移ります。元のExcelデータ（137疾病 × 40食生活パターン）をJSON形式で生成します。

**フェーズ1-2: 137疾病マトリックス（英語版）生成**

```json
{
  "version": "1.0",
  "source": "Hamada Disease-Diet Matrix",
  "total_diseases": 137,
  "disease_categories": {
    "digestive": ["acute_gastritis", "gastric_duodenal_ulcer", "chronic_gastritis", "gastritis", "gastric_cancer", "esophageal_cancer", "colorectal_cancer", "colorectal_polyp", "fatty_liver", "liver_cancer", "hepatitis", "cirrhosis", "pancreatic_cancer", "pancreatitis", "chronic_pancreatitis", "cholecystitis", "cholelithiasis", "gerd", "esophagitis", "gastroptosis", "irritable_bowel_syndrome", "constipation", "atonic_constipation", "diarrhea", "acute_enteritis", "chronic_enteritis"],
    "cardiovascular": ["hypertension", "hyperlipidemia", "atherosclerosis", "myocardial_infarction", "angina_pectoris", "heart_failure", "cerebral_infarction", "cerebral_hemorrhage", "transient_ischemic_attack", "subarachnoid_hemorrhage", "arteriosclerosis", "benign_nephrosclerosis"],
    "metabolic": ["diabetes_mellitus", "diabetic_retinopathy", "diabetic_nephropathy", "diabetic_neuropathy", "obesity", "gout_hyperuricemia", "hypothyroidism", "hyperthyroidism", "osteoporosis"],
    "renal_urological": ["nephritis", "chronic_nephritis", "nephrotic_syndrome", "pyelonephritis", "nephrolithiasis", "urethritis", "cystitis", "prostatic_hypertrophy", "prostate_cancer", "bladder_cancer"],
    "respiratory": ["bronchitis", "bronchiectasis", "bronchial_asthma", "pneumonia", "tuberculosis", "lung_cancer", "pharyngitis", "laryngitis"],
    "dermatological": ["atopic_dermatitis", "seborrheic_dermatitis", "urticaria", "pruritus_cutaneus", "alopecia_areata", "psoriasis", "cheilitis", "stomatitis", "angular_cheilitis", "periodontal_disease", "gingivitis"],
    "gynecological": ["dysmenorrhea", "menstrual_irregularity", "menorrhagia", "uterine_fibroids", "endometriosis", "uterine_cancer", "breast_cancer", "mastitis_mastopathy", "infertility"],
    "ophthalmological": ["cataract", "glaucoma", "keratitis", "conjunctivitis", "diabetic_retinopathy", "floaters", "retinal_detachment", "presbyopia"],
    "neurological_psychiatric": ["migraine", "trigeminal_neuralgia", "sciatica", "neuralgia", "parkinsons_disease", "alzheimers_disease", "depression", "insomnia", "autonomic_dysfunction", "menopause_disorders"],
    "others": ["anemia", "chronic_fatigue", "cold_sensitivity", "edema", "hypotension", "acute_otitis_media", "chronic_otitis_media", "menieres_disease", "sudden_hearing_loss", "presbycusis", "urinary_incontinence", "osteoporosis", "osteoarthritis", "lumbar_disc_herniation", "cervical_spondylosis", "rheumatoid_arthritis", "gout", "herpes_zoster", "collagen_disease", "autoimmune_disease", "food_allergy", "allergic_rhinitis", "hay_fever", "common_cold", "influenza", "tinnitus", "dizziness", "shoulder_stiffness", "low_back_pain", "eye_strain", "tension_headache", "cerebral_anemia", "brain_tumor", "leukemia", "pulmonary_fibrosis", "pulmonary_edema", "emphysema", "chronic_bronchitis", "pericarditis", "endocarditis", "myocarditis", "arrhythmia", "parkinsons_disease", "multiple_sclerosis", "myasthenia_gravis"]
  },
  "risk_factors": {
    "eating_patterns": {
      "irregular": "Meal times are irregular",
      "breakfast_skipping": "Often skip breakfast",
      "late_night_meal": "Often eat late-night snacks before bed",
      "fast_eating": "Eat quickly",
      "picky_eating": "Have many food preferences",
      "overeating": "Eat until full",
      "frequent_dining_out": "Eat out frequently",
      "drinking_without_food": "Skip meals when drinking alcohol"
    },
    "food_preferences": {
      "high_salt": "Prefer salty foods",
      "spicy": "Use strong spices",
      "high_fat": "Prefer fatty foods",
      "alcohol": "Drink alcohol daily",
      "heavy_drinking": "Drink heavily once starting",
      "burnt_food": "Like burnt meat and fish",
      "soft_food": "Prefer soft foods",
      "sweets": "Like sugary drinks and sweets",
      "hot_food": "Prefer hot foods and drinks",
      "caffeine": "Drink 5 or more cups of coffee daily",
      "soda_on_empty_stomach": "Drink soda on empty stomach"
    },
    "dietary_tendencies": {
      "high_meat": "Eat many meat dishes",
      "no_meat": "Dislike meat",
      "no_seafood": "Dislike fish",
      "no_blue_fish": "Dislike blue-backed fish",
      "western_diet": "Diet is Western-style",
      "low_vegetables": "Dislike dark-colored vegetables",
      "high_dairy": "Like milk and dairy products",
      "low_dairy": "Dislike milk and dairy products",
      "eggs_daily": "Eat 2 or more eggs daily",
      "high_fruit": "Like fruit",
      "low_fruit": "Dislike fruit",
      "low_seaweed": "Dislike seaweed",
      "low_small_fish": "Dislike small fish with bones",
      "low_soy": "Dislike soy products",
      "high_processed_food": "Frequently eat instant foods"
    },
    "fluid_intake": {
      "high_fluid": "Drink plenty of fluids",
      "low_fluid": "Often feel thirsty and sweat heavily",
      "high_snacking": "Snack frequently"
    },
    "dietary_change": {
      "became_bland": "Started preferring bland meals"
    }
  },
  "disease_matrix": [
    {
      "disease_id": "atopic_dermatitis",
      "disease_name": "Atopic Dermatitis",
      "risk_factors": ["breakfast_skipping", "picky_eating", "high_fat", "sweets", "soda_on_empty_stomach", "no_seafood", "no_blue_fish", "western_diet", "low_vegetables", "high_dairy", "eggs_daily", "high_processed_food", "high_snacking"],
      "metabolic_impact": "Impaired skin barrier function → chronic inflammation",
      "category": "dermatological"
    },
    {
      "disease_id": "allergic_rhinitis",
      "disease_name": "Allergic Rhinitis / Hay Fever",
      "risk_factors": ["breakfast_skipping", "picky_eating", "spicy", "high_fat", "no_seafood", "no_blue_fish", "western_diet", "low_vegetables", "high_dairy", "eggs_daily", "high_processed_food"],
      "metabolic_impact": "Immune dysregulation → histamine hypersensitivity",
      "category": "others"
    },
    {
      "disease_id": "acute_gastritis",
      "disease_name": "Acute Gastritis",
      "risk_factors": ["irregular", "late_night_meal", "fast_eating", "overeating", "drinking_without_food", "high_salt", "spicy", "hot_food", "caffeine", "soda_on_empty_stomach", "high_meat"],
      "metabolic_impact": "Gastric mucosal irritation → acute inflammation",
      "category": "digestive"
    },
    {
      "disease_id": "gastric_duodenal_ulcer",
      "disease_name": "Gastric / Duodenal Ulcer",
      "risk_factors": ["irregular", "breakfast_skipping", "late_night_meal", "overeating", "drinking_without_food", "high_salt", "spicy", "alcohol", "heavy_drinking", "hot_food", "soda_on_empty_stomach", "high_meat", "western_diet"],
      "metabolic_impact": "Mucosal defense factor deficiency → acid erosion",
      "category": "digestive"
    },
    {
      "disease_id": "transient_ischemic_attack",
      "disease_name": "Transient Ischemic Attack",
      "risk_factors": ["irregular", "breakfast_skipping", "late_night_meal", "fast_eating", "frequent_dining_out", "high_salt", "high_fat", "heavy_drinking", "high_meat", "no_seafood", "no_blue_fish", "western_diet", "low_vegetables", "high_dairy", "eggs_daily", "low_fluid", "high_snacking"],
      "metabolic_impact": "Transient cerebral blood flow reduction → temporary neurological deficits",
      "category": "cardiovascular"
    },
    {
      "disease_id": "pharyngitis",
      "disease_name": "Pharyngitis",
      "risk_factors": ["irregular", "overeating", "drinking_without_food", "alcohol", "heavy_drinking", "low_vegetables", "high_fruit"],
      "metabolic_impact": "Pharyngeal mucosal inflammation → sore throat",
      "category": "respiratory"
    },
    {
      "disease_id": "alopecia_areata",
      "disease_name": "Alopecia Areata",
      "risk_factors": ["picky_eating", "overeating", "drinking_without_food", "alcohol", "heavy_drinking", "low_vegetables", "high_fruit", "low_soy", "high_processed_food", "high_snacking"],
      "metabolic_impact": "Autoimmune reaction to hair follicles → patchy hair loss",
      "category": "dermatological"
    },
    {
      "disease_id": "keratitis",
      "disease_name": "Keratitis",
      "risk_factors": ["low_vegetables", "high_fruit"],
      "metabolic_impact": "Corneal inflammation → eye pain and sensitivity",
      "category": "ophthalmological"
    },
    {
      "disease_id": "common_cold",
      "disease_name": "Common Cold Syndrome",
      "risk_factors": ["irregular", "breakfast_skipping", "picky_eating", "no_meat", "no_seafood", "low_vegetables", "high_fruit", "low_soy"],
      "metabolic_impact": "Immune function decline → viral susceptibility",
      "category": "others"
    },
    {
      "disease_id": "irritable_bowel_syndrome",
      "disease_name": "Irritable Bowel Syndrome",
      "risk_factors": ["fast_eating", "overeating", "spicy", "alcohol", "hot_food", "caffeine", "soda_on_empty_stomach"],
      "metabolic_impact": "Gut-brain axis dysfunction → altered motility and sensitivity",
      "category": "digestive"
    },
    {
      "disease_id": "hepatitis",
      "disease_name": "Hepatitis",
      "risk_factors": ["drinking_without_food", "high_fat", "alcohol", "heavy_drinking"],
      "metabolic_impact": "Hepatocellular inflammation → liver enzyme elevation",
      "category": "digestive"
    },
    {
      "disease_id": "cirrhosis",
      "disease_name": "Cirrhosis",
      "risk_factors": ["irregular", "drinking_without_food", "high_fat", "alcohol", "heavy_drinking", "no_seafood", "low_vegetables", "high_fruit", "low_fruit"],
      "metabolic_impact": "Progressive liver fibrosis → synthetic dysfunction",
      "category": "digestive"
    },
    {
      "disease_id": "eye_strain",
      "disease_name": "Eye Strain",
      "risk_factors": ["irregular", "breakfast_skipping", "picky_eating", "drinking_without_food", "heavy_drinking", "low_vegetables", "high_fruit", "high_snacking"],
      "metabolic_impact": "Ciliary muscle fatigue → accommodative dysfunction",
      "category": "others"
    },
    {
      "disease_id": "psoriasis",
      "disease_name": "Psoriasis",
      "risk_factors": ["no_blue_fish", "low_vegetables", "high_fruit", "low_fruit", "low_soy", "high_processed_food", "high_snacking"],
      "metabolic_impact": "Accelerated keratinocyte proliferation → chronic inflammation",
      "category": "dermatological"
    },
    {
      "disease_id": "bronchitis",
      "disease_name": "Bronchitis",
      "risk_factors": ["breakfast_skipping", "picky_eating", "low_vegetables", "high_fruit"],
      "metabolic_impact": "Bronchial mucosal inflammation → cough and sputum",
      "category": "respiratory"
    },
    {
      "disease_id": "bronchiectasis",
      "disease_name": "Bronchiectasis",
      "risk_factors": ["breakfast_skipping", "picky_eating", "low_vegetables", "high_fruit"],
      "metabolic_impact": "Irreversible airway dilation → chronic sputum production",
      "category": "respiratory"
    },
    {
      "disease_id": "bronchial_asthma",
      "disease_name": "Bronchial Asthma",
      "risk_factors": ["irregular", "picky_eating", "spicy", "no_blue_fish"],
      "metabolic_impact": "Airway hyperresponsiveness → bronchoconstriction",
      "category": "respiratory"
    },
    {
      "disease_id": "angina_pectoris",
      "disease_name": "Angina Pectoris",
      "risk_factors": ["irregular", "breakfast_skipping", "late_night_meal", "fast_eating", "overeating", "frequent_dining_out", "high_salt", "high_fat", "alcohol", "heavy_drinking", "sweets", "caffeine", "soda_on_empty_stomach", "high_meat", "no_seafood", "no_blue_fish", "western_diet", "low_vegetables", "high_dairy", "eggs_daily", "low_fruit", "high_fruit", "low_seaweed", "low_soy", "high_processed_food", "low_fluid", "high_snacking"],
      "metabolic_impact": "Myocardial ischemia → chest pain on exertion",
      "category": "cardiovascular"
    },
    {
      "disease_id": "subarachnoid_hemorrhage",
      "disease_name": "Subarachnoid Hemorrhage",
      "risk_factors": ["irregular", "late_night_meal", "high_salt", "spicy", "heavy_drinking", "high_meat", "no_seafood"],
      "metabolic_impact": "Rupture of cerebral aneurysm → bleeding into subarachnoid space",
      "category": "cardiovascular"
    },
    {
      "disease_id": "dysmenorrhea",
      "disease_name": "Dysmenorrhea",
      "risk_factors": ["breakfast_skipping", "picky_eating", "high_meat", "no_seafood", "low_soy", "high_processed_food"],
      "metabolic_impact": "Excessive prostaglandin production → uterine cramping",
      "category": "gynecological"
    },
    {
      "disease_id": "conjunctivitis",
      "disease_name": "Conjunctivitis",
      "risk_factors": ["low_vegetables", "high_fruit"],
      "metabolic_impact": "Conjunctival inflammation → redness and discharge",
      "category": "ophthalmological"
    },
    {
      "disease_id": "diarrhea",
      "disease_name": "Diarrhea",
      "risk_factors": ["late_night_meal", "fast_eating", "overeating", "spicy", "soda_on_empty_stomach", "high_dairy"],
      "metabolic_impact": "Accelerated intestinal transit → loose stools",
      "category": "digestive"
    },
    {
      "disease_id": "hypertension",
      "disease_name": "Hypertension",
      "risk_factors": ["irregular", "breakfast_skipping", "late_night_meal", "fast_eating", "overeating", "high_salt", "alcohol", "low_vegetables", "low_fruit", "low_seaweed", "low_snacking"],
      "metabolic_impact": "Sustained elevated peripheral resistance → increased afterload",
      "category": "cardiovascular"
    },
    {
      "disease_id": "hyperlipidemia",
      "disease_name": "Hyperlipidemia",
      "risk_factors": ["irregular", "breakfast_skipping", "late_night_meal", "fast_eating", "overeating", "frequent_dining_out", "high_fat", "alcohol", "heavy_drinking", "sweets", "soda_on_empty_stomach", "high_meat", "no_blue_fish", "western_diet", "low_vegetables", "high_dairy", "eggs_daily", "low_seaweed", "low_soy", "high_processed_food", "high_snacking"],
      "metabolic_impact": "Lipid metabolism disorder → elevated cholesterol/triglycerides",
      "category": "metabolic"
    },
    {
      "disease_id": "hyperthyroidism",
      "disease_name": "Hyperthyroidism",
      "risk_factors": ["spicy"],
      "metabolic_impact": "Excessive thyroid hormone production → increased metabolic rate",
      "category": "metabolic"
    },
    {
      "disease_id": "hypothyroidism",
      "disease_name": "Hypothyroidism",
      "risk_factors": ["irregular", "picky_eating", "high_meat", "no_seafood", "low_soy"],
      "metabolic_impact": "Insufficient thyroid hormone production → reduced metabolic rate",
      "category": "metabolic"
    },
    {
      "disease_id": "cheilitis",
      "disease_name": "Cheilitis",
      "risk_factors": ["irregular", "breakfast_skipping", "picky_eating", "overeating", "frequent_dining_out", "drinking_without_food", "spicy", "heavy_drinking", "caffeine", "soda_on_empty_stomach", "high_fruit", "high_processed_food"],
      "metabolic_impact": "Lip inflammation → cracking and redness",
      "category": "dermatological"
    },
    {
      "disease_id": "laryngitis",
      "disease_name": "Laryngitis",
      "risk_factors": ["irregular", "heavy_drinking", "hot_food", "high_fruit"],
      "metabolic_impact": "Laryngeal mucosal inflammation → hoarseness",
      "category": "respiratory"
    },
    {
      "disease_id": "stomatitis",
      "disease_name": "Stomatitis",
      "risk_factors": ["irregular", "breakfast_skipping", "picky_eating", "overeating", "frequent_dining_out", "spicy", "heavy_drinking", "caffeine", "soda_on_empty_stomach", "high_fruit", "high_processed_food"],
      "metabolic_impact": "Oral mucosal ulceration → pain during eating",
      "category": "dermatological"
    },
    {
      "disease_id": "osteoporosis",
      "disease_name": "Osteoporosis",
      "risk_factors": ["picky_eating", "drinking_without_food", "high_salt", "sweets", "caffeine", "soda_on_empty_stomach", "no_seafood", "low_dairy", "low_small_fish", "low_soy", "high_processed_food"],
      "metabolic_impact": "Reduced bone mineral density → fracture risk",
      "category": "metabolic"
    },
    {
      "disease_id": "atonic_constipation",
      "disease_name": "Atonic Constipation",
      "risk_factors": ["irregular", "breakfast_skipping", "soft_food", "low_vegetables", "low_fruit", "low_seaweed", "low_small_fish", "low_soy", "high_processed_food", "low_fluid", "high_snacking"],
      "metabolic_impact": "Reduced colonic motility → infrequent bowel movements",
      "category": "digestive"
    },
    {
      "disease_id": "uterine_cancer",
      "disease_name": "Uterine Cancer",
      "risk_factors": ["irregular", "high_fat", "high_meat", "western_diet", "low_vegetables", "high_dairy", "eggs_daily", "high_fruit"],
      "metabolic_impact": "Estrogen dominance → endometrial proliferation",
      "category": "gynecological"
    },
    {
      "disease_id": "periodontal_disease",
      "disease_name": "Periodontal Disease / Pyorrhea / Gingivitis",
      "risk_factors": ["fast_eating", "high_meat", "western_diet", "low_vegetables", "high_fruit", "low_fruit", "low_soy", "high_processed_food", "high_snacking"],
      "metabolic_impact": "Gum inflammation → tooth mobility and loss",
      "category": "dermatological"
    },
    {
      "disease_id": "fatty_liver",
      "disease_name": "Fatty Liver",
      "risk_factors": ["irregular", "breakfast_skipping", "late_night_meal", "fast_eating", "overeating", "frequent_dining_out", "drinking_without_food", "high_fat", "alcohol", "heavy_drinking", "sweets", "soda_on_empty_stomach", "high_meat", "no_blue_fish", "western_diet", "low_vegetables", "high_dairy", "eggs_daily", "low_seaweed", "low_soy", "high_processed_food", "high_snacking"],
      "metabolic_impact": "Hepatic fat accumulation → steatosis",
      "category": "digestive"
    },
    {
      "disease_id": "esophagitis",
      "disease_name": "Esophagitis",
      "risk_factors": ["high_salt", "spicy", "heavy_drinking", "hot_food", "caffeine"],
      "metabolic_impact": "Esophageal mucosal inflammation → burning pain",
      "category": "digestive"
    },
    {
      "disease_id": "food_allergy",
      "disease_name": "Food Allergy",
      "risk_factors": ["high_fat", "high_dairy"],
      "metabolic_impact": "Immune reaction to food proteins → systemic inflammation",
      "category": "others"
    },
    {
      "disease_id": "seborrheic_dermatitis",
      "disease_name": "Seborrheic Dermatitis",
      "risk_factors": ["overeating", "spicy", "high_fat", "sweets", "high_meat", "no_blue_fish", "western_diet", "low_vegetables", "high_dairy", "eggs_daily", "low_seaweed", "high_processed_food", "high_snacking"],
      "metabolic_impact": "Malassezia yeast overgrowth → scaly, oily patches",
      "category": "dermatological"
    },
    {
      "disease_id": "pyelonephritis",
      "disease_name": "Pyelonephritis",
      "risk_factors": ["irregular", "low_fluid"],
      "metabolic_impact": "Kidney infection → flank pain and fever",
      "category": "renal_urological"
    },
    {
      "disease_id": "nephritis",
      "disease_name": "Nephritis",
      "risk_factors": ["irregular", "high_salt", "heavy_drinking", "low_vegetables", "high_fruit", "low_fluid"],
      "metabolic_impact": "Glomerular inflammation → proteinuria and hematuria",
      "category": "renal_urological"
    },
    {
      "disease_id": "myocardial_infarction",
      "disease_name": "Myocardial Infarction",
      "risk_factors": ["irregular", "breakfast_skipping", "late_night_meal", "fast_eating", "overeating", "frequent_dining_out", "high_salt", "high_fat", "alcohol", "heavy_drinking", "caffeine", "high_meat", "no_seafood", "no_blue_fish", "western_diet", "low_vegetables", "high_dairy", "eggs_daily", "low_fruit", "high_fruit", "low_seaweed", "low_soy", "high_processed_food", "low_fluid", "high_snacking"],
      "metabolic_impact": "Coronary artery occlusion → myocardial necrosis",
      "category": "cardiovascular"
    },
    {
      "disease_id": "heart_failure",
      "disease_name": "Heart Failure",
      "risk_factors": ["irregular", "late_night_meal", "fast_eating", "overeating", "drinking_without_food", "high_salt", "spicy", "high_fat", "alcohol", "heavy_drinking", "caffeine", "high_meat", "no_blue_fish", "western_diet", "low_vegetables", "high_dairy", "eggs_daily", "high_fruit", "low_fruit", "low_seaweed", "high_processed_food", "low_fluid"],
      "metabolic_impact": "Reduced cardiac output → fluid accumulation and fatigue",
      "category": "cardiovascular"
    },
    {
      "disease_id": "urticaria",
      "disease_name": "Urticaria",
      "risk_factors": ["picky_eating", "high_fat", "no_blue_fish", "low_vegetables", "eggs_daily", "high_fruit", "low_fruit"],
      "metabolic_impact": "Mast cell degranulation → itchy wheals",
      "category": "dermatological"
    },
    {
      "disease_id": "pancreatitis",
      "disease_name": "Pancreatitis",
      "risk_factors": ["irregular", "late_night_meal", "overeating", "drinking_without_food", "spicy", "high_fat", "heavy_drinking", "soda_on_empty_stomach", "high_meat", "western_diet"],
      "metabolic_impact": "Pancreatic enzyme autodigestion → severe abdominal pain",
      "category": "digestive"
    },
    {
      "disease_id": "menstrual_irregularity",
      "disease_name": "Menstrual Irregularity",
      "risk_factors": ["breakfast_skipping", "picky_eating", "high_meat", "no_seafood", "low_soy", "high_processed_food"],
      "metabolic_impact": "Hypothalamic-pituitary-ovarian axis dysfunction → cycle disruption",
      "category": "gynecological"
    },
    {
      "disease_id": "prostatic_hypertrophy",
      "disease_name": "Prostatic Hypertrophy",
      "risk_factors": ["no_seafood", "low_vegetables", "high_fruit", "low_fruit"],
      "metabolic_impact": "Benign prostate enlargement → urinary symptoms",
      "category": "renal_urological"
    },
    {
      "disease_id": "prostate_cancer",
      "disease_name": "Prostate Cancer",
      "risk_factors": ["breakfast_skipping", "high_fat", "high_meat", "western_diet", "low_vegetables", "high_dairy"],
      "metabolic_impact": "Androgen-driven proliferation → malignant transformation",
      "category": "renal_urological"
    },
    {
      "disease_id": "herpes_zoster",
      "disease_name": "Herpes Zoster",
      "risk_factors": ["irregular", "high_meat", "no_seafood", "high_processed_food"],
      "metabolic_impact": "Varicella-zoster virus reactivation → painful vesicular rash",
      "category": "others"
    },
    {
      "disease_id": "cholelithiasis",
      "disease_name": "Cholelithiasis",
      "risk_factors": ["irregular", "breakfast_skipping", "late_night_meal", "fast_eating", "frequent_dining_out", "high_fat", "sweets", "caffeine", "soda_on_empty_stomach", "high_meat", "low_vegetables", "high_fruit", "low_fruit", "high_snacking"],
      "metabolic_impact": "Bile supersaturation → gallstone formation",
      "category": "digestive"
    },
    {
      "disease_id": "cholecystitis",
      "disease_name": "Cholecystitis",
      "risk_factors": ["irregular", "overeating", "spicy", "heavy_drinking"],
      "metabolic_impact": "Gallbladder inflammation → right upper quadrant pain",
      "category": "digestive"
    },
    {
      "disease_id": "gout_hyperuricemia",
      "disease_name": "Gout / Hyperuricemia",
      "risk_factors": ["irregular", "breakfast_skipping", "late_night_meal", "fast_eating", "overeating", "frequent_dining_out", "drinking_without_food", "high_fat", "alcohol", "heavy_drinking", "sweets", "soda_on_empty_stomach", "high_meat", "western_diet", "low_vegetables", "high_fruit", "low_fruit", "high_snacking"],
      "metabolic_impact": "Uric acid crystallization → joint inflammation",
      "category": "metabolic"
    },
    {
      "disease_id": "diabetes_mellitus",
      "disease_name": "Diabetes Mellitus",
      "risk_factors": ["irregular", "breakfast_skipping", "late_night_meal", "overeating", "frequent_dining_out", "high_fat", "alcohol", "heavy_drinking", "sweets", "soda_on_empty_stomach", "western_diet", "low_vegetables", "high_dairy", "high_fruit", "high_snacking"],
      "metabolic_impact": "Insulin resistance and/or beta-cell dysfunction → hyperglycemia",
      "category": "metabolic"
    },
    {
      "disease_id": "diabetic_retinopathy",
      "disease_name": "Diabetic Retinopathy",
      "risk_factors": ["irregular", "breakfast_skipping", "late_night_meal", "fast_eating", "overeating", "frequent_dining_out", "high_salt", "high_fat", "alcohol", "heavy_drinking", "sweets", "soda_on_empty_stomach", "western_diet", "low_vegetables", "high_dairy", "high_fruit", "high_snacking"],
      "metabolic_impact": "Microvascular damage in retina → vision loss",
      "category": "ophthalmological"
    },
    {
      "disease_id": "atherosclerosis",
      "disease_name": "Atherosclerosis",
      "risk_factors": ["late_night_meal", "fast_eating", "overeating", "frequent_dining_out", "high_salt", "high_fat", "alcohol", "heavy_drinking", "high_meat", "no_seafood", "no_blue_fish", "western_diet", "low_vegetables", "high_dairy", "eggs_daily", "high_fruit", "low_fruit", "low_seaweed", "high_snacking"],
      "metabolic_impact": "Plaque formation in arterial walls → stenosis",
      "category": "cardiovascular"
    },
    {
      "disease_id": "mastitis_mastopathy",
      "disease_name": "Mastitis / Mastopathy",
      "risk_factors": ["breakfast_skipping", "high_fat", "caffeine", "low_vegetables"],
      "metabolic_impact": "Breast tissue inflammation → pain and nodules",
      "category": "gynecological"
    },
    {
      "disease_id": "urethritis",
      "disease_name": "Urethritis",
      "risk_factors": ["breakfast_skipping", "low_vegetables"],
      "metabolic_impact": "Urethral inflammation → dysuria and discharge",
      "category": "renal_urological"
    },
    {
      "disease_id": "nephrolithiasis",
      "disease_name": "Nephrolithiasis",
      "risk_factors": ["picky_eating", "drinking_without_food", "high_salt", "sweets", "caffeine", "soda_on_empty_stomach", "low_vegetables", "low_dairy", "high_fruit", "low_fruit", "high_fluid"],
      "metabolic_impact": "Crystal formation in urinary tract → stone disease",
      "category": "renal_urological"
    },
    {
      "disease_id": "cerebral_infarction",
      "disease_name": "Cerebral Infarction",
      "risk_factors": ["late_night_meal", "fast_eating", "overeating", "frequent_dining_out", "high_salt", "high_fat", "alcohol", "sweets", "caffeine", "soda_on_empty_stomach", "high_meat", "no_blue_fish", "western_diet", "low_vegetables", "high_dairy", "eggs_daily", "low_fluid", "high_snacking"],
      "metabolic_impact": "Thrombotic or embolic occlusion → ischemic stroke",
      "category": "cardiovascular"
    },
    {
      "disease_id": "cerebral_hemorrhage",
      "disease_name": "Cerebral Hemorrhage",
      "risk_factors": ["picky_eating", "drinking_without_food", "high_salt", "alcohol", "heavy_drinking", "high_meat", "no_seafood", "high_fruit"],
      "metabolic_impact": "Rupture of cerebral vessel → hemorrhagic stroke",
      "category": "cardiovascular"
    },
    {
      "disease_id": "pneumonia",
      "disease_name": "Pneumonia",
      "risk_factors": ["breakfast_skipping", "low_vegetables"],
      "metabolic_impact": "Lung parenchyma infection → fever and cough",
      "category": "respiratory"
    },
    {
      "disease_id": "tuberculosis",
      "disease_name": "Tuberculosis",
      "risk_factors": ["breakfast_skipping", "low_vegetables"],
      "metabolic_impact": "Mycobacterial infection → chronic cough and weight loss",
      "category": "respiratory"
    },
    {
      "disease_id": "cataract",
      "disease_name": "Cataract",
      "risk_factors": ["low_vegetables", "high_fruit"],
      "metabolic_impact": "Lens opacification → progressive vision loss",
      "category": "ophthalmological"
    },
    {
      "disease_id": "pruritus_cutaneus",
      "disease_name": "Pruritus Cutaneus",
      "risk_factors": ["no_meat", "no_seafood", "low_dairy", "high_fluid", "became_bland"],
      "metabolic_impact": "Skin itch without primary lesion → systemic cause",
      "category": "dermatological"
    },
    {
      "disease_id": "anemia",
      "disease_name": "Anemia",
      "risk_factors": ["irregular", "breakfast_skipping", "picky_eating", "frequent_dining_out", "high_meat", "no_seafood", "low_vegetables", "low_small_fish", "low_soy", "high_processed_food"],
      "metabolic_impact": "Reduced red blood cell mass → tissue hypoxia",
      "category": "others"
    },
    {
      "disease_id": "chronic_gastritis",
      "disease_name": "Chronic Gastritis",
      "risk_factors": ["late_night_meal", "fast_eating", "overeating", "drinking_without_food", "high_salt", "spicy", "alcohol", "heavy_drinking", "sweets", "hot_food", "caffeine", "soda_on_empty_stomach", "high_meat"],
      "metabolic_impact": "Chronic gastric mucosal inflammation → dyspepsia",
      "category": "digestive"
    },
    {
      "disease_id": "chronic_nephritis",
      "disease_name": "Chronic Nephritis",
      "risk_factors": ["irregular", "fast_eating", "overeating", "high_salt", "spicy", "alcohol", "heavy_drinking", "caffeine", "soda_on_empty_stomach", "high_fruit", "low_fruit", "high_fluid", "low_fluid"],
      "metabolic_impact": "Progressive glomerular damage → renal failure",
      "category": "renal_urological"
    },
    {
      "disease_id": "chronic_pancreatitis",
      "disease_name": "Chronic Pancreatitis",
      "risk_factors": ["overeating", "drinking_without_food", "spicy", "high_fat", "alcohol", "heavy_drinking", "high_meat", "western_diet", "low_vegetables", "high_dairy"],
      "metabolic_impact": "Irreversible pancreatic damage → maldigestion",
      "category": "digestive"
    },
    {
      "disease_id": "low_back_pain",
      "disease_name": "Low Back Pain",
      "risk_factors": ["irregular"],
      "metabolic_impact": "Musculoskeletal strain → lumbar discomfort",
      "category": "others"
    },
    {
      "disease_id": "benign_nephrosclerosis",
      "disease_name": "Benign Nephrosclerosis",
      "risk_factors": ["irregular", "frequent_dining_out", "high_salt", "western_diet", "low_fluid"],
      "metabolic_impact": "Hypertensive renal damage → arteriolar thickening",
      "category": "renal_urological"
    },
    {
      "disease_id": "dementia",
      "disease_name": "Dementia",
      "risk_factors": ["high_meat", "no_seafood", "low_vegetables"],
      "metabolic_impact": "Neurodegenerative changes → cognitive decline",
      "category": "neurological_psychiatric"
    },
    {
      "disease_id": "nephrolithiasis_2",
      "disease_name": "Nephrolithiasis",
      "risk_factors": ["late_night_meal", "picky_eating", "high_fluid"],
      "metabolic_impact": "Crystal formation in urinary tract → stone disease",
      "category": "renal_urological"
    },
    {
      "disease_id": "acute_enteritis",
      "disease_name": "Acute Enteritis",
      "risk_factors": ["late_night_meal", "high_salt", "high_meat"],
      "metabolic_impact": "Acute intestinal infection → diarrhea and vomiting",
      "category": "digestive"
    },
    {
      "disease_id": "chronic_enteritis",
      "disease_name": "Chronic Enteritis",
      "risk_factors": ["late_night_meal", "high_salt", "high_meat"],
      "metabolic_impact": "Chronic intestinal inflammation → malabsorption",
      "category": "digestive"
    },
    {
      "disease_id": "gastric_cancer",
      "disease_name": "Gastric Cancer",
      "risk_factors": ["irregular", "breakfast_skipping", "late_night_meal", "fast_eating", "overeating", "drinking_without_food", "high_salt", "spicy", "heavy_drinking", "burnt_food", "hot_food", "caffeine", "soda_on_empty_stomach", "high_meat", "low_vegetables", "low_dairy", "high_fruit", "low_fruit"],
      "metabolic_impact": "Chronic mucosal injury → malignant transformation",
      "category": "digestive"
    },
    {
      "disease_id": "lung_cancer",
      "disease_name": "Lung Cancer",
      "risk_factors": ["breakfast_skipping", "high_fat", "heavy_drinking", "high_meat", "low_vegetables"],
      "metabolic_impact": "Carcinogen exposure → malignant pulmonary growth",
      "category": "respiratory"
    },
    {
      "disease_id": "liver_cancer",
      "disease_name": "Liver Cancer",
      "risk_factors": ["breakfast_skipping", "drinking_without_food", "alcohol", "heavy_drinking", "high_meat", "no_seafood", "low_vegetables", "high_fruit", "low_fruit"],
      "metabolic_impact": "Hepatocellular carcinoma → liver mass",
      "category": "digestive"
    },
    {
      "disease_id": "colorectal_cancer",
      "disease_name": "Colorectal Cancer",
      "risk_factors": ["irregular", "breakfast_skipping", "frequent_dining_out", "drinking_without_food", "high_fat", "alcohol", "heavy_drinking", "high_meat", "no_seafood", "western_diet", "low_vegetables", "high_dairy", "high_fruit", "low_fruit", "low_seaweed", "low_small_fish"],
      "metabolic_impact": "Adenoma-carcinoma sequence → colon malignancy",
      "category": "digestive"
    },
    {
      "disease_id": "pancreatic_cancer",
      "disease_name": "Pancreatic Cancer",
      "risk_factors": ["breakfast_skipping", "drinking_without_food", "spicy", "high_fat", "heavy_drinking", "caffeine", "high_meat", "western_diet", "low_vegetables"],
      "metabolic_impact": "Pancreatic ductal adenocarcinoma → poor prognosis",
      "category": "digestive"
    },
    {
      "disease_id": "laryngeal_cancer",
      "disease_name": "Laryngeal Cancer",
      "risk_factors": ["breakfast_skipping", "high_salt", "spicy", "heavy_drinking", "hot_food", "low_vegetables"],
      "metabolic_impact": "Laryngeal mucosal malignancy → hoarseness",
      "category": "respiratory"
    },
    {
      "disease_id": "pharyngeal_cancer",
      "disease_name": "Pharyngeal Cancer",
      "risk_factors": ["breakfast_skipping", "heavy_drinking", "low_vegetables"],
      "metabolic_impact": "Pharyngeal malignancy → dysphagia",
      "category": "respiratory"
    },
    {
      "disease_id": "bladder_cancer",
      "disease_name": "Bladder Cancer",
      "risk_factors": ["breakfast_skipping", "low_vegetables"],
      "metabolic_impact": "Urothelial carcinoma → hematuria",
      "category": "renal_urological"
    },
    {
      "disease_id": "breast_cancer",
      "disease_name": "Breast Cancer",
      "risk_factors": ["irregular", "breakfast_skipping", "frequent_dining_out", "high_fat", "sweets", "high_meat", "western_diet", "low_vegetables", "high_dairy", "eggs_daily", "high_fruit", "low_fruit", "low_soy", "high_snacking"],
      "metabolic_impact": "Estrogen-driven proliferation → breast malignancy",
      "category": "gynecological"
    },
    {
      "disease_id": "obesity",
      "disease_name": "Obesity",
      "risk_factors": ["irregular", "breakfast_skipping", "late_night_meal", "fast_eating", "picky_eating", "overeating", "frequent_dining_out", "high_fat", "alcohol", "heavy_drinking", "sweets", "soda_on_empty_stomach", "high_meat", "western_diet", "low_vegetables", "high_dairy", "high_snacking"],
      "metabolic_impact": "Positive energy balance → excessive fat accumulation",
      "category": "metabolic"
    },
    {
      "disease_id": "diabetic_neuropathy",
      "disease_name": "Diabetic Neuropathy",
      "risk_factors": ["irregular", "breakfast_skipping", "late_night_meal", "fast_eating", "overeating", "high_salt", "high_fat", "alcohol", "heavy_drinking", "sweets", "soda_on_empty_stomach", "high_meat", "low_vegetables", "high_snacking"],
      "metabolic_impact": "Peripheral nerve damage → numbness and pain",
      "category": "metabolic"
    },
    {
      "disease_id": "esophageal_cancer",
      "disease_name": "Esophageal Cancer",
      "risk_factors": ["breakfast_skipping", "high_salt", "spicy", "heavy_drinking", "hot_food", "caffeine", "low_vegetables"],
      "metabolic_impact": "Squamous cell carcinoma → dysphagia",
      "category": "digestive"
    },
    {
      "disease_id": "colorectal_polyp",
      "disease_name": "Colorectal Polyp",
      "risk_factors": ["high_fat", "high_meat", "western_diet", "low_vegetables", "high_dairy", "low_fruit", "low_seaweed"],
      "metabolic_impact": "Adenomatous polyps → precursor to cancer",
      "category": "digestive"
    },
    {
      "disease_id": "alcoholic_liver_disease",
      "disease_name": "Alcoholic Liver Disease",
      "risk_factors": ["irregular", "drinking_without_food", "alcohol", "heavy_drinking"],
      "metabolic_impact": "Alcohol-induced hepatotoxicity → liver damage",
      "category": "digestive"
    },
    {
      "disease_id": "diabetic_nephropathy",
      "disease_name": "Diabetic Nephropathy",
      "risk_factors": ["irregular", "breakfast_skipping", "late_night_meal", "fast_eating", "overeating", "frequent_dining_out", "high_salt", "high_fat", "heavy_drinking", "sweets", "soda_on_empty_stomach", "western_diet", "low_vegetables", "high_dairy", "high_snacking"],
      "metabolic_impact": "Glomerular damage → progressive renal failure",
      "category": "renal_urological"
    },
    {
      "disease_id": "gastroptosis",
      "disease_name": "Gastroptosis",
      "risk_factors": ["late_night_meal", "overeating", "high_salt", "spicy", "hot_food", "high_meat"],
      "metabolic_impact": "Stomach prolapse → postprandial discomfort",
      "category": "digestive"
    },
    {
      "disease_id": "cerebral_arteriosclerosis",
      "disease_name": "Cerebral Arteriosclerosis",
      "risk_factors": ["high_salt", "high_meat"],
      "metabolic_impact": "Cerebral vessel stiffening → cognitive decline",
      "category": "cardiovascular"
    }
  ]
}
```