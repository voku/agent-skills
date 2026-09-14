---
id: zs-store-architecture
title: "Zustand Store Architecture: TypeScript Typing, Actions, and Selectors"
category: zustand
priority: CRITICAL
triggers: [zustand-store-creation, zustand-typescript, zustand-selectors, useshallow-zustand-v5]
tags: [zustand, state-management, typescript, selectors, useshallow]
---

# Zustand Store Architecture: TypeScript Typing, Actions, and Selectors

**Trigger Anchor:** Combine store state and actions into a unified typed interface, use scalar selectors or `useShallow` for multi-property selections to prevent infinite re-render loops, and expose state outside React via `.getState()`.

---

### Bad
```tsx
// ❌ Subscribing to entire store or returning fresh object references causes massive re-render waterfalls
import { useUIStore } from '@/stores/ui';

export function BadHeader() {
  // ❌ Subscribes to the entire store: ANY change anywhere in UI store re-renders Header
  const store = useUIStore();

  // ❌ Returning new object without shallow comparison causes infinite render loop in Zustand v5
  const { theme, sidebarOpen } = useUIStore((s) => ({
    theme: s.theme,
    sidebarOpen: s.sidebarOpen,
  }));

  return <div>{theme}</div>;
}
```

### Good
```typescript
// ✅ stores/useUIStore.ts: Type-safe store with co-located actions
import { create } from 'zustand';
import { devtools } from 'zustand/middleware';

interface UIState {
  theme: 'light' | 'dark' | 'system';
  sidebarOpen: boolean;
  modalId: string | null;
}

interface UIActions {
  setTheme: (theme: UIState['theme']) => void;
  toggleSidebar: () => void;
  openModal: (modalId: string) => void;
  closeModal: () => void;
}

export type UIStore = UIState & UIActions;

export const useUIStore = create<UIStore>()(
  devtools(
    (set, get) => ({
      // State
      theme: 'system',
      sidebarOpen: false,
      modalId: null,

      // Actions
      setTheme: (theme) => set({ theme }, false, 'ui/setTheme'),
      toggleSidebar: () => set((state) => ({ sidebarOpen: !state.sidebarOpen }), false, 'ui/toggleSidebar'),
      openModal: (modalId) => set({ modalId }, false, 'ui/openModal'),
      closeModal: () => set({ modalId: null }, false, 'ui/closeModal'),
    }),
    { name: 'UIStore' }
  )
);
```

```tsx
// ✅ src/components/Header.tsx: Fine-grained atomic selectors and useShallow
import { useUIStore } from '@/stores/useUIStore';
import { useShallow } from 'zustand/shallow'; // Required in Zustand v5

export function Header() {
  // 1. Single scalar selector: re-renders ONLY when theme changes
  const theme = useUIStore((s) => s.theme);
  const setTheme = useUIStore((s) => s.setTheme);

  // 2. Multi-property selection using useShallow: prevents infinite render loops
  const { sidebarOpen, toggleSidebar } = useUIStore(
    useShallow((s) => ({
      sidebarOpen: s.sidebarOpen,
      toggleSidebar: s.toggleSidebar,
    }))
  );

  return (
    <header className="flex justify-between">
      <button onClick={toggleSidebar}>Sidebar: {sidebarOpen ? 'Open' : 'Closed'}</button>
      <button onClick={() => setTheme(theme === 'dark' ? 'light' : 'dark')}>Theme: {theme}</button>
    </header>
  );
}

// 3. Accessing state outside of React components (e.g. event emitters, router interceptors)
export function logCurrentTheme() {
  const currentTheme = useUIStore.getState().theme;
  console.log('Current active theme:', currentTheme);
}
```
