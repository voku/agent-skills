# PHP Best Practices

Modern PHP 8.x guidance for strict typing, modern language features, explicit error handling, security, performance, architecture, PSR standards, and static analysis.

**Version:** 4.0.0  
**Rules:** 15 consolidated rules across 8 categories  
**PHP:** 8.0 - 8.5

## Canonical source

`SKILL.md` and `rules/` are the canonical contract for this skill. This README is a summary projection and must not introduce independent operational semantics.

## Before applying the skill

Detect the project's supported PHP version from `composer.json` and, when relevant, the runtime. Do not recommend syntax newer than the project can execute.

Prefer explicit, analyzable code with strict contracts and safe defaults. Native types come first; PHPDoc adds precision only where PHP cannot express enough. Use `final`/`readonly` deliberately, avoid magic-heavy design, and make failure observable instead of suppressing it.

## Categories

| Category | Impact | Rules |
|---|---|---:|
| Types | CRITICAL | 2 |
| Modern PHP | CRITICAL | 6 |
| Error Handling | HIGH | 1 |
| Security | CRITICAL | 1 |
| Performance | MEDIUM | 1 |
| Architecture & Design | HIGH | 2 |
| PSR Standards | HIGH | 1 |
| Quality Tooling & Analysis | CRITICAL | 1 |

## Rule index

### Types
- `type-strict-declarations`
- `type-composition`

### Modern PHP
- `modern-enums`
- `modern-readonly`
- `modern-property-hooks`
- `modern-constructor-arguments`
- `modern-expressions`
- `modern-attributes`

### Error Handling
- `error-handling`

### Security
- `sec-core-security`

### Performance
- `perf-efficiency`

### Architecture & Design
- `design-value-objects`
- `solid-principles`

### PSR Standards
- `psr-standards`

### Quality Tooling & Analysis
- `tooling-static-analysis`

## Validation principle

Use the repository's own test/static-analysis/style commands and report observed results. For PHP projects, prefer the strictest configured PHPStan level and the repository's configured formatter/fixer. Do not claim a check passed merely because the command was suggested.

Read the canonical rule files for trigger-specific guidance and concrete examples.