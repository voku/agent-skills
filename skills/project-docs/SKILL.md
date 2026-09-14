---
name: project-docs
description: Project documentation lifecycle for PHP/Laravel and Node/TypeScript/React projects — bootstrapping essential docs, naming and folder conventions, freshness, and cleanup of AI-generated junk and stale files. Use when starting a new project, setting up docs/ structure, auditing markdown files, cleaning up the docs folder, or deciding which docs to keep, archive, or delete. Triggers on "set up docs", "audit docs", "clean up markdown", "what docs does this project need", "organize docs folder", "find stale docs".
license: MIT
metadata:
  author: agent-skills
  version: "1.0.0"
---

# Project Documentation Lifecycle & Hygiene

Curated, high-density documentation guidelines covering repository structure, essential baseline documents, anti-slop content quality, hygiene/cleanup, and ADR lifecycles.

## Quick Reference

| Category | Impact | Rule File | Primary Focus |
|----------|--------|-----------|---------------|
| **Structure & Naming** | CRITICAL | [`doc-structure-naming`](rules/doc-structure-naming.md) | Standard uppercase root files, `docs/` hierarchy, kebab-case, sequential ADR numbering |
| **Essential Baseline** | CRITICAL | [`doc-essential-baseline`](rules/doc-essential-baseline.md) | `README.md` quickstarts, Keep-a-Changelog `CHANGELOG.md`, `LICENSE`, `SECURITY.md` |
| **Markdown Quality** | HIGH | [`doc-markdown-quality-anti-slop`](rules/doc-markdown-quality-anti-slop.md) | Eliminating AI conversational filler, tagged code blocks, sequential headings, link health |
| **Hygiene & Cleanup** | HIGH | [`doc-hygiene-cleanup`](rules/doc-hygiene-cleanup.md) | Purging scratchpads (`PLAN.md`, `TODO.md`), deduplication, archiving to `docs/archive/<year>/` |
| **Lifecycle & Freshness** | MEDIUM | [`doc-lifecycle-adr-freshness`](rules/doc-lifecycle-adr-freshness.md) | MADR decision tracking, "Last Verified" accuracy timestamps, PR-linked changelog updates |

---

## Operating Modes

### 1. Bootstrap Mode (New Project / Missing Docs)
1. **Detect Stack**: Inspect `composer.json` (PHP/Laravel) or `package.json` (Node/React).
2. **Gap Analysis**: Verify baseline files (`README.md`, `CHANGELOG.md`, `LICENSE`, `SECURITY.md`).
3. **Scaffold Structure**: Establish `docs/` hierarchy (`architecture/`, `adr/`, `guides/`, `archive/`).

### 2. Audit Mode (Existing Project Cleanup)
Classify all `.md` files in the repository:
- **KEEP**: Essential and actively maintained documentation.
- **UPDATE**: Outdated or contradicting current codebase implementation.
- **ARCHIVE**: Superseded historical documents (move to `docs/archive/<year>/`).
- **DELETE**: AI scratchpads (`PLAN.md`, `TODO.md`), empty stubs, or unmaintained duplicates.

### 3. Ledger Output Format
```markdown
## Documentation Audit Ledger
| File | Status | Action |
|------|--------|--------|
| PLAN.md | DELETE | Stale AI prompt scratchpad — remove |
| docs/legacy-v1.md | ARCHIVE | Move to docs/archive/2025/ |
```
