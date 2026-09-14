---
id: env-management-security
title: "Type-Safe Environment Variables and Zero Client-Secret Leakage"
category: env
priority: HIGH
triggers: [vite-env-variables, import-meta-env, client-secret-leak, env-mode-cascading]
tags: [vite, env, security, typescript, import-meta-env]
---

# Type-Safe Environment Variables and Zero Client-Secret Leakage

**Trigger Anchor:** Expose only client-safe variables prefixed with `VITE_`, enforce strict typing via `src/vite-env.d.ts`, and never bundle database credentials or private API keys into client code.

---

### Bad
```typescript
// ❌ Dangerous secret exposure and untyped environment access
// .env
VITE_STRIPE_SECRET_KEY=sk_live_999999999999 // 🚨 Leaks private payment credentials in public JS bundle!
DATABASE_URL=postgres://user:pass@host/db

// src/api.ts
const apiUrl = process.env.API_URL; // ❌ Node process is undefined in browser Vite apps
const secretKey = import.meta.env.VITE_STRIPE_SECRET_KEY; // ❌ Bundled into client code!
```

### Good
```typescript
// ✅ src/vite-env.d.ts: Strongly typed client environment variables
/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_APP_TITLE: string;
  readonly VITE_API_BASE_URL: string;
  readonly VITE_ENABLE_ANALYTICS: string;
}

interface ImportMeta {
  readonly env: ImportMetaEnv;
}
```

```env
# ✅ .env.production: Client variables prefixed with VITE_, private secrets kept on backend proxy
VITE_APP_TITLE=Production Portal
VITE_API_BASE_URL=https://api.example.com/v1
VITE_ENABLE_ANALYTICS=true
```

```typescript
// ✅ src/services/apiClient.ts: Safe client access with compile-time type validation
export function createApiClient() {
  const baseURL = import.meta.env.VITE_API_BASE_URL;
  if (!baseURL) {
    throw new Error('VITE_API_BASE_URL is not configured in current environment');
  }

  return {
    get: async (endpoint: string) => {
      const response = await fetch(`${baseURL}${endpoint}`, {
        headers: { 'Content-Type': 'application/json' },
      });
      return response.json();
    },
  };
}
```
