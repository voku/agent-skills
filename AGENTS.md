# Agent Skills Repository — Operational Guide

This repository contains portable engineering skills for AI coding agents.

## Repository ownership boundary

This repository owns **portable, tool-neutral engineering guidance**. It must not become a second canonical home for instructions whose correctness depends on a concrete tool's CLI, API, file layout, schema, generated artifacts, or lifecycle behavior.

For the `voku/agent-*` stack specifically:

- `voku/agent-recall-compiler` owns machine-readable operating-prompt recipes, typed arguments, rendering/template identity, and recipe applicability.
- `voku/agent-loop` owns governed Contract/Run lifecycle, approvals, canonical next actions, mutation authority, and workflow prompt envelopes.
- This repository may teach reusable prompting, review, testing, and implementation heuristics, but must not keep a second canonical copy of tool-owned behavior.
- When reusable guidance becomes coupled to one tool, move the executable/canonical form to that tool's repository and leave only the portable principle here.

Before adding or materially changing guidance, follow `CONTRIBUTING.md` and check whether an existing semantic owner already exists.

## Canonical skill contract

For each skill, treat these as authoritative in this order:

1. `skills/<skill>/SKILL.md` for scope, trigger, routing, and the compact skill contract.
2. `skills/<skill>/rules/*.md` for detailed rule semantics where rule files exist.
3. `README.md`, `AGENTS.md`, and `metadata.json` inside a skill directory are supporting projections only. They must not introduce independent rule semantics, counts, or tool contracts.

Do not infer current rule inventory from this root file. Inspect the selected skill's canonical contract instead.

---

## Rule Priority Model

When guidance from different skills conflicts, resolve it in this order:

| Priority | Category | Examples |
|----------|----------|---------|
| 1 | **Safety / Security** | OWASP, injection, authentication, encryption |
| 2 | **System / Developer constraints** | PHP version, framework version, detected stack |
| 3 | **User request** | Explicit instructions from the user |
| 4 | **Project workflow rules** | Git workflow, PR conventions, testing requirements |
| 5 | **Style / Formatting preferences** | Naming, spacing, comment style |

When uncertainty is factual, investigate current source and configuration first. Ask the user only when the remaining gap requires human intent, domain authority, permission, or risk acceptance.

---

## Step 1 — Detect Context

Before applying a skill, identify the relevant project stack from repository evidence rather than assumptions.

### PHP / Laravel

```bash
grep '"php"' composer.json
php -v
grep '"laravel/framework"' composer.json
grep '"pestphp/pest"' composer.json
grep '"phpunit/phpunit"' composer.json
```

### Frontend

```bash
grep '"react"' package.json
grep '"vite"' package.json
grep '"@inertiajs/react"' package.json
grep 'inertia-laravel' composer.json
grep '"@tanstack/react-query"' package.json
grep '"zustand"' package.json
```

Use detected versions and installed tooling. Do not invent unavailable commands or framework capabilities.

---

## Step 2 — Activate Relevant Skills

Load only skills that match the task and detected stack.

| Skill | Activate when... |
|-------|-----------------|
| `laravel-best-practices` | Writing or reviewing PHP / Laravel code |
| `laravel-inertia-react` | Project has `@inertiajs/react` and Laravel |
| `laravel-testing` | Writing tests in a Laravel project |
| `laravel-owasp-security` | Security audit or auth/payment work |
| `laravel-database-optimization` | Query performance, N+1, Eloquent optimization |
| `laravel-ai-sdk` | Code uses `Laravel\Ai` namespace or AI SDK features |
| `laravel-mcp` | Building or consuming MCP servers |
| `php-best-practices` | PHP implementation guidance |
| `php-static-analysis` | Strict PHPStan/Psalm typing and analyzer work |
| `operational-prompting` | Designing repo-owned agent instructions, task contracts, or validation guidance |
| `react-vite-best-practices` | React + Vite work |
| `typescript-react-patterns` | TypeScript in React |
| `tailwind-best-practices` | Tailwind CSS work |
| `state-management` | React Query, Zustand, or complex client state |
| `web-design-guidelines` | UI/UX, accessibility, responsive layout |
| `api-design-patterns` | REST API design/review |
| `clean-code-principles` | Architecture, refactoring, design decisions |
| `code-review-architecture` | Targeted architecture review |
| `code-review-error-handling` | Failure paths, retries, timeouts, resilience |
| `code-review-performance` | Bottlenecks, scalability, resource-heavy diffs |
| `code-review-security` | Vulnerabilities, validation, auth, secrets |
| `code-review-simplicity` | Readability, complexity, duplication, bounds |
| `code-review-type-safety` | Typing, schema alignment, unsafe coercions |
| `testing-best-practices` | Language-agnostic test design |
| `git-workflow` | Commits, branches, PRs |
| `seo-best-practices` | Public pages, metadata, structured data |
| `engineering-codelight` | Evidence-first reasoning for non-trivial engineering work |

