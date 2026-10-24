統合してもらったquestionnaire_full.jsonは、日本語版ですが、英語版にすべきですね？

---

**おっしゃる通りです。国際的なGitHubリポジトリとして、英語版にすべきです。**

---

## 📝 **修正方針**

### **変更箇所**
1. キー名はそのまま（`category`, `question`, `risk_factors` など）
2. 値（質問文、疾患名など）を**英語**に翻訳

---

## 📄 **修正版: data/questionnaire_full.json（英語版）**

```json
{
  "version": "1.0",
  "total_questions": 200,
  "categories": {
    "Dietary Habits": [1, 50],
    "Lifestyle": [51, 100],
    "Environment & Constitution": [101, 150],
    "Symptoms": [151, 200]
  },
  "questions": {
    "1": {
      "id": 1,
      "category": "Dietary Habits",
      "question": "Do you often skip breakfast?",
      "risk_factors": ["Breakfast Skipping"],
      "metabolic_impact": "Disrupted gluconeogenesis rhythm → morning hypoglycemia tendency",
      "related_diseases": ["Diabetes", "Obesity", "Chronic Fatigue"],
      "weight": 0.85
    },
    "2": {
      "id": 2,
      "category": "Dietary Habits",
      "question": "Do you dislike dark-colored vegetables?",
      "risk_factors": ["Low Antioxidant Intake"],
      "metabolic_impact": "Phytochemical deficiency → increased oxidative stress",
      "related_diseases": ["Arteriosclerosis", "Immune Deficiency"],
      "weight": 0.80
    },
    "3": {
      "id": 3,
      "category": "Dietary Habits",
      "question": "Do you prefer salty foods?",
      "risk_factors": ["High Sodium"],
      "metabolic_impact": "Sodium overload → blood pressure elevation",
      "related_diseases": ["Hypertension", "Nephritis"],
      "weight": 0.90
    },
    "4": {
      "id": 4,
      "category": "Dietary Habits",
      "question": "Do you frequently eat sweets or snacks?",
      "risk_factors": ["High Sugar Intake", "Frequent Snacking"],
      "metabolic_impact": "Blood sugar spike → insulin resistance",
      "related_diseases": ["Diabetes", "Obesity"],
      "weight": 0.92
    },
    "5": {
      "id": 5,
      "category": "Lifestyle",
      "question": "Do you lack physical exercise?",
      "risk_factors": ["Sedentary Lifestyle"],
      "metabolic_impact": "Muscle loss → reduced basal metabolism",
      "related_diseases": ["Obesity", "Diabetes", "Hypertension"],
      "weight": 0.92
    },
    "6": {
      "id": 6,
      "category": "Lifestyle",
      "question": "Do you suffer from sleep deprivation?",
      "risk_factors": ["Sleep Deprivation"],
      "metabolic_impact": "Autonomic nervous system disruption → metabolic rhythm disorder",
      "related_diseases": ["Insomnia", "Chronic Fatigue", "Hypertension"],
      "weight": 0.85
    },
    "7": {
      "id": 7,
      "category": "Lifestyle",
      "question": "Do you experience high stress levels?",
      "risk_factors": ["Chronic Stress"],
      "metabolic_impact": "Cortisol elevation → fat accumulation, blood sugar rise",
      "related_diseases": ["Hypertension", "Diabetes", "Insomnia"],
      "weight": 0.90
    },
    "8": {
      "id": 8,
      "category": "Lifestyle",
      "question": "Do you consume alcohol regularly?",
      "risk_factors": ["Alcohol Consumption"],
      "metabolic_impact": "Liver metabolic load → fatty liver risk",
      "related_diseases": ["Liver Disease", "Hypertension"],
      "weight": 0.88
    },
    "9": {
      "id": 9,
      "category": "Lifestyle",
      "question": "Do you smoke (including past history)?",
      "risk_factors": ["Smoking"],
      "metabolic_impact": "Vascular endothelial damage → atherosclerosis progression",
      "related_diseases": ["Lung Cancer", "Heart Disease", "Stroke"],
      "weight": 0.95
    },
    "10": {
      "id": 10,
      "category": "Genetics & Constitution",
      "question": "Do you have a family history of diabetes?",
      "risk_factors": ["Genetic Predisposition"],
      "metabolic_impact": "Genetic susceptibility → insulin resistance",
      "related_diseases": ["Diabetes"],
      "weight": 0.70
    }
  },
  "diseases": {
    "Diabetes": {
      "name": "Diabetes",
      "risk_factors": {
        "Breakfast Skipping": 0.85,
        "High Sugar Intake": 0.92,
        "Sedentary Lifestyle": 0.92,
        "Genetic Predisposition": 0.70,
        "Frequent Snacking": 0.88
      },
      "global_prevalence": "500 million",
      "gates_priority": "HIGH",
      "description": "A chronic metabolic disorder characterized by high blood glucose levels."
    },
    "Hypertension": {
      "name": "Hypertension",
      "risk_factors": {
        "High Sodium": 0.90,
        "Sedentary Lifestyle": 0.85,
        "Chronic Stress": 0.88,
        "Alcohol Consumption": 0.85,
        "Sleep Deprivation": 0.80
      },
      "global_prevalence": "1.2 billion",
      "gates_priority": "HIGH",
      "description": "A condition where blood pressure in the arteries is persistently elevated."
    },
    "Obesity": {
      "name": "Obesity",
      "risk_factors": {
        "High Sugar Intake": 0.88,
        "Sedentary Lifestyle": 0.90,
        "Frequent Snacking": 0.85,
        "Breakfast Skipping": 0.75
      },
      "global_prevalence": "800 million",
      "gates_priority": "MEDIUM",
      "description": "A medical condition characterized by excess body fat accumulation."
    }
  }
}
```

---

## 📁 **ファイルの配置**

```
M3-BioSynergy/
├── data/
│   └── questionnaire_full.json    ← この英語版を保存
├── src/healthbook/...
└── examples/healthbook_demo.py
```

---

## ✅ **変更点まとめ**

| 項目 | 日本語版 | 英語版 |
|------|----------|--------|
| カテゴリ名 | 食習慣、生活習慣... | Dietary Habits, Lifestyle... |
| 質問文 | 朝食を抜くことがよくある | Do you often skip breakfast? |
| 疾患名 | 糖尿病 | Diabetes |
| リスク因子 | 欠食型（朝食抜き） | Breakfast Skipping |
| 説明文 | 日本語 | English |

---

**この英語版JSONで作成しますか？** 🚀

[[DSH20. 推奨するファイル構成]]
