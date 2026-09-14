---
id: core-law-demeter
title: Law of Demeter (LoD)
category: core-principles
priority: critical
triggers: [train-wreck-calls, a-getB-getC-doD, dot-chaining-internals, tight-structural-coupling]
tags: [law-of-demeter, coupling, least-knowledge, encapsulation]
related: [core-encapsulation, solid-srp, core-separation-concerns]
---

# Law of Demeter (LoD)

**Trigger Anchor:** Principle of Least Knowledge. Talk only to immediate friends; do not navigate through an object's internal structure to reach indirect collaborators.

---

### Bad (Train Wreck Calls Traversing Internal Objects)
```typescript
// ❌ Caller knows internal structural hierarchy across 4 layers
const zip = order.getCustomer().getAddress().getGeoLocation().getZipCode();

// Calling methods on deep internals:
order.getCustomer().getWallet().charge(100);
```

### Good (Ask the Immediate Friend to Fulfill the Intent)
```typescript
// ✅ Delegate to immediate collaborator; internals remain encapsulated
const zip = order.getDeliveryZipCode();

// Or tell the immediate collaborator what to do:
order.chargeCustomer(100);
```
