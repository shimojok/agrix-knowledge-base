Kazさん、**おっしゃる通りです。** Vercelへのデプロイは**フロントエンド（表示）の更新**であり、バックエンド（Railway）のエンジンとの接続と表示確認は**別途必要**です。

---

## ✅ 確認すべきポイント

| 項目 | 確認方法 | 状態 |
|---|---|---|
| バックエンド（Railway）の再デプロイ | Railwayダッシュボードで確認 | ⏳ 未確認 |
| `/dashboard/summary` の応答 | ブラウザでJSON確認 | ⏳ 未確認 |
| Registry APIの応答 | `/registry/summary` を確認 | ⏳ 未確認 |
| フロントエンドとバックエンドの連携 | Registry Explorerでエントリ表示 | ⏳ 未確認 |

---

## 🚀 バックエンド（Railway）の状態確認

### 1. Railwayダッシュボードを開く

```
https://railway.app/dashboard
```

### 2. プロジェクト `pbpe-marketplace` を選択

### 3. 「Deployments」タブで最新のデプロイを確認

- **最新のデプロイが `main` ブランチの最新コミットを反映しているか**
- **ステータスが「Success」になっているか**

---

## 🔍 APIエンドポイントの直接確認

ブラウザで以下のURLを開いて、応答を確認してください：

| エンドポイント | URL |
|---|---|
| ルート | `https://pbpe-marketplace-production.up.railway.app/` |
| KPIサマリー | `https://pbpe-marketplace-production.up.railway.app/dashboard/summary` |
| Registryサマリー | `https://pbpe-marketplace-production.up.railway.app/registry/summary` |
| チェーンステータス | `https://pbpe-marketplace-production.up.railway.app/registry/chain/status` |

---

## 📌 もしJSONが表示されない場合

Railwayの再デプロイがまだ完了していないか、エラーが発生している可能性があります。

その場合は、Railwayダッシュボードで**デプロイログ**を確認してください。

---

**Kazさん、まずは `https://pbpe-marketplace-production.up.railway.app/` を開いて、`{"message":"PBPE Marketplace API is running"}` が表示されるか確認してください。結果を教えてください。**