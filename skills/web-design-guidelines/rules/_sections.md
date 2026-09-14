# Rule Sections

## Priority Levels

| Level | Description | When to Apply |
|-------|-------------|---------------|
| CRITICAL | Fundamental WCAG compliance & layout stability | Always |
| HIGH | Form interactions & input validation UX | Most interfaces |
| MEDIUM | Polish & responsive media loading | Scaling apps |

## Section Overview

### 1. Semantic Structure & Navigation (`a11y`)
- **Impact:** CRITICAL
- **Rules:** `a11y-semantic-structure`
- **Description:** Native HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<footer>`), sequential heading hierarchy (`h1` -> `h2` -> `h3`), top-level skip links, and contextual image `alt` descriptions.

### 2. Keyboard Navigation & Focus (`a11y`)
- **Impact:** CRITICAL
- **Rules:** `a11y-keyboard-focus`
- **Description:** Complete keyboard navigability without positive `tabindex`, modal focus trapping with return-on-close restoration, and prominent visible focus indicators.

### 3. Contrast, Labels, & Live Regions (`a11y`)
- **Impact:** CRITICAL
- **Rules:** `a11y-aria-contrast`
- **Description:** WCAG AA color contrast (4.5:1 / 3:1), redundant non-color status cues, accessible `aria-label` tags for icon buttons, and polite/assertive dynamic screen reader announcements via `aria-live`.

### 4. Form UX & Validation (`form`)
- **Impact:** HIGH
- **Rules:** `form-accessible-ux`
- **Description:** Explicit `<label>` associations, input type optimization (`email`, `tel`), browser `autoComplete` attributes, `aria-describedby` error linkages, and blur/submit validation timing.

### 5. Motion & Layout Stability (`motion`)
- **Impact:** CRITICAL
- **Rules:** `ux-motion-layout-stability`
- **Description:** Respecting `prefers-reduced-motion` media queries, eliminating Cumulative Layout Shift (CLS) with explicit dimensions / aspect ratios, and performant image loading.
