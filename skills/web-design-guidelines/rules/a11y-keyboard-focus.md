---
id: a11y-keyboard-focus
title: "Keyboard Navigation, Focus Trapping, and Visible Focus Indicators"
category: a11y
priority: CRITICAL
triggers: [keyboard-navigation-trap, modal-focus-management, outline-none-missing-focus, positive-tabindex-defect]
tags: [a11y, keyboard, focus, modal, dialog, tabindex]
---

# Keyboard Navigation, Focus Trapping, and Visible Focus Indicators

**Trigger Anchor:** Ensure every interactive element is navigable via keyboard without positive `tabindex`, provide high-contrast visible focus rings, and constrain focus within active modal dialogs with return-on-close.

---

### Bad
```tsx
// ❌ Outline removed without replacement, positive tabindex breaks tab order, modal bleeds focus
export function BadModal({ isOpen, onClose }: { isOpen: boolean; onClose: () => void }) {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-black/50">
      {/* ❌ outline: none without replacement leaves keyboard users blind */}
      <div tabIndex={1} style={{ outline: 'none' }} className="modal-content">
        {/* ❌ Div with click handler is unreachable by standard Tab navigation */}
        <div onClick={onClose} className="close-btn">X</div>
        <input tabIndex={5} placeholder="Name" /> {/* ❌ Positive tabindex corrupts document tab sequence */}
      </div>
    </div>
  );
}
```

### Good
```tsx
// ✅ Accessible dialog with focus trap, Escape key handling, and return-on-close focus restoration
import { useEffect, useRef } from 'react';

export function AccessibleModal({
  isOpen,
  onClose,
  title,
  children,
}: {
  isOpen: boolean;
  onClose: () => void;
  title: string;
  children: React.ReactNode;
}) {
  const dialogRef = useRef<HTMLDivElement>(null);
  const triggerElementRef = useRef<HTMLElement | null>(null);

  useEffect(() => {
    if (!isOpen) return;

    // 1. Remember previously focused element to restore upon modal close
    triggerElementRef.current = document.activeElement as HTMLElement;

    // 2. Move focus into the first focusable element inside the modal
    const focusableElements = dialogRef.current?.querySelectorAll<HTMLElement>(
      'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
    );
    const firstElement = focusableElements?.[0];
    const lastElement = focusableElements?.[focusableElements.length - 1];

    firstElement?.focus();

    // 3. Trap keyboard focus inside modal and close on Escape
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        e.preventDefault();
        onClose();
        return;
      }

      if (e.key === 'Tab') {
        if (e.shiftKey && document.activeElement === firstElement) {
          e.preventDefault();
          lastElement?.focus();
        } else if (!e.shiftKey && document.activeElement === lastElement) {
          e.preventDefault();
          firstElement?.focus();
        }
      }
    };

    document.addEventListener('keydown', handleKeyDown);

    return () => {
      document.removeEventListener('keydown', handleKeyDown);
      // Restore focus upon unmount
      triggerElementRef.current?.focus();
    };
  }, [isOpen, onClose]);

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 p-4" role="presentation">
      <div
        ref={dialogRef}
        role="dialog"
        aria-modal="true"
        aria-labelledby="dialog-title"
        className="w-full max-w-md rounded-xl bg-white p-6 shadow-2xl focus:outline-none"
      >
        <div className="flex items-center justify-between border-b pb-3">
          <h2 id="dialog-title" className="text-lg font-bold text-zinc-900">{title}</h2>
          <button
            onClick={onClose}
            aria-label="Close dialog"
            className="rounded-lg p-1.5 text-zinc-500 hover:bg-zinc-100 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-indigo-600 focus-visible:ring-offset-2"
          >
            ✕
          </button>
        </div>
        <div className="mt-4">{children}</div>
      </div>
    </div>
  );
}
```
