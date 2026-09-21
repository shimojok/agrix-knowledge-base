👉️Prompt

AGRIX-OSのdashboard/app.pyに「SafetyChain™ 鮮度保持力ダッシュボード」を追加してください。

## 追加コンポーネント
1. **Vitality Score (V-Score) ゲージ**
   - 収穫後のATP減少速度から「代謝寿命」をリアルタイム表示
   - 基準：MBT55処理作物 vs 慣行農業作物の比較

2. **4レイヤー動的価格表示**
   - P_total = P_market + V(機能性) + L(ロス削減) + m(医療費削減) + C(炭素隔離)
   - 各レイヤーの寄与額を積み上げ棒グラフで表示

3. **Metabolic Life カウントダウン**
   - 「この農産物の機能性はあと○日維持されます」
   - 温度・湿度センサー連動で動的更新

## ドキュメント参照
添付の SafetyChain™ 定義ドキュメント3点を参照してください。

(５時まで待ちー回答をDSに送付)

---
---
👉️ Claude の回答

まず既存コードとプロジェクト構造を確認します。

全構造把握完了。設計方針を決めます。

**Aesthetic Direction:** 生命科学×金融ダッシュボード。深海バイオルミネッセンスをイメージした暗色基調、有機的な曲線、データが「呼吸している」ような動的アニメーション。フォント: `IBM Plex Mono`（数値）+ `DM Serif Display`（見出し）。

Now inject CSS properly via `app.index_string`:

全テスト通過。ファイルを出力します。

## タスク完了レポート

全テスト通過: 2 callbacks / 10 outputs / 6 crops × 2 treatments = 12パターン全OK

---

### 実装サマリー

**`vitality_engine.py`** — ダッシュボードのすべての数理エンジン

| 関数 | 内容 |
|---|---|
| `compute_vscore()` | ATP減少速度モデル。SCFA保護・抗酸化力・SHEスコアで減衰定数を補正。Q10=2のアレニウス近似で保存温度感応 |
| `metabolic_life_remaining()` | V-Score=35の閾値交差点を二分探索。「あと○日」をリアルタイム返却 |
| `compute_ptotal()` | P_total = P_market + V + L + m + C の5層分解。炭素価格スライダー連動 |
| `build_dashboard_data()` | Dash callbackの単一エントリーポイント。全データを1コールで取得 |

**`app.py`** — Plotly Dash ダッシュボード

3パネル構成で、深海バイオルミネッセンスの暗色テーマ（`#050d1a`ベース）を採用：

- **V-Score ゲージ** — 段階的カラー（teal→gold→orange→red）のアーク型インジケーター。Platinum/Gold/Silver/Standard グレードをリアルタイム表示
- **Metabolic Lifeカウントダウン** — 大型72pxフォントで残日数を表示。V-Score≦2日は`pulse`アニメーションで点滅警告
- **P_total積み上げ横棒グラフ** — 5層を色分け。炭素価格スライダーでC層がリアルタイム変化
- **V-Score崩壊カーブ** — MBT55 vs 慣行農業の2曲線比較 + 「NOW」マーカー
- **損失ドーナツチャート** — エチレン/冷害/水分/SCFA保護の4成分分解

```bash
cd AGRIX-OS && python dashboard/app.py
# → http://127.0.0.1:8050
```

