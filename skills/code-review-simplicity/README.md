# Code Review Simplicity

Targeted simplicity review lens for readability, cognitive load, premature abstraction, dead logic, naming, and bounds clarity.

## Canonical source

`SKILL.md` and `rules/` are the canonical contract for this skill. This README is a summary projection and must not introduce independent review semantics or a separate rule inventory.

## Consolidated rules

| Rule | Priority | Primary focus |
|------|----------|---------------|
| `simp-premature-abstraction` | HIGH | Single-use interfaces, speculative factories, unnecessary wrappers |
| `simp-shallow-control-flow` | HIGH | Guard clauses, nesting, boolean flag control flow |
| `simp-bounds-range-clarity` | CRITICAL | Collapsed bounds, dead ranges, tautological comparisons |
| `simp-intention-revealing-naming` | MEDIUM | Domain verbs/nouns, affirmative booleans, noisy comments |
| `simp-dead-code-elimination` | HIGH | Unused code and asymmetric sibling branches |

## Usage

Use this lens for simplicity, readability, complexity, duplication, maintainability, or dead-range review. Keep it focused: if security, performance, architecture, type safety, or error handling becomes the dominant concern, hand off to one focused review lens instead of broadening this pass.

## References

- [Pi Ensemble simplicity lens](https://raw.githubusercontent.com/randomm/pi-ensemble/main/skill/code-review-simplicity/SKILL.md)
- [A Philosophy of Software Design](https://www.goodreads.com/book/show/39996759/a-philosophy-of-software-design)
