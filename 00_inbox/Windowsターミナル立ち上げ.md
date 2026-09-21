Kazさん、了解しました。**ゼロから**、Windowsターミナルを立ち上げて、バックエンドとフロントエンドを起動する手順を説明します。

今の混乱を全てリセットしましょう。

---

## 🚀 最初からやり直す（ゼロベース）

### Step 1: Windowsターミナルを開く
1. **Windowsキー** を押す
2. **「cmd」** と入力
3. **「コマンドプロンプト」** をクリック

---

### Step 2: バックエンドを起動する

```bash
cd C:\PBPE-Marketplace\backend
venv\Scripts\activate
python -m uvicorn main:app --reload --port 8000
```

---

### Step 3: 別のコマンドプロンプトを開く（フロントエンド用）

1. **もう一度** Windowsキー → 「cmd」 → Enter
2. 以下を実行：

```bash
cd C:\PBPE-Marketplace\frontend
npm run dev
```

---

### Step 4: ブラウザで確認

```
http://localhost:3000/dashboard/kpis
```

---

## 📌 もしエラーが出たら

| エラー | 対応 |
|---|---|
| `venv\Scripts\activate` でエラー | 無視して `python -m uvicorn ...` を直接実行 |
| `python` が見つからない | `py` に変更（`py -m uvicorn ...`） |
| `npm` が見つからない | Node.jsがインストールされていない |

---

**Kazさん、まずは Step 1 と Step 2 を実行してください。結果を教えてください。**