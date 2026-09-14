---
id: zs-persist-coordination
title: "Zustand Persistence Security and Server-State Boundary Coordination"
category: zustand
priority: HIGH
triggers: [zustand-persist-partialize, zustand-auth-token-security, server-vs-client-state, combine-query-zustand]
tags: [zustand, persist, middleware, security, partialize, server-state]
---

# Zustand Persistence Security and Server-State Boundary Coordination

**Trigger Anchor:** Use `persist` middleware with strict `partialize` to exclude secrets/passwords/tokens from localStorage, and maintain a clear boundary: React Query owns server cache; Zustand owns ephemeral client UI state.

---

### Bad
```typescript
// ❌ Storing sensitive auth tokens in localStorage and duplicating server data into Zustand
import { create } from 'zustand';
import { persist } from 'zustand/middleware';

export const useStore = create(
  persist(
    (set) => ({
      authToken: 'secret_jwt_token', // 🚨 Stored in plain text in localStorage, vulnerable to XSS!
      userPassword: '',
      serverPosts: [], // ❌ Duplicating server state in Zustand: causes cache staleness & desync
      setPosts: (posts) => set({ serverPosts: posts }),
    }),
    { name: 'app-storage' } // Persists everything indiscriminately!
  )
);
```

### Good
```typescript
// ✅ stores/useSettingsStore.ts: Strict partialize filter for non-sensitive client preferences
import { create } from 'zustand';
import { persist, createJSONStorage } from 'zustand/middleware';

interface SettingsState {
  // Non-sensitive client UI settings: safe to persist
  sidebarCollapsed: boolean;
  volume: number;
  locale: string;
  // Ephemeral or runtime-only state: excluded from persistence
  isAudioPlaying: boolean;
  activeSessionId: string | null;
}

interface SettingsActions {
  setVolume: (v: number) => void;
  toggleSidebar: () => void;
  setAudioPlaying: (playing: boolean) => void;
}

export const useSettingsStore = create<SettingsState & SettingsActions>()(
  persist(
    (set) => ({
      sidebarCollapsed: false,
      volume: 0.8,
      locale: 'en',
      isAudioPlaying: false,
      activeSessionId: null,

      setVolume: (volume) => set({ volume }),
      toggleSidebar: () => set((s) => ({ sidebarCollapsed: !s.sidebarCollapsed })),
      setAudioPlaying: (isAudioPlaying) => set({ isAudioPlaying }),
    }),
    {
      name: 'user-settings-storage',
      storage: createJSONStorage(() => localStorage),
      // Only persist safe, non-sensitive preferences
      partialize: (state) => ({
        sidebarCollapsed: state.sidebarCollapsed,
        volume: state.volume,
        locale: state.locale,
      }),
    }
  )
);
```

```tsx
// ✅ src/pages/Dashboard.tsx: Coordinating React Query (server state) with Zustand (client UI state)
import { useQuery } from '@tanstack/react-query';
import { useSettingsStore } from '@/stores/useSettingsStore';
import { useUIStore } from '@/stores/useUIStore';

export function Dashboard() {
  // 1. Server state managed entirely by React Query (caching, deduplication, refetching)
  const { data: projects, isLoading } = useQuery({
    queryKey: ['projects', 'list'] as const,
    queryFn: () => fetch('/api/projects').then((r) => r.json()),
  });

  // 2. Client UI state managed by Zustand (active filters, sidebar, selection)
  const sidebarCollapsed = useSettingsStore((s) => s.sidebarCollapsed);
  const selectedProjectId = useUIStore((s) => s.modalId);
  const openModal = useUIStore((s) => s.openModal);

  if (isLoading) return <div>Loading projects...</div>;

  return (
    <div className={`layout ${sidebarCollapsed ? 'sidebar-hidden' : ''}`}>
      <ul>
        {projects?.map((project: any) => (
          <li key={project.id} onClick={() => openModal(project.id)}>
            {project.name} {project.id === selectedProjectId && '(Selected)'}
          </li>
        ))}
      </ul>
    </div>
  );
}
```
