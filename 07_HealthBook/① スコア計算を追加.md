了解です。順番に進めます。  
まずは **① 投資スコア（1つの数字）を追加** します。

---

# ■ やること

**app.pyに「総合投資スコア」を追加します。**

---

# ■ 手順

---

## ■ ① スコア計算を追加

app.pyでこのコメントを探してください：

```python
# =========================
# ■ KPI表示
# =========================
```

---

## ■ ② KPI表示の「直前」に以下を追加

```python
# =========================
# ■ 投資スコア
# =========================

def normalize(value, min_val, max_val):
    if max_val - min_val == 0:
        return 0
    return (value - min_val) / (max_val - min_val)

# 正規化（簡易レンジ設定）
irr_score = normalize(irr_on, 0, 0.5)
co2_score = normalize(co2_on, 0, 500)
lcoa_score = 1 - normalize(lcoa_on, 50, 150)  # 低いほど良い

# 重み付け
investment_score = (
    irr_score * 0.4 +
    co2_score * 0.3 +
    lcoa_score * 0.3
)
```

---

## ■ ③ KPIとして表示（追加）

KPI表示の中に1つ追加してください：

```python
col0 = st.columns(1)[0]
col0.metric("Investment Score", round(investment_score, 3))
```

---

# ■ 表示結果（こうなる）

```text
Investment Score   0.72
```

---

# ■ 意味（最短）

```text
IRR（収益性）
CO2（環境価値）
LCOA（コスト効率）
→ 1つに統合
```

---

# ■ ここで重要な変化

```text
複数指標 → 単一意思決定指標
```

👉 投資判断が一瞬でできる

---

# ■ 次にやること（続行）

この次は：

```text
② 国別ランキング（自動スコア比較）
```

に進みます。

---

完了したら「OK」とだけください。