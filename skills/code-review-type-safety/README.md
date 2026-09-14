# Code Review Type Safety

Targeted type-safety review lens for honest contracts, native types, shape validation, symmetric rigor, and truthful nullability.

## Canonical source

`SKILL.md` and `rules/` are the canonical contract for this skill. This README is a summary projection and must not introduce an independent rule inventory.

## Consolidated rules

| Rule | Priority | Primary focus |
|------|----------|---------------|
| `type-strict-native-declarations` | CRITICAL | Native declarations and strict comparison |
| `type-shape-validation-boundaries` | CRITICAL | DTO/shape validation at trust boundaries |
| `type-symmetric-rigor` | HIGH | Symmetric contracts across sibling paths |
| `type-nullability-truthfulness` | HIGH | Honest nullable contracts |

## Usage

Use this lens when typing, schema alignment, coercion, nullability, or contract honesty dominates the review. Hand off when security, architecture, simplicity, or failure behavior becomes primary.

## References

- [Pi Ensemble type-safety lens](https://raw.githubusercontent.com/randomm/pi-ensemble/main/skill/code-review-type-safety/SKILL.md)
- [PHPStan Documentation](https://phpstan.org/user-guide/getting-started)
