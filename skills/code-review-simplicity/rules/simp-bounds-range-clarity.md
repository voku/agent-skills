---
id: simp-bounds-range-clarity
title: "Collapsed Bounds, Redundant Clamping, and Constant Outputs"
category: complexity
priority: CRITICAL
triggers: [collapsed-range, redundant-min-max, dead-branch-clamp, tautological-comparison]
tags: [simplicity, bounds, math-logic, clamping, dead-code]
---

# Collapsed Bounds, Redundant Clamping, and Constant Outputs

**Trigger Anchor:** Check mathematical bounds and condition ranges to prevent dead branches, collapsed min/max clamping where min > max or output is invariant, and tautological conditions.

---

### Bad
```php
// ❌ Collapsed clamp bounds: min is greater than max, resulting in constant or inverted output
function clampScore(int $score): int
{
    // Bug: max(50, ...) means value will never be below 50!
    // Combined with min(20, ...), output is perpetually locked to 50!
    return max(50, min(20, $score));
}

// ❌ Dead range condition that can never be true
function validatePort(int $port): bool
{
    // Impossible condition: a number cannot be both < 1024 and > 65535
    if ($port < 1024 && $port > 65535) {
        throw new InvalidArgumentException('Invalid port range'); // Unreachable!
    }
    return true;
}

// ❌ Redundant double comparison after type narrowing
if ($status === 'active' || ($status === 'active' && $count > 0)) {
    // Second sub-clause is completely redundant
}
```

### Good
```php
// ✅ Correct bounding: min lower bound is strictly less than max upper bound
function clampScore(int $score): int
{
    $min = 0;
    $max = 100;
    return max($min, min($max, $score));
}

// ✅ Correct disjoint range check using OR
function validatePort(int $port): bool
{
    if ($port < 1 || $port > 65535) {
        throw new InvalidArgumentException('Port must be between 1 and 65535.');
    }
    return true;
}

// ✅ Clean, simplified logical condition
if ($status === 'active') {
    // Clear and unambiguous
}
```
