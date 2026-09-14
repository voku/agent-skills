# Rule Sections

## Priority Levels

| Level | Description | When to Apply |
|-------|-------------|---------------|
| CRITICAL | Bounds, clamping logic, and mathematical invariants | Range transformations, clamps, and threshold comparisons |
| HIGH | Abstraction level, control flow nesting, and dead code | Method extractions, branching, and refactor cleanups |
| MEDIUM | Naming precision and comment hygiene | Code clarity and self-documentation |

## Section Overview

### 1. Premature Abstraction (`abstraction`)
- **Impact:** HIGH
- **Rules:** `simp-premature-abstraction`
- **Description:** Avoiding single-implementation interfaces, speculative factories, and bespoke wrappers built solely for unit test mocking.

### 2. Shallow Control Flow (`cognitive-load`)
- **Impact:** HIGH
- **Rules:** `simp-shallow-control-flow`
- **Description:** Early return guard clauses flattening nested if/else pyramids; eliminating boolean flag parameter anti-patterns.

### 3. Bounds & Range Clarity (`complexity`)
- **Impact:** CRITICAL
- **Rules:** `simp-bounds-range-clarity`
- **Description:** Verifying mathematical bounds to prevent collapsed clamp ranges, dead branches, and tautological conditions.

### 4. Intention-Revealing Naming (`readability`)
- **Impact:** MEDIUM
- **Rules:** `simp-intention-revealing-naming`
- **Description:** Replacing cryptic or manager-style names with precise domain verbs; removing comments that merely restate code.

### 5. Dead Code & Symmetry (`maintainability`)
- **Impact:** HIGH
- **Rules:** `simp-dead-code-elimination`
- **Description:** Removing unreferenced methods, unused parameters, and commented-out code; enforcing symmetric handling across branches.
