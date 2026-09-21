# MBT55 メタンガス排出削減ダッシュボード 設計仕様書

対象データ: `MethaneReductionSummary` JSON（Canonical値として扱う）
GWP(CH₄, IPCC AR6, 100年) = **27.9**

---

## 1. MBT55削減ロジックの明文化

### 1.1 共通計算式

各シーン i について、以下の3つの値は**JSON側で確定済みのCanonical値**であり、本ロジックは「なぜその値が導かれるか」を説明する層であって、値を再計算・上書きする層ではない。

```
reduction_rate_percent_i = mbt_reduction_i / baseline_emission_i × 100
```

CO₂e換算（ダッシュボード側で新たに導出する指標）:

```
baseline_co2e_i   = baseline_emission_ton_ch4_per_year_i   × GWP(27.9)
reduction_co2e_i  = mbt_reduction_ton_ch4_per_year_i        × GWP(27.9)
residual_co2e_i    = baseline_co2e_i - reduction_co2e_i
```

全体集計は各シーンのCO₂e換算値の単純合算（線形合算、シーン間の相互作用は想定していない）:

```
total_baseline_co2e  = Σ baseline_co2e_i
total_reduction_co2e = Σ reduction_co2e_i
```

**検算**: JSONのtotal値からCO₂e換算すると、
- total_baseline: 14,014,336.92 t-CH₄ × 27.9 ≈ **391.0 Mt-CO₂e/年**
- total_reduction: 8,243,727.6 t-CH₄ × 27.9 ≈ **230.0 Mt-CO₂e/年**

このtotal_reduction_co2e ≈230 Mtという値は、notesに記載の「総GHG削減目標510 Mt-CO₂eからの逆算」と整合しており、メタン起源の削減がGHG削減目標のうち約45%を占める計算になる（この対応関係はNotebookLM側のモデル設計思想であり、ダッシュボードは前提として表示するに留め、再検証はしない）。

### 1.2 シーン別ロジック

#### ① 家畜への発酵飼料投与（livestock_feed）
- **ベースラインロジック**: アフリカ全土の家畜頭数（牛3.5億頭、羊・ヤギ8億頭）に基づく腸内発酵由来メタンの標準排出係数を積算したもの。
- **削減ロジック**: MBT55が腸内環境を短鎖脂肪酸（SCFA）生成優位にシフトさせ、メタン生成基質である水素分圧を低下（dH₂/dt ≈ 0）させることで生成量を抑制。削減係数 0.012 kg-CH₄/kg-MBT55/日を用いた推定。
- **削減率**: 18.0%（実測寄りの係数として扱うが、頭数データ自体は統計値であり不確実性を含む）
- **区分**: 削減係数・頭数データ＝**推定/文献値**、削減メカニズム（dH₂/dt≈0）＝**MBT55固有の実測ロジック**

#### ② 水田へのMBT発酵肥料施用（rice_paddy）
- **ベースラインロジック**: 水田からの嫌気的メタン生成（メタン生成古細菌由来）の標準フラックス。
- **削減ロジック**: MBT55施用により土壌好気性画分を55%まで引き上げ、メタン酸化菌（Methanotrophs、例: *Methylococcus capsulatus*）を活性化。土壌酸化還元電位（Eh）を−100〜+200mVの範囲に制御することで嫌気的メタン生成を抑制。
- **削減率**: 45.0%（文献レンジ30-60%の中央値寄りの値として採用）
- **区分**: 削減率レンジ＝**文献値（30-60%）**、45%という採用値＝**モデル内の代表値（仮定）**

#### ③ 有機廃棄物のMBT処理（waste_management）
- **ベースラインロジック**: 生ごみ・食品廃棄物・加工残渣が埋立処分された場合に嫌気分解で発生するメタン量。
- **削減ロジック**: MBT55による24時間完全腐植化により、そもそも嫌気的分解プロセス自体が発生しない（Avoidance＝回避型削減）。したがって削減率は原理上100%。
- **削減率**: 100.0%（＝ベースライン排出が全量回避される前提）
- **区分**: 「24時間で完全腐植化する」という処理速度＝**実証（実測）データ**、「ゆえに埋立メタンが100%回避される」という因果＝**モデル上の仮定**（実際の廃棄物収集率・MBT処理カバー率は別途要考慮）

