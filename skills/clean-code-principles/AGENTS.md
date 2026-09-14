# Clean Code Principles - Agent Documentation

**Version:** 1.1.0  
**Focus:** SOLID Principles, Core Principles (DRY, KISS, YAGNI), Design Patterns  
**Rules:** 14 (5 SOLID + 8 Core + 1 Pattern)  
**License:** MIT  

---

This skill provides comprehensive clean code principles, SOLID guidelines, and design patterns for building maintainable, scalable software.

## Operational Contract

When applying this skill, agents must:
- Treat this skill as repo-owned guidance and defer to repository or task-specific instructions when they conflict.
- Limit work to the smallest relevant file and rule set for the current request.
- Stop and ask when the stack, validation command, or requirement is missing or contradictory.
- Prefer machine-readable evidence first, then summarize files reviewed, commands run, failures, and unresolved risks.

## Validation & Evidence

- Run the repository's existing validation commands in documented order when code changes are requested.
- If this repository does not define a validation command for the current task, say so instead of inventing one.

## Overview

The clean-code-principles skill offers language-agnostic software design principles organized into 3 categories, from CRITICAL (SOLID, Core Principles) to HIGH priority (Design Patterns). Each rule provides bad/good examples, explanations, and practical guidance.

## When to Use This Skill

Activate this skill when:
- Reviewing code architecture or design
- Refactoring existing code
- Making design decisions
- Establishing coding standards
- Teaching software design principles
- Addressing technical debt
- Improving code quality and maintainability

## Trigger Phrases

The skill activates on:
- "review architecture"
- "check code quality"
- "SOLID principles"
- "design patterns"
- "clean code"
- "refactoring advice"
- "code smells"
- "best practices"
- "DRY principle"
- "separation of concerns"

## Skill Structure

```
clean-code-principles/
├── SKILL.md              # Main skill definition
├── AGENTS.md             # This file - agent documentation
├── README.md             # User-facing documentation
├── metadata.json         # Structured metadata and references
└── rules/
    ├── _sections.md      # Category definitions and organization
    ├── _template.md      # Template for new rules
    ├── solid-*.md        # SOLID principles (5 rules)
    ├── core-*.md         # Core principles (8 rules)
    └── pattern-*.md      # Design patterns (1 rule)
```

## Rule Categories

### 1. SOLID Principles (CRITICAL - 5 rules)
**Prefix:** `solid-`

Five fundamental object-oriented design principles:
- **S**ingle Responsibility: `solid-srp` (class and function levels)
- **O**pen/Closed: `solid-ocp` (extension via abstraction)
- **L**iskov Substitution: `solid-lsp` (contracts, invariants, and preconditions)
- **I**nterface Segregation: `solid-isp` (focused, client-specific interfaces)
- **D**ependency Inversion: `solid-dip` (depend on abstractions, inject dependencies)

**Use when:** Designing architecture, planning refactoring, discussing system design

### 2. Core Principles (CRITICAL - 8 rules)
**Prefix:** `core-`

