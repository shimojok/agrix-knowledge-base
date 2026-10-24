# BioNexus Python Hypercycle Scheme 実現プロセス設計書
## — AGRIX Knowledge Base System (BioNexus Engine) 構築ロードマップ —

関連ノート: kb005（設計思想）、kb016（ハイパーサイクルの理解と正確な設計概念の再確認と訂正）、生態学的ハイパーサイクルの理論化、地球生態学の視点から見たMBT55生態学的ハイパーサイクルの理論的深化

---

## 0. 訂正の反映（本設計書の前提）

kb005における当初案は、ハイパーサイクルの説明にHealthBook（腸内細菌代謝連鎖）の例を用いていたが、kb016での訂正により、ハイパーサイクルの本義は **MBT55微生物群の代謝連鎖**（Wilkinsonの7基本プロセス）であることを確認した。HealthBookの腸内細菌代謝は、このMBTハイパーサイクルモデルを人体スケールに流用した応用先である。

この訂正を受け、`agrix-knowledge-base` 内の優先度は以下の通り再定義する。

| フォルダ | ノート数 | 位置づけ |
|---|---|---|
| 02_Biological_Systems | 69 | ハイパーサイクル基礎理論 |
| 03_MBT55 | 534 | ハイパーサイクル核心（AGRIX核心） |
| 04_AGRIX | 923 | ハイパーサイクル核心（AGRIX核心） |
| 05_AgriWare | 78 | 実装・運用層 |
| 06_PBPE | 509 | 経済価値変換層（AGRIX核心） |
| 07_HealthBook | 727 | 応用層・**凍結中**（RAGがAGRIX核心に完全接続するまで着手しない） |

AGRIX核心（03+04+06、約1,966ノート）とHealthBook（727ノート）の比率は約73:27であり、kb005の「AGRIX 70%:HealthBook 30%」という構成比は、モジュールの実装行数ではなくこのノート数比として解釈する。

---

## 1. 全体フロー概観

```
[Obsidian Vault: agrix-knowledge-base]
    │ (Phase 0: 埋め込み・優先度タグ付け)
    ▼
[Pinecone RAG Index] ⇄ [16 Repos RAG Index]        ← Phase 0-1
    │
    ▼
[Python Hypercycle Scheme: core/ → mbt_hypercycle/ → agrix/] ← Phase 2（仕様固定）
    │
    ▼
[コード生成AI: RAG仕様 → Pydantic型準拠コード]      ← Phase 3（人間レビューゲート）
    │
    ▼
[agrix-platform-kb.json（来歴バーコード付き）]      ← Phase 4
    │
    ▼
[抽出・整形Python Code] ─┬→ IPCC提出用レポート
                          ├→ 投資家ダッシュボード（PBPE NPV等）
                          └→ RAGへのフィードバック（新知見の還元・循環完了）
```

最後の矢印（成果がRAGへ還元される）が機能して初めて「BioNexus Engine」と呼べる。ここが機能しない限り、本システムは一方向パイプラインに過ぎず、ハイパーサイクルではない。

---

## 2. フェーズ詳細

### Phase 0：ローカルRAG再構築（意味論抽出層＋検索精度の2ゲート制）

**現状**：agrix-knowledge-base（~4,900+ノート）のうち3,400+ノートがPinecone（llama-text-embed-v2、統合推論モデル使用）へ処理済み。レート制限対応としてバッチ処理・指数バックオフ・チェックポイント再開を実装済み。

Phase 0は「検索(retrieval)が当たること」だけでは不十分であり、その手前の「抽出(extraction)が正しいこと」を別ゲートとして持つ。以下の内部順序で進める。

**0-1. 意味論抽出エンジンの仕様書（v1.0）確定**
何を抽出するか（concept / model / entity_type / domain / thread_id）、どのメタデータを生成するか、どの辞書を参照するかを先に固定する。ここが後続すべての設計図になる。

