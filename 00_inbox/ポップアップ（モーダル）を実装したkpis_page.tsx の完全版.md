承知しました。ポップアップ（モーダル）を実装した、`frontend/app/dashboard/kpis/page.tsx` の**完全版**を出力します。

---

## 📝 完全版：`frontend/app/dashboard/kpis/page.tsx`（ポップアップ対応）

```tsx
'use client'

import { useState, useEffect } from 'react'

export default function KPIsPage() {
  const [summary, setSummary] = useState<any>(null)
  const [loading, setLoading] = useState(true)
  const [mbtEnabled, setMbtEnabled] = useState(true)

  // ポップアップ（モーダル）用の状態
  const [modalData, setModalData] = useState<{ label: string; value: string; description: string } | null>(null)

  useEffect(() => {
    const params = new URLSearchParams(window.location.search)
    const mbtParam = params.get('mbt')
    if (mbtParam === 'on') setMbtEnabled(true)
    else if (mbtParam === 'off') setMbtEnabled(false)

    fetch('http://localhost:8000/dashboard/summary')
      .then(res => res.json())
      .then(data => {
        setSummary(data)
        setLoading(false)
      })
      .catch(() => {
        setLoading(false)
      })

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

  const d = isMbtOn ? summary : {
    ghg_reduction_tco2e_per_year: 150000000,
    units: 54850,
    pbpe_issued_per_year: 200000000,
    pbpe_price_usd: 5.0,
    pbpe_market_value_usd_per_year: 1000000000,
    green_premium_jpy_per_year: -5000000000000,
    roi_percent_per_year: 100,
    payback_months: 12,
    scope3_reduction_tco2e_per_year: 50000000,
    companies_onboarded: 30,
    countries: 5,
    scope3_reports_linked: 20
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
    { name: "Waste Avoidance", value: 50 },
    { name: "Food Loss", value: 30 },
    { name: "Soil Carbon", value: 20 },
    { name: "Fertilizer Reduction", value: 10 },
    { name: "Livestock Methane", value: 8 },
    { name: "Rice Methane", value: 5 },
    { name: "Biomass Increase", value: 4 },
  ]

  const creditsData = isMbtOn ? [
    { type: "Carbon", volume: 510, price: 10.00, value: 5100 },
    { type: "Biosecurity", volume: 30, price: 14.00, value: 420 },
    { type: "Food Loss", volume: 40, price: 9.00, value: 360 },
    { type: "Quality", volume: 40, price: 8.00, value: 320 },
  ] : [
    { type: "Carbon", volume: 150, price: 4.00, value: 600 },
    { type: "Biosecurity", volume: 8, price: 5.00, value: 40 },
    { type: "Food Loss", volume: 12, price: 3.50, value: 42 },
    { type: "Quality", volume: 10, price: 3.00, value: 30 },
  ]

  const flywheelSteps = isMbtOn ? [
    {
      label: "Investment",
      value: "¥2.74T",
      description: "MBT55導入・運用にかかる初期投資（設備・資材・人材）。\n\nこの投資により、生態系改善・生産性向上・PBPE発行の基盤が形成されます。"
    },
    {
      label: "Ecosystem Improvement",
      value: "Index 0.82",
      description: "土壌健康・生物多様性・水循環の統合改善指数（0-1）。\n\nMBT55の微生物活動が土壌を再生し、生態系全体を活性化します。"
    },
    {
      label: "Productivity",
      value: "+1.9x",
      description: "収量・品質・効率の総合生産性向上率（従来比）。\n\n収量+30〜50%、品質+1〜3点、廃棄物削減による効率化を実現。"
    },
    {
      label: "PBPE Issuance",
      value: "620M PBPE",
      description: "年間PBPE発行総量（Carbon/Soil/Water/Health合計）。\n\nGHG削減・土壌改善・水質向上・健康増進の価値を統合した指標です。"
    },
    {
      label: "Value Distribution",
      value: "40/40/20",
      description: "PBPE価値の分配：生産者40%／基金40%／プラットフォーム20%。\n\n持続可能な循環経済を実現する分配モデルです。"
    },
    {
      label: "Economic Return",
      value: "¥9.43T",
      description: "年間経済リターン（農家収益＋炭素クレジット＋保険効果）。\n\nROI 344%、投資回収期間3.5ヶ月という圧倒的な経済効率を実現。"
    },
    {
      label: "Reinvestment",
      value: "35%",
      description: "経済リターンの再投資率（次期MBT55導入・研究開発へ）。\n\n持続的成長を支える自己増殖型の経済循環モデルです。"
    },
  ] : [
    {
      label: "Investment",
      value: "¥1.0T",
      description: "従来型農業投資（推定値）。\n\nMBT55導入なしのベースライン投資額です。"
    },
    {
      label: "Ecosystem Improvement",
      value: "Index 0.30",
      description: "従来型農業の生態系改善指数（低水準）。\n\n化学肥料・農薬依存の限界を示しています。"
    },
    {
      label: "Productivity",
      value: "+0.5x",
      description: "従来型農業の生産性向上率（限定的）。\n\n収量向上は頭打ちで、品質改善も限られています。"
    },
    {
      label: "PBPE Issuance",
      value: "200M PBPE",
      description: "従来型農業でのPBPE発行量（ベースライン）。\n\nMBT55導入により2倍以上の発行が可能になります。"
    },
    {
      label: "Value Distribution",
      value: "40/40/20",
      description: "PBPE価値分配（従来も同じ構造）。\n\n分配構造自体は変わりませんが、価値の総量が異なります。"
    },
    {
      label: "Economic Return",
      value: "¥3.0T",
      description: "従来型農業の経済リターン（推定値）。\n\nMBT55導入時に比べて約3分の1のリターンです。"
    },
    {
      label: "Reinvestment",
      value: "15%",
      description: "従来型農業の再投資率（低い）。\n\n循環経済の循環が弱く、成長が鈍化します。"
    },
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
            {d.ghg_reduction_tco2e_per_year.toLocaleString()} tCO₂e
          </div>
          <div style={{ color: "#64748b" }}>Units: {d.units.toLocaleString()}</div>
        </div>
        <div style={cardStyle}>
          <div style={{ color: "#94a3b8" }}>PBPE Issued</div>
          <div style={{ fontSize: "28px", fontWeight: "bold", color: "#f1f5f9" }}>
            {d.pbpe_issued_per_year.toLocaleString()} PBPE
          </div>
          <div style={{ color: "#64748b" }}>Carbon / Soil / Water / Health</div>
        </div>
        <div style={cardStyle}>
          <div style={{ color: "#94a3b8" }}>PBPE Market Value</div>
          <div style={{ fontSize: "28px", fontWeight: "bold", color: "#f1f5f9" }}>
            ${(d.pbpe_market_value_usd_per_year / 1e9).toFixed(1)}B
          </div>
          <div style={{ color: "#64748b" }}>Price: ${d.pbpe_price_usd} / PBPE</div>
        </div>
        <div style={cardStyle}>
          <div style={{ color: "#94a3b8" }}>Green Premium</div>
          <div style={{ fontSize: "28px", fontWeight: "bold", color: isMbtOn ? "#22c55e" : "#64748b" }}>
            −¥{(Math.abs(d.green_premium_jpy_per_year) / 1e12).toFixed(1)}T
          </div>
          <div style={{ color: "#64748b" }}>{isMbtOn ? 'Negative (Profitable)' : 'Baseline'}</div>
        </div>
        <div style={cardStyle}>
          <div style={{ color: "#94a3b8" }}>ROI</div>
          <div style={{ fontSize: "28px", fontWeight: "bold", color: "#f1f5f9" }}>
            {d.roi_percent_per_year}%
          </div>
          <div style={{ color: "#64748b" }}>Payback: {d.payback_months} months</div>
        </div>
        <div style={cardStyle}>
          <div style={{ color: "#94a3b8" }}>Scope 3 Reduction</div>
          <div style={{ fontSize: "28px", fontWeight: "bold", color: "#f1f5f9" }}>
            {d.scope3_reduction_tco2e_per_year.toLocaleString()} tCO₂e
          </div>
          <div style={{ color: "#64748b" }}>Companies: {d.companies_onboarded}</div>
        </div>
      </div>

      {/* GHG Breakdown + Flywheel */}
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
                  width: isMbtOn ? `${(item.value / 180) * 100}%` : `${(item.value / 180) * 100}%`,
                  backgroundColor: isMbtOn ? "#22c55e" : "#64748b",
                  height: "100%",
                }} />
              </div>
            </div>
          ))}
        </div>

        {/* PBPE Value Flywheel - ポップアップ対応 */}
        <div style={cardStyle}>
          <h3 style={{ fontSize: "16px", fontWeight: "bold", marginBottom: "16px", color: "#f1f5f9" }}>
            PBPE Value Flywheel
          </h3>
          <div style={{ display: "flex", flexDirection: "column", gap: "8px" }}>
            {flywheelSteps.map((step, i) => (
              <div
                key={i}
                onClick={() => setModalData(step)}
                style={{
                  padding: "12px",
                  backgroundColor: "#1e293b",
                  border: "1px solid #334155",
                  borderRadius: "8px",
                  textAlign: "center",
                  color: isMbtOn ? "#94a3b8" : "#475569",
                  fontSize: "14px",
                  cursor: "pointer",
                  transition: "all 0.2s",
                }}
                onMouseEnter={(e) => {
                  e.currentTarget.style.backgroundColor = "#334155"
                  e.currentTarget.style.color = "#f1f5f9"
                }}
                onMouseLeave={(e) => {
                  e.currentTarget.style.backgroundColor = "#1e293b"
                  e.currentTarget.style.color = isMbtOn ? "#94a3b8" : "#475569"
                }}
              >
                {step.label} <span style={{ color: "#22c55e", fontWeight: "bold" }}>{step.value}</span>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Credits Table + Enterprise Usage */}
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
              <div style={{ fontSize: "28px", fontWeight: "bold", color: "#f1f5f9" }}>{d.companies_onboarded}</div>
              <div style={{ color: "#94a3b8", fontSize: "12px" }}>Companies</div>
            </div>
            <div style={{ textAlign: "center", padding: "12px", backgroundColor: "#1e293b", borderRadius: "8px", border: "1px solid #334155" }}>
              <div style={{ fontSize: "28px", fontWeight: "bold", color: "#f1f5f9" }}>{d.countries}</div>
              <div style={{ color: "#94a3b8", fontSize: "12px" }}>Countries</div>
            </div>
            <div style={{ textAlign: "center", padding: "12px", backgroundColor: "#1e293b", borderRadius: "8px", border: "1px solid #334155", gridColumn: "span 2" }}>
              <div style={{ fontSize: "28px", fontWeight: "bold", color: "#f1f5f9" }}>{d.scope3_reports_linked}</div>
              <div style={{ color: "#94a3b8", fontSize: "12px" }}>Scope 3 Reports Linked</div>
            </div>
          </div>
        </div>
      </div>

      {/* モーダル（ポップアップ） */}
      {modalData && (
        <div
          onClick={() => setModalData(null)}
          style={{
            position: "fixed",
            top: 0,
            left: 0,
            width: "100%",
            height: "100%",
            backgroundColor: "rgba(0,0,0,0.7)",
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            zIndex: 1000,
          }}
        >
          <div
            onClick={(e) => e.stopPropagation()}
            style={{
              backgroundColor: "#1e293b",
              border: "1px solid #334155",
              borderRadius: "16px",
              padding: "32px",
              maxWidth: "480px",
              width: "90%",
              boxShadow: "0 20px 60px rgba(0,0,0,0.8)",
              position: "relative",
            }}
          >
            <button
              onClick={() => setModalData(null)}
              style={{
                position: "absolute",
                top: "12px",
                right: "16px",
                background: "none",
                border: "none",
                color: "#94a3b8",
                fontSize: "24px",
                cursor: "pointer",
              }}
            >
              ✕
            </button>
            <div style={{ fontSize: "20px", fontWeight: "bold", color: "#f1f5f9", marginBottom: "8px" }}>
              {modalData.label}
            </div>
            <div style={{ fontSize: "16px", color: "#22c55e", fontWeight: "bold", marginBottom: "16px" }}>
              {modalData.value}
            </div>
            <div style={{ color: "#94a3b8", fontSize: "14px", lineHeight: "1.7", whiteSpace: "pre-line" }}>
              {modalData.description}
            </div>
          </div>
        </div>
      )}
    </div>
  )
}
```

---

## 🔑 このコードのポイント

| 機能 | 説明 |
|---|---|
| ポップアップ（モーダル） | Flywheelの各項目をクリックすると、詳細説明が表示される |
| オーバーレイ | 背景が暗くなり、モーダルに集中できる |
| 閉じるボタン（✕） | モーダルを閉じる |
| クリックで閉じる | モーダル外をクリックしても閉じる |
| ON/OFF連動 | Flywheelの内容もMBT ON/OFFで切り替わる |

---

## 🚀 手順

1. **このコードで `frontend/app/dashboard/kpis/page.tsx` を完全に上書き**
2. **保存（Ctrl+S）**
3. **ブラウザをリロード（Ctrl+Shift+R）**
4. **Flywheelの各項目をクリックしてポップアップが表示されるか確認**

---

**Kazさん、このコードで上書きしてください。完了したら「完了」と教えてください。**