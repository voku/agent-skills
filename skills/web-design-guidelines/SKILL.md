---
name: web-design-guidelines
description: UI/UX and accessibility review guidance for semantic structure, keyboard/focus behavior, ARIA and contrast, forms, motion, and layout stability. Use for focused accessibility audits and interface review; do not treat the focused audit as a WCAG conformance certification.
license: MIT
metadata:
  author: agent-skills
  version: "2.1.0"
---

# Web Design Guidelines & Accessibility Audit

Portable UI/UX and accessibility guidance covering semantic HTML, keyboard focus management, ARIA and contrast, accessible forms, reduced motion, and layout stability.

## Grounding and Scope

Before auditing, establish the requested pages/components, rendering stack, design-system conventions, browser/runtime behavior, and the repository's available accessibility tooling. Use source inspection, rendered behavior, and configured automated checks as complementary evidence.

This skill provides a **focused accessibility review**, not a WCAG conformance certification. WCAG conformance levels require satisfying the applicable success criteria at that level across the claimed scope; the five rule boundaries below are intentionally narrower. Report which checks were actually evaluated and do not infer an overall A/AA/AAA conformance level from this checklist alone.

## Canonical Rule Boundaries

### Semantic Structure
- [a11y-semantic-structure.md](rules/a11y-semantic-structure.md) — semantic landmarks, headings, skip navigation, and meaningful image alternatives.

### Keyboard and Focus
- [a11y-keyboard-focus.md](rules/a11y-keyboard-focus.md) — keyboard operability, visible focus, dialog focus management, and focus restoration.

### ARIA and Contrast
- [a11y-aria-contrast.md](rules/a11y-aria-contrast.md) — accessible names, live regions, non-color cues, and contrast checks.

### Accessible Forms
- [form-accessible-ux.md](rules/form-accessible-ux.md) — labels, input metadata, error association, and validation UX.

### Motion and Layout Stability
- [ux-motion-layout-stability.md](rules/ux-motion-layout-stability.md) — reduced-motion handling, image/layout stability, and loading behavior.

## Focused Audit Mode

When asked to audit accessibility or review WCAG-related concerns:

1. **Determine scope**: use the requested paths/components; if scope is broad, inspect the relevant UI surface rather than claiming unseen coverage.
2. **Load the relevant canonical rules** and verify observable behavior where source alone is insufficient.
3. **Record evidence** per finding with file/location or rendered behavior when available.
4. **Classify each evaluated check** as PASS, FAIL, or N/A only when there is enough evidence.
5. **Prioritize fixes** by user impact and confidence rather than by a fabricated compliance score.

A useful summary is:

```markdown
## Accessibility Audit Summary
- Scope: pages/components actually reviewed
- Evaluated checks: X
- PASS: X
- FAIL: X
- N/A: X
- Not evaluated / requires runtime or assistive-technology verification: ...
- Top priority fixes: ...
- Conformance claim: not assessed by this focused audit
```

## Evidence Boundary

- Automated tools can identify useful defects but do not replace keyboard, focus, screen-reader, visual, and interaction checks where those are relevant.
- Do not claim WCAG conformance from partial source inspection or from these five rule groups alone.
- Prefer native semantics before adding ARIA.
- Validate contrast, focus, form behavior, and motion against the actual rendered interface where possible.
- The target repository owns its component library, design tokens, browser support, validation commands, and any formal compliance process.

`README.md`, `AGENTS.md`, and `metadata.json` are supporting projections. If they disagree with this file or `rules/`, follow the canonical source and repair the projection.
