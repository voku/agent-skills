# PHP Best Practices — Agent Projection

**Version:** 4.0.0  
**Rules:** 15 consolidated rules across 8 categories  
**PHP:** 8.0 - 8.5

This file is a compact agent projection. The canonical contract is `SKILL.md` plus the files under `rules/`. Do not add independent PHP semantics here.

## Fast path

1. Detect the project's supported PHP version before suggesting syntax or language features.
2. Prefer explicit native types, strict contracts, immutable/value-oriented design, and observable failures.
3. Use PHPDoc only as a precision layer where native PHP cannot express enough.
4. Keep changes scoped to the verified problem; avoid unrelated modernization.
5. Validate with the repository's configured tests, PHPStan/static analysis, and formatter/fixer; report observed results only.

## Rule index

| Category | Canonical rules |
|---|---|
| Types | `type-strict-declarations`, `type-composition` |
| Modern PHP | `modern-enums`, `modern-readonly`, `modern-property-hooks`, `modern-constructor-arguments`, `modern-expressions`, `modern-attributes` |
| Error Handling | `error-handling` |
| Security | `sec-core-security` |
| Performance | `perf-efficiency` |
| Architecture & Design | `design-value-objects`, `solid-principles` |
| PSR Standards | `psr-standards` |
| Quality Tooling & Analysis | `tooling-static-analysis` |

## Version boundary

Only apply features available in the project/runtime version. In particular, PHP 8.4-only syntax such as property hooks or asymmetric visibility must not be suggested to an older target merely because the skill knows about it.

## Type and design boundary

- Native PHP types are authoritative where they can express the contract.
- Precise PHPDoc may add generics, array shapes, class-strings, ranges, and other static-analysis detail.
- Avoid `mixed` when a stable explicit type can be expressed.
- Prefer small immutable value objects when they carry real domain invariants.
- Avoid magic-heavy APIs when explicit typed methods are practical.

## Error and security boundary

- Do not suppress diagnostics to make validation quiet.
- Prefer narrow, contextual exceptions and explicit failure handling.
- Use parameterized SQL, context-aware output escaping, supported password hashing APIs, and validated upload boundaries.

## Evidence contract

- Use the repository's own validation commands rather than inventing replacements.
- PHPStan should run at the strictest configured level for the project.
- Formatting/style checks use the repository's configured toolchain.
- A command is evidence only when its actual result was observed.

## Canonical ownership

Detailed examples, exceptions, and version-specific guidance live in the 15 canonical rule files. If this projection disagrees with `SKILL.md` or a rule file, the canonical skill surface wins and this projection must be corrected.