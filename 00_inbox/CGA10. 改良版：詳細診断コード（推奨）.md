HealthBook-AIでJSONDecodeErrorが発生しています。

data/ ディレクトリの以下の3ファイルを1つずつ読み込み、エラーが出るファイルを特定してください。

import json, os

for f in ["data/questionnaire_200_jp.json", "data/disease_matrix_137.json", "data/kampo_metabolic_library.json"]:
    try:
        with open(f, "r", encoding="utf-8") as fh:
            data = json.load(fh)
        print(f"[OK] {f} — keys: {list(data.keys()) if isinstance(data, dict) else f'list({len(data)} items)'}")
    except json.JSONDecodeError as e:
        print(f"[ERROR] {f} — line {e.lineno}, col {e.colno}: {e.msg}")
    except FileNotFoundError:
        print(f"[MISSING] {f}")


エラーが特定できたら、該当ファイルの該当行を修正します。

---

提示された検証コードで十分に原因特定できますが、精度とデバッグ速度を上げるために「どこで壊れているか」をもう一段深く特定できるようにしましょう。

まず、そのまま実行すれば3ファイルのうちどれが壊れているかは判別できます。  
次にやるべきは **壊れているJSONの「具体的な位置と原因の型」特定**です。

---

## ✅ 改良版：詳細診断コード（推奨）

```python
import json

files = [
    "data/questionnaire_200_jp.json",
    "data/disease_matrix_137.json",
    "data/kampo_metabolic_library.json"
]

for f in files:
    print(f"\n--- Checking: {f} ---")
    try:
        with open(f, "r", encoding="utf-8") as fh:
            content = fh.read()
        
        # ① JSON構文チェック
        data = json.loads(content)
        print(f"[OK] {f}")
        
    except json.JSONDecodeError as e:
        print(f"[ERROR] {f}")
        print(f"Line: {e.lineno}, Column: {e.colno}")
        print(f"Message: {e.msg}")
        
        # ② エラー周辺を可視化
        lines = content.splitlines()
        error_line = lines[e.lineno - 1]
        
        print("\n--- Error Line ---")
        print(error_line)
        
        print("\n--- Pointer ---")
        print(" " * (e.colno - 1) + "^")
        
        # ③ 前後文表示（重要）
        print("\n--- Context ---")
        for i in range(max(0, e.lineno-3), min(len(lines), e.lineno+2)):
            print(f"{i+1}: {lines[i]}")
        
    except FileNotFoundError:
        print(f"[MISSING] {f}")
```

---

## 🔍 よくあるJSON破損パターン（今回ほぼ確実にどれか）

HealthBook系JSONは構造が複雑なので、以下が高確率です：

### 1. 末尾カンマ

```json
{
  "a": 1,
}
```

→ ❌ NG

---

### 2. ダブルクォート抜け

```json
"question": 朝食を抜くことが多い
```

→ ❌ NG（文字列は必ず ""）

---

### 3. キーのクォート抜け

```json
question: "朝食..."
```

→ ❌ NG

---

### 4. 日本語全角記号混入

```json
"weight": ０.85
```

→ ❌ NG（全角0）

---

### 5. 配列/オブジェクトの閉じ忘れ

```json
"questions": {
   "1": { ... }
   "2": { ... }
```

→ ❌ カンマ抜け or }不足

---

### 6. エンコーディング混在（UTF-8 BOMなど）

---

## 🎯 優先チェック順（重要）

この順で壊れている可能性が高いです：

1. **kampo_metabolic_library.json**
    
    - ネスト深い
        
    - 配列構造
        
    - 生薬データ（最も壊れやすい）
        
2. **disease_matrix_137.json**
    
    - 重み付き辞書（カンマミス多発）
        
3. **questionnaire_200_jp.json**
    
    - 比較的シンプルだが長い
        

---

## 🚀 次のアクション

1. 上記コードを実行
    
2. 出力結果をそのまま貼ってください
    

👉 こちらで「1行レベルで修正案」を提示します  
（単なる構文修正ではなく、HealthBook推論エンジン整合性まで見ます）

---

必要なら、**JSON自動修復スクリプト（半自動補正 + バリデーション）**も出せます。