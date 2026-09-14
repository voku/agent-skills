---
id: prd-structure-template
title: "PRD Document Structure: Single Source of Truth and Standardized Template"
category: structure
priority: CRITICAL
triggers: [prd-template-scaffolding, prd-output-location, single-source-of-truth-spec, prd-markdown-structure]
tags: [prd, template, structure, markdown, source-of-truth]
---

# PRD Document Structure: Single Source of Truth and Standardized Template

**Trigger Anchor:** Save every PRD to `docs/prd/{feature-name}.md` with YAML frontmatter, lead with an executive summary, and maintain a standardized 12-section layout serving as the single source of truth across product and engineering.

---

### Bad
```markdown
<!-- ❌ Freeform unstructured notes in Google Docs, unversioned, scattered across Slack channels -->
Here are some notes for the new search feature:
- Need search bar
- Should support fuzzy matching
- Tell backend team to make an API
```

### Good
```markdown
<!-- ✅ docs/prd/bulk-invoice-export.md: Standardized, version-controlled specification -->
---
title: Bulk Invoice Export for Accounting Systems
status: review
author: Product Team
created: 2026-03-14
updated: 2026-03-14
---

# PRD: Bulk Invoice Export for Accounting Systems

## 1. Executive Summary
Enable finance teams to export filtered invoice datasets directly to accounting-compatible CSV formats, eliminating 4.5 hours of manual data entry per week and reducing billing month-end close time by 2 days.

## 2. Problem Statement
Enterprise customers with >200 invoices per billing cycle cannot programmatically reconcile payments with external ERPs (NetSuite, QuickBooks), resulting in customer frustration and high churn risk.

## 3. Goals & Success Metrics
- Reduce average monthly reconciliation export time to under 15 seconds.
- Achieve 70% adoption among enterprise tier organizations within 60 days of launch.

## 4. User Personas
- **Primary:** Finance Manager (Alex) — Needs clean, pre-mapped CSV exports with line-item detail.
- **Secondary:** Auditor (Sam) — Needs immutable historical export logs and checksum receipts.

## 5. Scope Boundaries
- **In Scope:** CSV export, date and status filtering, async job generation >250 records.
- **Out of Scope:** Direct ERP OAuth API push (reserved for Q3 phase 2).
```
