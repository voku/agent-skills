---
name: code-slop
description: Review PHP/Laravel and TypeScript/React code for qualitative maintainability patterns associated with low-signal generated or boilerplate-heavy changes: narration comments, weak naming, premature abstraction, defensive overdose, mock-everything tests, and style escape hatches. Use when reviewing AI-assisted PRs, auditing code-quality taste, or hardening a review checklist. These heuristics identify code problems, not author provenance.
license: MIT
metadata:
  author: agent-skills
  version: "2.0.0"
---

# Code Slop Detection

Taste-level review for code that passes mechanical checks but still inflates comprehension cost, hides failure semantics, or weakens tests. Where `technical-debt` measures quantitative debt such as complexity or duplication, this skill focuses on qualitative review signals.

## Evidence Boundary

These rules are **not an authorship detector**. A flagged pattern is evidence about the code, not proof that a human or an LLM wrote it. Report the concrete maintainability problem and observable evidence; do not infer provenance from style alone.

Before applying language-specific examples or tools, ground the target repository:

- inspect `composer.json` and the PHP/Laravel toolchain for PHP projects;
- inspect `package.json`, TypeScript config, and lint/test tooling for Node/React projects;
- prefer the changed diff and surrounding project conventions over generic style expectations;
- use configured analyzers and tests where they can mechanically verify a concern.

## When to Apply

Reference this skill when:
- reviewing an AI-assisted PR before merge;
- auditing a repository for boilerplate-heavy or low-signal code patterns;
- hardening a team's code-review checklist;
- refactoring bloated services or noisy test suites.

## Canonical Rule Boundaries

### Comments
- [comments-hygiene.md](rules/comments-hygiene.md) - Strip line-by-line narration, empty docblocks, closing-brace labels, and stale placeholders; reserve comments for non-obvious why/context.

### Naming
- [naming-hygiene.md](rules/naming-hygiene.md) - Prefer concise intention-revealing names over generic placeholders, redundant type suffixes, vague grab-bag names, or sentence-length identifiers.

### Over-engineering
- [over-eng-simplicity.md](rules/over-eng-simplicity.md) - Reject abstractions without demonstrated polymorphic or reuse pressure, pass-through wrappers, and dependency sprawl.

### Defensive Balance
- [defensive-balance.md](rules/defensive-balance.md) - Avoid swallowing failures or defending impossible states while missing real boundary protections such as timeouts and explicit recovery semantics.

### Test Authenticity
- [test-authenticity.md](rules/test-authenticity.md) - Test observable behavior, boundaries, and state changes instead of reproducing implementation logic through mocks.

### Style Fingerprints
- [style-fingerprints.md](rules/style-fingerprints.md) - Remove debug artifacts, type-system escape hatches, and trivial boilerplate that obscures intent.

## Review Output

When useful, summarize findings in a ledger:

| File | Verdict | Evidence | Suggested action |
|------|---------|----------|------------------|
| `path/to/file` | CLEAN / SUSPICIOUS / INFLATED / CRITICAL | Concrete observed pattern | Smallest corrective action |

Verdicts are review prioritization aids, not provenance claims. Prefer the underlying findings over a score when the score would imply more certainty than the evidence supports.

## How to Use

Read only the rule files relevant to the current change. Keep findings tied to concrete code, repository conventions, and mechanical evidence where available. `README.md`, `AGENTS.md`, and `metadata.json` are supporting projections; if they disagree with this file or `rules/`, follow the canonical source and repair the projection.
