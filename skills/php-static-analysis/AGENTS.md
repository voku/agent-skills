# PHP Static Analysis — Agent Projection

**Version:** 2.0.0  
**Rules:** 5 consolidated rules  
**License:** MIT

This file is a compact projection for agents. The canonical skill contract is `SKILL.md` plus the files under `rules/`. Do not add independent static-analysis semantics here.

## Fast Path

1. Resolve analyzer failures by making the analyzer's claim untrue, not by hiding the diagnostic.
2. Decide whether the problem is a wrong contract or missing proof before editing types.
3. Fix the owning producer/boundary before adding repeated call-site assertions.
4. Keep ignores narrow, identified, and justified; prefer teaching the analyzer when dynamic behavior is real and reusable.
5. Verify with the target repository's actual analyzer command and report success only after observing its result.

## Canonical Rules

| Priority | Rule | Focus |
|----------|------|-------|
| CRITICAL | [`sa-native-types-first`](rules/sa-native-types-first.md) | Native PHP types and strict comparisons before PHPDoc workarounds |
| CRITICAL | [`sa-shape-precision`](rules/sa-shape-precision.md) | Precise array shapes, lists, generics, class-strings, and refined strings |
| HIGH | [`sa-contract-honesty`](rules/sa-contract-honesty.md) | Preserve correct strict contracts and prove boundary validity |
| HIGH | [`sa-root-cause-typing`](rules/sa-root-cause-typing.md) | Type producers/factories instead of repeating inline assertions |
| MEDIUM | [`sa-scoped-ignores-extensions`](rules/sa-scoped-ignores-extensions.md) | Narrow ignores, baselines, and analyzer extensions at the right boundary |

## Projection boundary

If this file disagrees with `SKILL.md` or a rule file, preserve the mismatch as evidence and follow the canonical source. Update this projection only when its routing/interface summary changes.
