---
id: a11y-aria-contrast
title: "Accessible Color Contrast, ARIA Labels, and Live Dynamic Regions"
category: a11y
priority: CRITICAL
triggers: [wcag-contrast-failure, aria-label-missing, live-region-announcement, color-only-status]
tags: [a11y, wcag, contrast, aria-labels, aria-live, color]
---

# Accessible Color Contrast, ARIA Labels, and Live Dynamic Regions

**Trigger Anchor:** Meet WCAG AA contrast (4.5:1 normal text, 3:1 UI components), never use color as the sole status indicator, provide `aria-label` for icon-only actions, and announce dynamic updates with `aria-live`.

---

### Bad
```tsx
// ❌ Low-contrast text, status conveyed by color alone, unlabeled icon button, silent dynamic updates
export function BadStatusNotification({ isError, message }: { isError: boolean; message: string }) {
  return (
    <div>
      {/* ❌ Light gray (#a1a1aa) on white fails WCAG AA (only 2.3:1 contrast) */}
      <span style={{ color: '#a1a1aa' }}>Status:</span>

      {/* ❌ Color alone conveys state: red/green colorblind users cannot perceive failure */}
      <div className={isError ? 'bg-red-500' : 'bg-green-500'}>
        {message}
      </div>

      {/* ❌ Icon-only button with no accessible text label */}
      <button onClick={() => console.log('Delete')}>
        <svg viewBox="0 0 20 20" fill="currentColor"><path d="M6 2l1 1h6l1-1H6zM4 5h12v12H4z" /></svg>
      </button>

      {/* ❌ Asynchronous toast appears in DOM silently: screen reader never announces it */}
      <div>{message}</div>
    </div>
  );
}
```

### Good
```tsx
// ✅ WCAG AA compliant contrast, redundant status markers, aria-label, and aria-live announcements
export function AccessibleStatusNotification({
  status,
  message,
  onDismiss,
}: {
  status: 'success' | 'error' | 'info';
  message: string;
  onDismiss: () => void;
}) {
  const statusConfig = {
    success: { bg: 'bg-emerald-50', text: 'text-emerald-900', border: 'border-emerald-300', icon: '✓', label: 'Success' },
    error: { bg: 'bg-rose-50', text: 'text-rose-900', border: 'border-rose-300', icon: '⚠', label: 'Error' },
    info: { bg: 'bg-blue-50', text: 'text-blue-900', border: 'border-blue-300', icon: 'ℹ', label: 'Information' },
  }[status];

  return (
    <div
      role={status === 'error' ? 'alert' : 'status'}
      aria-live={status === 'error' ? 'assertive' : 'polite'}
      className={`flex items-center justify-between rounded-lg border p-4 ${statusConfig.bg} ${statusConfig.border}`}
    >
      <div className="flex items-center space-x-3">
        {/* Visual icon + text label ensures status is never conveyed by color alone */}
        <span aria-hidden="true" className="font-bold">{statusConfig.icon}</span>
        <span className="sr-only">{statusConfig.label}: </span>
        <p className={`text-sm font-medium ${statusConfig.text}`}>{message}</p>
      </div>

      {/* Accessible icon-only button with explicit aria-label and visible focus ring */}
      <button
        type="button"
        onClick={onDismiss}
        aria-label="Dismiss notification"
        className="rounded p-1 text-zinc-600 hover:bg-zinc-200/60 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-zinc-900"
      >
        <span aria-hidden="true">✕</span>
      </button>
    </div>
  );
}
```
