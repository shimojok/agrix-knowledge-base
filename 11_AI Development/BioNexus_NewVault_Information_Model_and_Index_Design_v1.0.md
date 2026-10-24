# BioNexus New Vault — Cross-Source Reconciliation & Information/Index Design v1.0

**Status:** Design specification based on the eight supplied ZIP archives; not yet deployed or runtime-validated.  
**Scope:** Source mapping, canonical information model, provenance, index outputs, database responsibilities, and implementation order.  
**Primary architecture decision:** `agrix-knowledge-base` is the Primary Knowledge Substrate; Python extraction and Local RAG are derived layers. HealthBook ZIPs and repository ZIPs are secondary/project-specific source packages, not replacements for the primary Vault.

## 1. Evidence boundary and corpus inventory

The supplied ZIPs are partial, selected packages. They are not the complete BioNexus corpus, and the counts below describe files inside these ZIPs only. `.git` internals are excluded from the counts.

| Package | Non-Git files | Types | Verified role in this analysis |
|---|---:|---|---|
| `08_mbt_kampolibrary.zip` | 217 | 216 MD, 1 XLSX | MBT/Kampo library notes and spreadsheet |
| `09_MBT_漢方代謝ライブラリー.zip` | 160 | 158 MD, 2 XLSX | Metabolic library, pathway maps, system diagrams |
| `healthbook-vault.zip` | 446 | 404 MD, 23 JSON, 13 PY, 3 PDF, 2 CSV, 1 XLSX | HealthBook/MIOS architecture, canonical schemas, data and engines |
| `MBT-Biosecurity-Engine_GH_0611.zip` | 80 | 69 MD, 1 JSON, 9 PY, 1 TXT | Biosecurity models, data model and Streamlit dashboards |
| `agrix-knowledge-base構築.zip` | 156 | 156 MD | Architecture decisions, pipeline specifications and implementation history; **not the actual 6,000+ note Vault** |
| `BioNexus-Enterprise.zip` | 77 | 75 MD, 1 PY, 1 JSON | MBT55 evidence notes, ODE engine and parameters |
| `M3-BioSynergy-Core.zip` | 61 | 40 MD, 12 PY, 5 CSV, 1 PNG, 3 PYC | Hypercycle, microbial/enzyme/flux models, AGRIX application and planetary adapter |
| `PBPE-Marketplace_GH_0611.zip` | 206 | 100 MD, 39 PY, 23 TSX, 13 TS, 6 SVG, 6 CSS, 3 YAML, 3 SQL, 3 JSON, 1 JS, 1 Prisma, 1 TXT, 1 PNG | PBPE Marketplace repository snapshot, API, UI, registry/credits code and evidence index |

**Total:** 1,403 non-Git files across the eight ZIPs. This is a package file count, not a unique-document count; duplicate versions and overlapping material may exist.

### Important limits

- The actual local `agrix-knowledge-base` Vault directory and its live files were not included as a full corpus in these ZIPs. Its current path, actual note count, live Git sync state and existing local RAG runtime were not independently inspected here.
- The uploaded `agrix-knowledge-base構築.zip` is a set of architecture/history notes. References inside it to `build_rag_index.py`, `update_rag_index.py`, `ask_rag.py`, and a downloadable extraction pipeline are **claims recorded in notes**, not proof that those scripts are present in the uploaded package.
- The user's direct report of the older local RAG (6,400+ notes, e5-small, ChromaDB, `update_rag_index.py`, Ollama/llama3) is an important project fact, but its current runtime and source files remain to be inspected.
- A Pinecone history is mentioned in prior design notes, but the supplied files do not establish a currently available Pinecone index or credentials.

## 2. Cross-source mapping

