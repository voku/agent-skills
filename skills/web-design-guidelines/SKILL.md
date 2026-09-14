---
name: web-design-guidelines
description: UI/UX best practices and accessibility audit. Use when reviewing UI code, checking accessibility, running accessibility audits, auditing forms, or ensuring web interface best practices. Triggers on "audit accessibility", "check WCAG", "review UI", "check accessibility", "audit design", "review UX", or "check best practices".
license: MIT
metadata:
  author: agent-skills
  version: "2.1.0"
---

# Web Design Guidelines & Accessibility Audit

Curated, high-density UI/UX and WCAG accessibility guidelines covering semantic HTML, keyboard focus management, ARIA & contrast, accessible forms, and reduced motion / layout stability.

## Quick Reference

| Category | Impact | Rule File | Primary Focus |
|----------|--------|-----------|---------------|
| **Semantic Structure** | CRITICAL | [`a11y-semantic-structure`](rules/a11y-semantic-structure.md) | HTML5 landmarks, sequential heading hierarchy (`h1`→`h2`→`h3`), skip links, meaningful `alt` text |
| **Keyboard & Focus** | CRITICAL | [`a11y-keyboard-focus`](rules/a11y-keyboard-focus.md) | Tab navigation, visible focus rings, modal dialog focus trapping, return-on-close focus |
| **Contrast & ARIA** | CRITICAL | [`a11y-aria-contrast`](rules/a11y-aria-contrast.md) | WCAG AA contrast (4.5:1 / 3:1), non-color status markers, `aria-label` on icons, `aria-live` regions |
| **Accessible Forms** | HIGH | [`form-accessible-ux`](rules/form-accessible-ux.md) | Explicit `<label>`, `autoComplete`, `aria-describedby` error linkage, blur validation timing |
| **Motion & Stability** | CRITICAL | [`ux-motion-layout-stability`](rules/ux-motion-layout-stability.md) | `prefers-reduced-motion` compliance, CLS prevention with aspect ratios, `loading="lazy"` |

---

## Accessibility Audit Mode

When the user asks to "audit accessibility", "check WCAG compliance", or "review accessibility" — run this audit against their codebase:

### Step 1: Determine Scope
- If arguments provided (`$ARGUMENTS`): audit only those files or components
- If no arguments: audit all UI components and pages in the codebase

### Step 2: Run Verification Checklist
Work through each checkpoint, reporting exact `file:line` for failures:
1. **Semantic Landmarks & Hierarchy**: Check `<header>`, `<main>`, `<nav>`, `<footer>`, sequential heading levels (`h1`→`h2`), top-level skip link, and `alt` attributes on all images.
2. **Keyboard Navigation & Focus**: Verify all clickable elements are `<button>` or `<a>` (not `<div onClick>`), no positive `tabindex`, visible focus rings, and modal focus traps.
3. **Color & Contrast**: Validate 4.5:1 text contrast ratio, confirm no status is conveyed by color alone, and verify icon buttons have `aria-label`.
4. **Forms**: Check every input has an associated `<label>`, errors are linked via `aria-describedby`, input `type` and `autoComplete` attributes are present.
5. **Motion**: Ensure `@media (prefers-reduced-motion: reduce)` disables animations and transitions.

### Step 3: Audit Summary Output
```markdown
## Accessibility Audit Summary
- **PASS**: X checks
- **FAIL**: X checks
- **WCAG Level**: AA / Partial AA / Below AA
- **Top Priority Fixes**: (list the 3 most impactful FAIL items with code diffs)
```
