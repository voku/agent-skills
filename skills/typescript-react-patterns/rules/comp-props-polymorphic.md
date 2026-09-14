---
id: comp-props-polymorphic
title: Component Props, Children, and Polymorphic Components
category: comp
priority: CRITICAL
triggers: [untyped-props, polymorphic-as-prop, react-fc-anti-pattern, untyped-children]
tags: [react, typescript, components, props, polymorphic, children]
---

# Component Props, Children, and Polymorphic Components

**Trigger Anchor:** Declare typed props via interfaces or type aliases, use `ReactNode` for children, avoid `React.FC`, handle default props via destructuring, and build polymorphic components using `ComponentPropsWithoutRef<T>` with `as?: T`.

---

### Bad
```tsx
// ❌ Using React.FC, unconstrained `any` children, and untyped HTML attribute spreads
import React from 'react';

interface ButtonProps {
  children?: any;
  onClick?: any;
}

export const Button: React.FC<ButtonProps> = ({ children, onClick, ...props }) => {
  return <button onClick={onClick} {...props}>{children}</button>;
};
```

### Good
```tsx
import type { ComponentPropsWithoutRef, ElementType, ReactNode } from 'react';

// ✅ Standard function component with explicit ReactNode children & destructuring defaults
interface CardProps {
  title: string;
  children: ReactNode;
  variant?: 'elevated' | 'outlined';
}

export function Card({ title, children, variant = 'elevated' }: CardProps) {
  return (
    <div className={`card card--${variant}`}>
      <h3 className="card__title">{title}</h3>
      <div className="card__content">{children}</div>
    </div>
  );
}

// ✅ Polymorphic component supporting "as" prop (e.g. <Button as="a" href="...">)
type PolymorphicButtonProps<T extends ElementType = 'button'> = {
  as?: T;
  variant?: 'primary' | 'secondary';
  children: ReactNode;
} & ComponentPropsWithoutRef<T>;

export function PolymorphicButton<T extends ElementType = 'button'>({
  as,
  variant = 'primary',
  children,
  ...props
}: PolymorphicButtonProps<T>) {
  const Component = as || 'button';
  return (
    <Component className={`btn btn--${variant}`} {...props}>
      {children}
    </Component>
  );
}
```
