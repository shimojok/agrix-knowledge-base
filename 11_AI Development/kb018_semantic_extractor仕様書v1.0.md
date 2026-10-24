# semantic_extractor.py 仕様書 v1.0
## — 意味論抽出エンジン設計仕様 —

関連：kb016（ハイパーサイクルの理解と正確な設計概念の再確認と訂正）、kb017（BioNexus Python Hypercycle Scheme 実現プロセス設計書）、CO005（Copilot案）

---

## 1. 目的とスコープ

`semantic_extractor.py` は、`01scanvault.py`（インジェスト層）が出力したチャンクを入力とし、意味論メタデータ（domain / entity_type / concept / model / thread_id）を付与した `LlamaIndex Document` を出力する。

**やること**：チャンク本文からメタデータを抽出し、検索・分類を可能にする。
**やらないこと**：γ_ij等の数値計算、生化学・経済ロジックの実行（これは `mbt_hypercycle/` 以下のエンジンの責務であり、本エンジンとは明確に分離する）。

---

## 2. 入力仕様

`01scanvault.py` から受け取るチャンクは以下の形を前提とする。

```python
class RawChunk(BaseModel):
    chunk_id: str              # 一意識別子
    source_note_id: str        # 由来ノートのファイル名/パス
    source_folder: str         # 例: "03_MBT55"
    heading_path: list[str]    # 例: ["設計思想", "2. アーキテクチャ"]
    text: str                  # チャンク本文
    chunk_type: str            # 暫定分類（後述4章で定義）
```

`source_folder` は kb016の訂正済みフォルダ構造（02_Biological_Systems, 03_MBT55, 04_AGRIX, 05_AgriWare, 06_PBPE, 07_HealthBook 等）にそのまま対応させる。

---

## 3. 出力仕様（メタデータスキーマ）

```python
class SemanticMetadata(BaseModel):
    chunk_id: str
    domain: Literal["mbt55", "agrix", "pbpe", "biological_systems",
                     "agriware", "healthbook", "pmos", "bionexus_integration",
                     "cross_domain", "unclassified"]
    priority: Literal["core", "deferred"]       # kb016優先度。domainから機械的に決定
    entity_type: list[str]                      # 複数可。4章で定義する分類のいずれか
    concept: list[str]                          # semantic_dictionary.json中の概念名。複数可
    model_ref: list[str] = []                   # 言及されているモデル名（例: "γ_ij interaction matrix"）
    thread_id: str | None = None                # 議論の連番があれば付与（例: kb005〜kb017の系列）
    confidence: dict[str, float]                # フィールドごとの抽出信頼度 0.0-1.0
    extraction_method: Literal["table_lookup", "dictionary_match", "llm_assisted", "hybrid"]
    engine_version: str                         # 例: "semantic_extractor.v1.0"
    extracted_at: datetime
```

`domain` は必須（`unclassified` を許容し、無理にどれかへ分類しない）。`entity_type` と `concept` は0件を許容する（本文に該当がなければ空リストが正しい）。

---

## 4. 抽出対象の定義

### 4.1 domain（1チャンク1値、ただし `cross_domain` あり）

判定は2段階とする。

1. **テーブル参照（最優先）**：デイリーノート由来のチャンクは「agrix-knowledge-base 分野別仕訳け」ノートに記載された PROJECT 01〜06 分類を第一情報源とする（PROJECT 01=healthbook, 02=agrix, 03=mbt55, 04=pbpe, 05=pmos, 06=bionexus_integration, その他=unclassified）。このテーブルはKazさんによる手動分類であり、機械的なフォルダ推定より優先する。
2. **フォルダ名参照（次点）**：テーブルに一致するエントリがないチャンクは、`02_Biological_Systems`/`03_MBT55`/`04_AGRIX`/`05_AgriWare`/`06_PBPE`/`07_HealthBook` 等のトピック別フォルダ名を情報源とする

本文中の明示的な言及（他domainの用語が主題として登場する場合）による上書きを許容する。上書きが起きた場合は `confidence` を下げて記録する。

**`pmos` の扱い**：KB/RAGシステム自体の設計対話（Python Hypercycle Scheme、意味論抽出エンジン、インジェスト層、RAG運用方針の決定等）は `pmos` に分類する。`agrix`/`mbt55`/`pbpe` の用語が本文に頻出していても、主題がシステム設計そのものであれば `pmos` を優先する（例：kb005, kb016, CO005はいずれも`pmos`）。

