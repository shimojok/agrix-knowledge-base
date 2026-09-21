Streamlit、View系、Route系の違い、Pages Router、App Routerの関係性についてまとめてください。

---

# 結論

**Streamlit** と **View系 / Route系**、さらに **Pages Router / App Router** は、レイヤーが異なる概念です。

```text
UI Framework
├─ Streamlit
├─ React
├─ Vue
└─ Svelte

Routing Layer
├─ Route系
│   ├─ React Router
│   ├─ Next.js Pages Router
│   └─ Next.js App Router
│
└─ 非Route系
    └─ Streamlit Pages

View Layer
├─ Page
├─ Component
├─ Widget
└─ Dashboard
```

---

# Architecture

## 1. Streamlitとは

Streamlitは

```text
Python
 ↓
UI生成
 ↓
Webアプリ
```

を実現するフレームワークです。

特徴

```text
Backend
  Python

Frontend
  自動生成

Routing
  最小限

状態管理
  Session State
```

開発者は

```python
st.text_input()
st.button()
st.dataframe()
```

を書くのみでUIが生成されます。

---

## 2. View系とは

View系は

```text
「何を表示するか」
```

を管理します。

例

```text
Dashboard
Disease Report
Risk Analysis
Patient Detail
AGRIX Farm Detail
```

構造

```text
View
 ├─ Header
 ├─ Graph
 ├─ Table
 └─ Form
```

HealthBookで言うと

```text
Risk View
Phenotype View
Nutrition View
Microbiome View
```

がViewになります。

---

## 3. Route系とは

Route系は

```text
URL
 ↓
画面
```

の対応を管理します。

例

```text
/                     → Home
/risk                 → Risk View
/phenotype            → Phenotype View
/report               → Report View
```

Routeは

```text
どの画面を表示するか
```

を決定します。

---

# Data Flow

```text
URL
 ↓
Route
 ↓
View
 ↓
Component
 ↓
User
```

例

```text
/healthbook/report/123
           ↓
       Route
           ↓
      Report View
           ↓
   Risk Components
           ↓
        User
```

---

# Pages Router

## 概要

古いNext.js方式

```text
/pages
```

フォルダがルーティングになります。

例

```text
pages
├─ index.tsx
├─ risk.tsx
├─ report.tsx
└─ phenotype.tsx
```

自動的に

```text
/
/risk
/report
/phenotype
```

が生成されます。

---

## 特徴

```text
シンプル
理解しやすい
SEO対応
```

しかし

```text
Server Components
Streaming
Nested Layout
```

が弱い。

---

# App Router

## 概要

Next.js 13以降の新方式

```text
/app
```

ベース。

例

```text
app
├─ page.tsx
├─ risk
│   └─ page.tsx
├─ report
│   └─ page.tsx
└─ layout.tsx
```

---

## 特徴

### Nested Layout

```text
Root Layout
 ├─ Risk
 ├─ Phenotype
 └─ Report
```

共通ヘッダを共有可能。

---

### Server Components

```text
Server
 ↓
Data Fetch
 ↓
HTML生成
 ↓
Client
```

高速。

---

### Streaming

```text
ページ全体完成を待たない

先に表示
 ↓
後から追記
```

大規模アプリ向き。

---

# StreamlitとPages Router

Streamlitは本質的には

```text
Single Page Application
```

です。

昔は

```text
app.py
```

のみ。

後に

```text
pages/
```

が追加されました。

例

```text
app.py

pages
├─ Risk.py
├─ Phenotype.py
└─ Report.py
```

左メニューで遷移します。

しかしこれは

```text
Next.js Pages Router
```

ほど高度なRouterではありません。

---

# StreamlitとApp Router

Streamlitには

```text
App Router相当
```

は存在しません。

不足する機能

```text
Nested Layout
Server Components
Parallel Routes
Streaming Routes
Intercepting Routes
```

---

# HealthBook-AIでの位置づけ

## 現在のStreamlit構成

```text
HealthBook-AI
│
├─ app.py
├─ pages
│   ├─ Disease Risk
│   ├─ Phenotype
│   ├─ MBT55
│   └─ Report
```

これは

```text
View中心設計
```

です。

---

## 将来推奨構成

```text
Frontend
 └─ Next.js App Router

Backend
 └─ FastAPI

AI
 └─ M3-Core-Engine

Data
 └─ PostgreSQL
```

```text
User
 ↓
App Router
 ↓
View
 ↓
API
 ↓
M3 Engine
 ↓
Database
```

---

# Repository Structure

