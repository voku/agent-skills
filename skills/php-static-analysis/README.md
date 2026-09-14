# PHP Static Analysis

Implementation guidance for making PHP code provably typed under a strict static analyzer.

**Version:** 2.0.0  
**Rules:** 5 consolidated rules

## Canonical source

`SKILL.md` and `rules/` are the canonical contract for this skill. This README is a summary projection and must not introduce independent analyzer semantics.

## Overview

This skill provides:
- An order of attack for analyzer errors: native type, then shape/precision, then proof
- The distinction between a wrong contract and a proof gap
- Root-cause typing instead of per-call-site assertions
- Scoped ignores and baselines when suppression is genuinely required
- Analyzer extensions when dynamic behavior is real and reusable

## Rules

| Rule | Impact |
|------|--------|
| `sa-native-types-first` | CRITICAL |
| `sa-shape-precision` | CRITICAL |
| `sa-contract-honesty` | HIGH |
| `sa-root-cause-typing` | HIGH |
| `sa-scoped-ignores-extensions` | MEDIUM |

## Relationship to the review lenses

`code-review-type-safety` is the review counterpart: it finds the weak contract in a diff. This skill is what you apply while writing the fix.
