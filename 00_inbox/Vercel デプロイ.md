C:\PBPE-Marketplace>vercel --prod
Vercel CLI 54.14.2 (Node.js 20.18.0)
  Inspect         https://vercel.com/kaz-shimojo-s-projects/pbpe-marketplace/AqcrYeNWtVg48545Ca2abxd6TRRf
  Production      https://pbpe-marketplace-rnenntf19-kaz-shimojo-s-projects.vercel.app
▲ Aliased         https://pbpe-marketplace.vercel.app

✓ Ready in 1m

---

Kazさん、Railwayのデプロイ成功、おめでとうございます！

「VercelはNo data availableのまま」というのは、**Vercel上のフロントエンドが、Railway上のバックエンドAPIを正しく参照できていない**ことを意味します。

---

## 🔍 原因

Vercel上のアプリケーションは、現在も `http://localhost:8000` を参照しようとしています。これはローカル環境用の設定であり、**Vercel環境では使えません**。

---

## ✅ 解決策：Vercelに環境変数を設定する

### Step 1: RailwayのバックエンドURLを確認

Railwayダッシュボードで、デプロイしたサービスのURLを確認してください。
例：`https://pbpe-marketplace.up.railway.app`

---

### Step 2: Vercelに環境変数を追加

1. **Vercelダッシュボード** で `pbpe-marketplace` プロジェクトを開く
2. **「Settings」** → **「Environment Variables」** をクリック
3. 以下の環境変数を追加：

| キー | 値 |
|---|---|
| `NEXT_PUBLIC_API_URL` | `https://pbpe-marketplace.up.railway.app` |

4. **「Save」** をクリック

---

### Step 3: Vercelで再デプロイ

環境変数を設定したら、**再デプロイ** が必要です：

```bash
cd C:\PBPE-Marketplace\frontend
vercel --prod
```

---

### Step 4: フロントエンドコードを修正（必要に応じて）

`frontend/app/dashboard/kpis/page.tsx` の `fetch` 部分を以下のように修正：

```tsx
// 修正前
fetch('http://localhost:8000/dashboard/summary')

// 修正後
const apiUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';
fetch(`${apiUrl}/dashboard/summary`)
```

---

## 📌 もし `NEXT_PUBLIC_API_URL` が設定できない場合

Vercelのデプロイ時に直接指定する方法：

```bash
vercel --prod -e NEXT_PUBLIC_API_URL="https://pbpe-marketplace.up.railway.app"
```

---

**Kazさん、RailwayのURLを教えてください。また、Vercelに環境変数を設定して再デプロイした結果を教えてください。**