```text
healthbook-platform
│
├─ frontend-nextjs
│   ├─ app
│   │   ├─ risk
│   │   ├─ phenotype
│   │   ├─ microbiome
│   │   └─ report
│   │
│   └─ components
│
├─ api-gateway
│
├─ m3-core-engine
│
└─ healthbook-data
```

---

# 意思決定

BioNexus 3 / HealthBook の商用展開を前提とする場合、

```text
PoC
 ↓
Streamlit

β版
 ↓
Streamlit + FastAPI

正式版
 ↓
Next.js App Router + FastAPI + M3-Core-Engine
```

が最も再現性が高い構成です。

**HealthBook-AIを今後もStreamlit中心で維持しますか、それとも Next.js App Router を前提とした正式プロダクト構成へ移行しますか？**

---

# 結論

**HealthBook と AGRIX/PBPE Marketplace の正式プロダクト構築であれば、App Router を採用すべきです。**

Pages Router は PoC・小規模運用向けです。

```text
PoC
 └─ Pages Router

Production
 └─ App Router
```

BioNexus 3 が目指している

- Disease Risk Engine
    
- Phenotype Engine
    
- Microbiome Engine
    
- Marketplace
    
- Multi-Tenant
    
- API Economy
    
- AI Agent
    

を考えると、Pages Routerでは将来的に構造的負債が発生します。

---

# Architecture

## HealthBook

HealthBookは実質的に

```text
HealthBook
├─ Dashboard
├─ Disease Risk
├─ Phenotype
├─ Nutrition
├─ Microbiome
├─ MBT55
├─ Recommendation
└─ Report
```

という「医療データポータル」です。

必要な機能

```text
認証
権限制御
データストリーミング
患者別URL
レポート生成
AI解析
```

これらは App Router が得意な領域です。

---

## AGRIX/PBPE Marketplace

Marketplaceはさらに App Router 向きです。

```text
AGRIX Marketplace
├─ Producer
├─ Product
├─ Batch
├─ PBPE Score
├─ Carbon Credit
├─ Buyer
├─ Transaction
└─ Traceability
```

---

# Data Flow

## Pages Router

```text
Browser
 ↓
Page
 ↓
API
 ↓
Database
```

単純。

---

## App Router

```text
Browser
 ↓
Route
 ↓
Server Component
 ↓
API
 ↓
M3 Core Engine
 ↓
Database
```

大規模化に対応。

---

# HealthBook適合性

## Pages Router

```text
◎ 開発容易

△ データ量増加

△ URL管理

△ 権限制御

△ 多言語
```

---

## App Router

```text
◎ Nested Layout

◎ Dynamic Route

◎ Multi Tenant

◎ AI連携

◎ Server Rendering

◎ SEO

◎ 将来拡張
```

---

# AGRIX Marketplace適合性

Marketplaceで重要なのは

```text
商品
 ↓
生産者
 ↓
ロット
 ↓
PBPE証明
 ↓
購入
```

です。

例えば

```text
/marketplace

/producer/[id]

/product/[id]

/batch/[id]

/carbon-credit/[id]
```

が必要になります。

これは App Router の設計思想と完全に一致します。

---

# 推奨構成

```text
BioNexus Platform
│
├─ Frontend
│   └─ Next.js App Router
│
├─ API Gateway
│   └─ FastAPI
│
├─ HealthBook Engine
│
├─ AGRIX Engine
│
├─ Marketplace Engine
│
├─ M3-Core-Engine
│
└─ PostgreSQL
```

---

# Repository Structure

```text
bionexus-platform
│
├─ apps
│   ├─ healthbook-web
│   ├─ agrix-web
│   └─ marketplace-web
│
├─ services
│   ├─ api-gateway
│   ├─ healthbook-service
│   ├─ agrix-service
│   └─ marketplace-service
│
├─ engines
│   └─ m3-core-engine
│
└─ docs
```

---

# Governance Rules

## Pages Router を選ぶ条件

```text
PoC
社内利用
利用者100人未満
短期運用
```

---

## App Router を選ぶ条件

```text
商用SaaS
Marketplace
API公開
AI Agent統合
Multi-Tenant
国際展開
```

HealthBook と AGRIX/PBPE Marketplace はいずれも後者に該当するため、**App Router を標準アーキテクチャとして固定するのが適切**です。

---

# KPI

|項目|目標|
|---|---|
|初回表示速度|< 1.5秒|
|API応答時間|< 300ms|
|同時接続数|10,000+|
|Marketplace取引処理成功率|> 99.9%|
|AIレポート生成時間|< 5秒|
|システム稼働率|> 99.95%|

**BioNexus Platform 全体の標準フロントエンドを「Next.js App Router」に固定しますか？**