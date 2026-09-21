---
title: <% tp.file.title %>
created: <% tp.file.creation_date("YYYY-MM-DD HH:mm") %>
updated: <% tp.file.last_modified_date("YYYY-MM-DD HH:mm") %>
platform: <% await tp.system.suggester(["AGRIX", "PBPE", "HealthBook", "共通/その他"], ["AGRIX", "PBPE", "HealthBook", "Common"]) %>
tags:
  - BioNexus
---

# <% tp.file.title %>

