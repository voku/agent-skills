---
id: prd-scope-metrics
title: "Scope Boundaries, Non-Goals, and Quantifiable Success Metrics"
category: scope
priority: HIGH
triggers: [scope-creep-prevention, prd-non-goals, quantifiable-kpis-spec, vague-language-elimination, risk-register]
tags: [prd, scope, non-goals, kpis, metrics, risk-management]
---

# Scope Boundaries, Non-Goals, and Quantifiable Success Metrics

**Trigger Anchor:** Enforce explicit "Out of Scope" and "Non-Goals" sections to prevent feature creep, define 3-5 quantifiable KPIs tied to problem resolution, and eliminate vague buzzwords ("fast", "intuitive", "scalable").

---

### Bad
```markdown
<!-- ❌ Vague goals and ambiguous scope leading to unlimited scope creep -->
## Goals
- Make the app much faster.
- Provide a modern export experience.
- Scale seamlessly to lots of users.

## Scope
- We will build export and whatever else finance asks for during development.
```

### Good
```markdown
<!-- ✅ Razor-sharp boundaries, non-goals, and quantifiable metrics -->
## Scope Boundaries

### Out of Scope (Phase 1)
- **Direct ERP API Sync:** We will not build direct OAuth connectors to NetSuite or Xero in this phase.
- **Custom Column Builder:** Column schema is fixed standard; user-customized field ordering is deferred.
- **PDF Stitching:** Generating multi-page concatenated PDF archives is excluded.

### Non-Goals
- **Replacing Accounting Software:** This feature does not calculate tax liabilities or adjust ledger postings.
- **Sub-second Large Exports:** For files >10,000 rows, background email delivery takes priority over instant download speed.

## Quantifiable Success Metrics (KPIs)

| Metric | Baseline | Target (30 days post-launch) | Tracking Mechanism |
|--------|----------|------------------------------|--------------------|
| **Export Failure Rate** | N/A | < 0.2% of all export jobs | Sentry / Datadog APM |
| **P95 Latency (<250 rows)** | N/A | < 2.0 seconds | Server request duration logs |
| **Enterprise Adoption** | 0% | ≥ 65% of Enterprise accounts run ≥1 export/mo | Mixpanel event tracking |
| **Support Tickets** | 18/mo ("Cannot export invoices") | < 2/mo | Zendesk tag analytics |

## Dependencies & Risk Register

| Risk / Dependency | Impact | Mitigation Strategy | Owner |
|-------------------|--------|---------------------|-------|
| Background queue worker memory exhaustion on large CSVs | High | Stream rows directly from database via cursor into Flysystem S3 bucket | Lead Backend Eng |
| Malicious CSV formula injection | Critical | Sanitize leading formula prefixes (`=`, `+`, `-`, `@`) | Security Reviewer |
```
