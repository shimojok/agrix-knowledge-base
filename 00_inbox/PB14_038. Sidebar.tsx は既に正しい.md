アドバイス１

## Sidebar.tsx は既に正しい

このファイルは問題ありません。`next/link` を正しく使っています。

---

## エラーの原因は別ファイル

ビルドログのエラーは：

```
./src/components/layout/Sidebar.tsx:2:22
Cannot find module 'react-router-dom'
```

**古いキャッシュ or 別バージョンのファイルを参照している**可能性が高いです。

---

## 確認・対処の順番

**1. 他ファイルに react-router-dom が残っていないか検索**

```bash
grep -r "react-router-dom" src/
```

どこかに残っているはずです。

**2. デプロイ環境（Vercel等）の場合、キャッシュクリア**

Vercelなら：

- Dashboard → プロジェクト → Settings → **Redeploy with "Clear cache"** を選択

**3. ローカルでクリーンビルド確認**

```bash
rm -rf .next node_modules package-lock.json
npm install
npm run build
```

---

まず `grep` の結果を教えてください。**他のファイルに `react-router-dom` が残っているのが本命**です。

---
現在のエラー


Failed to compile. ./src/pages/Auth/Login.tsx:2:10 Type error: Module '"../../api/auth"' has no exported member 'login'. Did you mean to use 'import login from "../../api/auth"' instead? 1 | import React, { useState } from "react";

> 2 | import { login } from "../../api/auth"; | ^ 3 | 4 | export default function LoginPage() { 5 | const [email, setEmail] = useState("test@example.com"); Error: Command "npm run build" exited with 1



---

アドバイス２

## 原因：`api/auth` の export 形式の不一致

`Login.tsx` が **named export** `{ login }` を期待しているのに、`api/auth` は **default export** になっています。

---

`src/api/auth.ts`（または `auth.js`）の内容を貼ってください。

おそらく以下のどちらかになっているはずです：

```ts
// パターンA：default export になっている
export default function login() { ... }

// パターンB：関数名が違う
export const loginUser = () => { ... }
```

---

## ファイルの中身が確認できない場合の即時対処

**Option 1：`api/auth` 側を named export に修正**

```ts
// api/auth.ts
export const login = async (email: string, password: string) => {
  // 既存の処理
};
```

**Option 2：`Login.tsx` 側を default import に修正**

```ts
import login from "../../api/auth";
```

`api/auth.ts` の内容を貼っていただければ、どちらを直すべきか確定できます。