#### ④ 流木・災害廃棄物のMBT処理（disaster_sludge）
- **ベースラインロジック**: baseline=1.0t-CH₄という値は代表値（プレースホルダー）であり、他シーンのような統計的積算値ではない。
- **削減ロジック**: 岩沼汚泥（震災汚泥）等での数日内分解実績はあるが、統計モデル化に足る削減統計が不足しているため、reduction=0.0、rate=0.0%としている。
- **区分**: **完全にデータ不足区分**。ダッシュボード上は「実証事例あり・定量化未了」として明示すべきで、他シーンと同列の棒グラフで見せると誤読を招く（後述）。

---

## 2. ダッシュボード構成案

既存のAGRIX Architecture Dashboard（index.html / ja.html / en.html）の構成トーンに合わせ、以下の4セクションを提案する。

### セクション A：全体サマリー（Hero / KPI Cards）
| 指標 | 表示形式 |
|---|---|
| 総削減率 58.82% | 大型ドーナツ/ゲージチャート |
| 年間CH₄削減量 8,243,728 t | KPIカード（サブに t-CH₄/年） |
| 年間CO₂e削減量 ≈230.0 Mt | KPIカード（メイン指標として最も目立たせる） |
| ベースライン排出量 14,014,337 t-CH₄（≈391 Mt-CO₂e） | 比較用の淡色カード |

推奨: CO₂e換算値をヘッダーの主指標にし、t-CH₄値はサブテキストとして併記（投資家・政策決定者はCO₂e単位に慣れているため）。

### セクション B：シーン別削減量
- **グラフ種別**: 横棒グラフ（stacked bar、ベースライン vs 削減量を同一バー内で色分け）
- 4シーン（家畜／水田／廃棄物／災害廃棄物）を縦に並べ、各バーに「削減率%」ラベルを重畳
- **注意点**: disaster_sludgeはbaseline=1.0という極小値のため、対数軸にしない限り他シーンと並べると視覚的に消える。この対策として:
  - 別枠（サイドカード）で「実証事例あり・定量化未了」バッジ付きで独立表示するか
  - 対数スケールの補助グラフを併設

### セクション C：削減率比較 ＋ 導入前後比較
- **削減率**: 横棒 or レーダーチャートで4シーンを比較（18% / 45% / 100% / 0%）
- **導入前後比較**: グループ化縦棒グラフ（各シーンごとに「導入前」「導入後」の2本のバー）
- CH₄とCO₂eをトグル切替できるUIにする（単位切替ボタン）

### セクション D：コスト指標（$/ton-CO₂e）
> **重要な前提の明示**: 提供JSONには投資額・運営コストのフィールドが存在しない。したがってこのセクションは**現時点でデータ欠落**であり、実装する場合は以下のいずれかを取る必要がある：
> 1. 別途MSCモデル（本文書の元資料にあるMBT Sustainable Cycleの経済レイヤー、例：炭素市場単価65 USD/t等）から仮の単価を注入し「試算値」であることを明示
> 2. コストデータが未接続であることを示す「Coming Soon」プレースホルダーとして表示
>
> 数値を勝手に生成して確定値のように見せることは避けるべき。

---

## 3. 実装向けレイアウト・コンポーネント案

### 3.1 ページ構成（擬似コード）

