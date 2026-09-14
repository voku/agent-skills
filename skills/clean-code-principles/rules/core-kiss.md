---
id: core-kiss
title: Keep It Simple, Stupid (KISS)
category: core-principles
priority: critical
tags: [KISS, simplicity, readability, maintainability, over-engineering]
related: [core-yagni, core-dry, solid-srp]
---

# Keep It Simple, Stupid (KISS)

Choose the simplest correct solution that solves the verified problem. Code is read far more often than it is written; optimize for clarity, shallow control flow, and straightforward execution over cleverness or premature architectural layers.

---

## 1. Avoid Over-Engineering (Simplicity)

Do not introduce design patterns, abstract strategies, or multi-layered architectures for simple, straightforward requirements.

### Bad Example

```typescript
// ❌ Over-engineered solution for a simple permission check
interface AccessControlStrategy {
  evaluate(context: AccessContext): AccessDecision;
}

class AdminAccessControlStrategy implements AccessControlStrategy {
  evaluate(context: AccessContext): AccessDecision {
    return new AccessDecision(context.getUser().hasRole('admin'));
  }
}

class AccessControlStrategyFactory {
  create(type: string): AccessControlStrategy {
    if (type === 'admin') return new AdminAccessControlStrategy();
    throw new StrategyNotFoundException();
  }
}
```

### Good Example

```typescript
// ✅ Straightforward, readable, and immediately understandable
function canAccessResource(user: User, resource: Resource): boolean {
  if (user.isAdmin) return true;
  return resource.ownerId === user.id;
}
```

---

## 2. Avoid Cryptic "Clever" Code (Readability)

Avoid dense one-liners, nested ternary operators, and obscure bitwise tricks that save a few characters at the cost of high cognitive load for future readers.

### Bad Example

```typescript
// ❌ Cryptic one-liner and nested ternaries
const res = d.filter(x => x.s === 'a' && x.t > Date.now() - 864e5)
  .reduce((a, x) => ({ ...a, [x.c]: (a[x.c] || 0) + x.v }), {});

const status = score > 90 ? 'elite' : score > 75 ? 'senior' : score > 50 ? 'mid' : 'junior';
```

### Good Example

```typescript
// ✅ Clear, intention-revealing steps
const ONE_DAY_MS = 24 * 60 * 60 * 1000;
const cutoffTime = Date.now() - ONE_DAY_MS;

const activeRecentEvents = events.filter(e => e.status === 'active' && e.timestamp > cutoffTime);

const totalsByCategory: Record<string, number> = {};
for (const event of activeRecentEvents) {
  totalsByCategory[event.category] = (totalsByCategory[event.category] ?? 0) + event.value;
}

function getRank(score: number): string {
  if (score > 90) return 'elite';
  if (score > 75) return 'senior';
  if (score > 50) return 'mid';
  return 'junior';
}
```

## Why it Matters

1. **Reduced Debugging Time**: Simple, linear logic makes edge cases and bugs immediately visible.
2. **Lower Cognitive Load**: Team members and reviewers do not have to mentally deconstruct complex expressions.
3. **Easier Maintenance**: Simple code is easy to refactor or delete when requirements change.
