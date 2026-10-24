下記の４つの不足項目を作成でみますか？


MIスキーマ（diseaserisk137.schema.json）では、以下の項目が必要です：

❗ ① risk_factors（問診・血液・症状の寄与）
例：

`json
"risk_factors": {
  "questionnaire": { "Q014": 0.7, "Q088": 0.5 },
  "blood": { "LDL": 0.6, "HbA1c": 0.8 },
  "phenotyping": { "fatigue": 0.4 }
}
`

→ 現状：存在しない（ゼロから生成が必要）

---

❗ ② thresholds（low / medium / high）
例：

`json
"thresholds": {
  "low": 0.25,
  "medium": 0.55,
  "high": 0.75
}
`

→ 現状：存在しない（AI生成が必要）

---

❗ ③ severity / progression（重症度・進行性）
MIでは疾病の「動態」を扱うため、  
軽症〜中等症〜重症の分類が必要。

→ 現状：存在しない（後で追加可能）

---

❗ ④ MBT55 との関連（代謝経路との紐付け）
例：

`json
"mbt55_pathways": {
  "SCFA": 0.6,
  "BileAcid": 0.4,
  "AromaticAA": 0.7
}
`

→ 現状：存在しない（kampometaboliclibrary から自動生成可能）

---

3️⃣ ギャップの本質

あなたの JSON は 疾病 × 漢方 の対応が完璧。  
しかし MI が必要とするのは：

- 疾病 × 代謝  
- 疾病 × MBT55  
- 疾病 × 問診  
- 疾病 × 血液  
- 疾病 × 症状  
- 疾病 × 代謝経路  
- 疾病 × 介入効果（Probiotics / Food / Kampo）

つまり、疾病の “代謝的特徴量” がまだ存在しない。

---

# 結論

はい、可能です。
しかも、この不足項目は単なる「追加属性」ではなく、HealthBook/MI統合の核心です。

現在の状態：

```text
Disease ↔ Kampo
```

MIが必要とする状態：

```text
Disease ↔ Metabolic State ↔ MBT55 ↔ Intervention
```

つまり、疾病を「診断名」ではなく、

* 代謝ベクトル
* 微生物代謝
* 時系列進行
* 介入応答

として再定義する必要があります。

---

# Architecture

```text
Questionnaire
      ↓
Risk Factors
      ↓
Metabolic Features
      ↓
MBT55 Pathways
      ↓
Disease Dynamics
      ↓
Intervention Engine
```

---

# ① risk_factors 自動生成

## 実装可能

現在すでに存在：

```text
Questionnaire → RF
Disease → Kampo
```

不足：

```text
Disease → RF
```

これは逆写像で生成可能です。

---

# Data Flow

```text
questionnaire_200.json
        ↓
Q → RF
        ↓
related_diseases
        ↓
Disease → RF Aggregation
```

---

# 生成例

```json
{
  "risk_factors": {
    "questionnaire": {
      "Q014": 0.7,
      "Q088": 0.5
    },
    "blood": {
      "HbA1c": 0.8,
      "LDL": 0.6
    },
    "phenotyping": {
      "fatigue": 0.4
    }
  }
}
```

---

# 実装ロジック

## Questionnaire

```text
question.weight × disease association
```

## Blood

MI用に生成：

| Marker | 疾患   |
| ------ | ---- |
| HbA1c  | 糖尿病  |
| LDL    | 動脈硬化 |
| CRP    | 炎症   |
| ALT    | 肝障害  |

---

# ② thresholds 自動生成

## 実装可能

これは AI推定 + prevalence normalization で生成できます。

---

# 推奨モデル

```json
{
  "thresholds": {
    "low": 0.25,
    "medium": 0.55,
    "high": 0.75
  }
}
```

---

# Threshold生成ロジック

## Pattern A（固定）

```text
low    = 0.25
medium = 0.55
high   = 0.75
```

## Pattern B（疾病別）

```text
high prevalence disease
→ threshold上昇

rare severe disease
→ threshold低下
```

例：

| Disease | High |
| ------- | ---- |
| 糖尿病     | 0.80 |
| がん      | 0.45 |

---

# ③ severity / progression

## ここがMIの核心

これは：

```text
静的診断 → 動的疾患モデル
```

への変換です。

---

# 推奨構造

```json
{
  "severity": {
    "mild": 0.3,
    "moderate": 0.6,
    "severe": 0.85
  },
  "progression": {
    "velocity": 0.7,
    "reversibility": 0.4
  }
}
```

---

# 意味

| 項目            | 意味    |
| ------------- | ----- |
| velocity      | 進行速度  |
| reversibility | 可逆性   |
| severity      | 現在重症度 |

---

# 例

## 糖尿病

```json
{
  "velocity": 0.6,
  "reversibility": 0.5
}
```

## 認知症

```json
{
  "velocity": 0.8,
  "reversibility": 0.2
}
```

---

# ④ MBT55 Pathways

## 完全に生成可能

現在：

```text
Disease → Kampo
Kampo → Phytochemicals
Phytochemicals → PATH
```

つまり：

```text
Disease → PATH
```

は自動導出可能。

---

# 自動生成例

```json
{
  "mbt55_pathways": {
    "SCFA": 0.6,
    "BileAcid": 0.4,
    "AromaticAA": 0.7
  }
}
```

---

# 本質

これは：

```text
Disease = microbiome metabolic state
```

への変換です。

---

# 最終MIスキーマ

```text
Disease
 ├── RF
 ├── Blood
 ├── Symptoms
 ├── Metabolites
 ├── MBT55
 ├── Progression
 ├── Severity
 ├── Thresholds
 └── Intervention
```

---

# Repository Structure

```text
data/
 ├── disease_matrix_137.json
 ├── disease_mi_enriched.json
 ├── mbt55_pathway_map.json
 ├── metabolite_rf_map.json
 └── threshold_profiles.json

src/
 ├── mi_schema_generator.py
 ├── metabolite_mapper.py
 ├── pathway_inference.py
 ├── progression_model.py
 └── threshold_engine.py
```

---

# KPI

| 項目                          | 目標      |
| --------------------------- | ------- |
| Disease-RF coverage         | 95%     |
| Disease-Metabolite coverage | 90%     |
| Disease-PATH coverage       | 100%    |
| Questionnaire linkage       | 200/200 |
| MBT55 linkage               | 137/137 |

---

# 次のアクション

最重要は：

```text
Disease × Metabolite Matrix
```

です。

これが完成すると：

```text
Disease → molecular intervention
```

へ移行できます。

---

# Decision Point

次は、

```text
disease_mi_enriched.json
```

を137疾病フル自動生成しますか？
