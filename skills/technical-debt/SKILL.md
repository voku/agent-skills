---
name: technical-debt
description: Technical debt inventory, prioritization, and audit for PHP/Laravel (MySQL) and Node/TypeScript/React projects. 10 rules across 10 categories covering code, security, design, dependencies, tests, performance, data, docs, infrastructure, and process debt. Triggers on "audit technical debt", "find tech debt", "debt inventory", "what should we refactor first", or tasks involving code health, security debt, performance debt, data debt, observability debt, debt prioritization, or remediation planning.
license: MIT
metadata:
  author: agent-skills
  version: "2.0.0"
---

# Technical Debt

Technical debt audit and prioritization framework for **PHP/Laravel (MySQL) and Node/TypeScript/React** projects. Contains **10 consolidated rules across 10 categories** covering code, security, design, dependency, test, performance, data, documentation, infrastructure, and process debt. Produces a ranked ledger (effort × impact) so teams know **what to fix first**, not just what's broken.

## Metadata

- **Version:** 2.0.0
- **Scope:** PHP / Laravel (MySQL) + Node / TypeScript / React
- **Rule Count:** 10 rules across 10 categories
- **License:** MIT

## How to Audit

When the user asks to "audit technical debt", "find tech debt", or "what should we refactor first" — run the checklist below against their codebase and produce a ranked debt ledger.

### Audit Step 1: Determine Scope

- If arguments provided (`$ARGUMENTS`): audit only those paths or modules
- If no arguments: audit the entire repository starting from the root

### Audit Step 2: Detect Project Stack

Inspect `composer.json` and `package.json` to determine the stack (PHP/Laravel, Node/TypeScript/React, or both).

### Audit Step 3: Run Debt Checklist

Work through the 10 categories:
- **PASS** — brief confirmation of what was verified
- **FAIL** — exact `file:line`, description of the debt, **effort estimate** (S/M/L), and **impact** (LOW/MED/HIGH/CRITICAL)
- **N/A** — if the check does not apply to this project

## Rule Categories by Priority

| Priority | Category | Impact | Prefix | Rules |
|----------|----------|--------|--------|-------|
| 1 | Code Debt | CRITICAL | `code-` | 1 |
| 2 | Security Debt | CRITICAL | `security-` | 1 |
| 3 | Design Debt | HIGH | `design-` | 1 |
| 4 | Dependency Debt | HIGH | `deps-` | 1 |
| 5 | Test Debt | HIGH | `test-` | 1 |
| 6 | Performance Debt | HIGH | `perf-` | 1 |
| 7 | Data Debt | HIGH | `data-` | 1 |
| 8 | Documentation Debt | MEDIUM | `docs-` | 1 |
| 9 | Infrastructure Debt | MEDIUM | `infra-` | 1 |
| 10 | Process Debt | MEDIUM | `process-` | 1 |

## Quick Reference

### 1. Code Debt (CRITICAL) — 1 rule
- [code-smells.md](rules/code-smells.md) - Break down god classes, split high-cyclomatic functions (>10), eliminate duplicate blocks (>30 lines), remove dead code, group wide parameter lists into DTOs, and replace magic literals with typed constants.

### 2. Security Debt (CRITICAL) — 1 rule
- [security-debt.md](rules/security-debt.md) - Eliminate hardcoded credentials in source/git, validate all public input via strict schemas/FormRequests, hash passwords with Argon2id/Bcrypt, enforce explicit route authorization, and rate-limit sensitive endpoints.

### 3. Design Debt (HIGH) — 1 rule
- [design-architecture.md](rules/design-architecture.md) - Break circular module dependencies, enforce unidirectional layering (UI -> Domain -> Infrastructure), encapsulate implementation details, and eliminate shotgun surgery.

### 4. Dependency Debt (HIGH) — 1 rule
- [deps-lifecycle.md](rules/deps-lifecycle.md) - Audit dependencies for known CVEs (`composer audit`, `npm audit`), replace abandoned packages (>24mo unmaintained), prune unused dependencies, and keep packages within 2 major versions.

### 5. Test Debt (HIGH) — 1 rule
- [test-reliability.md](rules/test-reliability.md) - Ensure critical revenue/security paths have integration test coverage, quarantine or fix flaky tests immediately, track down disabled/skipped tests, and enforce test duration budgets (<10 minutes).

### 6. Performance Debt (HIGH) — 1 rule
- [perf-optimization.md](rules/perf-optimization.md) - Eliminate N+1 queries with eager loading, enforce pagination on all list endpoints, cache expensive read aggregations, and split frontend bundle chunks (<200KB initial load).

### 7. Data Debt (HIGH) — 1 rule
- [data-integrity.md](rules/data-integrity.md) - Maintain strict migration-only schema provenance, index foreign keys and query predicate columns, and enforce foreign-key constraints to prevent orphaned records.

### 8. Documentation Debt (MEDIUM) — 1 rule
- [docs-currency.md](rules/docs-currency.md) - Keep architecture decision records and README setup up-to-date, delete contradictory or stale comments, and document public APIs with OpenAPI or typed signatures.

### 9. Infrastructure Debt (MEDIUM) — 1 rule
- [infra-resilience.md](rules/infra-resilience.md) - Maintain supported LTS runtime engines (PHP/Node), treat build warnings as errors, migrate deprecated framework APIs, inject secrets via secret managers, and configure structured JSON logging with p95 telemetry.

### 10. Process Debt (MEDIUM) — 1 rule
- [process-governance.md](rules/process-governance.md) - Track technical debt in a prioritized ledger, retire stale feature flags and `@deprecated` markers after release cycles, prune aged `TODO`/`FIXME` comments (>6 months), and assign clear code ownership.

## Ranked Debt Ledger Template

```markdown
## Technical Debt Ledger

| Category | Finding | Location | Effort | Impact | ROI Priority |
|----------|---------|----------|--------|--------|--------------|
| security | Hardcoded Stripe test secret | `app/Services/Billing.php:14` | S | CRITICAL | P0 |
| perf | N+1 query loop on order listing | `app/Controllers/OrderController.php:42` | S | HIGH | P1 |
| data | Missing index on `order_items.order_id` | `database/migrations/2023_01_01_create_order_items.php` | S | HIGH | P1 |
| code | 850-line God class with 18 dependencies | `app/Services/OrderProcessor.php` | L | HIGH | P2 |
| deps | Guzzle 6.2 with CVE-2022-31160 | `composer.json` | M | HIGH | P2 |
| process | 3 feature flags active > 14 months | `app/Providers/AppServiceProvider.php:88` | S | LOW | P3 |
```

## How to Use

Read individual rule files in `rules/` for concise triggers, Bad vs Good comparisons, and actionable remediation steps.
