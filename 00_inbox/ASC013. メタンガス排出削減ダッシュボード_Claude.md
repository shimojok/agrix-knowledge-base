これから、メタンガス排出削減ダッシュボードに関するPromptを、TypeScript型＋Claude向けPrompt＋NotebookLMのJSONをセットで送ります。

/**

- 単一の削減シーン（発酵飼料、水田、食品廃棄物、流木災害など）ごとの
- メタン排出削減シミュレーション結果。 _/ export interface MethaneReductionScene { /_* シーンの一意なID（例: 'livestock_feed', 'rice_paddy', 'food_waste', 'driftwood_disaster'） _/ scene_id: string; /_* シーン名（日本語） _/ scene_name: string; /_* NotebookLMから抽出した、シーンの詳細説明 _/ description: string; /_* MBT導入前の年間メタン排出量 [ton-CH4/year] _/ baseline_emission_ton_ch4_per_year: number; /_* MBT発酵肥料・飼料導入後の年間メタン削減量 [ton-CH4/year] _/ mbt_reduction_ton_ch4_per_year: number; /_* 削減率 [%] = mbt_reduction / baseline_emission * 100 _/ reduction_rate_percent: number; /_* 削減量算出に使った主要パラメータ（NotebookLMからの出典を含む） _/ key_parameters: string[]; /_* NotebookLM内のどのドキュメント・セクションから抽出したかのメモ */ data_source_notes: string; }

/**

- 全シーンを統合した、MBT55によるメタン削減シミュレーションの集計結果。 _/ export interface MethaneReductionSummary { /_* 全シーン合計のMBT導入前年間メタン排出量 [ton-CH4/year] _/ total_baseline_emission_ton_ch4_per_year: number; /_* 全シーン合計のMBT導入後年間メタン削減量 [ton-CH4/year] _/ total_mbt_reduction_ton_ch4_per_year: number; /_* 全体削減率 [%] _/ total_reduction_rate_percent: number; /_* 各シーンの詳細結果リスト _/ scenes: MethaneReductionScene[]; /_* 前提条件・不確実性・補足説明など */ notes?: string; }

次はPromptです。

あなたは、MBT55 BioHubによるメタンガス排出削減ロジックを設計し、 経営者・投資家・政策決定者向けのダッシュボードを構築する専門家です。

以下に、NotebookLMから抽出した「MBT発酵肥料・発酵飼料・MBT廃棄物処理によるメタン削減シミュレーション」の 構造化データ（MethaneReductionSummary）が JSON 形式で与えられます。

【入力データ（Contract-First）】

- MethaneReductionSummary JSON
    - total_baseline_emission_ton_ch4_per_year
    - total_mbt_reduction_ton_ch4_per_year
    - total_reduction_rate_percent
    - scenes[]（各シーンの詳細）

【あなたのタスク】

1. **MBT55削減ロジックの明文化**
    
    - 各シーンごとに、
        - ベースライン排出量の算出ロジック
        - MBT導入後削減量の算出ロジック
        - 削減率 [%] の意味と前提条件 を、数式と文章で明確に説明してください。
    - 可能であれば、CH₄ → CO₂e への換算も行い、
        - 「年間 CO₂e 削減量」として統合してください。
2. **ダッシュボード構成案の設計**
    
    - 既存の AGRIX Architecture Dashboard（index.html / ja.html / en.html / agrix_architecture_dashboard など）を参考に、
        - 以下のようなセクション構成を提案してください：
            - 全体削減量（CH₄ / CO₂e）のサマリー
            - シーン別削減量（家畜 / 水田 / 食品廃棄物 / 災害廃棄物 / その他）
            - 削減率 [%] と、MBT導入前後の比較グラフ
            - 投資額・運営コストと、削減量あたりのコスト指標（例：$/ton-CO₂e）
    - 各セクションについて、
        - どの指標を表示するか
        - どのグラフ（棒グラフ・折れ線・円グラフなど）を使うか を具体的に記述してください。
3. **実装に使えるレイアウト・コンポーネント案**
    
    - HTML/CSS/JavaScriptで実装することを想定し、
        - ページ構成（ヘッダー／メイン／サイドバー）
        - 主要コンポーネント（カード、チャート、テーブル） の構造を、擬似コードレベルで示してください。
    - 可能であれば、各チャートに対応するデータ構造（TypeScriptインターフェース）も提案してください。

【出力フォーマット】

- 1. MBT55削減ロジックの説明（数式＋文章）
- 2. ダッシュボード構成案（セクションごとの説明）
- 3. 実装向けレイアウト・コンポーネント案（擬似コード＋インターフェース）

【重要な前提】

- 入力 JSON の数値は「Canonical値」として扱い、勝手に変更しないでください。
- 不確実性やレンジがある場合は、ロジック内で明示し、 「どの部分が仮定で、どの部分がNotebookLM由来の実測・推定値か」を区別してください。

JSONコードを添付しました。

---

👉下記が、Claudeが出力した内容です。

要点だけ先にまとめます。

- **CO₂e換算**: total_reduction 8,243,727.6 t-CH₄ × GWP27.9 ≈ **230.0 Mt-CO₂e/年**、baseline ≈391.0 Mt-CO₂e/年。この230 Mtという値はnotesの「総GHG削減目標510 Mt-CO₂eからの逆算」と綺麗に整合しています。
- **disaster_sludgeシーンが特殊**: baseline=1.0（プレースホルダー）、reduction=0なので、他3シーンと同じ棒グラフに並べると視覚的に消えます。ダッシュボード上は「実証事例あり・定量化未了」バッジ付きの別枠にすることを提案しています。
- **コスト指標（$/ton-CO₂e）はJSONに存在しません**。勝手に数値を作らず、「データ未接続」のプレースホルダーとして扱うべき、と明記しました。

ファイルには、①4シーンそれぞれの数式ロジックと推定/実測の区分、②AGRIXダッシュボード流のセクション構成案(KPIカード・積み上げ棒グラフ・グループ化比較・コスト枠)、③擬似コード＋TypeScript型（`MethaneSceneViewModel`, `KPICardData`, `StackedBarDatum`など）を収録しています。


![[MBT55_Methane_Dashboard_Spec]]