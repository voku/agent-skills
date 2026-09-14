---
id: a11y-semantic-structure
title: "Semantic HTML Landmarks, Heading Hierarchy, Skip Links, and Alt Text"
category: a11y
priority: CRITICAL
triggers: [semantic-html-landmarks, heading-hierarchy-skipped, skip-link-navigation, image-alt-text-missing]
tags: [a11y, wcag, semantic-html, headings, skip-links, alt-text]
---

# Semantic HTML Landmarks, Heading Hierarchy, Skip Links, and Alt Text

**Trigger Anchor:** Enforce native HTML5 landmark elements (`<header>`, `<nav>`, `<main>`, `<footer>`), strict sequential heading levels (`h1` -> `h2` -> `h3`), a top-level skip-to-content link, and contextual `alt` attributes (`alt=""` for decorative images).

---

### Bad
```html
<!-- ❌ Div soup, broken heading hierarchy, missing landmarks, and bad image descriptions -->
<div class="top-nav">
  <div class="nav-item" onclick="navigate('/')">Home</div>
  <img src="/icons/star.png" alt="star icon decorative image" /> <!-- Decorative image announced unnecessarily -->
</div>

<div class="content">
  <!-- ❌ Skipped heading level (no h1, jumps straight to h3) -->
  <h3>User Profile</h3>
  <img src="/avatars/john.jpg" /> <!-- 🚨 Missing alt attribute causes screen reader to read entire raw image URL -->
</div>
```

### Good
```tsx
// ✅ Accessible page layout with landmark structure, skip link, and heading hierarchy
export function Layout({ children }: { children: React.ReactNode }) {
  return (
    <>
      {/* 1. Skip link: visible on keyboard focus to bypass repeated navigation */}
      <a
        href="#main-content"
        className="sr-only focus:not-sr-only focus:fixed focus:left-4 focus:top-4 focus:z-50 focus:rounded-md focus:bg-indigo-600 focus:px-4 focus:py-2 focus:text-white focus:shadow-lg"
      >
        Skip to main content
      </a>

      {/* 2. Semantic landmarks with accessible labels where multiple exist */}
      <header className="border-b bg-white">
        <nav aria-label="Main Navigation" className="mx-auto flex max-w-7xl items-center justify-between p-4">
          <a href="/" aria-label="Home, Acme Portal">
            <img src="/logo.svg" alt="" aria-hidden="true" className="h-8 w-auto" />
          </a>
          <ul className="flex space-x-4">
            <li><a href="/projects" className="text-zinc-700 hover:text-indigo-600">Projects</a></li>
            <li><a href="/settings" className="text-zinc-700 hover:text-indigo-600">Settings</a></li>
          </ul>
        </nav>
      </header>

      {/* 3. Main landmark with sequential heading hierarchy */}
      <main id="main-content" tabIndex={-1} className="mx-auto max-w-7xl p-6 outline-none">
        <article>
          <header>
            <h1 className="text-3xl font-bold tracking-tight text-zinc-900">Project Overview</h1>
            <p className="text-zinc-500">Active metrics and deliverables</p>
          </header>

          <section className="mt-8" aria-labelledby="milestones-heading">
            <h2 id="milestones-heading" className="text-xl font-semibold text-zinc-900">Milestones</h2>
            <p>Milestone details...</p>
          </section>
        </article>
      </main>

      <footer className="mt-auto border-t p-6 text-center text-sm text-zinc-500">
        <p>&copy; {new Date().getFullYear()} Acme Corp. All rights reserved.</p>
      </footer>
    </>
  );
}
```
