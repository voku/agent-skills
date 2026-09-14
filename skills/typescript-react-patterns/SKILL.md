---
name: typescript-react-patterns
description: TypeScript best practices for React development. 7 rules across 7 categories covering component props, hooks, event handling, refs, generics, context, and utility types. Triggers on tasks involving TypeScript errors, type definitions, props typing, or type-safe React patterns.
license: MIT
metadata:
  author: agent-skills
  version: "3.0.0"
---

# TypeScript React Patterns

Type-safe React patterns for modern TypeScript applications. Contains **7 consolidated rules across 7 categories** covering component typing, hooks, event handling, refs, generic components, context, and utility types.

## Metadata

- **Version:** 3.0.0
- **Rule Count:** 7 rules across 7 categories
- **License:** MIT

## When to Apply

Reference these guidelines when:
- Typing React component props and polymorphic elements
- Creating custom hooks and typing `useReducer`/`useState`
- Handling DOM events with precise synthetic types
- Managing DOM refs and imperative handles
- Building generic reusable components
- Setting up typed React Context providers
- Modeling complex UI state machines with discriminated unions

## Rule Categories by Priority

| Priority | Category | Impact | Prefix | Rules |
|----------|----------|--------|--------|-------|
| 1 | Component Typing | CRITICAL | `comp-` | 1 |
| 2 | Hook Typing | CRITICAL | `hook-` | 1 |
| 3 | Event Handling | HIGH | `event-` | 1 |
| 4 | Ref Typing | HIGH | `ref-` | 1 |
| 5 | Generic Components | MEDIUM | `generic-` | 1 |
| 6 | Context & State | MEDIUM | `ctx-` | 1 |
| 7 | Utility Types | LOW | `util-` | 1 |

## Quick Reference

### 1. Component Typing (CRITICAL) — 1 rule
- [comp-props-polymorphic.md](rules/comp-props-polymorphic.md) - Declare typed props via interfaces or type aliases, use `ReactNode` for children, avoid `React.FC`, handle default props via destructuring, and build polymorphic components using `ComponentPropsWithoutRef<T>` with `as?: T`.

### 2. Hook Typing (CRITICAL) — 1 rule
- [hook-types-generics.md](rules/hook-types-generics.md) - Provide explicit generic types when `useState<T>` initial values are null/optional, type `useReducer` actions as discriminated unions with exhaustive checks, and type custom hook return tuples using `as const`.

### 3. Event Handling (HIGH) — 1 rule
- [event-handler-types.md](rules/event-handler-types.md) - Type event handlers using React's SyntheticEvent generics specifying the exact HTML target element (`ChangeEvent<HTMLInputElement>`, `FormEvent<HTMLFormElement>`, `MouseEvent<HTMLButtonElement>`).

### 4. Ref Typing (HIGH) — 1 rule
- [ref-dom-imperative.md](rules/ref-dom-imperative.md) - Initialize DOM refs with `useRef<T>(null)` using concrete HTMLElement types, use callback refs for dynamic nodes or ResizeObservers, and define handle interfaces when exposing methods via `useImperativeHandle`.

### 5. Generic Components (MEDIUM) — 1 rule
- [generic-components.md](rules/generic-components.md) - Build reusable collection components (lists, selects, tables) with generic type parameters (`<T extends { id: Key }>`), allowing call-site prop inference without manual casting.

### 6. Context & State (MEDIUM) — 1 rule
- [ctx-patterns.md](rules/ctx-patterns.md) - Initialize Context with `null` default, export a custom hook that throws an informative error when invoked outside its Provider, and bundle Context with `useReducer` for modular state.

### 7. Utility Types (LOW) — 1 rule
- [util-discriminated-types.md](rules/util-discriminated-types.md) - Model asynchronous UI states as discriminated unions (`idle | loading | success | error`), inherit HTML element attributes via `ComponentPropsWithoutRef<T>`, and derive related prop types with `Pick` and `Omit`.

## How to Use

Read individual rule files in `rules/` for concise triggers, Bad vs Good code comparisons, and concrete TypeScript React idioms.
