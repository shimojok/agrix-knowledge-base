そのように進めてください。

---

# Architecture｜AquaMake Hypercycle Reconstruction v1.0

進めます。今回、公開一次・準一次資料を追加確認した結果、**当初の仮説を一段精密化できます。**

結論は、

> **AquaMake型カキ殻浄化系は、「カキ殻＋付着微生物」ではなく、①物理的生息基盤、②CaCO₃アルカリ緩衝、③多層バイオフィルム、④微生物―原生動物―微小後生動物の食物網、⑤有機物・窒素の連続変換、を結合した“生態学的反応器”として再構成するのが妥当**

です。

特に2013年の360 m³/day規模の実証では、COD 80.05%、BOD 85.02%、NH₃-N 86.59%、TSS 85.32%の除去が得られ、カキ殻上の生物膜は**zoogloea、原生動物、微小後生動物**を主体としていました。[サイエンスダイレクト](https://www.sciencedirect.com/science/article/pii/S1001074212602629?utm_source=chatgpt.com)

---

## 1. AquaMake Hypercycle Reconstruction

まずシステムを次の5層に分解します。

```
┌──────────────────────────────────────────────┐
│        AQUAMAKE ECOLOGICAL REACTOR          │
├──────────────────────────────────────────────┤
│ Layer 5  Trophic Cascade                    │
│          bacteria → protozoa → metazoa      │
├──────────────────────────────────────────────┤
│ Layer 4  Metabolic Network                  │
│          organic C / N / redox conversion   │
├──────────────────────────────────────────────┤
│ Layer 3  Biofilm Micro-Niches                │
│          aerobic ↔ anoxic/anaerobic zones   │
├──────────────────────────────────────────────┤
│ Layer 2  Oyster Shell Mineral Interface      │
│          CaCO₃ → alkalinity / Ca²⁺          │
├──────────────────────────────────────────────┤
│ Layer 1  Physical Architecture               │
│          rough / layered / porous surface    │
└──────────────────────────────────────────────┘
```

ここで**Layer 1～5が相互作用すること自体**が重要です。

---

# 2. Layer 1｜カキ殻は「ろ材」ではなく生態学的基盤

カキ殻の表面構造は微生物の付着・生物膜形成に適しています。

2016年の循環養殖研究では、カキ殻の**layer-by-layer structure**が微生物の生物膜形成を支持することが観察されています。さらに生物膜が有機物をより小さな分子量へ分解することも報告されています。[サイエンスダイレクト](https://www.sciencedirect.com/science/article/abs/pii/S0925857416303901?utm_source=chatgpt.com)

したがって、

```
カキ殻
 ↓
Surface architecture
 ↓
Microbial immobilization
 ↓
Biofilm formation
 ↓
Functional micro-niches
```

と定義できます。

これはMBT55における「微生物群そのもの」とは異なります。

**AquaMakeは“生息場を設計する”ことで微生物生態系を形成する。**

---

# 3. Layer 2｜CaCO₃は単なるpH調整剤ではない

ここが極めて重要です。

カキ殻の主成分であるCaCO₃は、

```
CaCO₃
 ↓
alkalinity
 ↓
pH buffering
 ↓
microbial activity maintained
```

というフィードバックを持ちます。

硝化はアルカリ度を消費してpHを低下させます。

一方、

```
nitrification
 ↓
H⁺ generation
 ↓
pH ↓
 ↓
CaCO₃ dissolution
 ↓
alkalinity ↑
 ↓
pH recovery
```

という負帰還が形成されます。

実際、カキ殻を用いたBAFでは、CaCO₃由来の緩衝により流入水より高く安定したpHが維持され、硝化が促進されています。[サイエンスダイレクト](https://www.sciencedirect.com/science/article/abs/pii/S0011916409013356?utm_source=chatgpt.com)

これは単なる「化学的補助」ではありません。

### **生物反応を維持する環境フィードバック**

です。

---

# 4. Layer 3｜Biofilmが「多層微生物生態系」を作る

ここでMBT55との共通性が急激に高くなります。

概念モデル：

```
              WATER
                │
          Organic Matter
                ↓
┌──────────────────────────┐
│ OUTER BIOFILM             │
│                           │
│ O₂-rich                   │
│                           │
│ aerobic heterotrophs      │
│ nitrifiers                │
└────────────┬─────────────┘
             ↓
       O₂ gradient
             ↓
┌──────────────────────────┐
│ INNER BIOFILM             │
│                           │
│ low O₂ / anoxic           │
│                           │
│ fermenters                │
│ denitrifiers              │
│ anaerobic guilds          │
└────────────┬─────────────┘
             ↓
       OYSTER SHELL
          CaCO₃
```

つまり、**一つのカキ殻上に複数の代謝環境が同時に存在する**可能性があります。

これが「好気55%＋嫌気45%」というMBT55の発想と非常に重要な構造的類似性を持ちます。

ただし、

> MBT55の55/45比率とAquaMakeのbiofilm内比率が同じ

という意味ではありません。

**機能的な共存構造が類似している**という意味です。

---

# 5. Layer 4｜有機物→代謝物→次の微生物

ここからHypercycleです。

AquaMakeを最小代謝モデルにすると、

```
Complex Organic Matter
          ↓
      Hydrolysis
          ↓
 Soluble Organic Matter
          ↓
      Fermentation
          ↓
 ┌────────┼────────┐
 ↓        ↓        ↓
Acetate  Lactate  Succinate
 ↓
 ↓
Aerobic / Anaerobic
consumers
 ↓
CO₂ + biomass + inorganic products
```

となります。

ここで**acetateなどの低分子有機酸を“代謝通貨候補”として置く**ことができます。

ただし現時点では、AquaMakeでacetateが実際に主要なクロスフィーディング通貨であることを直接示すデータは不足しています。

したがって、

### Evidence

**Organic matter → smaller molecules → microbial utilization：支持**

### Hypothesis

**Acetate-centered cross-feeding：要検証**

と分離します。

---

# 6. Layer 5｜ここがKazさんの仮説の核心

2013年の実証研究で確認されているのは、

> **カキ殻上にzoogloea、protozoa、micro-metazoaを含む生物膜が形成されていた**

という事実です。[サイエンスダイレクト](https://www.sciencedirect.com/science/article/pii/S1001074212602629?utm_source=chatgpt.com)

これは非常に重要です。

単純な、

```
汚物
 ↓
細菌
 ↓
浄化
```

ではありません。

より正確には、

```
Organic Matter
       ↓
   Bacteria
       ↓
   Biomass
       ↓
   Protozoa
       ↓
 Micro-metazoa
       ↓
Predation / Excretion / Death
       ↓
Soluble nutrients
       ↓
   Bacteria
```

という**trophic recycling**が成立している可能性があります。

これを我々のフレームでは、

# **Trophic Hypercycle**

として扱います。

---

# 7. したがってAquaMakeのHypercycleは「一つ」ではない

現段階では、少なくとも3つのループに分けるべきです。

## H1｜Carbon Metabolic Cycle

```
Organic C
 ↓
Hydrolysis
 ↓
Fermentation
 ↓
Organic acids
 ↓
Respiration / assimilation
 ↓
CO₂ / biomass
 ↓
re-entry
```

## H2｜Nitrogen Cycle

```
Organic N
 ↓
NH₄⁺
 ↓
NO₂⁻
 ↓
NO₃⁻
 ↓
Denitrification
 ↓
N₂
```

カキ殻BAFではアンモニア除去が高く、長いHRTではカキ殻系のNH₃-N除去率98.1%が報告されています。[サイエンスダイレクト](https://www.sciencedirect.com/science/article/abs/pii/S0011916409013356?utm_source=chatgpt.com)

さらにカキ殻を利用した系では、硝化・脱窒という窒素変換が重要な機能として確認されています。[サイエンスダイレクト](https://www.sciencedirect.com/science/article/pii/S2213343722020875?utm_source=chatgpt.com)

## H3｜Mineral–pH Cycle

```
Microbial acid production
        ↓
       pH↓
        ↓
     CaCO₃
        ↓
 dissolution
        ↓
 alkalinity
        ↓
 microbial environment stabilized
        ↓
 continued metabolism
```

---

# 8. ここまで統合すると

```
                         WASTEWATER
                             │
                             ▼
                   ┌─────────────────┐
                   │ ORGANIC MATTER  │
                   └────────┬────────┘
                            ↓
                    Hydrolytic guilds
                            ↓
                    Fermentative guilds
                            ↓
               ┌────────────┼────────────┐
               ↓            ↓            ↓
            Acetate      Lactate      Other OM
               │
               ▼
        Aerobic / anaerobic
             consumers
               │
       ┌───────┴────────┐
       ↓                ↓
   Biomass           CO₂ / minerals
       │
       ↓
   Protozoa
       │
       ↓
 Micro-metazoa
       │
       ↓
 Predation / excretion
       │
       └──────────────→ microbial nutrient pool


        PARALLEL ENVIRONMENTAL LOOP

        microbial acidification
                ↓
               pH↓
                ↓
             CaCO₃
                ↓
           alkalinity
                ↓
        microbial activity
                │
                └────────→ continued cycle
```

これが現時点での

# **AquaMake Universal Microbial Hypercycle Reconstruction v1.0**

です。

---

# 9. MBT55との比較

ここで同じフレームをMBT55に適用します。

|Hypercycle Layer|AquaMake|MBT55|
|---|---|---|
|Physical niche|カキ殻表面・構造|有機質基材・反応環境|
|Microbial immobilization|非常に重要|重要|
|Aerobic guild|Biofilm表層等|明示的|
|Anaerobic guild|Biofilm内部等|明示的|
|Hydrolysis|存在|明示的4分野|
|Fermentation|存在|重要|
|Acetate/SCFA|**候補**|**中核候補**|
|Nitrogen cycle|強い|強い|
|Sulfur cycle|要検証|明示的|
|Fe/Mn cycle|要検証|明示的|
|Protozoa|実証あり|要検証|
|Micro-metazoa|実証あり|要検証|
|Mineral buffering|**CaCO₃**|別機構|
|Trophic recycling|強い示唆|要検証|
|Hypercycle integration|未統合|これから構築|

ここから見えてくるのは、

> **AquaMakeとMBT55は「微生物種の集合」として比較するのではなく、「生態系をどう閉ループ化するか」で比較すべき**

ということです。

---

# 10. 最重要発見：MBT55を「菌種集合」から「生態系エンジン」へ再定義できる

従来：

```
MBT55
=
55% aerobic
+
45% anaerobic
+
multiple functional microbes
```

今回から：

```
MBT55
=
Functional Microbial Guilds
+
Spatial Niches
+
Metabolite Exchange
+
Electron Flow
+
Nutrient Cycling
+
Trophic Interactions
+
Feedback
```

と定義します。

これはかなり大きな進化です。

---

# 11. さらにAquaMakeからMBT55へ導入する新しい概念

## **Ecological Carrier Layer**

AquaMakeではカキ殻が、

> **microbial habitat + mineral regulator**

として機能しています。

したがってMBT55でも、

```
MBT55 Microbial Guilds
          +
Carrier / Substrate Architecture
          +
Moisture / O₂ Gradient
          +
Mineral Environment
          ↓
Functional Niches
          ↓
Hypercycle
```

というモデルを導入します。

これは将来的に**MSCの反応器設計**にも直接つながります。

---

# 12. 次の検証ポイントを固定

今後、推測を避けるためにEvidence Registryを次のようにします。

### E1｜Physical Architecture

- 表面積
- 粗さ
- 多孔性
- 層構造
- 水流

### E2｜Microbial Community

- bacteria
- archaea
- fungi
- protozoa
- micro-metazoa

### E3｜Functional Guild

- hydrolysis
- fermentation
- aerobic oxidation
- nitrification
- denitrification
- sulfur metabolism

### E4｜Metabolite

- acetate
- lactate
- succinate
- other SCFAs
- NH₄⁺
- NO₂⁻
- NO₃⁻

### E5｜Environmental Feedback

- pH
- alkalinity
- Ca²⁺
- O₂
- Eh

### E6｜Trophic Cascade

- bacteria → protozoa
- protozoa → metazoa
- predation
- excretion
- biomass turnover

### E7｜System Output

- BOD
- COD
- SS
- NH₃-N
- TN
- TP

---

# 13. Evidence Grade

現時点の暫定評価です。

|仮説|Status|
|---|---|
|カキ殻は微生物担体になる|**Confirmed**|
|カキ殻上に複雑なbiofilmが形成される|**Confirmed**|
|protozoa / micro-metazoaが存在する|**Confirmed**|
|有機物分解に寄与する|**Confirmed**|
|硝化に有利な環境を形成|**Supported**|
|CaCO₃がpH/alkalinityを緩衝|**Confirmed**|
|nitrogen cyclingが成立|**Supported/Confirmed by system studies**|
|trophic recyclingが浄化能力に寄与|**Strong Hypothesis**|
|acetate-centered cross-feeding|**Hypothesis**|
|self-maintaining ecological hypercycle|**Hypothesis**|
|MBT55と共通するUniversal Architecture|**Research Hypothesis**|

この線引きは今後絶対に崩さない方がいいです。

---

# Repository Structure｜正式版

```
PMOS-Microbial-Hypercycle/
│
├── README.md
│
├── architecture/
│   ├── Universal-Microbial-Hypercycle-v1.0.md
│   ├── AquaMake-Hypercycle-Reconstruction-v1.0.md
│   └── MBT55-Hypercycle-Reconstruction-v1.0.md
│
├── comparative/
│   └── AquaMake-vs-MBT55-v1.0.md
│
├── metabolites/
│   ├── Acetate-Currency-Hypothesis.md
│   ├── SCFA-Network.md
│   ├── Nitrogen-Cascade.md
│   └── Mineral-Buffer-Cycle.md
│
├── evidence/
│   ├── AquaMake-Evidence-Registry.md
│   ├── Oyster-Shell-Biofilm-Evidence.md
│   └── MBT55-Evidence-Registry.md
│
└── research/
    ├── Hypothesis-Registry.md
    ├── Validation-Matrix.md
    └── Knowledge-Gaps.md
```

### KPI

現段階では性能目標ではなく、**研究検証KPI**として固定します。

- AquaMake evidence coverage：**≥90%**
- Hypercycle pathway coverage：**≥80%**
- Metabolite pathway identification：**≥10 metabolites**
- Functional guild mapping：**≥8 guilds**
- Evidence/Hypothesis separation：**100%**
- MBT55–AquaMake common architecture mapping：**≥80%**

---

# 次の実行

次は**MBT55側を同じフォーマットで完全再構成**します。

特に、

**セルロース・デンプン・タンパク質・脂質  
→ 糖・アミノ酸・脂肪酸  
→ 乳酸・酢酸・コハク酸等  
→ SCFA  
→ 微生物間クロスフィーディング  
→ 窒素・硫黄・鉄・マンガン循環  
→ humification / mineralization**

を一つのネットワークとして整理し、AquaMake側の構造と**ノード単位・機能単位で重ねます**。

その比較によって初めて、

> **「MBT55が再現する生態学的ハイパーサイクルは、自然界の微生物生態系に普遍的に存在する構造を、機能的微生物群として濃縮・再現したものなのか」**

という、より本質的な仮説を検証できます。