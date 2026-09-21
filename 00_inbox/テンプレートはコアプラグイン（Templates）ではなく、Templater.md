---
title: テンプレートはコアプラグイン（Templates）ではなく、Templater
created: 2026-09-08 08:08
updated: 2026-09-08 11:55
platform: AGRIX
tags:
  - BioNexus
---


# テンプレートはコアプラグイン（Templates）ではなく、Templater



テンプレートは、コアプラグインでいいですか？ホルダーを作る必要がありますね？

---

Kaz、ここは誤解しやすいポイントなので、**Obsidian のテンプレート機能（コアプラグイン）と Templater の役割の違い**をまず整理し、そのうえで **あなたの AGRIX Knowledge Base に最適な設計**をまとめます。

---

# 🎯 結論  
**テンプレートはコアプラグイン（Templates）ではなく、Templater に入れるべきです。**  
そして、**専用フォルダーを作る必要があります。**

理由は以下の通り：

- コアテンプレートは「静的なコピペ」しかできない  
- Templater は「動的生成（YAML自動挿入・日付・フォルダ名・入力プロンプト）」ができる  
- あなたのテンプレートはすべて **動的生成が必須**  
- AGRIX Knowledge Base は「構造化された知識OS」なので、静的テンプレートでは不十分

つまり、  
**あなたのテンプレートは Templater 専用フォルダに置くのが正解**です。

---

# 📁 フォルダ設計（あなたの Vault に最適化）

## ① Templater 用テンプレートフォルダ（必須）
```
Templates/
└── AGRIX/
    ├── concept-template.md
    ├── architecture-template.md
    └── model-template.md
```

Templater の設定で、このフォルダを「Template Folder」に指定します。

---

## ② AGRIX Knowledge Base 本体のフォルダ（ノートを作る場所）
```
agrix-knowledge-base/
├── 01_Concepts/
├── 02_Architecture/
├── 03_Models/
├── 04_References/
└── 05_Dashboards/
```

### ● 使い方  
- **概念ノート → 01_Concepts**  
- **技術アーキテクチャ → 02_Architecture**  
- **モデル仕様書 → 03_Models**  
- **根拠ノート → 04_References**  
- **可視化・計算結果 → 05_Dashboards**

---

# 🧠 「#6. 根拠ノート・参照 コード」とは？

あなたの質問に明確に答えます。

## ✔ 意味  
**そのノートの内容が、どのノート・どのコードに基づいているかを明示する欄。**

AGRIX Knowledge Base は「ハルシネーションゼロ」「SSOT（Single Source of Truth）」が特徴なので、  
**根拠を明示することが技術的信頼性の中心**になります。

---

## ✔ 具体例（あなたの環境）

### ● 根拠ノート（Evidence Notes）
- `/agrix-knowledge-base/01_Concepts/MBT55.md`  
- `/agrix-knowledge-base/01_Concepts/AquaGrid.md`  
- `/agrix-knowledge-base/02_Architecture/GraphRAG.md`  
- 過去の研究ノート  
- GitHub の仕様書

### ● 参照コード（Reference Code）
- `ghg_calc.py`（GHG削減量モデル）  
- `roi_model.py`（ROIモデル）  
- `metabolic_chain.py`（代謝連鎖モデル）  
- Neo4j のクエリ  
- GitHub のコミットID

---

## ✔ なぜ重要なのか？
あなたのシステムは：

- **LLM（推論）と Python Code Engine（計算）を完全分離**  
- **GitHub ⇔ Obsidian ⇔ VectorDB の完全同期**  
- **ハルシネーションゼロ構造**

だからこそ、  
**「どの知識に基づいているか」**  
**「どのコードで計算しているか」**  
を明示する欄が必要なのです。

---

# 🧩 どのテンプレートをどこに入れるか（最終版）

|テンプレート|配置フォルダ|用途|
|---|---|---|
|concept-template.md|`Templates/AGRIX/`|ビジョン・概念仕様書|
|architecture-template.md|`Templates/AGRIX/`|技術アーキテクチャ仕様書|
|model-template.md|`Templates/AGRIX/`|数式・Pythonモデル仕様書|

---

# 📌 使い方（あなたの運用に最適化）

### 1. ノートを作りたいフォルダへ移動  
例：`agrix-knowledge-base/03_Models/`

### 2. 新規ノート作成  
タイトルを入力（例：`GHG_Reduction_Model`）

