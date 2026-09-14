---
id: core-composition
title: Composition Over Inheritance
category: core-principles
priority: critical
triggers: [deep-inheritance-hierarchy, fragile-base-class, override-throws-unsupported, forced-multiple-inheritance]
tags: [composition, inheritance, modularity, strategy-pattern]
related: [solid-srp, solid-dip, core-encapsulation]
---

# Composition Over Inheritance

**Trigger Anchor:** Favor composing objects from smaller, focused collaborators over deep class hierarchies. Prevent the fragile base class problem and LSP violations.

---

### Bad (Rigid Hierarchy with Incompatible Subtypes)
```typescript
// ❌ Base class forces behavior onto subclasses that cannot support it
class Bird {
  fly() { /* flying logic */ }
}

class Penguin extends Bird {
  fly() { throw new Error('Penguins cannot fly'); } // LSP violation & broken contract
}
```

### Good (Composed Behaviors & Capabilities)
```typescript
// ✅ Delegate capabilities via composed strategies
interface FlightBehavior { fly(): void; }

class WingsFlying implements FlightBehavior { fly() { /* flying */ } }
class NoFlying implements FlightBehavior { fly() { /* no-op or unlisted */ } }

class Bird {
  constructor(private flight: FlightBehavior) {}
  performFly() { this.flight.fly(); }
}

const eagle = new Bird(new WingsFlying());
const penguin = new Bird(new NoFlying());
```
