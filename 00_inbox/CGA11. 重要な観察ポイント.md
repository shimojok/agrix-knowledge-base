結論から言うと、このログだけでは**どのJSONファイルが壊れているかは特定できません**。  
理由はシンプルで、**Streamlitがエラーメッセージをマスクしているため「lineno / colno」が消えている**からです。

ただし、このトレースから分かる“重要な構造的問題”はあります。

---

## 🔍 重要な観察ポイント

### ① エラー発生箇所

```
File "/mount/src/healthbook-ai/src/inference_engine.py", line 9
→ q_data = self._load_json(q_path)
```

その後：

```
File "...", line 16, in _load_json
→ d_data = self._load_json(d_path)
```

👉 これは明らかに異常です

---

## ⚠️ バグ確定：_load_jsonの実装が壊れている

通常 `_load_json` はこうなるべきです：

```python
def _load_json(self, path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
```

しかしログを見ると：

```python
q_data = self._load_json(q_path)
↓
_load_json内で
d_data = self._load_json(d_path)
```

👉 **再帰呼び出ししている**  
👉 **しかも引数がすり替わっている可能性が高い**

---

## 🎯 起きていること（ほぼ確定）

- `_load_json()` の中で別JSONを読み込もうとしている
    
- その際に壊れたJSONに当たっている
    
- しかしどのファイルかログに出ない
    

---

## ✅ 対処①（最優先）：_load_jsonを修正

```python
def _load_json(self, path):
    import json
    
    print(f"[LOAD] {path}")  # ← これ重要
    
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
```

👉 これで「どのファイルで落ちるか」確定します

---

## ✅ 対処②：ロード順を分離（デバッグ用）

```python
q_data = self._load_json(q_path)
print("Q OK")

d_data = self._load_json(d_path)
print("D OK")

k_data = self._load_json(k_path)
print("K OK")
```

👉 どこで止まるか一発で分かる

---

## ✅ 対処③（最短ルート）：ローカル検証

あなたが最初に提示したコードを**そのまま実行**してください：

```python
for f in [
 "data/questionnaire_200_jp.json",
 "data/disease_matrix_137.json",
 "data/kampo_metabolic_library.json"
]:
```

👉 これが最速・確実

---

## 🔥 高確率で壊れているファイル

プロジェクト構造から見て：

### 最も怪しい

👉 `kampo_metabolic_library.json`

理由：

- ネスト深い
    
- 配列 + 辞書混在
    
- 生薬JSONは人手編集が多く壊れやすい
    

---

## 🚀 次の一手（これで確定）

どちらかを実行してください：

### 方法A（推奨）

- `_load_json` に print追加
    
- Streamlit再実行
    

### 方法B（最速）

- ローカルで3ファイル検証コード実行
    

---

## 👉 次にやること

結果をそのまま貼ってください：

例：

```
[ERROR] data/kampo_metabolic_library.json — line 142, col 18
```

👉 そこをピンポイントで修正します  
👉 必要なら「完全に壊れないJSON構造」に再設計します（HealthBook仕様準拠）

---

必要なら次は：

- JSON自動修復ツール
    
- スキーマバリデーション（Pydantic）
    
- Azure/FHIR互換整形
    

まで一気に持っていけます。