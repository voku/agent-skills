# Rule Sections

## Priority Levels

| Level | Description | When to Apply |
|-------|-------------|---------------|
| CRITICAL | Transaction boundaries and domain vs controller separation | Database writes, side-effect flows, and MVC layer design |
| HIGH | Loose coupling, dependency inversion, and unidirectional data flow | Cross-module calls, DTO contracts, and repository design |
| MEDIUM | Contract rigor and resisting deep inheritance sprawl | Class design, interface segregation, and plugin architectures |

## Section Overview

### 1. Transaction Boundaries (`transactions`)
- **Impact:** CRITICAL
- **Rules:** `arch-transaction-side-effects`
- **Description:** Preventing irreversible external network calls inside database transactions; using outbox patterns and post-commit events.

### 2. Separation of Concerns (`boundaries`)
- **Impact:** CRITICAL
- **Rules:** `arch-separation-domain-presentation`
- **Description:** Thin HTTP controllers, pure view templates, and dedicated domain services owning calculation and persistence.

### 3. Coupling & Cohesion (`coupling`)
- **Impact:** HIGH
- **Rules:** `arch-coupling-cohesion`
- **Description:** Dependency inversion, avoiding direct instantiation of database clients in domain code, and preventing leaky abstractions.

### 4. Data Flow & Immutability (`data-flow`)
- **Impact:** HIGH
- **Rules:** `arch-unidirectional-data-flow`
- **Description:** Unidirectional data flow using immutable DTOs; eliminating global mutable state and action-at-a-distance.

### 5. Contract Rigor & Simplicity (`maintainability`)
- **Impact:** MEDIUM
- **Rules:** `arch-contract-rigor-extensibility`
- **Description:** Composition over deep inheritance hierarchies; small role-focused interfaces over sprawling god-classes.
