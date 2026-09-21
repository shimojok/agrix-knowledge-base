Kazさん、このエラーは、`layout.tsx` のトグル部分を修正した際に、`window` オブジェクトの参照が原因で発生しています。Server Component では `window` が使えないため、`useEffect` を使用して Client サイドでのみ実行するように修正する必要があります。

---

## ✅ 修正版 `frontend/app/layout.tsx`（全文）

以下のコードで `frontend/app/layout.tsx` を**完全に上書き**してください：

```tsx
// frontend/app/layout.tsx
'use client'

import './globals.css'
import { useState, useEffect } from 'react'

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  // URLパラメータから初期状態を読み取る
  const [mbtEnabled, setMbtEnabled] = useState(true)

  useEffect(() => {
    // クライアントサイドでのみ実行
    if (typeof window !== 'undefined') {
      const params = new URLSearchParams(window.location.search)
      const mbtParam = params.get('mbt')
      if (mbtParam === 'on') setMbtEnabled(true)
      else if (mbtParam === 'off') setMbtEnabled(false)
    }
  }, [])

  const toggleMBT = () => {
    const newState = !mbtEnabled
    setMbtEnabled(newState)
    // URLを更新
    if (typeof window !== 'undefined') {
      const url = new URL(window.location.href)
      url.searchParams.set('mbt', newState ? 'on' : 'off')
      window.history.pushState({}, '', url.toString())
    }
  }

  const navItems = [
    { href: '/dashboard/kpis', label: 'Global KPIs' },
    { href: '/dashboard/impact', label: 'Impact Breakdown' },
    { href: '/dashboard/market', label: 'PBPE Credits Market' },
    { href: '/dashboard/finance', label: 'Bonds & Insurance' },
    { href: '/dashboard/enterprise', label: 'Scope 3 × PBPE' },
    { href: '/dashboard/pbpe', label: 'PBPE Issuance' },
  ]

  return (
    <html lang="en" className="dark">
      <body style={{
        backgroundColor: '#0f172a',
        color: '#f1f5f9',
        margin: 0,
        padding: 0,
        fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif',
        minHeight: '100vh',
      }}>
        <div style={{ display: 'flex', minHeight: '100vh' }}>
          {/* サイドバー */}
          <aside style={{
            width: '260px',
            backgroundColor: '#020617',
            borderRight: '1px solid #334155',
            padding: '24px 16px',
            display: 'flex',
            flexDirection: 'column',
            justifyContent: 'space-between',
            flexShrink: 0,
          }}>
            <div>
              <div style={{ fontSize: '20px', fontWeight: 'bold', marginBottom: '32px', color: '#f1f5f9' }}>
                🌍 PBPE Marketplace
              </div>
              <nav>
                {navItems.map((item) => (
                  <a
                    key={item.href}
                    href={item.href}
                    style={{
                      display: 'block',
                      padding: '10px 12px',
                      marginBottom: '4px',
                      borderRadius: '8px',
                      color: '#94a3b8',
                      textDecoration: 'none',
                      fontSize: '14px',
                      transition: 'all 0.2s',
                    }}
                    onMouseEnter={(e) => {
                      e.currentTarget.style.backgroundColor = '#1e293b'
                      e.currentTarget.style.color = '#f1f5f9'
                    }}
                    onMouseLeave={(e) => {
                      e.currentTarget.style.backgroundColor = 'transparent'
                      e.currentTarget.style.color = '#94a3b8'
                    }}
                  >
                    {item.label}
                  </a>
                ))}
              </nav>
            </div>

            {/* MBT55 Toggle */}
            <div style={{
              padding: '16px',
              backgroundColor: '#1e293b',
              borderRadius: '12px',
              border: '1px solid #334155',
            }}>
              <div style={{ fontSize: '12px', color: '#94a3b8', marginBottom: '12px' }}>
                MBT55 Microbial System
              </div>
              <button
                onClick={toggleMBT}
                style={{
                  width: '100%',
                  padding: '10px',
                  borderRadius: '8px',
                  border: 'none',
                  fontWeight: 'bold',
                  cursor: 'pointer',
                  backgroundColor: mbtEnabled ? '#22c55e' : '#475569',
                  color: 'white',
                  transition: 'all 0.2s',
                }}
              >
                {mbtEnabled ? '🟢 ON' : '⚫ OFF'}
              </button>
              <div style={{ fontSize: '10px', color: '#94a3b8', marginTop: '8px', textAlign: 'center' }}>
                {mbtEnabled ? 'Climate-positive mode active' : 'Conventional farming baseline'}
              </div>
            </div>
          </aside>

          {/* メインコンテンツ */}
          <main style={{ flex: 1, padding: '24px', overflow: 'auto', backgroundColor: '#0f172a' }}>
            {children}
          </main>
        </div>
      </body>
    </html>
  )
}
```

