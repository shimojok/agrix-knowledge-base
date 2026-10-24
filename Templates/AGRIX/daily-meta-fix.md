<%*
// 既存の本文を取得
let content = tp.file.content;
let tags = ["daily-log"];

// フォルダ体系（01〜22）に応じたキーワード検知ロジック
if (/Planetary_Problems|Planetary\s*Problems/i.test(content)) tags.push("01_Planetary_Problems");
if (/Biological_Systems|Biological\s*Systems/i.test(content)) tags.push("02_Biological_Systems");
if (/MBT55/i.test(content)) tags.push("03_MBT55");
if (/AGRIX/i.test(content)) tags.push("04_AGRIX");
if (/AgriWare/i.test(content)) tags.push("05_AgriWare");
if (/PBPE/i.test(content)) tags.push("06_PBPE");
if (/HealthBook/i.test(content)) tags.push("07_HealthBook");
if (/mbt_kampolibrary|kampolibrary/i.test(content)) tags.push("08_mbt_kampolibrary");
if (/漢方代謝ライブラリー|漢方/i.test(content)) tags.push("09_MBT_漢方代謝ライブラリー");
if (/Probiotics|プロバイオティクス/i.test(content)) tags.push("10_MBT_Probiotics");
if (/AI_Development|AI\s*Development/i.test(content)) tags.push("11_AI_Development");
if (/Claude/i.test(content)) tags.push("22_Claude");

// タグの重複排除とYAML書き出し用の整形
let uniqueTags = [...new Set(tags)];
let tagYaml = uniqueTags.map(t => `  - "${t}"`).join("\n");
-%>
---
id: "<% tp.file.title %>"
type: daily-note
date: <% tp.file.title %>
created: <% tp.file.title %> 00:00:00
modified: <% tp.file.title %> 00:00:00
tags:
<% tagYaml %>
vault_source: dailyNote
aliases:
  - "<% tp.file.title %>"
---

<% tp.file.content %>