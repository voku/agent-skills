---
id: component-patterns-cn
title: "Component Class Merging with cn(), CVA, and Accessible Variants"
category: component
priority: HIGH
triggers: [tailwind-class-conflict, string-concatenation-classes, cva-pattern-needed, accessible-button-styling]
tags: [tailwind, clsx, tailwind-merge, cva, components, variants]
---

# Component Class Merging with cn(), CVA, and Accessible Variants

**Trigger Anchor:** Combine conditional classes using `cn()` (`clsx` + `tailwind-merge`) to resolve utility precedence conflicts, and manage component variants with Class Variance Authority (CVA).

---

### Bad
```tsx
// ❌ Naive string concatenation: `p-4` and `p-2` both exist in class string, CSS order wins unpredictably
export function Button({ className, isSmall }: { className?: string; isSmall?: boolean }) {
  return (
    <button className={`bg-blue-500 text-white p-4 ${isSmall ? 'p-2' : ''} ${className}`}>
      Click
    </button>
  );
}
```

### Good
```tsx
import type { ComponentPropsWithoutRef } from 'react';
import { cva, type VariantProps } from 'class-variance-authority';
import { clsx, type ClassValue } from 'clsx';
import { twMerge } from 'tailwind-merge';

// ✅ Universal cn helper merging conditional logic and overriding conflicting Tailwind classes
export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

// ✅ Type-safe variant configuration
const buttonVariants = cva(
  'inline-flex items-center justify-center rounded-lg font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50',
  {
    variants: {
      variant: {
        primary: 'bg-indigo-600 text-white hover:bg-indigo-500 focus-visible:ring-indigo-600',
        secondary: 'bg-zinc-100 text-zinc-900 hover:bg-zinc-200 dark:bg-zinc-800 dark:text-zinc-100',
        destructive: 'bg-red-600 text-white hover:bg-red-500 focus-visible:ring-red-600',
      },
      size: {
        sm: 'h-8 px-3 text-xs',
        md: 'h-10 px-4 text-sm',
        lg: 'h-12 px-6 text-base',
      },
    },
    defaultVariants: {
      variant: 'primary',
      size: 'md',
    },
  },
);

interface ButtonProps
  extends ComponentPropsWithoutRef<'button'>,
    VariantProps<typeof buttonVariants> {}

export function Button({ className, variant, size, ...props }: ButtonProps) {
  return <button className={cn(buttonVariants({ variant, size, className }))} {...props} />;
}
```