---

## 🔑 修正ポイント

| 修正内容 | 説明 |
|---|---|
| `'use client'` を追加 | Client Component としてマーク |
| `useEffect` で `window` をチェック | サーバーサイドでのエラーを防止 |
| `typeof window !== 'undefined'` でガード | クライアントサイドでのみ実行 |

---

## 🚀 修正後の手順

1. **`layout.tsx` を上記コードで上書き保存**
2. **フロントエンドを再起動**（`Ctrl+C` → `npm run dev`）
3. **ブラウザをリロード**（`Ctrl + Shift + R`）

---

**Kazさん、このコードで `layout.tsx` を上書きしてください。完了したら「完了」と教えてください。**


Kazさん、申し訳ありません。私のコードにタイプエラー（構文エラー）があった可能性があります。

---

## ✅ 修正版：`frontend/app/dashboard/kpis/page.tsx`

以下のコードで再度上書きしてください（タイプエラーを修正済み）：

```tsx
// frontend/app/dashboard/kpis/page.tsx
'use client'

import { useState, useEffect } from 'react'

export default function KPIsPage() {
  const [summary, setSummary] = useState<any>(null)
  const [loading, setLoading] = useState(true)
  const [mbtEnabled, setMbtEnabled] = useState(true)

  useEffect(() => {
    // URLパラメータからmbt状態を取得
    const params = new URLSearchParams(window.location.search)
    const mbtParam = params.get('mbt')
    if (mbtParam === 'on') setMbtEnabled(true)
    else if (mbtParam === 'off') setMbtEnabled(false)

    // データ取得
    fetch('http://localhost:8000/dashboard/summary')
      .then(res => {
        if (!res.ok) throw new Error('API error')
        return res.json()
      })
      .then(data => {
        setSummary(data)
        setLoading(false)
      })
      .catch(err => {
        console.error('Fetch error:', err)
        setLoading(false)
      })

    // URL変更を監視
    const handlePopState = () => {
      const p = new URLSearchParams(window.location.search)
      const m = p.get('mbt')
      if (m === 'on') setMbtEnabled(true)
      else if (m === 'off') setMbtEnabled(false)
    }
    window.addEventListener('popstate', handlePopState)
    return () => window.removeEventListener('popstate', handlePopState)
  }, [])

  if (loading) {
    return <div style={{ color: '#f1f5f9', padding: '24px' }}>Loading...</div>
  }
  if (!summary) {
    return <div style={{ color: '#f1f5f9', padding: '24px' }}>No data available</div>
  }

  const isMbtOn = mbtEnabled

  const displayData = isMbtOn ? {
    ghg_reduction: summary.ghg_reduction_tco2e_per_year,
    units: summary.units,
    pbpe_issued: summary.pbpe_issued_per_year,
    pbpe_price: summary.pbpe_price_usd,
    pbpe_market_value: summary.pbpe_market_value_usd_per_year,
    green_premium: summary.green_premium_jpy_per_year,
    roi: summary.roi_percent_per_year,
    payback: summary.payback_months,
    scope3_reduction: summary.scope3_reduction_tco2e_per_year,
    companies: summary.companies_onboarded,
    countries: summary.countries,
    scope3_reports: summary.scope3_reports_linked
  } : {
    ghg_reduction: 0,
    units: 0,
    pbpe_issued: 0,
    pbpe_price: 0,
    pbpe_market_value: 0,
    green_premium: 0,
    roi: 0,
    payback: 0,
    scope3_reduction: 0,
    companies: 0,
    countries: 0,
    scope3_reports: 0
  }

  const cardStyle = {
    backgroundColor: '#1e293b',
    border: '1px solid #334155',
    borderRadius: '12px',
    padding: '16px',
    boxShadow: '0 1px 3px rgba(0,0,0,0.5)',
  }

  const ghgSources = isMbtOn ? [
    { name: "Waste Avoidance", value: 180 },
    { name: "Food Loss", value: 110 },
    { name: "Soil Carbon", value: 70 },
    { name: "Fertilizer Reduction", value: 40 },
    { name: "Livestock Methane", value: 30 },
    { name: "Rice Methane", value: 20 },
    { name: "Biomass Increase", value: 15 },
  ] : [
    { name: "Waste Avoidance", value: 0 },
    { name: "Food Loss", value: 0 },
    { name: "Soil Carbon", value: 0 },
    { name: "Fertilizer Reduction", value: 0 },
    { name: "Livestock Methane", value: 0 },
    { name: "Rice Methane", value: 0 },
    { name: "Biomass Increase", value: 0 },
  ]

  const flywheelSteps = [
    "Investment",
    "Ecosystem Improvement",
    "Productivity",
    "PBPE Issuance",
    "Value Distribution",
    "Economic Return",
    "Reinvestment"
  ]

  const creditsData = isMbtOn ? [
    { type: "Carbon", volume: 510, price: 10.00, value: 5100 },
    { type: "Biosecurity", volume: 30, price: 14.00, value: 420 },
    { type: "Food Loss", volume: 40, price: 9.00, value: 360 },
    { type: "Quality", volume: 40, price: 8.00, value: 320 },
  ] : [
    { type: "Carbon", volume: 0, price: 0, value: 0 },
    { type: "Biosecurity", volume: 0, price: 0, value: 0 },
    { type: "Food Loss", volume: 0, price: 0, value: 0 },
    { type: "Quality", volume: 0, price: 0, value: 0 },
  ]

  return (
    <div style={{ padding: "0" }}>
      <h1 style={{ fontSize: "24px", fontWeight: "bold", marginBottom: "8px", color: "#f1f5f9" }}>
        Global KPIs {isMbtOn ? '(MBT ON)' : '(MBT OFF)'}
      </h1>
      <p style={{ color: "#94a3b8", marginBottom: "24px" }}>
        Planetary balance sheet — GHG, Soil, Water, Health, Stability, PBPE
      </p>

      {/* 6 KPI Cards */}
      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))',
        gap: '16px',
        marginBottom: '24px',
      }}>
        <div style={cardStyle}>
          <div style={{ color: "#94a3b8" }}>GHG Reduction</div>
          <div style={{ fontSize: "28px", fontWeight: "bold", color: "#f1f5f9" }}>
            {displayData.ghg_reduction.toLocaleString()} tCO₂e
          </div>
          <div style={{ color: "#64748b" }}>Units: {displayData.units.toLocaleString()}</div>
        </div>
        <div style={cardStyle}>
          <div style={{ color: "#94a3b8" }}>PBPE Issued</div>
          <div style={{ fontSize: "28px", fontWeight: "bold", color: "#f1f5f9" }}>
            {displayData.pbpe_issued.toLocaleString()} PBPE
          </div>
          <div style={{ color: "#64748b" }}>Carbon / Soil / Water / Health</div>
        </div>
        <div style={cardStyle}>
          <div style={{ color: "#94a3b8" }}>PBPE Market Value</div>
          <div style={{ fontSize: "28px", fontWeight: "bold", color: "#f1f5f9" }}>
            ${(displayData.pbpe_market_value / 1e9).toFixed(1)}B
          </div>
          <div style={{ color: "#64748b" }}>Price: ${displayData.pbpe_price} / PBPE</div>
        </div>
        <div style={cardStyle}>
          <div style={{ color: "#94a3b8" }}>Green Premium</div>
          <div style={{ fontSize: "28px", fontWeight: "bold", color: isMbtOn ? "#22c55e" : "#475569" }}>
            −¥{(Math.abs(displayData.green_premium) / 1e12).toFixed(1)}T
          </div>
          <div style={{ color: "#64748b" }}>{isMbtOn ? 'Negative (Profitable)' : 'No impact'}</div>
        </div>
        <div style={cardStyle}>
          <div style={{ color: "#94a3b8" }}>ROI</div>
          <div style={{ fontSize: "28px", fontWeight: "bold", color: "#f1f5f9" }}>
            {displayData.roi}%
          </div>
          <div style={{ color: "#64748b" }}>Payback: {displayData.payback} months</div>
        </div>
        <div style={cardStyle}>
          <div style={{ color: "#94a3b8" }}>Scope 3 Reduction</div>
          <div style={{ fontSize: "28px", fontWeight: "bold", color: "#f1f5f9" }}>
            {displayData.scope3_reduction.toLocaleString()} tCO₂e
          </div>
          <div style={{ color: "#64748b" }}>Companies: {displayData.companies}</div>
        </div>
      </div>

      {/* Middle Section: GHG Breakdown + Flywheel */}
      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(380px, 1fr))',
        gap: '24px',
        marginBottom: '24px',
      }}>
        <div style={cardStyle}>
          <h3 style={{ fontSize: "16px", fontWeight: "bold", marginBottom: "16px", color: "#f1f5f9" }}>
            GHG Reduction by Source
          </h3>
          {ghgSources.map((item, i) => (
            <div key={i} style={{ marginBottom: "12px" }}>
              <div style={{ display: "flex", justifyContent: "space-between", color: "#94a3b8", fontSize: "13px", marginBottom: "4px" }}>
                <span>{item.name}</span>
                <span>{item.value} MtCO₂e</span>
              </div>
              <div style={{ backgroundColor: "#334155", borderRadius: "8px", height: "8px", overflow: "hidden" }}>
                <div style={{
                  width: isMbtOn ? `${(item.value / 180) * 100}%` : '0%',
                  backgroundColor: isMbtOn ? "#22c55e" : "#475569",
                  height: "100%",
                }} />
              </div>
            </div>
          ))}
        </div>

        <div style={cardStyle}>
          <h3 style={{ fontSize: "16px", fontWeight: "bold", marginBottom: "16px", color: "#f1f5f9" }}>
            PBPE Value Flywheel
          </h3>
          <div style={{ display: "flex", flexDirection: "column", gap: "8px" }}>
            {flywheelSteps.map((step, i) => (
              <div key={i} style={{
                padding: "12px",
                backgroundColor: "#1e293b",
                border: "1px solid #334155",
                borderRadius: "8px",
                textAlign: "center",
                color: isMbtOn ? "#94a3b8" : "#475569",
                fontSize: "14px",
              }}>
                {step}
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Bottom Section: Credits Table + Enterprise Usage */}
      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(380px, 1fr))',
        gap: '24px',
      }}>
        <div style={cardStyle}>
          <h3 style={{ fontSize: "16px", fontWeight: "bold", marginBottom: "16px", color: "#f1f5f9" }}>
            PBPE Credits Market
          </h3>
          <table style={{ width: "100%", borderCollapse: "collapse" }}>
            <thead>
              <tr style={{ borderBottom: "1px solid #334155" }}>
                <th style={{ textAlign: "left", padding: "8px", color: "#94a3b8" }}>Type</th>
                <th style={{ textAlign: "right", padding: "8px", color: "#94a3b8" }}>Volume</th>
                <th style={{ textAlign: "right", padding: "8px", color: "#94a3b8" }}>Price</th>
                <th style={{ textAlign: "right", padding: "8px", color: "#94a3b8" }}>Value</th>
              </tr>
            </thead>
            <tbody>
              {creditsData.map((item, i) => (
                <tr key={i} style={{ borderBottom: "1px solid #334155" }}>
                  <td style={{ padding: "8px", fontWeight: 500, color: "#f1f5f9" }}>{item.type}</td>
                  <td style={{ textAlign: "right", padding: "8px", color: "#94a3b8" }}>{item.volume}M</td>
                  <td style={{ textAlign: "right", padding: "8px", color: "#94a3b8" }}>${item.price.toFixed(2)}</td>
                  <td style={{ textAlign: "right", padding: "8px", color: "#94a3b8" }}>${item.value}M</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        <div style={cardStyle}>
          <h3 style={{ fontSize: "16px", fontWeight: "bold", marginBottom: "16px", color: "#f1f5f9" }}>
            Enterprise Usage
          </h3>
          <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "16px" }}>
            <div style={{ textAlign: "center", padding: "12px", backgroundColor: "#1e293b", borderRadius: "8px", border: "1px solid #334155" }}>
              <div style={{ fontSize: "28px", fontWeight: "bold", color: "#f1f5f9" }}>{displayData.companies}</div>
              <div style={{ color: "#94a3b8", fontSize: "12px" }}>Companies</div>
            </div>
            <div style={{ textAlign: "center", padding: "12px", backgroundColor: "#1e293b", borderRadius: "8px", border: "1px solid #334155" }}>
              <div style={{ fontSize: "28px", fontWeight: "bold", color: "#f1f5f9" }}>{displayData.countries}</div>
              <div style={{ color: "#94a3b8", fontSize: "12px" }}>Countries</div>
            </div>
            <div style={{ textAlign: "center", padding: "12px", backgroundColor: "#1e293b", borderRadius: "8px", border: "1px solid #334155", gridColumn: "span 2" }}>
              <div style={{ fontSize: "28px", fontWeight: "bold", color: "#f1f5f9" }}>{displayData.scope3_reports}</div>
              <div style={{ color: "#94a3b8", fontSize: "12px" }}>Scope 3 Reports Linked</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
```

---

## 🚀 手順

1. **上記コードで `frontend/app/dashboard/kpis/page.tsx` を上書き**
2. **保存**（`Ctrl + S`）
3. **フロントエンド再起動**（`Ctrl+C` → `npm run dev`）
4. **ブラウザをリロード**（`Ctrl + Shift + R`）

---

**Kazさん、このコードで再度試してください。完了したら「完了」と教えてください。**