### 3. Templater を実行  
右上のコマンドパレット →  
**Templater: Insert Template**  
→ `model-template.md` を選択

### 4. 自動で YAML が生成される  
- created  
- updated  
- platform  
- project  
- tags  
- model_id  
- ssot_path  
などが自動挿入される

---

# 🎯 最終結論  
- **テンプレートはコアプラグインではなく、Templater に入れるべき**  
- **専用フォルダ（Templates/AGRIX）を作る必要がある**  
- **根拠ノート・参照コードは、SSOTとハルシネーションゼロ構造のための必須フィールド**

あなたの AGRIX Knowledge Base System（BioNexus Engine）に最適化した設計です。

---

# 🔗 次のステップ  
フォルダ構造を実際に作るなら、どれから進めますか？

- AGRIX テンプレートフォルダを作成  
- Knowledge Base のフォルダ構造を作成  
- Templater の設定を最適化

---

コミュニティプラグインのTemplaterを導入するのですね？

---

結論から言うと **はい、Templater はコミュニティプラグインとして導入する必要があります。**  
そして、Kaz の AGRIX Knowledge Base System のような「構造化・自動化・メタデータ標準化」が必須の Vault では、**Templater は必須プラグイン**になります。

---

## 🎯 なぜコアテンプレートではなく、コミュニティ版 Templater が必要なのか

### コアテンプレート（Core Plugin）
- ただの「静的コピペ」
- YAML の自動生成ができない
- 日付の自動挿入ができない
- フォルダ名の取得ができない
- プロジェクト名の入力プロンプトができない
- SSOT（Single Source of Truth）情報を自動挿入できない

→ **AGRIX Knowledge Base のような“知識OS”には機能不足**

---

### Templater（コミュニティプラグイン）
- YAML を自動生成  
- created / updated を自動挿入  
- platform をフォルダ名から自動取得  
- model_id を入力プロンプトで生成  
- ssot_path を自動挿入  
- GitHub の commit ID を自動で入れることも可能  
- AGRIX / BioNexus / HealthBook のテンプレートを分岐可能  

→ **あなたの巨大 Vault（6,600ノート）に必須の“構造化エンジン”**

---

# 📁 フォルダは必ず作る必要があります（最適設計）

Kaz の Vault に最適化したテンプレート配置はこれです。

```
Templates/
└── AGRIX/
    ├── concept-template.md
    ├── architecture-template.md
    └── model-template.md
```

### ✔ なぜフォルダを作るのか？
- Templater は「テンプレートフォルダ」を指定する必要がある  
- AGRIX 専用テンプレートをまとめることで管理が容易  
- 他のプロジェクト（BioNexus / HealthBook）と混ざらない  
- 将来テンプレートが増えても整理しやすい  

---

# 🧠 「根拠ノート・参照コード」の意味（再整理）

あなたの質問に対して、最も正確な説明をまとめます。

### ✔ 根拠ノート（Evidence Notes）
そのノートの内容が **どの知識に基づいているか** を示す欄。

例：
- MBT55 の定義ノート  
- AquaGrid の設計ノート  
- PBPE Marketplace の数式ノート  
- 過去の研究メモ  
- GitHub の仕様書  

### ✔ 参照コード（Reference Code）
そのノートの内容が **どのコードで計算されているか** を示す欄。

例：
- `ghg_calc.py`  
- `roi_model.py`  
- `metabolic_chain.py`  
- Neo4j クエリ  
- GitHub のコミットID  

### ✔ なぜ必要なのか？
AGRIX Knowledge Base System は：

- ハルシネーションゼロ  
- 決定論的計算  
- SSOT（Single Source of Truth）  
- GitHub ⇔ Obsidian ⇔ VectorDB の完全同期  

を特徴とするため、  
**「どの知識・どのコードに基づいているか」** を明示することが技術的信頼性の根幹になる。

---

# 🎯 最終結論  
- **Templater はコミュニティプラグインとして導入する必要がある**  
- **専用フォルダ（Templates/AGRIX）を作る必要がある**  
- **根拠ノート・参照コードは、AGRIX Knowledge Base の信頼性を支える必須フィールド**

あなたの AGRIX Knowledge Base System（BioNexus Engine）に最適化した設計です。

---

# 🔗 次のステップ  
フォルダ構造を実際に作るなら、どれから進めますか。

- テンプレートフォルダを作成  
- Templater の設定を最適化  
- AGRIX Knowledge Base のフォルダ構造を作成