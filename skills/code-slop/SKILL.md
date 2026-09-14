---
name: code-slop
description: Detect AI-generated code patterns ("slop") in PHP/Laravel and TypeScript/React source — comment narration, generic naming, premature interfaces, defensive overdose, mock-everything tests, and style fingerprints. 6 rules across 6 categories. Use when reviewing AI-assisted PRs, auditing code for taste/quality, or hardening a code-review checklist. Triggers on "review for AI slop", "find AI patterns", "check code feels human", "audit code-quality taste".
license: MIT
metadata:
  author: agent-skills
  version: "2.0.0"
---

# Code Slop Detection

Taste-level review of code for AI-generated patterns ("slop"). Contains **6 consolidated rules across 6 categories** covering comments, naming, over-engineering, defensive overdose, test authenticity, and style fingerprints. Where `technical-debt` measures quantitative code debt (complexity, duplication, CVEs), this skill catches qualitative degradation: code that passes linting but inflates comprehension cost and hides defects.

## Metadata

- **Version:** 2.0.0
- **Scope:** PHP / Laravel + TypeScript / React (Node)
- **Rule Count:** 6 rules across 6 categories
- **License:** MIT

## Why this skill exists

AI-generated code frequently exhibits specific anti-patterns:
- **Narration comments** that merely restate syntax in English
- **Generic catches** that log and swallow errors, converting failures into silent corruption
- **Mock-everything tests** that verify test mocks instead of real business invariants
- **Premature interfaces** with only a single implementation and zero polymorphic need

The core insight: **reading cost > writing cost**. Code that cannot be quickly parsed and trusted creates comprehension debt.

## When to Apply

Reference this skill when:
- Reviewing an AI-assisted PR before merge
- Auditing a repo that has accepted heavy generative code contributions
- Hardening a team's code-review checklist against LLM boilerplate
- Refactoring bloated services and noisy test suites

## Rule Categories by Priority

| Priority | Category | Impact | Prefix | Rules |
|----------|----------|--------|--------|-------|
| 1 | Comments | CRITICAL | `comments-` | 1 |
| 2 | Naming | CRITICAL | `naming-` | 1 |
| 3 | Over-engineering | HIGH | `over-eng-` | 1 |
| 4 | Defensive Overdose | HIGH | `defensive-` | 1 |
| 5 | Test Slop | HIGH | `test-` | 1 |
| 6 | Style Fingerprints | MEDIUM | `style-` | 1 |

## Quick Reference

### 1. Comments (CRITICAL) — 1 rule
- [comments-hygiene.md](rules/comments-hygiene.md) - Strip line-by-line comment narration, empty docblocks, closing-brace tags (`} // end if`), and lingering placeholder/TODO markers; reserve comments strictly for non-obvious *why*.

### 2. Naming (CRITICAL) — 1 rule
- [naming-hygiene.md](rules/naming-hygiene.md) - Use concise, intention-revealing nouns and verbs without redundant type suffixes (`userArray`, `orderObj`), vague grab-bag suffixes (`*Helper`, `*Manager`), or run-on sentences (`theActiveAdminUser`).

### 3. Over-engineering (HIGH) — 1 rule
- [over-eng-simplicity.md](rules/over-eng-simplicity.md) - Reject premature single-implementation interfaces, single-method wrapper classes, pass-through delegate functions, and dependency sprawl; prefer top-level functions and direct classes.

### 4. Defensive Overdose (HIGH) — 1 rule
- [defensive-balance.md](rules/defensive-balance.md) - Stop swallowing errors in generic catch blocks or asserting impossible nulls on typed values; catch only specific recoverable exceptions and enforce real boundary defenses (timeouts, rate limits).

### 5. Test Slop (HIGH) — 1 rule
- [test-authenticity.md](rules/test-authenticity.md) - Test observable behavior, boundary conditions, and state changes instead of mocking every collaborator; eliminate "does-not-throw" smoke tests, mirror implementations, and uninspected snapshots.

### 6. Style Fingerprints (MEDIUM) — 1 rule
- [style-fingerprints.md](rules/style-fingerprints.md) - Eliminate debug dumps (`console.log`, `dd`), type-system escape hatches (`as any`, `@ts-ignore`), and trivial boolean boilerplate (`if (x) return true; else return false`).

## Audit Ledger Format

When auditing PRs or codebases, summarize findings in this ledger:

| File | Verdict | Top findings | Suggested action |
|------|---------|--------------|------------------|
| `app/Services/UserExportService.php` | INFLATED | Comment narration; `*Helper` suffix; missing external timeout | Strip comments; inline trivial helper; add timeout |
| `resources/js/Pages/Orders/Show.tsx` | CRITICAL | Type escapes (`as any`); mock-everything test; swallow catch | Narrow types; write behavioral test; propagate error |
| `app/Models/Order.php` | CLEAN | Direct methods, strict typing | None |

### Verdict Bands
- **CLEAN:** < 5% of touched lines flagged -> Ship
- **SUSPICIOUS:** 5–15% flagged -> Review flagged files before merge
- **INFLATED:** 15–30% flagged -> Strip boilerplate and comments, re-test
- **CRITICAL:** > 30% flagged -> Refactor section before merging

## How to Use

Read individual rule files in `rules/` for concise triggers, Bad vs Good code comparisons, and concrete PHP/TypeScript refactoring examples.
