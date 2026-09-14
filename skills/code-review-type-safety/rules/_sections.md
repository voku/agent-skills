# Rule Sections

## Priority Levels

| Level | Description | When to Apply |
|-------|-------------|---------------|
| CRITICAL | Strict native types, strict comparisons, and boundary shape validation | Class properties, external payloads, and entity comparisons |
| HIGH | Symmetric rigor across branches and honest nullability contracts | Method returns, normalization routines, and caller null checks |

## Section Overview

### 1. Strict Native Declarations (`type-correctness`)
- **Impact:** CRITICAL
- **Rules:** `type-strict-native-declarations`
- **Description:** Native property types, strict comparisons (`===`), and eliminating falsy return value folding.

### 2. Shape Validation at Boundaries (`type-safety`)
- **Impact:** CRITICAL
- **Rules:** `type-shape-validation-boundaries`
- **Description:** Typed DTOs and validated array shapes at external trust boundaries; avoiding unconstrained `mixed`.

### 3. Symmetric Rigor (`asymmetric-rigor`)
- **Impact:** HIGH
- **Rules:** `type-symmetric-rigor`
- **Description:** Symmetric type handling across sibling branches and consistent normalization rules.

### 4. Honest Nullability (`nullability`)
- **Impact:** HIGH
- **Rules:** `type-nullability-truthfulness`
- **Description:** Truthful nullable contracts (`?Type`), explicit OrThrow methods, and eliminating false non-null assertions.