**0-2. 抽出対象の辞書（`semantic_dictionary.json`）作成**
AGRIX概念一覧・PBPE指標一覧・MBT55代謝因子一覧・HealthBook MIOS構成要素・entity_type分類辞書・domain判定辞書・モデル名/パラメータ名辞書。抽出エンジンの燃料。

**0-2b. デイリーノート domain ルックアップテーブル（`domain_lookup_table.json`）作成**
「agrix-knowledge-base 分野別仕訳け」ノートに記載された PROJECT 01〜06（HealthBook-MIOS / AGRIX / MBT55・MSC / PBPE / PMOS / BioNexus Integration）＋その他の手動分類を機械可読化したもの。デイリーノート由来のチャンクについては、これを`semantic_dictionary.json`より優先する一次情報源として扱う（kb018仕様書4.1節参照）。

**0-3. インジェスト層（`01scanvault.py`）実装**
Vault読み込み、チャンク化、Markdown構造（H1/H2/H3）抽出、ファイル名・タイトル抽出。意味論判断は行わず、素材整形に徹する。

**0-4. 抽出エンジン（`semantic_extractor.py`）実装**
仕様書＋辞書＋インジェスト層の出力を用い、実際に意味論メタデータ（concept/model/entity_type/domain/thread_id）を抽出し、LlamaIndex Document等を生成する。kb016の訂正を反映した優先度メタデータ（`domain: mbt55|agrix|pbpe|healthbook`, `priority: core|deferred`）もここで付与する。

**完了判定基準（両方を満たすこと）**：

- **抽出精度ゲート**：`gold_annotations.jsonl`（各chunk_type分散済み・最低10〜15件のゴールドスタンダード）に対し、`semantic_extractor.py` が出すdomain/entity_type/concept抽出結果を突合し、一致率が事前設定した閾値以上であることを確認済み
- **検索精度ゲート**：`03_MBT55`・`04_AGRIX`・`06_PBPE`・`02_Biological_Systems`・`05_AgriWare` への検索クエリで、γ_ij・CCE・HFR・NCS・Wilkinson由来の一次情報が上位ヒットすることを `scripts/ask_rag.py` 等で疎通検証済み。`07_HealthBook` は検索対象に含めるが `priority: deferred` タグにより主要ソースとして誤引用されない

抽出精度ゲートを検索精度ゲートより先に置く理由は、抽出が誤っていれば検索結果の上位ヒット自体が誤ったメタデータに基づく偽陽性になり得るため。両ゲートを満たすまで、Phase 2（Pydantic型の仕様固定）には進まない。

### Phase 1：16リポジトリのRAG化

**前提作業**：repo-consolidation方針（M3-BioSynergy→M3-Core-Engine、HealthBook-AI→HealthBook-MBT55-Unified、PBPE群→PBPE-Marketplace、Azure-PMOS→BioNexus-Enterprise）の統合を先に実行してから、統合後のリポジトリをRAG化する。順序を逆にすると、統合で消えるはずの重複コードがインデックスに残り検索汚染となる。

**作業内容**：
- 統合後の各リポジトリについて、README／docstring／関数シグネチャを抽出
- Obsidianノートと同一Pineconeプロジェクト内の別namespace（例：`agrix-code-base`）へ格納し、理論（ノート）と実装（コード）を分離管理

### Phase 2：Python Hypercycle Schemeの枠組み確定

`core/` → `mbt_hypercycle/` → `agrix/`（`healthbook/`は凍結）の骨格を、実装の前に**仕様として先に固定**する。

```
src/bionexus_kb/
├── core/
│   ├── rag_interface.py
│   ├── pipeline.py
│   └── base_model.py
│
├── mbt_hypercycle/                  # [Hypercycle本体 — 最優先・共有カーネル]
│   ├── guild_network.py             # 120菌種・機能ギルド分担
│   ├── interaction_matrix.py        # γ_ij 菌間相互作用行列
│   ├── energy_flow.py               # 熱力学的最適化 η≈0.92、MEP原理
│   └── carbon_sequestration.py      # CCE・HFR・NCS
│
├── agrix/                           # [03_MBT55, 04_AGRIX, 05_AgriWare, 02_Biological_Systems 由来]
│   ├── agriware/
│   ├── safetychain/
│   ├── agrix_phenotype/
│   └── pbpe/                        # 06_PBPE — カーボン/経済価値変換
│
└── healthbook/                      # [凍結]
    └── pathways/
```

