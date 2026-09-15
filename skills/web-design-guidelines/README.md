# Web Design Guidelines & Accessibility Audit

Portable UI/UX and accessibility review guidance for semantic structure, keyboard/focus behavior, ARIA and contrast, forms, motion, and layout stability.

## Canonical Source

`SKILL.md` defines activation, focused-audit semantics, evidence boundaries, and the limit against unsupported WCAG conformance claims. The files under `rules/` contain the canonical detailed guidance. This README is a routing projection only; it must not own a second rule inventory, count, WCAG checklist, or compiled example set.

## When to Use

Use this skill for focused accessibility reviews, UI audits, keyboard/focus checks, accessible forms, contrast/ARIA issues, reduced-motion handling, or layout-stability concerns.

## Routing

1. Establish the actual pages/components and behavior in scope.
2. Read `SKILL.md` first.
3. Load only relevant canonical rule files.
4. Combine source inspection with rendered/runtime evidence where required.
5. Report evaluated checks and unresolved evidence explicitly.

## Conformance Boundary

This focused audit does not establish WCAG A/AA/AAA conformance. Formal conformance requires evaluating the applicable WCAG success criteria across the claimed scope. Do not convert a partial checklist or automated scan into a conformance claim.

## Projection Boundary

If this projection disagrees with `SKILL.md` or `rules/`, follow the canonical source and repair the projection. Do not copy current rule IDs, counts, WCAG tables, or long examples into this file.