```
<Dashboard>
  <Header>
    <Title>MBT55 Methane Reduction Dashboard</Title>
    <UnitToggle options={["t-CH4", "t-CO2e"]} />
  </Header>

  <MainGrid>
    <SummarySection>
      <KPICard label="総削減率" value={58.82} unit="%" style="gauge" />
      <KPICard label="年間CH4削減量" value={8243727.6} unit="t-CH4/年" />
      <KPICard label="年間CO2e削減量" value={230000000} unit="t-CO2e/年" highlight />
      <KPICard label="ベースライン排出量" value={14014336.92} unit="t-CH4/年" muted />
    </SummarySection>

    <SceneBreakdownSection>
      <StackedBarChart data={scenes} xKey="scene_name" 
        series={["baseline_emission", "mbt_reduction"]} />
      <SceneCard scene="disaster_sludge" badge="実証事例あり・定量化未了" />
    </SceneBreakdownSection>

    <ComparisonSection>
      <GroupedBarChart data={scenes} groups={["before", "after"]} />
      <ReductionRateRadar data={scenes} />
    </ComparisonSection>

    <CostSection status="data_not_provided">
      <Placeholder text="投資額・運営コストデータ未接続" />
    </CostSection>
  </MainGrid>

  <Sidebar>
    <NoteBox text={summary.notes} />
    <DataSourceList scenes={scenes} field="data_source_notes" />
  </Sidebar>
</Dashboard>
```

### 3.2 TypeScript型（既存インターフェースを継承・拡張）

```typescript
// --- 既存の入力契約（変更しない） ---
// MethaneReductionScene, MethaneReductionSummary は与件のまま使用

// --- ダッシュボード内部で導出する表示用の型 ---

/** CO2e換算を加えたシーン表示用モデル */
export interface MethaneSceneViewModel extends MethaneReductionScene {
  baseline_co2e_ton: number;   // baseline_emission_ton_ch4_per_year * GWP
  reduction_co2e_ton: number;  // mbt_reduction_ton_ch4_per_year * GWP
  residual_co2e_ton: number;   // baseline_co2e_ton - reduction_co2e_ton
  data_quality: "measured" | "literature_estimate" | "placeholder";
}

/** サマリーKPIカード用 */
export interface KPICardData {
  label: string;
  value: number;
  unit: "t-CH4/year" | "t-CO2e/year" | "%";
  highlight?: boolean;
  muted?: boolean;
}

/** 積み上げ棒グラフ用データ構造 */
export interface StackedBarDatum {
  scene_id: string;
  scene_name: string;
  baseline: number;
  reduction: number;
  residual: number; // baseline - reduction
}

/** コスト指標セクション（未接続時のフォールバック型） */
export interface CostMetric {
  scene_id: string;
  cost_usd_per_ton_co2e: number | null; // null = データ未提供
  source: "provided" | "assumption" | "unavailable";
}

/** 単位切替に対応した共通変換ユーティリティのシグネチャ */
export function toViewModel(
  scenes: MethaneReductionScene[],
  gwp: number = 27.9
): MethaneSceneViewModel[];
```

### 3.3 コンポーネント責務まとめ

| コンポーネント | 役割 | 入力データ |
|---|---|---|
| `KPICard` | 単一指標の強調表示 | `KPICardData` |
| `StackedBarChart` | シーン別 before/after 可視化 | `StackedBarDatum[]` |
| `ReductionRateRadar` | シーン間の削減率比較 | `MethaneSceneViewModel[]` |
| `SceneCard` | 定量化未了シーンの個別表示（disaster_sludge等） | `MethaneSceneViewModel` |
| `CostSection` | $/ton-CO2e（現状プレースホルダー） | `CostMetric[] \| null` |
| `NoteBox` | notesフィールドの不確実性注記表示 | `summary.notes` |

---

## 補足：データ品質の分類まとめ

| シーン | ベースライン | 削減ロジック | 総合区分 |
|---|---|---|---|
| livestock_feed | 統計（頭数）＋文献係数 | MBT55固有メカニズム記述あり | 推定値（中） |
| rice_paddy | 文献レンジの中央値採用 | メカニズム明確（Eh制御） | 推定値（中） |
| waste_management | 統計積算 | 回避型（100%）＝モデル仮定 | 仮定強め（要検証） |
| disaster_sludge | プレースホルダー(=1.0) | 未定量化 | データ欠落・実証事例のみ |

ダッシュボードには、この品質区分を色分けバッジ（例：緑=実測寄り、黄=文献推定、灰=データ欠落）として各シーンカードに表示することを推奨する。