`mbt_hypercycle/` は `agrix/` の一部門ではなく、`agriware` や `pbpe` を含む全エンジンが共有する共通カーネルとして独立させる。

**このフェーズでの成果物**：Pydanticスキーマと `BaseHypercycleEngine` インターフェースの確定のみ。中身の実装はPhase 3以降に回す。ここを先に固定することで、Phase 3で生成AIに書かせるコードの抽象がセッションごとにばらつくのを防ぐ。

### Phase 3：コードを扱う生成AI

生成AIの役割を厳密に限定する：**RAG（Phase 0/1）から抽出した仕様を、Phase 2で固定した型に流し込む変換器**とし、数値や生化学ロジックそのものは考案させない。

| 項目 | 内容 |
|---|---|
| 入力 | RAG検索結果（ノート＋既存コード）＋ Phase 2のPydanticインターフェース |
| 出力 | インターフェースを満たす `.py` ドラフト |
| 人間レビューゲート（必須） | γ_ij等、実測値ベースの数式はAI出力をそのまま採用せず、RAG一次ソース（ノート内数式）と1行ずつ突合してから確定 |
| 推奨ツール | Claude Code等、ファイル操作とRAG検索を1セッション内でエージェント的に実行できるツール |

### Phase 4：生成されるJSONコードの格納

`agrix-platform-kb.json` / `healthbook-platform-kb.json` の出力先をスキーマバージョン管理付きで設計する。

```
outputs/
├── agrix-platform-kb/
│   ├── schema_v1/
│   └── schema_v2/
└── healthbook-platform-kb/   # 凍結中は空のまま
```

各JSONに「来歴バーコード」（由来ノートID＋入力ハッシュ＋エンジンバージョン）を必須フィールドとして付与し、Phase 5の抽出コードが数値の出所を自動追跡できるようにする。

### Phase 5：JSONから必要情報を抽出するPython Code

Phase 4のJSON群を用途別（IPCC提出用、投資家向けダッシュボード、PBPE Marketplace取引用等）に整形するレイヤー。決定論的な集計・変換のみとし、生成AIは関与させない（数値の二次加工にAIを挟むと来歴バーコードの意味が薄れるため）。

### Phase 6：必要なツール・ライブラリの整理

| 用途 | 候補 |
|---|---|
| RAG検索 | ChromaDB（ローカル）or Pinecone（既存） |
| 型安全スキーマ | Pydantic v2 |
| 動的平衡モデル | NumPy / SciPy（`solve_ivp`）、勾配計算が必要な場合はJAX |
| コード生成エージェント | Claude Code |
| JSONバージョン管理 | Pydanticの`model_json_schema()`によるスキーマ自体の出力・差分管理 |
| 来歴追跡 | `hashlib`（stdlib、外部依存を増やさない） |

このフェーズで一度確定させ、以降のフェーズで追加するのは基本的に避ける。

---

## 3. 未解決の設計課題

- **循環の実装**：Phase 4のJSONを新規ノートとしてVaultへ書き戻し、Phase 0のインデックスへ再度乗せる仕組みが、現状どのフェーズにも明示的に組み込まれていない。ここを後回しにすると「循環」構想が実装上は循環しないまま終わる。
- **γ_ij 行列の実データ充足**：`mbt_hypercycle/interaction_matrix.py` の相互作用係数を、RAGから抽出した実測値で埋める作業が未着手。

---

## 4. 実行順序の原則

各フェーズは並列に進めず、Phase 0の完了判定基準を満たしてからPhase 1へ、という直列進行を原則とする（並行ワークストリームを避ける、動くコードを優先するという既定の作業方針に基づく）。

**次の着手点**：Phase 0の完了判定（RAGクエリ疎通検証）。
