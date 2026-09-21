Kazさん、**Registry Explorerの表示確認、ありがとうございます。**

`No registry entries found. Issuing PBPE will create entries.` という表示は、**レジストリ自体は正常に動作している** が、まだエントリが存在しないだけです。

ただし、**サイドメニューに `PBPE Registry` がない** のは、**サイドバーのナビゲーション項目に `/dashboard/registry` が追加されていない** ことが原因です。

---

## ✅ 解決策：サイドバーに Registry を追加する

`frontend/app/layout.tsx` の `navItems` 配列に Registry を追加します。

### 修正するファイル：`frontend/app/layout.tsx`

**現在の `navItems` 配列：**
```tsx
const navItems = [
  { href: '/dashboard/kpis', label: 'Global KPIs' },
  { href: '/dashboard/impact', label: 'Impact Breakdown' },
  { href: '/dashboard/market', label: 'PBPE Credits Market' },
  { href: '/dashboard/finance', label: 'Bonds & Insurance' },
  { href: '/dashboard/enterprise', label: 'Scope 3 × PBPE' },
  { href: '/dashboard/pbpe', label: 'PBPE Issuance' },
]
```

**修正後（Registryを追加）：**
```tsx
const navItems = [
  { href: '/dashboard/kpis', label: 'Global KPIs' },
  { href: '/dashboard/impact', label: 'Impact Breakdown' },
  { href: '/dashboard/market', label: 'PBPE Credits Market' },
  { href: '/dashboard/finance', label: 'Bonds & Insurance' },
  { href: '/dashboard/enterprise', label: 'Scope 3 × PBPE' },
  { href: '/dashboard/pbpe', label: 'PBPE Issuance' },
  { href: '/dashboard/registry', label: 'PBPE Registry' },  // ← 追加
]
```

---

## 🚀 デプロイ手順

1. **`frontend/app/layout.tsx` に上記の修正を加える**
2. **GitHubにプッシュ**（Vercelが自動デプロイ）
3. **デプロイ完了後、ブラウザで確認**

---

## 🔧 確認用コマンド（必要に応じて）

```bash
cd C:\PBPE-Marketplace
git add frontend/app/layout.tsx
git commit -m "Add PBPE Registry to sidebar navigation"
git push origin main
```

---

**Kazさん、`layout.tsx` を修正してプッシュしてください。完了したら「完了」と教えてください。**