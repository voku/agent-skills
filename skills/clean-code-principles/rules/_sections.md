# Clean Code Principles - Rule Categories

This document defines the organizational structure for clean code principles, ordered by priority and impact.

## Category Overview

| Priority | Category | Impact | Rule Count | Prefix |
|----------|----------|--------|------------|--------|
| 1 | SOLID Principles | CRITICAL | 5 | `solid-` |
| 2 | Core Principles | CRITICAL | 8 | `core-` |
| 3 | Design Patterns | HIGH | 1 | `pattern-` |

---

## 1. SOLID Principles (CRITICAL)

**Priority:** CRITICAL  
**Impact:** Architectural foundation, affects entire codebase structure  
**Prefix:** `solid-`

The five fundamental principles of object-oriented design that guide maintainable, scalable software architecture.

### Rules

- `solid-srp` - Single Responsibility Principle (class and function levels)
- `solid-ocp` - Open/Closed Principle (extension via abstraction)
- `solid-lsp` - Liskov Substitution Principle (contracts, invariants, and preconditions)
- `solid-isp` - Interface Segregation Principle (focused, client-specific interfaces)
- `solid-dip` - Dependency Inversion Principle (depend on abstractions, inject dependencies)

---

## 2. Core Principles (CRITICAL)

**Priority:** CRITICAL  
**Impact:** Daily coding practices, code quality foundation  
**Prefix:** `core-`

Fundamental principles that apply across paradigms and languages.

### Rules

- `core-dry` - Don't Repeat Yourself (single source of truth & logic extraction)
- `core-kiss` - Keep It Simple, Stupid (simplicity over over-engineering & readability)
- `core-yagni` - You Aren't Gonna Need It (avoid speculative features and premature abstractions)
- `core-separation-concerns` - Different concerns in different modules
- `core-composition` - Favor composition over inheritance
- `core-law-demeter` - Only talk to immediate friends (principle of least knowledge)
- `core-fail-fast` - Detect and report errors early
- `core-encapsulation` - Hide implementation details

---

## 3. Design Patterns (HIGH)

**Priority:** HIGH  
**Impact:** Solves recurring problems with proven solutions  
**Prefix:** `pattern-`

### Rules

- `pattern-repository` - Abstraction for data access layer
