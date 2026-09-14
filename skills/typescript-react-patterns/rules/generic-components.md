---
id: generic-components
title: Generic Components with Type Parameter Inference
category: generic
priority: MEDIUM
triggers: [untyped-item-list, generic-component-any, lost-item-type-inference, unconstrained-generic-select]
tags: [react, typescript, generics, generic-components, type-inference]
---

# Generic Components with Type Parameter Inference

**Trigger Anchor:** Build reusable collection components (lists, selects, tables) with generic type parameters (`<T extends { id: Key }>`), allowing call-site prop inference without manual casting.

---

### Bad
```tsx
// ❌ Using any or an inflexible base type that forces call-site type casting
interface ListProps {
  items: any[];
  renderItem: (item: any) => React.ReactNode;
}

export function List({ items, renderItem }: ListProps) {
  return <ul>{items.map(renderItem)}</ul>;
}
```

### Good
```tsx
import type { Key, ReactNode } from 'react';

// ✅ Generic interface constrained by minimum required properties
interface GenericListProps<T> {
  items: readonly T[];
  getKey: (item: T) => Key;
  renderItem: (item: T) => ReactNode;
  onSelect?: (item: T) => void;
}

// ✅ Generic function component preserving item type T at call-site
export function GenericList<T>({
  items,
  getKey,
  renderItem,
  onSelect,
}: GenericListProps<T>) {
  return (
    <ul className="generic-list">
      {items.map((item) => (
        <li
          key={getKey(item)}
          onClick={() => onSelect?.(item)}
          className="generic-list__item"
        >
          {renderItem(item)}
        </li>
      ))}
    </ul>
  );
}

// Call site: T is automatically inferred as User without manual annotation
// <GenericList items={users} getKey={(u) => u.id} renderItem={(u) => u.name} />
```
