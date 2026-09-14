---
name: prd-writing
description: Step-by-step workflow for writing Product Requirements Documents. Use when creating PRDs, documenting features, writing specifications, or planning new products. Triggers on "write PRD", "create PRD", "document requirements", "feature spec", or "product requirements".
license: MIT
metadata:
  author: agent-skills
  version: "1.0.0"
---

# Product Requirements Document (PRD) Writing

Curated, high-density workflow and guidelines for writing actionable, engineering-grounded Product Requirements Documents.

## Quick Reference

| Phase | Impact | Rule File | Primary Focus |
|-------|--------|-----------|---------------|
| **Discovery** | CRITICAL | [`prd-discovery-problem`](rules/prd-discovery-problem.md) | Problem-first framing, codebase grounding, targeted clarifying questions |
| **Structure** | CRITICAL | [`prd-structure-template`](rules/prd-structure-template.md) | Standardized template, `docs/prd/{feature}.md`, executive summary, single source of truth |
| **Requirements** | HIGH | [`prd-requirements-criteria`](rules/prd-requirements-criteria.md) | User stories, numbered FRs, numeric NFRs, Gherkin (`Given/When/Then`) criteria |
| **Scope & KPIs** | HIGH | [`prd-scope-metrics`](rules/prd-scope-metrics.md) | Explicit out-of-scope, non-goals, risk mitigation register, quantifiable KPIs |
| **Technical Specs** | MEDIUM | [`prd-technical-review`](rules/prd-technical-review.md) | High-level data models, RBAC authorization, API endpoint contracts, sign-off review |

---

## 6-Step PRD Workflow

1. **Assess Project State**: Check existing codebase (models, routes, auth policies) or brainstorm greenfield architecture constraints.
2. **Ask Clarifying Questions**: Ask 3-5 targeted multiple-choice (A/B/C) questions to resolve core ambiguities.
3. **Draft the Specification**: Populate the standardized PRD structure with testable requirements and scope limits.
4. **Present for Review**: Present draft highlighting problem framing, user workflows, and explicit non-goals.
5. **Iterate**: Incorporate feedback and resolve open questions.
6. **Store Spec**: Commit to `docs/prd/{feature-name}.md` with frontmatter metadata.
