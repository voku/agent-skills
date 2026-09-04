# Sections

This file defines the section ordering, severity, and summary used by this skill.

---

## 1. Native Types First (sa-native-types-first)

**Impact:** CRITICAL
**Description:** PHPDoc used where a real PHP type would have made the contract enforceable at runtime.

## 2. Shape & Generic Precision (sa-shape-precision)

**Impact:** CRITICAL
**Description:** Loose array and mixed types that force every caller to re-validate a known structure.

## 3. Contract Honesty (sa-contract-honesty)

**Impact:** HIGH
**Description:** A stricter, correct type relaxed to satisfy the analyzer instead of supplying the missing proof.

## 4. Root-Cause Over Inline Assertion (sa-root-cause-typing)

**Impact:** HIGH
**Description:** The same value re-asserted at every call site because its source was never typed.

## 5. Ignore & Baseline Scoping (sa-ignore-scoping)

**Impact:** MEDIUM
**Description:** Broad suppressions that also hide the next, unrelated defect.

## 6. Analyzer Extensions (sa-analyzer-extensions)

**Impact:** MEDIUM
**Description:** Casts around dynamic helpers the analyzer was never taught about.
