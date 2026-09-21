CGA10が先、エラーメッセージを見た回答がCGA11です。

---

CGA11の指摘は重要です。`inference_engine.py`の`_load_json`にバグがある可能性が高いと。

---

## [① PMO] 2つの問題が混在している可能性

| 問題 | 内容 |
|:---|:---|
| **問題A** | `inference_engine.py` の `_load_json` が壊れている（CGA11の指摘） |
| **問題B** | JSONファイル自体が破損している可能性 |

---

## [① PMO] 先に問題Aを修正

`src/inference_engine.py` の `_load_json` メソッドを**以下の1行だけ**にしてください。

```python
def _load_json(self, path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
```

現在のコードが複雑な実装になっている場合（再帰呼び出しなど）、それを**完全に削除**して上記3行に置き換えてください。

---

## [① PMO] 次に問題Bを確認

上記修正後にStreamlit Cloudが再デプロイされます。

**もしそれでもエラーが出る場合**は、CGA10の診断コードをChatGPT（HealthBook-AIプロジェクト内）で実行して、破損ファイルを特定してください。

```
import json

files = [
    "data/questionnaire_200_jp.json",
    "data/disease_matrix_137.json",
    "data/kampo_metabolic_library.json"
]

for f in files:
    try:
        with open(f, "r", encoding="utf-8") as fh:
            data = json.loads(fh.read())
        print(f"[OK] {f}")
    except json.JSONDecodeError as e:
        print(f"[ERROR] {f} — line {e.lineno}, col {e.colno}: {e.msg}")
    except FileNotFoundError:
        print(f"[MISSING] {f}")
```

結果を教えてください。