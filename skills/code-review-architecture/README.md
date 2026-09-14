# Code Review Architecture

Targeted architecture review lens for design quality, coupling, cohesion, boundaries, and rollback-safe side effects.

## Canonical source

`SKILL.md` and `rules/` are the canonical contract for this skill. This README is a summary projection and must not introduce an independent rule inventory.

## Consolidated rules

| Rule | Priority | Primary focus |
|------|----------|---------------|
| `arch-transaction-side-effects` | CRITICAL | External side effects outside DB transactions |
| `arch-separation-domain-presentation` | CRITICAL | Domain/presentation separation |
| `arch-coupling-cohesion` | HIGH | Dependency direction and cohesive ownership |
| `arch-unidirectional-data-flow` | HIGH | Explicit data flow and immutable transfer objects |
| `arch-contract-rigor-extensibility` | MEDIUM | Narrow contracts and composition |

## Usage

Use this lens when architecture, module boundaries, transaction ownership, or structural maintainability is the dominant concern. Hand off when performance, error handling, security, type safety, or simplicity becomes primary.

## References

- [Pi Ensemble architecture lens](https://raw.githubusercontent.com/randomm/pi-ensemble/main/skill/code-review-architecture/SKILL.md)
- [Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
