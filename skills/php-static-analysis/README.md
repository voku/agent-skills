# PHP Static Analysis

Implementation guidance for making PHP code provably typed under a strict static analyzer.

## Overview

This skill provides:
- An order of attack for analyzer errors: native type, then shape, then proof
- The distinction between a wrong contract and a proof gap
- Root-cause typing instead of per-call-site assertions
- Scoping rules for ignores and baselines
- When to teach the analyzer with an extension or a custom rule

## Rules

| Rule | Impact |
|------|--------|
| `sa-native-types-first` | CRITICAL |
| `sa-shape-precision` | CRITICAL |
| `sa-contract-honesty` | HIGH |
| `sa-root-cause-typing` | HIGH |
| `sa-ignore-scoping` | MEDIUM |
| `sa-analyzer-extensions` | MEDIUM |

## Relationship to the review lenses

`code-review-type-safety` is the review counterpart: it finds the weak contract in a diff.
This skill is what you apply while writing the fix.