For `code-review-*`, prefer one dominant review lens first. Hand off to one smaller follow-up lens only when another concern becomes dominant.

---

## Step 3 — Apply the Canonical Contract

1. Read the selected skill's `SKILL.md`.
2. Load only rule files relevant to the current task.
3. Treat supporting `AGENTS.md`, README, and metadata as projections, not additional authorities.
4. Apply higher-impact findings before lower-impact style concerns when the skill defines severities.
5. If a projection disagrees with `SKILL.md` or `rules/`, preserve the mismatch as evidence and follow the canonical source.

---

## Step 4 — Generate Verifiable Output

- Use only features supported by the detected language/framework version.
- Lead reviews with the highest-impact proven findings.
- Provide a concrete correction for each defect.
- Do not report a command, test, or CI result as successful unless its result was actually observed.
- Preserve unknown or blocked states instead of turning missing evidence into success.

---

## Skills Overview

This table is intentionally count-free. Rule inventory belongs to each skill's canonical files and changes independently of this routing index.

| Skill | Primary focus |
|-------|---------------|
| `api-design-patterns` | REST, error handling, pagination |
| `clean-code-principles` | SOLID, DRY, design patterns |
| `code-review-architecture` | Coupling, boundaries, rollback-safe design |
| `code-review-error-handling` | Timeouts, retries, cleanup, observability |
| `code-review-performance` | Cost, queries, caching, concurrency |
| `code-review-security` | Injection, auth, validation, data protection |
| `code-review-simplicity` | Readability, complexity, duplication, bounds |
| `code-review-type-safety` | Typing, runtime validation, generics |
| `engineering-codelight` | Evidence, authority, uncertainty, falsification, recovery |
| `git-workflow` | Commits, branching, PRs |
| `laravel-ai-sdk` | Agents, tools, embeddings, testing |
| `laravel-best-practices` | Laravel architecture, Eloquent, security |
| `laravel-database-optimization` | Eloquent queries, indexing, caching, N+1 |
| `laravel-inertia-react` | Laravel + Inertia + React |
| `laravel-mcp` | MCP servers, tools, prompts, resources |
| `laravel-owasp-security` | OWASP, secure coding, auth |
| `laravel-testing` | Laravel tests, Pest/PHPUnit, factories, fakes |
| `operational-prompting` | Repo-owned instructions, scope, validation, portability |
| `php-best-practices` | PHP 8.x implementation practices |
| `php-static-analysis` | Strict analyzer-friendly PHP typing |
| `prd-writing` | PRDs, feature specs, requirements |
| `react-vite-best-practices` | Build optimization, code splitting |
| `seo-best-practices` | Metadata, structured data, Core Web Vitals |
| `state-management` | React Query, Zustand |
| `tailwind-best-practices` | Responsive Tailwind usage |
| `testing-best-practices` | Unit tests, mocking, coverage |
| `typescript-react-patterns` | TypeScript, React, generics |
| `web-design-guidelines` | Accessibility, UX, responsive design |

---

## Contributing

Use `CONTRIBUTING.md` as the contribution contract. New guidance must establish semantic ownership, evidence, non-duplication, whether structural enforcement is preferable, and what would make the prose removable later.