| Domain / layer | Source artifacts verified in supplied packages | Role in the new Vault | Handling rule |
|---|---|---|---|
| Primary knowledge architecture | `agrix-knowledge-base構築/2026-09-03/Hsm040...`, `Hsm042...`, `Hsm043...`, `Hsm044...`, `Hsm046...` | Governance, architecture decisions, extraction and provenance requirements | Store as design/history records. Preserve decision status and source chronology; do not treat every note as an equally current instruction. |
| MBT55 / hypercycle theory and models | `M3-BioSynergy-Core/core_model.py`, `2_Models/*.py`, `planetary_os_adapter.py`; `BioNexus-Enterprise/src/mbt55_ode_engine.py` | Scientific concepts, executable models, parameters, adapters | Index code separately from explanatory prose. Link model → parameter file → evidence source → run/test. Do not merge incompatible parameter files without validation. |
| MBT55 evidence | `BioNexus-Enterprise/02_Evidence/{ja,en}/*.md`; `PBPE-Marketplace.../docs/evidence/MBT55_*`; MBT Biosecurity case notes | Case descriptions, observed data, source URLs and claims | Keep source claim, observation, interpretation and independent validation status distinct. Preserve original URLs and line/page location where available. |
| AGRIX / AgriWare / SafetyChain | `M3-BioSynergy-Core/4_Applications/AGRIX.md`; architecture notes and MBT55/AGRIX references | Agricultural platform concepts and interfaces | Preserve AGRIX as a cross-domain platform. Treat AgriWare and SafetyChain as named components/functional layers where the source supports them; do not infer undocumented schemas or APIs. |
| HealthBook / MIOS | `healthbook-vault.zip`: `mios_canonical_object_envelope.schema.json`, `mios_mi_object.schema.json`, `mios_metabolic_snapshot.schema.json`, `mi_object_type_registry.v1.0.json`, `disease_matrix_137.json`, `questionnaire_200_jp.json`, `kampo_metabolic_library.json`, and Python engines | Canonical schemas, domain datasets, inference/pathway engines, architecture genealogy | Keep schemas/data/code as separate artifact types. Preserve schema version, status, provenance and evidence references. Do not collapse all HealthBook material into prose chunks. |
| MBT biosecurity / agriculture | `MBT-Biosecurity-Engine.../09_Code_Models/*.py`, `08_Dashboard/Data_Model.json`, `Streamlit_Production*.py` | Executable risk/soil-carbon/One Health models, data model, dashboard versions | Keep each code version separate; record imports, parameters, inputs/outputs and validation state. Dashboard files are alternative snapshots until the authoritative version is determined. |
| PBPE implementation history | `PBPE-Marketplace.../backend/routers/credits.py`, `registry.py`, `dashboard.py`, `backend/blockchain/*`, `frontend/app/dashboard/*`, `docs/architecture/*` | Legacy marketplace code and design history | Mark as legacy/under-reconciliation where it uses credit/token/trading constructs. Do not treat its current implementation as the approved PBPE architecture without an explicit decision record. |
| Cross-project daily notes and archive libraries | `08_mbt_kampolibrary.zip`, `09_MBT_漢方代謝ライブラリー.zip`, dated folders in `healthbook-vault.zip` | Historical source material and cross-domain knowledge | Preserve package name and archive-relative path. Do not use folder names alone to force a single project classification. |

### Confirmed code-level reconciliation findings

1. `BioNexus-Enterprise/src/mbt55_ode_engine.py` defines `PARAM_FILE` as `src/parameters.json`, while the supplied repository snapshot contains `src/parameters_optimized.json`. This is a **path mismatch to resolve before execution**, not proof that the model is invalid.
2. `parameters_optimized.json` itself includes a caveat that the fit is a single-start fit and direct metabolite CSV data would be needed for full Tier 2 compliance. Preserve that caveat alongside the parameter artifact.
3. `M3-BioSynergy-Core/2_Models/hypercycle.py` composes microbial dynamics, enzyme cascade, carbon flux and nitrogen flux modules. Treat it as a model integration point; its existence alone does not validate the biological assumptions or numerical outputs.
4. `PBPE-Marketplace_GH_0611/backend/routers/credits.py` implements a credits issuance flow and uses an in-memory store. This is legacy implementation evidence, not an approved source of truth for the currently intended Impact Asset architecture.
5. Some PBPE snapshot files are zero bytes, including several engine/API/schema files. Inventory and record them as empty source artifacts; do not infer their intended implementation from their filenames.
6. The architecture/history notes contain different descriptions of embedding and RAG choices (local e5-small/Ollama versus OpenAI Embeddings/hybrid options). The user's latest statement about the older local system is the working baseline; actual runtime/config files must be inspected before copying settings to the new Vault.

## 3. Canonical information model

Use a **small canonical envelope with typed records**, not a large ontology-first redesign. Every record has a stable ID, type, version/status and provenance. The record types below are for indexing and reconciliation; they do not rewrite source content.

### 3.1 Shared envelope

