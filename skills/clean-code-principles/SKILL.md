---
name: clean-code-principles
description: Language-agnostic design and maintainability guidance covering SOLID, DRY, KISS, YAGNI, separation of concerns, composition, Law of Demeter, fail-fast behavior, encapsulation, and the repository pattern. Use for architecture review, refactoring, and code-quality decisions.
license: MIT
metadata:
  author: Agent Skills
  version: "1.1.0"
---

# Clean Code Principles

Portable software-design heuristics for maintainable code. The canonical detailed guidance lives in the rule files below; apply only the rules relevant to the concrete design pressure rather than treating every principle as a mandate to add abstractions.

## Grounding and Decision Discipline

Before recommending a design change, inspect the target repository's architecture, language conventions, existing abstractions, tests/static analysis, and the actual change pressure.

- Prefer the smallest design that satisfies the current requirement.
- Treat DRY as shared knowledge/logic ownership, not an instruction to merge merely similar code.
- Apply SOLID principles to observed coupling/change pressure rather than mechanically adding interfaces or layers.
- Prefer composition when it reduces coupling; do not replace a simple inheritance relationship merely to satisfy a slogan.
- Introduce patterns such as Repository only when they solve a concrete boundary or substitution problem.
- Preserve project-local architecture and stronger task/repository instructions.

## Canonical Rule Boundaries

### SOLID Principles
- [solid-srp.md](rules/solid-srp.md) — Single Responsibility Principle.
- [solid-ocp.md](rules/solid-ocp.md) — Open/Closed Principle.
- [solid-lsp.md](rules/solid-lsp.md) — Liskov Substitution Principle.
- [solid-isp.md](rules/solid-isp.md) — Interface Segregation Principle.
- [solid-dip.md](rules/solid-dip.md) — Dependency Inversion Principle.

### Core Principles
- [core-dry.md](rules/core-dry.md) — avoid duplicated knowledge and logic without creating accidental coupling.
- [core-kiss.md](rules/core-kiss.md) — prefer the simplest correct design.
- [core-yagni.md](rules/core-yagni.md) — avoid speculative features and abstractions.
- [core-separation-concerns.md](rules/core-separation-concerns.md) — keep unrelated responsibilities behind appropriate boundaries.
- [core-composition.md](rules/core-composition.md) — use composition where it produces clearer, less coupled behavior.
- [core-law-demeter.md](rules/core-law-demeter.md) — limit knowledge of distant collaborators.
- [core-fail-fast.md](rules/core-fail-fast.md) — surface invalid states and failures close to their cause.
- [core-encapsulation.md](rules/core-encapsulation.md) — hide implementation detail behind meaningful contracts.

### Design Pattern
- [pattern-repository.md](rules/pattern-repository.md) — repository abstraction for an appropriate data-access boundary.

## Review Output

When reporting a finding, tie it to observable code and change pressure rather than naming a principle alone. Prefer:

```text
file:line - [rule-id] observed problem -> smallest useful correction
```

If a principle does not materially improve the current design, do not report it merely because the code could be made more abstract.

`README.md`, `AGENTS.md`, and `metadata.json` are supporting projections. If they disagree with this file or `rules/`, follow the canonical source and repair the projection.
