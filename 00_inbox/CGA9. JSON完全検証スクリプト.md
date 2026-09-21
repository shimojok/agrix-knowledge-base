HealthBook-AIのStreamlitデプロイでJSONDecodeErrorが発生しています。

data/questionnaire_200_jp.json
data/disease_matrix_137.json
data/kampo_metabolic_library.json

のいずれかが破損しています。各ファイルのJSONとしての妥当性を検証するコードを書いてください。

---

まず結論から言うと、**単に `json.load()` を試すだけでは不十分**です。  
今回の構成（200問診・137疾病・漢方ライブラリ）は「構造バリデーション」までやらないと再発します。

以下に **実運用レベルの検証スクリプト**を提示します。

---

# ✅ JSON完全検証スクリプト

（構文 + スキーマ + クロス参照チェック）

```python
import json
import os


FILES = [
    "data/questionnaire_200_jp.json",
    "data/disease_matrix_137.json",
    "data/kampo_metabolic_library.json"
]


# -----------------------------
# ① JSON構文チェック
# -----------------------------
def validate_json_syntax(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return True, data
    except json.JSONDecodeError as e:
        print(f"[❌ JSON ERROR] {path}")
        print(f" -> line {e.lineno}, col {e.colno}")
        print(f" -> {e.msg}")
        return False, None
    except Exception as e:
        print(f"[❌ FILE ERROR] {path}: {e}")
        return False, None


# -----------------------------
# ② questionnaire構造チェック
# -----------------------------
def validate_questionnaire(data):

    errors = []

    if "questions" not in data:
        errors.append("Missing 'questions' key")
        return errors

    for qid, q in data["questions"].items():

        if "question" not in q:
            errors.append(f"{qid}: missing question")

        if not ("risk_factors" in q or "rf" in q):
            errors.append(f"{qid}: missing risk_factors/rf")

        if "weight" not in q:
            errors.append(f"{qid}: missing weight")

    return errors


# -----------------------------
# ③ disease_matrix構造チェック
# -----------------------------
def validate_disease_matrix(data):

    errors = []

    if "disease_matrix" not in data:
        errors.append("Missing 'disease_matrix'")
        return errors

    for d in data["disease_matrix"]:

        if "disease_id" not in d:
            errors.append("missing disease_id")

        if "disease_name_ja" not in d:
            errors.append(f"{d.get('disease_id')}: missing name")

        if "risk_factors" not in d:
            errors.append(f"{d.get('disease_id')}: missing risk_factors")

        if "recommended_kampo" not in d:
            errors.append(f"{d.get('disease_id')}: missing kampo")

    return errors


# -----------------------------
# ④ kampo構造チェック
# -----------------------------
def validate_kampo(data):

    errors = []

    if not isinstance(data, list):
        errors.append("Kampo JSON must be list")
        return errors

    for k in data:

        if "id" not in k:
            errors.append("missing kampo id")

        if "name_en" not in k:
            errors.append(f"{k.get('id')}: missing name")

        if "phytochemicals" not in k:
            errors.append(f"{k.get('id')}: missing phytochemicals")

    return errors


# -----------------------------
# ⑤ クロス参照チェック
# -----------------------------
def validate_cross_reference(q_data, d_data, k_data):

    errors = []

    # RF集合
    rf_set = set()
    for q in q_data["questions"].values():
        rf_list = q.get("risk_factors") or q.get("rf") or []
        rf_set.update(rf_list)

    # 疾患RF存在チェック
    for d in d_data["disease_matrix"]:
        for rf in d.get("risk_factors", []):
            if rf not in rf_set:
                errors.append(f"{d['disease_id']}: unknown RF '{rf}'")

    # Kampo存在チェック
    kampo_ids = {k["id"] for k in k_data}

    for d in d_data["disease_matrix"]:
        for kid in d.get("recommended_kampo", []):
            if kid not in kampo_ids:
                errors.append(f"{d['disease_id']}: invalid kampo '{kid}'")

    return errors


# -----------------------------
# 🚀 実行
# -----------------------------
def main():

    loaded = {}

    print("\n=== JSON Syntax Check ===")
    for path in FILES:
        ok, data = validate_json_syntax(path)
        if ok:
            print(f"[OK] {path}")
            loaded[path] = data
        else:
            print(f"[FAIL] {path}")
            return  # 構文エラーは即停止

    print("\n=== Structure Check ===")

    q_errors = validate_questionnaire(loaded[FILES[0]])
    d_errors = validate_disease_matrix(loaded[FILES[1]])
    k_errors = validate_kampo(loaded[FILES[2]])

    for e in q_errors:
        print("[Q ERROR]", e)

    for e in d_errors:
        print("[D ERROR]", e)

    for e in k_errors:
        print("[K ERROR]", e)

    print("\n=== Cross Reference Check ===")

    cross_errors = validate_cross_reference(
        loaded[FILES[0]],
        loaded[FILES[1]],
        loaded[FILES[2]]
    )

    for e in cross_errors:
        print("[X ERROR]", e)

    print("\n=== DONE ===")


if __name__ == "__main__":
    main()
```

---

# 🔥 よくあるJSONDecodeErrorの原因（今回ほぼこれ）

実務上の経験的に、今回の3ファイルなら原因は高確率で以下です：

### 1. 末尾カンマ

```json
{
  "a": 1,
}
```

### 2. ダブルクォート欠落

```json
{ key: "value" }
```

### 3. 全角文字混入（不可視）

- 特に 　（全角スペース）
    
- BOM付きUTF-8
    

### 4. 配列/オブジェクト混在

```json
{ "kampo": { ... } }  ← 本来 list
```

---

# ⚠️ デバッグの最短ルート

もし時間を無駄にしたくなければ：

```bash
python validator.py
```

→ エラー行番号が出る  
→ 該当ファイルをVS Codeで開く  
→ **その行の直前が原因**

---

# 🚀 次の一手（重要）

この問題は「一度直す」では不十分です。

### CIに組み込んでください

```bash
pre-commit hook
```

### もしくは

```bash
GitHub ActionsでJSON検証
```

---

必要なら：

- JSON Schema（正式定義）
    
- 自動修復スクリプト
    
- VS Code用Lint設定
    

まで一気に整備できます。