Required fields:
- `record_id`: deterministic identifier
- `record_type`: controlled type
- `schema_version`: e.g. `1.0.0`
- `status`: `observed`, `candidate`, `confirmed`, `superseded`, `deprecated`, or `unresolved` as applicable to the record type
- `source_refs`: one or more source/document references
- `created_at` / `indexed_at`: timestamps for the generated record
- `content_hash`: SHA-256 of the source content/version where applicable
- `pipeline_version`: extractor/indexer version
- `confidence_or_review_state`: only when the extraction process supplies it; do not invent confidence scores.

### 3.2 Record types

| Type | Purpose | Minimum fields |
|---|---|---|
| `SourceArtifact` | Any file in a source package or Vault | `source_id`, `source_root`, `relative_path`, `filename`, `extension`, `size_bytes`, `sha256`, `mtime`, `encoding`, `package_id`, `is_empty`, `scan_status` |
| `Document` | Parsed file-level content | `document_id`, `source_id`, `title`, `format`, `frontmatter`, `tags`, `aliases`, `created_date_if_explicit`, `modified_date_if_explicit`, `parse_status` |
| `KnowledgeUnit` | Searchable section/chunk derived from a source | `unit_id`, `document_id`, `heading_path`, `heading_level`, `start_line`, `end_line`, `text`, `text_hash`, `language_if_detected`, `project_relevance[]` |
| `LinkEdge` | Obsidian, Markdown or code reference | `edge_id`, `source_record_id`, `target_raw`, `target_resolved_id_if_known`, `link_type`, `label`, `line_number`, `resolution_status` |
| `CodeArtifact` | Executable or schema artifact | `code_id`, `source_id`, `language`, `imports[]`, `entrypoint_if_known`, `input_refs[]`, `output_refs[]`, `parameter_refs[]`, `test_status`, `execution_status` |
| `EvidenceRecord` | Observation, experiment, document, video or dataset supporting a claim | `evidence_id`, `source_id`, `evidence_kind`, `source_locator`, `observed_date_if_explicit`, `method_if_explicit`, `raw_observation`, `limitations_as_stated`, `verification_status` |
| `ClaimRecord` | A claim extracted from source text, kept distinct from evidence | `claim_id`, `claim_text`, `claim_kind`, `source_unit_id`, `evidence_refs[]`, `status`, `quantities_and_units[]`, `contradiction_refs[]` |
| `DecisionRecord` | Architecture/design decision and its lifecycle | `decision_id`, `decision_text`, `decision_status`, `decision_date_if_explicit`, `supersedes[]`, `superseded_by[]`, `rationale_source_refs[]`, `authority_source_ref` |
| `EntityRecord` | Named platform, model, organism/strain, metabolite, pathway, organization, KPI, etc. | `entity_id`, `canonical_label`, `entity_type`, `aliases[]`, `source_refs[]`, `review_status` |
| `RelationshipCandidate` | Explicit or extracted relation between records/entities | `relation_id`, `subject_id`, `predicate`, `object_id_or_literal`, `source_refs[]`, `extraction_method`, `review_status` |
| `ProjectRelevance` | Multi-label relevance to BioNexus Projects 01–06 | `record_id`, `project_id`, `relevance_basis`, `source_ref`, `review_status` |
| `IndexRun` | Reproducibility and update manifest | `run_id`, `started_at`, `finished_at`, `source_root_id`, `pipeline_version`, `file_count`, `changed_count`, `deleted_or_missing_count`, `error_count`, `output_hashes`, `embedding_model`, `vector_collection_version` |

### 3.3 Identifier rules

- Keep `source_id` stable for the same source-root-relative path; keep `sha256` separate so content changes are detectable.
- Generate `document_id` from a stable source identity, not the title alone.
- Generate `unit_id` deterministically from `document_id` + heading path + normalized text hash; store line ranges separately because line numbers can shift.
- Never use an AI-generated title or project label as the sole identifier.
- A path rename is recorded as a new path until a verified rename mapping is available; do not silently merge records based on similar titles.
- Duplicate content is a relationship (`duplicate_of`/`same_content_hash`), not a reason to delete either source.

## 4. Provenance and conflict rules

