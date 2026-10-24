質問します。


frontend/src/pages/dashboard.tsx　☛pages/ にあります。

```
import { useState } from "react";
import api from "../api";

export default function Dashboard() {
  const [result, setResult] = useState<any | null>(null);
  const [loading, setLoading] = useState(false);

  const handleConvertScope3 = async () => {
    try {
      setLoading(true);

      const payload = {
        sample: "data",
      };

      const res = await api.post("/scope3/convert", payload);
      setResult(res.data);
    } catch (e) {
      console.error(e);
      setResult({ error: "Request failed" });
    } finally {
      setLoading(false);
    }
  };

  return (
    <main style={{ padding: 32 }}>
      <h1>PBPE Dashboard</h1>

      <button onClick={handleConvertScope3} disabled={loading}>
        {loading ? "Converting..." : "Convert Scope3"}
      </button>

      <pre style={{ marginTop: 24, background: "#f5f5f5", padding: 16 }}>
        {result ? JSON.stringify(result, null, 2) : "No result yet"}
      </pre>
    </main>
  );
}
```

frontend/src/pages/dashboard/Dashboard.css　☛　pages/dashboard/ にあります。

```
.dashboard-container {
  display: flex;
}

.dashboard-content {
  flex: 1;
  padding: 24px;
}
```

Step 11：PBPE Marketplace Dashboard v3 ― 最終統合では、

📌 `frontend/src/styles/dashboard.css`　となっています。

```css
.dashboard-page {
  padding: 24px;
}

.page-title {
  font-size: 24px;
  font-weight: 600;
  margin-bottom: 24px;
}

.kpi-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
  margin-bottom: 24px;
}

.chart-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
  margin-bottom: 24px;
}

.finance-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
}

.kpi-card,
.chart-box,
.table-box {
  background: #ffffff;
  border-radius: 12px;
  padding: 24px;
  border: 1px solid #dddddd;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}
```

dashboard.tsx　の正しいパスを確認下さい。

dashboard.css　のパスが変更になっていますが、pages/dashboard/ は不要で、 `frontend/src/styles/dashboard.css`が正しいのではないですか？