[ \text{Coupon} = r_0

- \alpha \cdot \frac{\text{PBPE}{\text{actual}} - \text{PBPE}{\text{floor}}}{\text{PBPE}_{\text{floor}}}
    
- \beta \cdot \frac{\text{Impact}{\text{actual}} - \text{Impact}{\text{floor}}}{\text{Impact}_{\text{floor}}} ] GitHubに張り付けると、数式表示されません。　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　$$ \text{Coupon} = r_0
    
- \alpha \cdot \frac{\text{PBPE}{\text{actual}} - \text{PBPE}{\text{floor}}}{\text{PBPE}_{\text{floor}}}
    
- \beta \cdot \frac{\text{Impact}{\text{actual}} - \text{Impact}{\text{floor}}}{\text{Impact}{\text{floor}}} $$　　　　　　　　　　　　　　　　　　　こうすると、Obsidianでは問題ないのですが、うまく行きません。　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　$$ \text{Coupon}{\text{final}} = \min(\max(\text{Coupon}, r_{\text{min}}), r_{\text{max}}) $$　　　　　　　　　　　　　　　こちらは、GitHubで表示されます。表示方法を教えてください。



---

GitHubは**一部のLaTeX構文を正しく処理できない**制約があります。問題の原因と解決策を説明します。

---

### 原因

GitHubのMath renderingは `$` や `$$` をサポートしていますが、**subscriptのアンダースコア `_` がMarkdownのイタリック記号と競合**するため、複数の `_` が含まれる数式でパースが崩れます。

特に `\text{PBPE}_{\text{actual}}` のような `\text{...}_{\text{...}}` パターンが問題です。

---

### 解決策：`\mathit` または `\mathrm` + 波括弧を明示

```latex
$$
\text{Coupon} = r_0
+ \alpha \cdot \frac{\mathrm{PBPE}_{\mathrm{actual}} - \mathrm{PBPE}_{\mathrm{floor}}}{\mathrm{PBPE}_{\mathrm{floor}}}
+ \beta \cdot \frac{\mathrm{Impact}_{\mathrm{actual}} - \mathrm{Impact}_{\mathrm{floor}}}{\mathrm{Impact}_{\mathrm{floor}}}
$$
```

`\text{}` → `\mathrm{}` に変えるだけで多くの場合解決します。

---

### さらに確実な方法：改行を避けて1行に

GitHubは**数式内の改行（`+` で行を分ける書き方）が不安定**なため、1行にまとめるのが最も安全です。

```latex
$$
\text{Coupon} = r_0 + \alpha \cdot \frac{\mathrm{PBPE}_{\mathrm{actual}} - \mathrm{PBPE}_{\mathrm{floor}}}{\mathrm{PBPE}_{\mathrm{floor}}} + \beta \cdot \frac{\mathrm{Impact}_{\mathrm{actual}} - \mathrm{Impact}_{\mathrm{floor}}}{\mathrm{Impact}_{\mathrm{floor}}}
$$
```

---

### まとめ

|問題|原因|対処|
|---|---|---|
|`\text{}_{\text{}}` が崩れる|`_` がMarkdownと競合|`\mathrm{}` に変更|
|複数行数式が崩れる|GitHub改行処理が不安定|1行にまとめる|
|Obsidianでは動く|ObsidianはMathJax完全対応|GitHub用に別途調整|

`$$ ... $$` ブロック自体は正しいので、**`\text` → `\mathrm` への置換**が最初の一手です。





$$
\text{Coupon} = r_0
+ \alpha \cdot \frac{\mathrm{PBPE}_{\mathrm{actual}} - \mathrm{PBPE}_{\mathrm{floor}}}{\mathrm{PBPE}_{\mathrm{floor}}}
+ \beta \cdot \frac{\mathrm{Impact}_{\mathrm{actual}} - \mathrm{Impact}_{\mathrm{floor}}}{\mathrm{Impact}_{\mathrm{floor}}}
$$


$$
\text{Coupon} = r_0 + \alpha \cdot \frac{\mathrm{PBPE}_{\mathrm{actual}} - \mathrm{PBPE}_{\mathrm{floor}}}{\mathrm{PBPE}_{\mathrm{floor}}} + \beta \cdot \frac{\mathrm{Impact}_{\mathrm{actual}} - \mathrm{Impact}_{\mathrm{floor}}}{\mathrm{Impact}_{\mathrm{floor}}}
$$