1. Raw source files are immutable inputs to this pipeline: no move, overwrite, deletion or auto-edit.
2. Every extracted section, claim, evidence record and code artifact must point back to a source path and source hash. Markdown-derived records also retain heading and line range.
3. Separate **source assertion** from **verified fact**. A document that says “24-hour complete decomposition” establishes that the document makes the claim; it does not by itself establish independent validation.
4. Keep decision/history documents. A later document only supersedes an earlier decision when the source explicitly records that relationship or the user confirms it.
5. When sources disagree, create a conflict/reconciliation record with both source references. Do not automatically resolve by newest file modification time, model preference or folder name.
6. Preserve incomplete/partial source packages as partial. Absence from the supplied ZIP is not evidence that an artifact does not exist elsewhere.
7. Store extraction errors and unresolved links as records in the run output; do not silently discard them.
8. The user-approved primary source is the live `agrix-knowledge-base` Vault. The uploaded ZIPs are supplemental, source-attributed packages unless explicitly promoted to primary status.

## 5. Index design

### 5.1 Generated artifacts (JSONL + manifest)

Use a versioned output directory outside the source content area or in a clearly excluded generated-data directory:

```text
_knowledge_index/
  v1/
    source_inventory.jsonl
    documents.jsonl
    sections.jsonl
    links.jsonl
    code_artifacts.jsonl
    evidence_records.jsonl
    claims.jsonl
    decisions.jsonl
    entities.jsonl
    relationships.jsonl
    project_relevance.jsonl
    provenance.jsonl
    run_manifest.json
```

For the first structural pass, `source_inventory.jsonl`, `documents.jsonl`, `sections.jsonl`, `links.jsonl`, `provenance.jsonl`, and `run_manifest.json` are mandatory. The semantic files are populated only by explicit rules or later reviewed extraction; they must not be fabricated in the structural pass.

### 5.2 Source DB — SQLite + FTS5

SQLite is the canonical queryable metadata/provenance store. Tables should include:
- `source_artifacts`
- `documents`
- `knowledge_units`
- `links`
- `code_artifacts`
- `evidence_records`
- `claims`
- `decisions`
- `entities`
- `relationships`
- `project_relevance`
- `index_runs`
- `record_conflicts`

Use foreign keys, uniqueness constraints on stable IDs, indexes on `relative_path`, `sha256`, `record_type`, `status`, and `project_id`. Use FTS5 for searchable text (`title`, `heading_path`, `text`, `tags`, `aliases`) with an external-content or rebuildable strategy. The database is generated/derived from source; source files remain authoritative.

### 5.3 Vector DB — ChromaDB

The user reports the existing local RAG uses e5-small + ChromaDB + Ollama/llama3. For continuity, the initial target is a **new, separate Chroma persistence directory and collection** for the new Vault, using the already deployed embedding model only after the actual model and vector dimensions are confirmed. Do not change to BGE-M3 or another embedding model just because it is available.

Recommended collection separation:
- `bionexus_knowledge_units_v1` — searchable section-level knowledge units
- Optional later: `bionexus_code_units_v1` — code/docstrings/API/schema text, only if separate ranking proves useful

Required vector metadata should stay flat and scalar/list-of-supported-values compatible with the installed Chroma version:
- `unit_id`, `document_id`, `source_id`
- `relative_path`, `filename`, `extension`
- `heading_path`, `start_line`, `end_line`
- `project_ids` or one primary project field plus a separate relation table; avoid relying on complex nested JSON metadata
- `record_type`, `status`, `content_hash`, `pipeline_version`

The vector DB is a **derived retrieval index**, not the authority for provenance, claims or architecture decisions. Store IDs and retrieval metadata in Chroma; retrieve authoritative source/decision/evidence details from SQLite and the source file.

### 5.4 Retrieval

Initial retrieval is hybrid:
1. SQLite FTS5 lexical search for exact strings, acronyms, filenames, IDs and parameter names.
2. Chroma semantic search for conceptually related passages.
3. Link traversal for explicit Obsidian/Markdown relationships.
4. Merge and deduplicate by `unit_id`, apply optional project/status filters, then fetch provenance and relevant source lines from SQLite/source.
5. Return source-grounded snippets with paths, heading, line ranges and hashes.

Do not add a graph database or a separate GraphRAG stack in v1.0. The extracted `links` and `relationships` tables provide sufficient first-stage relationship navigation.

## 6. Model and engine integration rules

