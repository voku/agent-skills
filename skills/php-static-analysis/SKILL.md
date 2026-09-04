---
name: php-static-analysis
description: Implementation guidance for making PHP code provably typed under a strict static analyzer - native types first, precise array shapes and generics, honest contracts, scoped ignores, and analyzer extensions instead of inline casts. Triggers on "phpstan error", "psalm error", "type precision", "array shape", "class-string", "baseline", and related static-analysis work.
license: MIT
metadata:
  author: Agent Skills Team
  version: "1.0.0"
---

# PHP Static Analysis

Implementation guidance for raising the precision of PHP code under a strict static analyzer. This is the writing counterpart to a review lens: it says how to make the contract true, not just how to spot that it is false. Contains 6 rules across 6 focused categories.

## When to Apply

Reference these guidelines when:
- An analyzer error must be resolved without weakening the contract
- A public API, factory, or collection helper needs an analyzable signature
- Inline casts, `@var` annotations, or a growing baseline are being used to keep the build green
- A repository is raising its analysis level and needs an order of attack

## Rule Categories by Priority

| Priority | Category | Impact | Prefix |
|----------|----------|--------|--------|
| 1 | Native Types First | CRITICAL | `sa-native-types-first` |
| 2 | Shape & Generic Precision | CRITICAL | `sa-shape-precision` |
| 3 | Contract Honesty | HIGH | `sa-contract-honesty` |
| 4 | Root-Cause Over Inline Assertion | HIGH | `sa-root-cause-typing` |
| 5 | Ignore & Baseline Scoping | MEDIUM | `sa-ignore-scoping` |
| 6 | Analyzer Extensions | MEDIUM | `sa-analyzer-extensions` |

## Quick Reference

- `sa-native-types-first` - Solve it with a PHP type before reaching for PHPDoc
- `sa-shape-precision` - `array{...}`, `list<T>`, `non-empty-*`, `class-string<T>` instead of `array` and `mixed`
- `sa-contract-honesty` - Do not relax a stricter type just because the analyzer cannot prove it today
- `sa-root-cause-typing` - Type the source instead of asserting the result at every call site
- `sa-ignore-scoping` - Scope an ignore to the exact reported line or file family, never a directory
- `sa-analyzer-extensions` - Teach the analyzer about dynamic helpers instead of casting around them

## Scope Discipline

### In Scope

- Typing decisions in the code under change and its direct call sites
- The smallest contract change that makes the analyzer's claim true
- Deciding between a wrong contract and a proof gap
- Keeping an existing strict contract intact while narrowing inputs earlier

### Out of Scope

- Repository-wide type migrations that were not requested
- Style or naming changes unrelated to the reported error
- Silencing an error whose underlying behavior is genuinely wrong - that is a bug, not a typing task

## Output Format

State, per finding: the analyzer message, the real cause (wrong contract or missing proof), the chosen fix at its owning layer, and the command that verified it. Claim a pass only after observing the analyzer's exit code on the changed scope.

## Severity Scale

- **CRITICAL** - The declared contract is false at runtime; callers can be handed a value the signature forbids
- **HIGH** - The contract is true but unprovable, so every caller re-asserts it
- **MEDIUM** - Precision loss that spreads: a widening ignore, a baseline entry, or a cast that hides the source
