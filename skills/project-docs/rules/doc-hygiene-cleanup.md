---
id: doc-hygiene-cleanup
title: "Documentation Hygiene: AI Junk Cleanup, Deduplication, and Archiving"
category: cleanup
priority: HIGH
triggers: [cleanup-ai-scratch-files, documentation-audit, delete-stale-markdown, archive-superseded-docs]
tags: [docs, cleanup, hygiene, ai-junk, archive, deduplication]
---

# Documentation Hygiene: AI Junk Cleanup, Deduplication, and Archiving

**Trigger Anchor:** Audit and remove transient AI scratch files (`PLAN.md`, `TODO.md`, `SESSION_NOTES.md`), eliminate copy-pasted duplicate documentation, purge empty placeholder stubs, and relocate superseded design documents into `docs/archive/<year>/`.

---

### Bad
```
# ❌ Accumulating transient task files and leaving superseded docs in active navigation
.
├── PLAN.md                         # Created by AI subagent 3 months ago, forgotten
├── IMPLEMENTATION_SUMMARY.md       # Ephemeral chat dump
├── TODO.md                         # Out-of-sync personal checklist
└── docs/
    ├── architecture-v1-old.md      # Outdated system design still sitting in active docs
    └── billing-spec.md             # Empty file with "# Billing\nTODO: write this"
```

### Good
```bash
# ✅ Audit & Cleanup Workflow

# 1. Inspect repository for transient AI scratchpads and prompt user before deletion
git status -s | grep -E '(PLAN|TODO|NOTES|TEMP|SUMMARY)\.md'

# 2. Archive superseded historical docs to yearly archive directory
mkdir -p docs/archive/2025
git mv docs/architecture/v1-legacy-overview.md docs/archive/2025/

# 3. Add deprecation notice to archived files
# Top of docs/archive/2025/v1-legacy-overview.md:
# > **Archived:** Superseded by [Current Architecture](docs/architecture/overview.md) on 2026-01-10.

# 4. Remove empty / TODO-only stub files
git rm docs/billing-spec.md
```
