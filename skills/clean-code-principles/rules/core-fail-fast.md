---
id: core-fail-fast
title: Fail Fast Principle
category: core-principles
priority: critical
triggers: [deep-nested-if-statements, arrow-anti-pattern, silent-null-returns, swallowed-exceptions, late-error-detection]
tags: [fail-fast, guard-clauses, validation, defensive-programming]
related: [solid-lsp, core-encapsulation]
---

# Fail Fast Principle

**Trigger Anchor:** Validate inputs, state, and preconditions immediately at the boundary. Exit early with guard clauses rather than nesting logic.

---

### Bad (Deeply Nested Arrow Anti-Pattern & Silent Nulls)
```typescript
// ❌ Deep nesting, late failure, hard to read
function processUser(user: User | null, config: Config | null) {
  if (user !== null) {
    if (user.isActive) {
      if (config !== null) {
        // Deeply nested actual work
        return save(user);
      }
    }
  }
  return null; // Silent failure masks bugs!
}
```

### Good (Early Return Guard Clauses)
```typescript
// ✅ Preconditions validated at the top; flat and obvious happy path
function processUser(user: User, config: Config) {
  if (!user.isActive) throw new InactiveUserError(user.id);

  // Flat, unindented core execution
  return save(user, config);
}
```