Fundamental coding practices:
- **DRY** (Don't Repeat Yourself): `core-dry` (single source of truth & logic extraction)
- **KISS** (Keep It Simple): `core-kiss` (simplicity over over-engineering & readability)
- **YAGNI** (You Aren't Gonna Need It): `core-yagni` (avoid speculative features and premature abstractions)
- **Other**: `core-separation-concerns`, `core-composition`, `core-law-demeter`, `core-fail-fast`, `core-encapsulation`

**Use when:** Daily coding, code reviews, addressing duplication or complexity

### 3. Design Patterns (HIGH - 1 rule)
**Prefix:** `pattern-`

Common solutions to recurring problems:
- Repository Pattern: `pattern-repository` (data access abstraction)

**Use when:** Solving architectural problems, abstracting infrastructure concerns

## How to Use Rules

### Accessing Rules

1. **By ID:** Reference specific rules using their ID
   ```
   Check against solid-srp and core-dry
   ```

2. **By Category:** Apply all rules in a category
   ```
   Review this class against SOLID principles
   ```

3. **By Scenario:** Choose relevant rules for the context
   ```
   This has duplicated validation logic - check DRY rules
   ```

## Practical Application Examples

### Example 1: Architecture Review

**User:** "Review the architecture of this OrderService class"

**Agent Approach:**
1. Check class responsibilities against `solid-srp`
2. Evaluate dependencies against `solid-dip`
3. Look for data access against `pattern-repository`
4. Check for proper separation against `core-separation-concerns`

**Agent Output:**
```
Architecture Review - OrderService

CRITICAL Issues:
1. [solid-srp] Class has multiple responsibilities:
   - Order validation (should be separate validator)
   - Direct database access (should use repository)
   - Email sending (should be separate service)
   - Payment processing (should be separate service)

2. [solid-dip] Direct dependency on concrete implementations:
   - Instantiates MySQLDatabase directly (line 15)
   - Creates StripePaymentGateway in constructor (line 18)

3. [pattern-repository] Direct SQL queries in service layer:
   - Lines 45-50: Raw SQL should be in repository

Recommendations:
1. Split into focused classes following SRP
2. Inject dependencies through constructor (DIP)
3. Create repository abstraction for data access
4. Extract email and payment to separate services

See: solid-srp.md, solid-dip.md, pattern-repository.md
```

### Example 2: Code Quality Check

**User:** "Check this validation function for code quality issues"

**Agent Approach:**
1. Check for duplication (`core-dry`)
2. Check complexity (`core-kiss`)
3. Check function responsibility (`solid-srp`)

**Agent Output:**
```
Code Quality Issues:

utils/validation.ts:
  Line 23 - [core-dry] Email regex duplicated from line 45 and validators/email.ts
  Line 30 - [core-dry] Password validation logic should be extracted to reusable validator
  Line 50 - [solid-srp] Function validates both email AND password - split into two functions

Suggested refactoring:
1. Extract common regex patterns to constants file (core-dry)
2. Create separate validateEmail() and validatePassword() functions (solid-srp)
3. Import from shared validators module (core-dry)

See: core-dry.md, solid-srp.md
```

### Example 3: Design Decision

**User:** "Should I use inheritance or composition for this User/Admin relationship?"

**Agent Approach:**
1. Apply `core-composition` principle
2. Check LSP implications (`solid-lsp`)
3. Consider YAGNI (`core-yagni`)

**Agent Output:**
```
Recommendation: Use Composition

Analysis:
1. [core-composition] Favor composition over inheritance:
   - Admin "has roles/permissions", not strictly "is a User with extra fields"
   - Composition allows dynamic role assignment without class proliferation
   - Inheritance creates rigid hierarchies that break down when SuperAdmin or Auditor roles emerge

2. [solid-lsp] Liskov Substitution Principle:
   - If Admin overrides User methods to disallow standard operations, LSP is violated

3. [core-yagni] Avoid speculative class hierarchies:
   - Start with User holding a collection of Permissions/Roles
```

## Rule Reference Quick Guide

### Most Common Rules

**For duplication:**
- `core-dry` - Single source of truth & logic extraction

**For complex code:**
- `core-kiss` - Simplicity over over-engineering and readability
- `core-yagni` - Don't build speculative features or premature abstractions

**For class design:**
- `solid-srp` - Single responsibility for classes and functions
- `solid-dip` - Dependency injection and abstractions
- `core-separation-concerns` - Separate different concerns
- `core-composition` - Favor composition over inheritance

**For interfaces:**
- `solid-isp` - Small, client-specific interfaces

**For extensibility:**
- `solid-ocp` - Open for extension, closed for modification via abstraction

**For inheritance:**
- `solid-lsp` - Subtypes must honor base contracts, invariants, and preconditions
- `core-composition` - Prefer composition

**For data access:**
- `pattern-repository` - Abstract data persistence

## Metadata

**Version:** 1.1.0  
**Rules:** 14 (5 SOLID, 8 Core, 1 Pattern)  
**Categories:** 3 (SOLID Principles, Core Principles, Design Patterns)  
**Languages:** Language-agnostic (examples in TypeScript)  
**Last Updated:** 2026-09-14  

## Resources

### Books
- Clean Code (Robert C. Martin)
- Design Patterns (Gang of Four)
- Refactoring (Martin Fowler)
- The Pragmatic Programmer (Hunt & Thomas)

### Online
- [Refactoring Guru](https://refactoring.guru/) - Design patterns and code smells
- [Martin Fowler's Catalog](https://refactoring.com/catalog/) - Refactoring techniques
- [Uncle Bob's Blog](https://blog.cleancoder.com/) - Software craftsmanship

## License

MIT License. This skill is provided as-is for educational and development purposes.
