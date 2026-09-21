![[agrix_architecture_dashboard.html]]進めてください。

---

ファイルとして作成します。## AGRIX Platform Architecture Dashboard 完成

---

### 構成サマリー

**ダッシュボードの設計思想**

「本格的なシステム構築ではなく、アーキテクチャの提示で納得させる」という方針に沿い、Bill Gates氏・Microsoft向けの**事業譲渡ピッチ用**に特化した設計としました。深海バイオルミネッセンスの暗色基調、`Fraunces`（表示）+`JetBrains Mono`（データ）という組み合わせで精密計器的な美学を実現しています。

**7つのパネル**

|パネル|内容|ソース|
|---|---|---|
|**M³同心円リング**|Microbial/Metabolic/Modularの3層がSHEスコアに連動して脈動|署名要素|
|**KPI 4指標**|SHE™ Score / GHG Flux / V-Score / P_total がシミュレーション連動|soil_dynamics + vitality_engine|
|**GHG削減チャート**|MBT55 vs 慣行農業、12ヶ月推移|IPCC Tier 2準拠|
|**SHE™スコア軌跡**|42→80への土壌再生プロセスを可視化|agriware_engine|
|**P_total積み上げバー**|5層価値分解（$2.80→$3.52、+8%）|SafelyChain™定義|
|**V-Score崩壊カーブ**|ATP代謝寿命の比較（MBT55 vs 慣行）|vitality_engine|
|**Multi-Agent AI**|Microbe→Cascade→Inertia→Health の4エージェントフロー + Gem7 JSONスキーマ|Gem4/Gem7|
|**5-Layer Architecture**|Physical→Digital→Trust→Value→Health|統合アーキテクチャ|

### 次のアクション候補

**E.** PBPE Marketplace の `FastAPI` バックエンド（`/api/v1/prescribe` + `/api/v1/pbpe/mint`）— BioNexus-Core の `04_pbpe-finance` ドキュメントから設計  
**F.** HealthBook™ との接続部 — `MBT Probiotics スクリーニング` の `disease_matrix_137.json` スキーマ設計  
**G.** GitHub Actions による自動デプロイ設定（`shimojok/AGRIX-OS` リポジトリへのプッシュ）  
**H.** 投資家・Microsoft向け **英語ホワイトペーパー PDF**（BioNexus-Core `04_pbpe-finance/HAT-3. White Paper: The AGRIX Protocol.md` ベース）

---

