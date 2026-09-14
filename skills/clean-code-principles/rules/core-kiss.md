---
id: core-kiss
title: Keep It Simple, Stupid (KISS)
category: core-principles
priority: critical
triggers: [premature-patterns, cryptic-one-liners, nested-ternaries, pattern-overkill]
tags: [KISS, simplicity, readability, low-cognitive-load]
---

# Keep It Simple, Stupid (KISS)

**Trigger Anchor:** Choose the simplest correct solution that solves the verified problem. Optimize for readability and low cognitive load over cleverness.

---

### Bad (Over-Engineered Strategy for a Simple Check)
```typescript
// ❌ 3 classes and a factory for a simple role boolean
interface AccessStrategy { evaluate(u: User): boolean; }
class AdminAccessStrategy implements AccessStrategy { evaluate(u: User) { return u.isAdmin; } }
class AccessStrategyFactory { create(t: string) { return new AdminAccessStrategy(); } }
```

### Good (Direct and Obvious)
```typescript
// ✅ Straightforward function with zero indirection
function canAccessResource(user: User, resource: Resource): boolean {
  return user.isAdmin || resource.ownerId === user.id;
}
```

---

### Bad (Cryptic "Clever" Expressions)
```typescript
// ❌ Dense one-liner & nested ternaries
const res = d.filter(x => x.s === 'a' && x.t > Date.now() - 864e5).reduce((a, x) => ({ ...a, [x.c]: (a[x.c] || 0) + x.v }), {});
const rank = score > 90 ? 'gold' : score > 75 ? 'silver' : score > 50 ? 'bronze' : 'none';
```

### Good (Clear Intent & Linear Flow)
```typescript
// ✅ Intention-revealing code
const activeEvents = events.filter(e => e.isActive && isRecent(e.timestamp));

function getRank(score: number): string {
  if (score > 90) return 'gold';
  if (score > 75) return 'silver';
  if (score > 50) return 'bronze';
  return 'none';
}
```