**`bionexus_integration` の扱い**：クロスプラットフォーム戦略、外部パートナーシップ、Enterprise関連は `bionexus_integration` とする。

**domain → priority マッピング（暫定）**：

| domain | priority |
|---|---|
| mbt55, agrix, biological_systems, agriware, pbpe | core |
| healthbook | deferred |
| pmos | core（RAG/抽出エンジン自体の設計に直結するため） |
| bionexus_integration | **要Kazさん判断**（本仕様書では暫定 deferred とするが、事業戦略上の優先度は技術ロードマップと別軸のため要確認） |
| cross_domain, unclassified | 個別判断 |

### 4.2 entity_type（複数可、固定分類）
初版では以下に限定する（増やす場合は辞書側で管理し、本仕様書はv1.1に改版）：

- `metric`（数値指標：CCE, HFR, NCS, DSCR等）
- `model_component`（モデルの構成要素：γ_ij, guild_network等）
- `process`（プロセス・フェーズ名：Phase 0, Wilkinsonの7プロセス等）
- `entity`（組織・システム名：AGRIX, PBPE-Marketplace等）
- `parameter`（入力パラメータ：温度、pH等）
- `decision`（設計上の決定事項）

### 4.3 concept（`semantic_dictionary.json` 参照必須）
辞書に存在する語彙のみを `concept` として採用する。辞書にない候補語をLLMが提案した場合は `concept` に入れず、別フィールド `candidate_concepts`（本仕様書スコープ外、v1.1で検討）に退避する。**辞書にない概念を本番出力に混入させない**ことを優先する。

### 4.4 model_ref / thread_id
model_refは辞書のモデル名一覧と完全一致・部分一致で判定。thread_idはノートのファイル名連番（kb005, kb016, kb017等）がある場合のみ付与し、推測では付与しない。

---

## 5. 抽出方式

**テーブル参照＋辞書優先＋LLM補助のハイブリッド方式**とする。

1. デイリーノート由来のチャンクは、まず「分野別仕訳け」ノートの PROJECT 01〜06 マッピングと突合し、一致すれば `domain` を確定する（`extraction_method: table_lookup`。信頼度最高）
2. テーブルに一致しない場合、`semantic_dictionary.json` との文字列マッチングで `concept` / `model_ref` / `domain候補` を確定（`extraction_method: dictionary_match`）
3. 辞書マッチだけでは埋まらないフィールド（特に `entity_type`、曖昧な`domain`）についてのみLLMに判定させる（`extraction_method: llm_assisted` または `hybrid`）
3. LLMには辞書に**存在する語彙リストを候補として渡し、その中から選ばせる**（自由生成させない）。これによりPhase 3のコード生成AIと同じ原則（仕様と辞書に流し込む変換器としてのみ使う）を抽出エンジンにも適用する

---

## 6. 検証：ゴールドスタンダードとの突合

- `gold_annotations.jsonl`：各`chunk_type`が分散するよう最低10〜15件を人手でラベル付け（**Kazさんの担当**、7章参照）
- 評価指標：
  - `domain`：完全一致率（単一ラベル分類として評価）
  - `entity_type` / `concept`：多ラベル分類として precision / recall / F1
- 閾値：本仕様書ではまだ固定しない。ゴールドセットと辞書v0.1の実データを見てから、kb017 Phase 0の抽出精度ゲートに数値を書き戻す

---

## 7. 非対応・既知の制約（v1.0時点）

- 複数言語混在チャンク（日英混在）の扱いは未定義。当面は日本語チャンクのみを対象とし、英語チャンクはv1.1で扱う
- `cross_domain` 判定のロジックは未確定（複数domainの用語が同程度出現した場合の優先順位）
- `candidate_concepts`（辞書外語彙の扱い）はスコープ外

---

## 8. バージョニング

`engine_version` はセマンティックバージョンで管理し、`semantic_dictionary.json` のバージョンとは独立に管理する（辞書更新のたびにエンジンを再バージョンしない）。出力メタデータには両方のバージョンを記録できるよう、`SemanticMetadata` に将来 `dictionary_version` フィールドを追加する余地を残す（v1.0では未実装、v1.1候補）。
