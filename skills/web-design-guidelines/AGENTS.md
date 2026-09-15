# Web Design Guidelines — Agent Projection

This file is a compact routing projection. The canonical contract is `SKILL.md` plus the files under `rules/`. Do not maintain a second accessibility rule inventory, count, WCAG checklist, or compiled example set here.

## Fast Path

1. Establish the exact pages/components and rendered interaction surface being reviewed.
2. Read `SKILL.md` first and load only the relevant canonical rule files.
3. Use source inspection, rendered behavior, keyboard/focus checks, and configured accessibility tooling as complementary evidence.
4. Report only checks actually evaluated; distinguish source-only evidence from runtime/assistive-technology verification.
5. Prioritize concrete user-impacting defects rather than manufacturing a compliance score.

## Ownership Boundary

- `SKILL.md` owns activation, audit scope, evidence semantics, and the boundary against unsupported conformance claims.
- `rules/` owns detailed semantic, keyboard/focus, ARIA/contrast, form, and motion/layout guidance.
- the target repository owns its component library, design tokens, browser support, accessibility tooling, validation commands, and any formal compliance process.
- W3C/WAI owns WCAG conformance requirements and version-sensitive standards guidance.
- this projection owns no independent accessibility semantics.

## Evidence Boundary

- A focused code/UI review is not a WCAG conformance certification.
- Do not infer A/AA/AAA from a partial checklist or automated tool result.
- Prefer native semantics before ARIA.
- Verify focus, contrast, forms, motion, and dynamic announcements against rendered behavior when source alone cannot prove the result.
- Record unevaluated or uncertain areas explicitly rather than converting missing evidence into PASS.

## Projection Boundary

If this file disagrees with `SKILL.md`, `rules/`, or stronger repository/task instructions, follow the authoritative source and repair this projection. Do not copy current rule IDs, counts, WCAG tables, or long examples back into this file.
