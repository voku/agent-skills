---
name: clean-code-principles
description: SOLID principles, design patterns, DRY, KISS, and clean code fundamentals. Use when reviewing architecture, checking code quality, refactoring, or discussing design decisions. Triggers on "review architecture", "check code quality", "SOLID principles", "design patterns", or "clean code".
license: MIT
metadata:
  author: Agent Skills
  version: "1.1.0"
---

# Clean Code Principles

Fundamental software design principles, SOLID, design patterns, and clean code practices. Language-agnostic guidelines for writing maintainable, scalable software.

## When to Apply

Reference these guidelines when:
- Designing new features or systems
- Reviewing code architecture
- Refactoring existing code
- Discussing design decisions
- Improving code quality

## Rule Categories by Priority

| Priority | Category | Impact | Prefix | Rules |
|----------|----------|--------|--------|-------|
| 1 | SOLID Principles | CRITICAL | `solid-` | 5 |
| 2 | Core Principles | CRITICAL | `core-` | 8 |
| 3 | Design Patterns | HIGH | `pattern-` | 1 |

## Quick Reference

### 1. SOLID Principles (CRITICAL)

- `solid-srp` - Single Responsibility Principle (class and function levels)
- `solid-ocp` - Open/Closed Principle (extension via abstraction)
- `solid-lsp` - Liskov Substitution Principle (contracts, invariants, and preconditions)
- `solid-isp` - Interface Segregation Principle (focused, client-specific interfaces)
- `solid-dip` - Dependency Inversion Principle (depend on abstractions, inject dependencies)

### 2. Core Principles (CRITICAL)

- `core-dry` - Don't Repeat Yourself (single source of truth & logic extraction)
- `core-kiss` - Keep It Simple, Stupid (simplicity over over-engineering & readability)
- `core-yagni` - You Aren't Gonna Need It (avoid speculative features and premature abstractions)
- `core-separation-concerns` - Different concerns in different modules
- `core-composition` - Favor composition over inheritance
- `core-law-demeter` - Only talk to immediate friends (principle of least knowledge)
- `core-fail-fast` - Detect and report errors early
- `core-encapsulation` - Hide implementation details

### 3. Design Patterns (HIGH)

- `pattern-repository` - Repository pattern for data access abstraction

## Essential Guidelines

For detailed examples and explanations, see the rule files in `rules/`:

- [solid-srp.md](rules/solid-srp.md) - Single Responsibility Principle
- [solid-ocp.md](rules/solid-ocp.md) - Open/Closed Principle
- [solid-lsp.md](rules/solid-lsp.md) - Liskov Substitution Principle
- [solid-isp.md](rules/solid-isp.md) - Interface Segregation Principle
- [solid-dip.md](rules/solid-dip.md) - Dependency Inversion Principle
- [core-dry.md](rules/core-dry.md) - Don't Repeat Yourself principle
- [core-kiss.md](rules/core-kiss.md) - Keep It Simple, Stupid
- [core-yagni.md](rules/core-yagni.md) - You Aren't Gonna Need It
- [pattern-repository.md](rules/pattern-repository.md) - Repository pattern for data access

### Quick Examples

```typescript
// Single Responsibility - one class, one job
class UserService {
  constructor(
    private validator: UserValidator,
    private repository: UserRepository,
  ) {}

  createUser(data: UserData) {
    this.validator.validate(data);
    return this.repository.create(data);
  }
}

// Dependency Inversion - depend on abstractions
interface Repository<T> {
  find(id: string): Promise<T | null>;
  save(entity: T): Promise<T>;
}

class OrderService {
  constructor(private repository: Repository<Order>) {}
}

// DRY - single source of truth
const EMAIL_REGEX = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
const isValidEmail = (email: string) => EMAIL_REGEX.test(email);

// Meaningful names over magic numbers
const MINIMUM_AGE = 18;
if (user.age >= MINIMUM_AGE) { /* ... */ }
```

## Output Format

When auditing code, output findings in this format:

```
file:line - [principle] Description of issue
```

Example:
```
src/services/UserService.ts:15 - [solid-srp] Class handles validation, persistence, and notifications
src/utils/helpers.ts:42 - [core-dry] Email validation duplicated from validators/email.ts
src/models/Order.ts:28 - [core-kiss] Deeply nested ternary should be replaced by early return function
```

## References

This skill is built on established software engineering principles:

### Core Books
- **Clean Code** by Robert C. Martin - Foundation for clean code practices
- **Design Patterns** by Gang of Four - Classic design pattern catalog
- **Refactoring** by Martin Fowler - Improving code structure
- **The Pragmatic Programmer** by Hunt & Thomas - Practical wisdom

### Online Resources
- [Refactoring Guru](https://refactoring.guru/) - Design patterns and code smells
- [Martin Fowler's Refactoring Catalog](https://refactoring.com/catalog/) - Comprehensive refactoring techniques
- [Uncle Bob's Clean Coder Blog](https://blog.cleancoder.com/) - Software craftsmanship articles

## Metadata

**Version:** 1.1.0  
**Status:** Active  
**Coverage:** 14 rules across 3 categories (SOLID, Core Principles, Design Patterns)  
**Last Updated:** 2026-09-14  

### Rule Statistics
- SOLID Principles: 5 rules
- Core Principles: 8 rules
- Design Patterns: 1 rule