[AGRIX Platform OS — Architecture Dashboard](file:///C:/Users/user/Downloads/agrix_architecture_dashboard.html)

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>AGRIX Platform OS — Architecture Dashboard</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;1,9..144,400&family=JetBrains+Mono:wght@300;400;500&family=Outfit:wght@300;400;500&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box;margin:0;padding:0}
:root{
  --bg:#060B14;--surf:#0C1521;--elev:#111E2E;--bord:#1A3050;--mut:#243C58;
  --dim:#3A5A7A;--txt:#7AAFC8;--hi:#C2DCF0;--wh:#EAF4FF;
  --m3:#00D4A0;--agri:#2E9CFF;--safe:#F5C542;--pbpe:#A855F7;
  --hlth:#FF6B9D;--carb:#34D058;--warn:#FF7043;
}
body{background:var(--bg);color:var(--txt);font-family:'Outfit',sans-serif;font-size:13px;
     min-height:100vh;
     background-image:radial-gradient(ellipse at 15% 15%,#00D4A008 0%,transparent 55%),
                       radial-gradient(ellipse at 85% 85%,#A855F708 0%,transparent 55%)}
.mono{font-family:'JetBrains Mono',monospace}
.display{font-family:'Fraunces',serif}
.lbl{font-family:'JetBrains Mono',monospace;font-size:8px;letter-spacing:.18em;
     text-transform:uppercase;color:var(--dim);margin-bottom:8px}
.card{background:var(--surf);border:1px solid var(--bord);border-radius:12px;padding:16px 18px}
/* KPI chips */
.chip{background:var(--elev);border:1px solid var(--bord);border-radius:8px;padding:8px 12px;flex:1}
.chip .cv{font-family:'JetBrains Mono',monospace;font-size:19px;font-weight:500;line-height:1}
.chip .cl{font-family:'JetBrains Mono',monospace;font-size:7px;letter-spacing:.14em;
          text-transform:uppercase;color:var(--dim);margin-bottom:2px}
.chip .cs{font-family:'JetBrains Mono',monospace;font-size:7px;color:var(--dim);margin-top:3px}
/* dot */
.dot{width:7px;height:7px;border-radius:50%;display:inline-block;margin-right:4px;vertical-align:middle}
/* platform pills */
.plat{background:var(--surf);border:1px solid var(--bord);border-radius:8px;
      padding:10px 12px;border-left:3px solid var(--pc,#3A5A7A);margin-bottom:8px}
.plat .pn{font-family:'JetBrains Mono',monospace;font-size:10px;font-weight:600;letter-spacing:.08em}
.plat .pd{font-size:11px;color:var(--hi);line-height:1.5;margin:4px 0}
.plat .pk{font-family:'JetBrains Mono',monospace;font-size:8px;color:var(--dim);line-height:1.7}
/* agent cards */
.agent{background:var(--elev);border:1px solid var(--bord);border-radius:8px;
       padding:10px 12px;cursor:pointer;transition:all .2s}
.agent:hover,.agent.act{border-color:var(--ac,#2E9CFF);
  background:color-mix(in srgb,var(--ac,#2E9CFF) 8%,var(--elev))}
.agent .ai{font-size:16px;margin-bottom:3px}
.agent .an{font-family:'JetBrains Mono',monospace;font-size:8px;font-weight:600;letter-spacing:.08em}
.agent .ar{font-size:10px;color:var(--txt);margin-bottom:4px}
.iorow{display:grid;grid-template-columns:1fr 1fr;gap:4px;margin-top:6px;
       font-family:'JetBrains Mono',monospace;font-size:8px;line-height:1.6}
.iol{font-size:7px;letter-spacing:.1em;text-transform:uppercase;color:var(--dim);margin-bottom:2px}
/* flow boxes */
.flowrow{display:flex;align-items:center;gap:6px;overflow-x:auto;padding-bottom:4px;margin-bottom:10px;flex-wrap:wrap}
.fbox{background:var(--elev);border:1px solid var(--bord);border-radius:6px;
      padding:5px 10px;text-align:center;min-width:66px;cursor:pointer;
      transition:all .2s;flex-shrink:0}
.fbox:hover,.fbox.act{box-shadow:0 0 10px color-mix(in srgb,var(--ac,#2E9CFF) 40%,transparent);
  border-color:var(--ac,#2E9CFF)}
.farr{color:var(--mut);flex-shrink:0;font-size:12px}
/* P_total bar */
.bar-wrap{display:flex;height:26px;border-radius:5px;overflow:hidden;gap:1px}
.bseg{display:flex;align-items:center;justify-content:center;
      font-family:'JetBrains Mono',monospace;font-size:8px;
      color:#060B14;font-weight:600;overflow:hidden;white-space:nowrap;
      transition:flex .6s ease}
/* 5-layer */
.layer{border-radius:8px;padding:10px 12px;background:var(--elev);
       border-top:3px solid var(--lc,#3A5A7A)}
.layer .ln{font-family:'JetBrains Mono',monospace;font-size:7px;letter-spacing:.1em;margin-bottom:3px}
.layer .lt{font-family:'Fraunces',serif;font-size:11px;font-style:italic;color:var(--hi);margin-bottom:6px}
.layer .li{font-family:'JetBrains Mono',monospace;font-size:7px;color:var(--dim);line-height:1.6}
/* toggle btn */
#simBtn{background:none;border:1px solid var(--bord);border-radius:5px;
        color:var(--txt);font-family:'JetBrains Mono',monospace;
        font-size:8px;padding:3px 10px;cursor:pointer;letter-spacing:.1em}
#simBtn:hover{border-color:var(--m3);color:var(--m3)}
/* legend item */
.legitem{display:flex;align-items:center;gap:4px;font-family:'JetBrains Mono',monospace;font-size:8px}
.legsq{width:10px;height:10px;border-radius:2px;flex-shrink:0}
</style>
</head>
<body>
<div style="padding:16px 20px;max-width:1400px;margin:0 auto">

<!-- Header -->
<div style="display:flex;align-items:center;gap:14px;margin-bottom:14px;
            padding-bottom:12px;border-bottom:1px solid var(--bord)">
  <div>
    <div style="display:flex;align-items:baseline;gap:12px">
      <span class="display" style="font-size:26px;color:var(--wh)">AGRIX</span>
      <span class="mono" style="font-size:9px;color:var(--m3);letter-spacing:.2em">PLATFORM OS</span>
    </div>
    <div class="mono" style="font-size:9px;color:var(--dim);margin-top:2px">
      M³-BioSynergy · AgriWare™ · SafelyChain™ · PBPE Marketplace · HealthBook™
    </div>
  </div>
  <div style="margin-left:auto;display:flex;align-items:center;gap:10px">
    <span id="liveDot" class="dot" style="background:var(--m3);box-shadow:0 0 7px var(--m3)"></span>
    <span class="mono" style="font-size:9px;color:var(--dim)">LIVE SIM · <span id="monthLbl">Jan</span></span>
    <button id="simBtn" onclick="toggleSim()">PAUSE</button>
  </div>
</div>

<!-- Main 2-col grid -->
<div style="display:grid;grid-template-columns:210px 1fr;gap:14px">

<!-- ── LEFT ── -->
<div>
  <!-- M³ Ring -->
  <div class="card" style="margin-bottom:12px;text-align:center">
    <div class="lbl" style="color:var(--m3)">M³-BioSynergy Core</div>
    <svg viewBox="0 0 160 155" width="160" height="155" style="display:block;margin:0 auto">
      <!-- Background rings -->
      <circle cx="80" cy="85" r="65" fill="none" stroke="#A855F722" stroke-width="9"/>
      <circle cx="80" cy="85" r="48" fill="none" stroke="#2E9CFF22" stroke-width="9"/>
      <circle cx="80" cy="85" r="30" fill="none" stroke="#00D4A022" stroke-width="9"/>
      <!-- Progress rings -->
      <circle id="ringMod" cx="80" cy="85" r="65" fill="none" stroke="var(--pbpe)" stroke-width="9"
        stroke-dasharray="40 368" stroke-linecap="round" transform="rotate(-90 80 85)"
        style="transition:stroke-dasharray 1.1s cubic-bezier(.4,0,.2,1)"/>
      <circle id="ringMet" cx="80" cy="85" r="48" fill="none" stroke="var(--agri)" stroke-width="9"
        stroke-dasharray="30 271" stroke-linecap="round" transform="rotate(-90 80 85)"
        style="transition:stroke-dasharray 1.1s cubic-bezier(.4,0,.2,1)"/>
      <circle id="ringMic" cx="80" cy="85" r="30" fill="none" stroke="var(--m3)" stroke-width="9"
        stroke-dasharray="18 170" stroke-linecap="round" transform="rotate(-90 80 85)"
        style="transition:stroke-dasharray 1.1s cubic-bezier(.4,0,.2,1)"/>
      <!-- Centre -->
      <text id="sheNum" x="80" y="80" text-anchor="middle"
        font-family="JetBrains Mono,monospace" font-size="22" font-weight="700" fill="#00D4A0">42</text>
      <text x="80" y="96" text-anchor="middle"
        font-family="JetBrains Mono,monospace" font-size="7" fill="#3A5A7A" letter-spacing=".1em">SHE™ SCORE</text>
    </svg>
    <!-- Ring legend -->
    <div style="display:flex;justify-content:center;gap:10px;margin-top:4px">
      <div><span class="dot" style="background:var(--m3)"></span><span class="mono" style="font-size:7px;color:var(--m3)">Microbial</span></div>
      <div><span class="dot" style="background:var(--agri)"></span><span class="mono" style="font-size:7px;color:var(--agri)">Metabolic</span></div>
      <div><span class="dot" style="background:var(--pbpe)"></span><span class="mono" style="font-size:7px;color:var(--pbpe)">Modular</span></div>
    </div>
  </div>

  <!-- Platform stack -->
  <div class="lbl">Platform Components</div>
  <div class="plat" style="--pc:var(--agri)">
    <div class="pn" style="color:var(--agri)">⚙ AgriWare™</div>
    <div class="pd">Soil OS — diagnose → prescribe → control</div>
    <div class="pk">5-phase EcoPhenotype · MBT55 24h clock · ODE</div>
  </div>
  <div class="plat" style="--pc:var(--safe)">
    <div class="pn" style="color:var(--safe)">🔗 SafelyChain™</div>
    <div class="pd">Post-traceability · metabolic proof of quality</div>
    <div class="pk">V-Score · P_total · Blockchain · SCFA</div>
  </div>
  <div class="plat" style="--pc:var(--pbpe)">
    <div class="pn" style="color:var(--pbpe)">💹 PBPE Marketplace</div>
    <div class="pd">Carbon × food × health → tokenised impact</div>
    <div class="pk">1 PBPE = 10 kg CO₂e · ESG bond / token</div>
  </div>
  <div class="plat" style="--pc:var(--hlth)">
    <div class="pn" style="color:var(--hlth)">🧬 HealthBook™</div>
    <div class="pd">MBT Probiotics × metabolomics</div>
    <div class="pk">137 disease matrix · 294 TCM · m-ROI</div>
  </div>
</div>

<!-- ── RIGHT ── -->
<div style="display:flex;flex-direction:column;gap:12px">

  <!-- KPIs -->
  <div style="display:flex;gap:8px">
    <div class="chip">
      <div class="cl">SHE™ Score</div>
      <div class="cv" id="kShe" style="color:var(--m3)">42</div>
      <div class="cs" id="kSheSub">+0pts since Jan</div>
    </div>
    <div class="chip">
      <div class="cl">GHG Flux</div>
      <div class="cv" id="kGhg" style="color:var(--carb)">8.2</div>
      <div class="cs" id="kGhgSub">g CO₂/m²/day</div>
    </div>
    <div class="chip">
      <div class="cl">V-Score</div>
      <div class="cv" id="kVs" style="color:var(--safe)">100.0</div>
      <div class="cs">ATP metabolic vitality</div>
    </div>
    <div class="chip">
      <div class="cl">P_total</div>
      <div class="cv" id="kPt" style="color:var(--pbpe)">$3.521</div>
      <div class="cs">+8.0% over market</div>
    </div>
  </div>

  <!-- Charts row -->
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px">
    <div class="card">
      <div class="lbl" style="color:var(--carb)">GHG Reduction · MBT55 vs Conventional</div>
      <div style="position:relative;height:90px"><canvas id="ghgChart" role="img" aria-label="GHG flux comparison chart">GHG flux over 12 months.</canvas></div>
      <div class="mono" style="font-size:8px;color:var(--carb);margin-top:6px" id="ghgSave">▼ 0% GHG reduction over 12 months</div>
      <div style="display:flex;gap:10px;margin-top:4px">
        <div class="legitem"><div class="legsq" style="background:#34D058"></div>MBT55</div>
        <div class="legitem"><div class="legsq" style="background:#FF7043;opacity:.7"></div>Conventional</div>
      </div>
    </div>
    <div class="card">
      <div class="lbl" style="color:var(--m3)">SHE™ Score Trajectory (0–100)</div>
      <div style="position:relative;height:90px"><canvas id="sheChart" role="img" aria-label="SHE score trajectory">SHE score over 12 months.</canvas></div>
      <div style="display:flex;gap:3px;margin-top:6px" id="sheDots"></div>
    </div>
  </div>

  <!-- P_total bar -->
  <div class="card">
    <div class="lbl" style="color:var(--safe)">
      P_total = P_market + V(機能性) + L(ロス削減) + m(医療費) + C(炭素隔離)
    </div>
    <div class="bar-wrap">
      <div class="bseg" style="flex:2.800;background:#3A5A7A">$2.800</div>
      <div class="bseg" style="flex:0.420;background:var(--m3)">V</div>
      <div class="bseg" style="flex:0.180;background:var(--agri)">L</div>
      <div class="bseg" style="flex:0.064;background:var(--hlth)">m</div>
      <div class="bseg" style="flex:0.017;background:var(--carb)">C</div>
    </div>
    <div style="display:flex;gap:10px;flex-wrap:wrap;margin-top:10px;align-items:center">
      <div class="legitem"><div class="legsq" style="background:#3A5A7A"></div>Market $2.800</div>
      <div class="legitem"><div class="legsq" style="background:var(--m3)"></div><span style="color:var(--m3)">V</span> $0.420</div>
      <div class="legitem"><div class="legsq" style="background:var(--agri)"></div><span style="color:var(--agri)">L</span> $0.180</div>
      <div class="legitem"><div class="legsq" style="background:var(--hlth)"></div><span style="color:var(--hlth)">m</span> $0.064</div>
      <div class="legitem"><div class="legsq" style="background:var(--carb)"></div><span style="color:var(--carb)">C</span> $0.017</div>
      <div style="margin-left:auto;font-family:'JetBrains Mono',monospace;font-size:12px;color:var(--safe);font-weight:600">
        Total $3.521/kg &nbsp;<span style="font-size:9px;color:var(--dim)">+8.0%</span>
      </div>
    </div>
  </div>

  <!-- V-Score decay chart -->
  <div class="card">
    <div class="lbl" style="color:var(--safe)">V-Score Decay · MBT55 vs Conventional (days post-harvest)</div>
    <div style="position:relative;height:90px"><canvas id="vsChart" role="img" aria-label="V-Score decay comparison">V-Score decay over time.</canvas></div>
    <div style="display:flex;gap:14px;margin-top:6px;align-items:center">
      <div class="legitem"><div class="legsq" style="background:var(--m3)"></div>MBT55</div>
      <div class="legitem"><div class="legsq" style="background:var(--warn);opacity:.7"></div>Conventional</div>
      <span class="mono" style="font-size:8px;color:var(--dim);margin-left:auto">Functional threshold: V-Score = 35</span>
    </div>
  </div>

  <!-- Multi-Agent Architecture -->
  <div class="card">
    <div class="lbl" style="color:var(--agri)">Multi-Agent AI Architecture · AgriWare™ Core</div>
    <!-- Data flow row -->
    <div class="flowrow">
      <div class="fbox act" id="fa0" style="--ac:var(--m3)" onclick="setAgent(0)">
        <div style="font-size:14px">🦠</div>
        <div class="mono" style="font-size:7px;color:var(--m3)">Microbe</div>
      </div>
      <div class="farr">→</div>
      <div class="fbox" id="fa1" style="--ac:var(--agri)" onclick="setAgent(1)">
        <div style="font-size:14px">🌿</div>
        <div class="mono" style="font-size:7px;color:var(--agri)">Cascade</div>
      </div>
      <div class="farr">→</div>
      <div class="fbox" id="fa2" style="--ac:var(--safe)" onclick="setAgent(2)">
        <div style="font-size:14px">⏱</div>
        <div class="mono" style="font-size:7px;color:var(--safe)">Inertia</div>
      </div>
      <div class="farr">→</div>
      <div class="fbox" id="fa3" style="--ac:var(--hlth)" onclick="setAgent(3)">
        <div style="font-size:14px">❤</div>
        <div class="mono" style="font-size:7px;color:var(--hlth)">Health</div>
      </div>
      <div class="farr">→</div>
      <div class="fbox" style="--ac:var(--safe);border-color:var(--safe);background:#F5C54210">
        <div style="font-size:14px">🔗</div>
        <div class="mono" style="font-size:7px;color:var(--safe)">SafelyChain</div>
      </div>
      <div class="farr">→</div>
      <div class="fbox" style="--ac:var(--pbpe);border-color:var(--pbpe);background:#A855F710">
        <div style="font-size:14px">💹</div>
        <div class="mono" style="font-size:7px;color:var(--pbpe)">PBPE</div>
      </div>
    </div>
    <!-- Agent detail grid -->
    <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:8px" id="agentGrid"></div>
  </div>

  <!-- 5-layer architecture -->
  <div class="card">
    <div class="lbl">System Architecture · 5-Layer Integration</div>
    <div style="display:grid;grid-template-columns:repeat(5,1fr);gap:8px">
      <div class="layer" style="--lc:var(--m3)">
        <div class="ln" style="color:var(--m3)">L1 · Physical</div>
        <div class="lt">MBT55 Hypercycle</div>
        <div class="li">· 120-species consortium<br>· 80–100°C reactor<br>· 24h biological clock<br>· 55% aerobic / 45% anaerobic</div>
      </div>
      <div class="layer" style="--lc:var(--agri)">
        <div class="ln" style="color:var(--agri)">L2 · Digital</div>
        <div class="lt">AgriWare™ ODE</div>
        <div class="li">· M³-BioSynergy ODE<br>· EcoPhenotype 5-phase<br>· Azure IoT MQTT/OPC UA<br>· Multi-agent AI</div>
      </div>
      <div class="layer" style="--lc:var(--safe)">
        <div class="ln" style="color:var(--safe)">L3 · Trust</div>
        <div class="lt">SafelyChain™</div>
        <div class="li">· Blockchain ledger<br>· SCFA phenoprint<br>· V-Score / MetLife<br>· Proof of Regeneration</div>
      </div>
      <div class="layer" style="--lc:var(--pbpe)">
        <div class="ln" style="color:var(--pbpe)">L4 · Value</div>
        <div class="lt">PBPE Finance</div>
        <div class="li">· 1 PBPE = 10 kg CO₂e<br>· Multi-layer P_total<br>· ESG bond / token<br>· PBPE Marketplace</div>
      </div>
      <div class="layer" style="--lc:var(--hlth)">
        <div class="ln" style="color:var(--hlth)">L5 · Health</div>
        <div class="lt">HealthBook™</div>
        <div class="li">· 137 disease matrix<br>· m-ROI calculator<br>· MBT Probiotics<br>· 294 TCM library</div>
      </div>
    </div>
  </div>

  <!-- JSON schema preview (Gem7 agent communication) -->
  <div class="card">
    <div class="lbl" style="color:var(--agri)">Agent Communication Schema · Inter-Agent JSON (Gem7)</div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">
      <div>
        <div class="mono" style="font-size:8px;color:var(--m3);margin-bottom:4px">Microbe → Cascade (MBT-SOIL-001)</div>
        <pre style="background:var(--elev);border:1px solid var(--bord);border-radius:6px;
                    padding:8px;font-size:8px;color:var(--hi);overflow:auto;line-height:1.6">{
  "transaction_id": "MBT-SOIL-001",
  "agent": "Microbe-Agent",
  "payload": {
    "hypercycle_velocity": 0.85,
    "metabolic_currency": {
      "lactate_pool_mg_kg": 120.5,
      "redox_potential_eh": -150.0,
      "electron_shuttle": 0.92
    },
    "soil_health_score": 94,
    "security_status": "Pathogen-Suppressed"
  }
}</pre>
      </div>
      <div>
        <div class="mono" style="font-size:8px;color:var(--safe);margin-bottom:4px">Inertia → SafelyChain™ (MBT-LOGI-003)</div>
        <pre style="background:var(--elev);border:1px solid var(--bord);border-radius:6px;
                    padding:8px;font-size:8px;color:var(--hi);overflow:auto;line-height:1.6">{
  "transaction_id": "MBT-LOGI-003",
  "agent": "Inertia-Agent",
  "payload": {
    "metabolic_inertia_days": 14.5,
    "decay_coefficient": 0.024,
    "v_index_final": {
      "functionality": 158,
      "stability": 92,
      "security": 100
    },
    "dynamic_pricing_premium": 0.15
  }
}</pre>
      </div>
    </div>
  </div>

</div><!-- /RIGHT -->
</div><!-- /grid -->

<!-- Footer -->
<div style="border-top:1px solid var(--bord);padding:10px 0 0;
            display:flex;justify-content:space-between;margin-top:14px">
  <span class="mono" style="font-size:8px;color:var(--dim)">
    AGRIX-OS · BioNexus-Core · shimojok/AGRIX-OS
  </span>
  <span class="mono" style="font-size:8px;color:var(--carb)">
    PBPE Carbon Pipeline Active · IPCC Tier 2 Compliant
  </span>
  <span class="mono" style="font-size:8px;color:var(--dim)">
    Bill Gates Foundation · Microsoft Azure Partnership
  </span>
</div>

</div><!-- /container -->

<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>
<script>
// ── Data ──────────────────────────────────────────────────────────
const MONTHS=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
const SHE_S=[42,44,47,52,58,64,69,73,76,78,79,80];
const GHG_M=[8.2,7.1,6.0,5.2,4.5,4.0,3.6,3.3,3.1,2.9,2.8,2.7];
const GHG_C=[8.2,8.0,7.9,7.8,7.7,7.6,7.5,7.4,7.3,7.2,7.1,7.0];
const VS_M =[100,97.1,94.3,91.6,89.0,86.4,83.9,81.5,79.2,76.9,74.7,72.5];
const VS_C =[100,95.4,91.0,86.8,82.8,78.9,75.2,71.7,68.4,65.2,62.1,59.2];

const AGENTS=[
  {id:0,icon:'🦠',name:'Microbe-Agent',color:'#00D4A0',cvar:'var(--m3)',
   role:'Soil hypercycle dynamics',
   inputs:['Eh (mV)','pH','Temp °C','Moisture %'],
   outputs:['ω_cycle','μ_MBT','hypercycle_vel'],schema:'MBT-SOIL-001'},
  {id:1,icon:'🌿',name:'Cascade-Agent',color:'#2E9CFF',cvar:'var(--agri)',
   role:'Nutrient cascade tracking',
   inputs:['NDVI / PRI','Conductance','N/P/K soil'],
   outputs:['η_metabolic','Φ_functional','SCFA pool'],schema:'MBT-PLANT-002'},
  {id:2,icon:'⏱',name:'Inertia-Agent',color:'#F5C542',cvar:'var(--safe)',
   role:'Post-harvest metabolic decay',
   inputs:['ATP (harvest)','Ethylene rate','Storage T°'],
   outputs:['τ_inertia','V-Score','MetabolicLife'],schema:'MBT-LOGI-003'},
  {id:3,icon:'❤',name:'Health-Agent',color:'#FF6B9D',cvar:'var(--hlth)',
   role:'Gut microbiome coupling',
   inputs:['V-Index','SCFA density','HealthBook'],
   outputs:['SCFA impact','m_ROI (USD)','Disease risk Δ'],schema:'HB-004'},
];

// ── State ─────────────────────────────────────────────────────────
let step=0, running=true, activeAgent=0;

// ── Charts ────────────────────────────────────────────────────────
const GRID_COLOR='rgba(26,48,80,0.5)';
const TICK_STYLE={font:{size:8,family:'JetBrains Mono'},color:'#3A5A7A'};

const ghgChart=new Chart(document.getElementById('ghgChart').getContext('2d'),{
  type:'line',
  data:{labels:MONTHS,datasets:[
    {label:'MBT55',      data:[...GHG_M],borderColor:'#34D058',borderWidth:2,
     pointRadius:GHG_M.map((_,i)=>i===0?4:0),fill:false,tension:.4},
    {label:'Conventional',data:[...GHG_C],borderColor:'#FF7043',borderWidth:1.5,
     borderDash:[4,3],pointRadius:0,fill:false,tension:.3},
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    plugins:{legend:{display:false},tooltip:{mode:'index',intersect:false}},
    scales:{
      x:{ticks:{...TICK_STYLE,maxRotation:0},grid:{color:GRID_COLOR}},
      y:{ticks:{...TICK_STYLE},grid:{color:GRID_COLOR},min:2,max:9},
    }}
});

const sheChart=new Chart(document.getElementById('sheChart').getContext('2d'),{
  type:'line',
  data:{labels:MONTHS,datasets:[
    {label:'SHE',data:[...SHE_S],borderColor:'#00D4A0',borderWidth:2,
     pointRadius:SHE_S.map((_,i)=>i===0?4:0),
     fill:true,backgroundColor:'rgba(0,212,160,0.07)',tension:.5},
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    plugins:{legend:{display:false}},
    scales:{
      x:{ticks:{...TICK_STYLE,maxRotation:0},grid:{color:GRID_COLOR}},
      y:{ticks:{...TICK_STYLE},grid:{color:GRID_COLOR},min:35,max:85},
    }}
});

const vsChart=new Chart(document.getElementById('vsChart').getContext('2d'),{
  type:'line',
  data:{labels:MONTHS,datasets:[
    {label:'MBT55',      data:[...VS_M],borderColor:'#00D4A0',borderWidth:2,
     pointRadius:0,fill:true,backgroundColor:'rgba(0,212,160,0.06)',tension:.4},
    {label:'Conventional',data:[...VS_C],borderColor:'#FF7043',borderWidth:1.5,
     borderDash:[4,3],pointRadius:0,fill:false,tension:.3},
  ]},
  options:{responsive:true,maintainAspectRatio:false,
    plugins:{legend:{display:false},
      annotation:{annotations:{thr:{type:'line',yMin:35,yMax:35,
        borderColor:'#FF7043',borderWidth:1,borderDash:[3,3]}}}},
    scales:{
      x:{ticks:{...TICK_STYLE,maxRotation:0},grid:{color:GRID_COLOR}},
      y:{ticks:{...TICK_STYLE},grid:{color:GRID_COLOR},min:20,max:105},
    }}
});

// ── M³ Ring update ────────────────────────────────────────────────
function updateRings(she){
  const s=she/100;
  const specs=[
    {id:'ringMod',r:65,mult:1.25,total:408},
    {id:'ringMet',r:48,mult:1.10,total:301},
    {id:'ringMic',r:30,mult:1.00,total:188},
  ];
  specs.forEach(sp=>{
    const prog=Math.min(s*sp.mult,1);
    const on=(sp.total*prog).toFixed(1);
    const off=(sp.total*(1-prog)).toFixed(1);
    document.getElementById(sp.id).setAttribute('stroke-dasharray',`${on} ${off}`);
  });
  document.getElementById('sheNum').textContent=she;
}

// ── SHE progress dots ─────────────────────────────────────────────
function buildDots(){
  const c=document.getElementById('sheDots');
  c.innerHTML='';
  for(let i=0;i<12;i++){
    const d=document.createElement('div');
    d.style.cssText=`flex:1;height:3px;border-radius:2px;transition:background .4s;`+
      `background:${i<=step?'#00D4A0':'#1A3050'}`;
    c.appendChild(d);
  }
}

// ── Agent detail grid ─────────────────────────────────────────────
function buildAgents(){
  const g=document.getElementById('agentGrid');
  g.innerHTML='';
  AGENTS.forEach(ag=>{
    const isAct=ag.id===activeAgent;
    const d=document.createElement('div');
    d.className='agent'+(isAct?' act':'');
    d.style.setProperty('--ac',ag.cvar);
    let inner=`<div class="ai">${ag.icon}</div>
      <div class="an" style="color:${ag.color};margin-bottom:3px">${ag.name}</div>
      <div class="ar">${ag.role}</div>`;
    if(isAct){
      inner+=`<div class="iorow">
        <div>
          <div class="iol">Inputs</div>
          ${ag.inputs.map(x=>`<div style="color:var(--hi)">← ${x}</div>`).join('')}
        </div>
        <div>
          <div class="iol">Outputs</div>
          ${ag.outputs.map(x=>`<div style="color:${ag.color}">→ ${x}</div>`).join('')}
        </div>
      </div>
      <div class="mono" style="font-size:7px;color:var(--mut);border-top:1px solid var(--bord);
           padding-top:5px;margin-top:5px">schema: ${ag.schema}</div>`;
    }
    d.innerHTML=inner;
    d.onclick=()=>setAgent(ag.id);
    g.appendChild(d);
  });
  // flow box highlights
  [0,1,2,3].forEach(i=>{
    const el=document.getElementById('fa'+i);
    if(el) el.classList.toggle('act',i===activeAgent);
  });
}

function setAgent(i){activeAgent=i;buildAgents();}

// ── Chart point highlights ────────────────────────────────────────
function highlightStep(chart,idx){
  chart.data.datasets[0].pointRadius=
    chart.data.datasets[0].data.map((_,i)=>i===idx?4:0);
  chart.update('none');
}

// ── Tick ─────────────────────────────────────────────────────────
function tick(){
  if(!running) return;
  step=(step+1)%12;
  const she=SHE_S[step], ghg=GHG_M[step], vs=VS_M[step];

  // KPIs
  document.getElementById('kShe').textContent=she;
  document.getElementById('kSheSub').textContent=`+${she-SHE_S[0]}pts since Jan`;
  document.getElementById('kGhg').textContent=ghg.toFixed(1);
  const pct=((GHG_C[step]-ghg)/GHG_C[0]*100).toFixed(0);
  document.getElementById('kGhgSub').textContent=`▼${pct}% vs conventional`;
  document.getElementById('kVs').textContent=vs.toFixed(1);
  document.getElementById('monthLbl').textContent=MONTHS[step];

  // GHG save badge
  document.getElementById('ghgSave').textContent=`▼ ${pct}% GHG reduction vs conventional`;

  // Rings
  updateRings(she);

  // Chart highlights
  highlightStep(ghgChart,step);
  highlightStep(sheChart,step);

  // Dots
  buildDots();
}

function toggleSim(){
  running=!running;
  document.getElementById('simBtn').textContent=running?'PAUSE':'RESUME';
  const dot=document.getElementById('liveDot');
  dot.style.boxShadow=running?'0 0 7px #00D4A0':'none';
  dot.style.background=running?'#00D4A0':'#3A5A7A';
}

// ── Init ──────────────────────────────────────────────────────────
buildDots();
buildAgents();
updateRings(SHE_S[0]);
setInterval(tick,1600);
</script>
</body>
</html>



