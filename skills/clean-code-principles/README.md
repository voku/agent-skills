# Clean Code Principles

Fundamental software design principles for writing maintainable, scalable code.

**Version:** 1.1.0  
**Rules:** 14 (5 SOLID + 8 Core + 1 Pattern)  
**License:** MIT  

---

## Overview

Language-agnostic guidelines covering SOLID principles, core coding principles (DRY, KISS, YAGNI), and design patterns. Examples are written in TypeScript but apply to any object-oriented or functional language.

## Categories (14 rules implemented)

### 1. SOLID Principles (Critical) — 5 rules
Five fundamental object-oriented design principles: Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion.

### 2. Core Principles (Critical) — 8 rules
DRY (Single Source of Truth & Logic Extraction), KISS (Simplicity & Readability), YAGNI (Lean Development & Avoiding Premature Abstractions), Separation of Concerns, Composition over Inheritance, Law of Demeter, Fail Fast, Encapsulation.

### 3. Design Patterns (High) — 1 rule
Repository pattern for data access abstraction.

## Usage

Ask the coding assistant to:
- "Review architecture" — triggers SOLID + Separation of Concerns analysis
- "Check SOLID principles" — targeted SOLID review
- "Check code quality" — DRY, KISS, YAGNI audit
- "Suggest design patterns" — pattern recommendations
- "Refactoring advice" — actionable improvements with rule references

## Key Principles

### SOLID
| Principle | Rule | Summary |
|-----------|------|---------|
| **S**ingle Responsibility | `solid-srp` | One reason to change (class and function levels) |
| **O**pen/Closed | `solid-ocp` | Open for extension, closed for modification via abstraction |
| **L**iskov Substitution | `solid-lsp` | Subtypes must honor base contracts, invariants, and preconditions |
| **I**nterface Segregation | `solid-isp` | Small, focused, client-specific interfaces |
| **D**ependency Inversion | `solid-dip` | Depend on abstractions, inject dependencies |

### Core

| Principle | Rules | Summary |
|-----------|-------|---------|
| **DRY** | `core-dry` | Single source of truth & logic extraction without accidental coupling |
| **KISS** | `core-kiss` | Simplest correct solution over clever or over-engineered code |
| **YAGNI** | `core-yagni` | Build only what is needed; avoid speculative features and premature abstractions |

## Output Format

When auditing code:

```
file:line - [rule-id] Description of issue
```

Example:
```
src/services/UserService.ts:15 - [solid-srp] Class handles validation, persistence, and email
src/utils/helpers.ts:42 - [core-dry] Email validation duplicated from validators/email.ts
src/models/Order.ts:28 - [core-yagni] Generic notification abstraction used in only one place
```

## References

- **Clean Code** by Robert C. Martin — Foundation for clean code practices
- **Design Patterns** by Gang of Four — Classic design pattern catalog
- **Refactoring** by Martin Fowler — Improving code structure
- **The Pragmatic Programmer** by Hunt & Thomas — Practical software wisdom
- [Refactoring Guru](https://refactoring.guru/) — Design patterns and code smells
- [Martin Fowler's Refactoring Catalog](https://refactoring.com/catalog/) — Comprehensive techniques