- RAG retrieves source passages and evidence references; it does not certify the validity of a biological claim.
- Mathematical engines calculate using explicit code and parameters. The LLM must not replace numerical calculation with prose estimation.
- Record each engine's code hash, parameter file hash, input set, output set, dependency versions and execution/test status.
- For MBT55 ODE work, resolve the `parameters.json` vs `parameters_optimized.json` mismatch before claiming that the supplied engine runs with the supplied parameter set.
- For PBPE, retain the supplied marketplace repository as historical implementation material. The current intended PBPE Impact Asset/Planetary Cost Transformation architecture must be represented by explicit decision records and reconciled against legacy credits/token endpoints before implementation reuse.
- UI/dashboards are downstream of source/index correctness. Do not start the Streamlit/3D dashboard before the extraction and retrieval layer passes acceptance tests.

## 7. Incremental update protocol

1. Scan the source root in read-only mode and create a run manifest.
2. Compute SHA-256 for eligible files. Compare path + hash to the previous successful run.
3. Parse only new/changed files; reuse prior derived records for unchanged files.
4. For changed files, create a new content version and refresh document/section/link/provenance rows transactionally.
5. If a prior path is missing, mark it `missing_from_latest_scan`; do not delete its history or associated evidence records.
6. Update FTS5 rows in the same transaction as source metadata.
7. Update/delete corresponding Chroma vectors only after the SQLite extraction run validates; use idempotent upsert by `unit_id`.
8. Commit the run as successful only when counts, hashes and error thresholds pass. Otherwise keep the last successful index available and mark the new run failed.
9. Maintain a reproducible manifest including pipeline version, embedding model/version, collection name, source root, counts and error summary.

## 8. Acceptance criteria before Local RAG is considered ready

- Every indexed record resolves to an existing source file or is explicitly marked historical/missing.
- Repeated extraction of unchanged inputs produces the same stable IDs and content hashes.
- Changed files update their records without modifying the source Vault.
- Obsidian links are retained whether resolved or unresolved.
- Exact search finds known identifiers (e.g. MBT55, AgriWare, SafetyChain, MIOS schema IDs, PBPE route names).
- Semantic search retrieves cross-domain passages without silently forcing one project classification.
- Returned answers include path, heading, line range and source reference.
- Claims and model outputs are visibly distinguished from verified evidence.
- The RAG index can be rebuilt from the Vault and the extraction code.
- The existing local RAG runtime is not overwritten; the new index uses a separate persistence path until migration is approved.

## 9. Fixed implementation sequence

1. **Source/runtime audit:** inspect the actual new Vault path and current older-RAG scripts/configs; do not infer them from design notes.
2. **Structural extraction:** read-only scanner, hashing, Markdown/frontmatter parser, heading/section extraction, link extraction, provenance and manifest.
3. **Reconciliation:** identify duplicate paths/content, empty files, conflicting decisions, parameter/config mismatches, and unresolvable links.
4. **SQLite + FTS5:** build queryable source and provenance records.
5. **Embedding/Chroma:** use the verified existing embedding model in a separate new-Vault collection.
6. **Hybrid retrieval tests:** lexical + semantic + link-based retrieval and citation/line-range checks.
7. **MCP exposure:** expose read-only search, source-section retrieval, related-note traversal and index status.
8. **Engine connection:** register code artifacts and parameter dependencies; run model tests separately.
9. **Dashboard:** only after source retrieval and engine execution contracts pass acceptance tests.

## 10. Decisions fixed by this specification

- Primary substrate: live `agrix-knowledge-base` Vault.
- Secondary sources: supplied ZIPs and GitHub repository snapshots, individually source-attributed.
- Raw source: immutable and read-only to the pipeline.
- Core searchable unit: heading/section-derived `KnowledgeUnit`, not whole-file-only and not forced into one project.
- Project assignment: many-to-many relevance metadata; never physical reclassification.
- Source/provenance database: SQLite + FTS5.
- Vector database: ChromaDB, separate collection/path for the new Vault after the existing model/runtime is verified.
- Local inference baseline: the user's reported Ollama/llama3 environment; verify before reusing.
- No Pinecone dependency in v1.0.
- No new graph database in v1.0.
- No automatic claim verification or automatic supersession of design decisions.
- Build structural extraction and source indexing before semantic enrichment, RAG, MCP and dashboard.

**Open blockers before implementation:** actual new Vault path; actual existing RAG code/config and Chroma persistence location; exact embedding model artifact/version and dimensions; source synchronization/Git policy; whether supplemental ZIP contents should be indexed as independent source roots or selectively imported into the Vault.
