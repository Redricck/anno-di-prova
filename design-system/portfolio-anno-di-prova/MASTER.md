# Design System Master File

> **LOGIC:** When building a specific page, first check `design-system/pages/[page-name].md`.
> If that file exists, its rules **override** this Master file.
> If not, strictly follow the rules below.

---

**Project:** Portfolio Anno di Prova
**Generated:** 2026-06-10 12:34:37
**Category:** SaaS (General)

---

## Global Rules

> **AGGIORNATO 10/06/2026** — direzione "Bento vibrante" approvata dall'utente al checkpoint visivo
> (sostituisce la proposta iniziale glassmorphism/Poppins).

### Color Palette

| Role | Hex | CSS Variable |
|------|-----|--------------|
| Primary | `#1E40AF` | `--blue-800` |
| On Primary | `#FFFFFF` | — |
| Heading | `#172554` | `--navy-900` |
| Text | `#0F172A` | `--ink` |
| Text Muted | `#475569` / `#64748B` | `--slate-600` / `--slate-500` |
| Accent 1 (cyan) | `#0891B2` · tinte `#67E8F9` `#ECFEFF` | `--cyan-*` |
| Accent 2 (lime) | `#65A30D` · tinte `#BEF264` `#F7FEE7` | `--lime-*` |
| Background | `#F4F6FB` (+ pattern a punti blu 7%) | `--bg` |
| Card | `#FFFFFF` | `--card` |
| Border | `#DDE3EF` | `--line` |

**Color Notes:** blu profondo dominante, cyan e lime come accenti netti; niente toni sabbia/crema, niente gradienti viola-rosa.

### Typography

- **Heading Font:** Outfit (700/800, tracking -0.02em)
- **Body Font:** Outfit (400/500)
- **Mono (tag, date, kicker, codice):** JetBrains Mono (400/500)
- **Mood:** modern, geometric, vibrant, friendly-professional
- **Hosting:** self-hosted woff2 in `assets/fonts/` via `@font-face` (vincolo offline — NO CDN)

### Spacing Variables

| Token | Value | Usage |
|-------|-------|-------|
| `--space-xs` | `4px` / `0.25rem` | Tight gaps |
| `--space-sm` | `8px` / `0.5rem` | Icon gaps, inline spacing |
| `--space-md` | `16px` / `1rem` | Standard padding |
| `--space-lg` | `24px` / `1.5rem` | Section padding |
| `--space-xl` | `32px` / `2rem` | Large gaps |
| `--space-2xl` | `48px` / `3rem` | Section margins |
| `--space-3xl` | `64px` / `4rem` | Hero padding |

### Shadow Depths

| Level | Value | Usage |
|-------|-------|-------|
| `--shadow-sm` | `0 1px 2px rgba(0,0,0,0.05)` | Subtle lift |
| `--shadow-md` | `0 4px 6px rgba(0,0,0,0.1)` | Cards, buttons |
| `--shadow-lg` | `0 10px 15px rgba(0,0,0,0.1)` | Modals, dropdowns |
| `--shadow-xl` | `0 20px 25px rgba(0,0,0,0.15)` | Hero images, featured cards |

---

## Component Specs

### Buttons

```css
/* Primary Button */
.btn-primary {
  background: #0369A1;
  color: white;
  padding: 12px 24px;
  border-radius: 8px;
  font-weight: 600;
  transition: all 200ms ease;
  cursor: pointer;
}

.btn-primary:hover {
  opacity: 0.9;
  transform: translateY(-1px);
}

/* Secondary Button */
.btn-secondary {
  background: transparent;
  color: #0F172A;
  border: 2px solid #0F172A;
  padding: 12px 24px;
  border-radius: 8px;
  font-weight: 600;
  transition: all 200ms ease;
  cursor: pointer;
}
```

### Cards

```css
.card {
  background: #F8FAFC;
  border-radius: 12px;
  padding: 24px;
  box-shadow: var(--shadow-md);
  transition: all 200ms ease;
  cursor: pointer;
}

.card:hover {
  box-shadow: var(--shadow-lg);
  transform: translateY(-2px);
}
```

### Inputs

```css
.input {
  padding: 12px 16px;
  border: 1px solid #E2E8F0;
  border-radius: 8px;
  font-size: 16px;
  transition: border-color 200ms ease;
}

.input:focus {
  border-color: #0F172A;
  outline: none;
  box-shadow: 0 0 0 3px #0F172A20;
}
```

### Modals

```css
.modal-overlay {
  background: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(4px);
}

.modal {
  background: white;
  border-radius: 16px;
  padding: 32px;
  box-shadow: var(--shadow-xl);
  max-width: 500px;
  width: 90%;
}
```

---

## Style Guidelines

**Style:** Bento Grid (vibrante)

**Keywords:** card arrotondate (radius 16–22px), griglia bento asimmetrica, hero card colorata piena, ombre morbide a doppio livello, pill/chip colorate, flat (niente blur decorativo)

**Best For:** portfolio moderni, product page, dashboard di presentazione

**Key Effects:** hover lift -3px con ombra ampia, count-up numeri KPI, reveal-on-scroll, glow radiali cyan/lime SOLO dentro le card blu/navy

### Page Pattern

**Pattern Name:** Bento hero + commit-log timeline

- **Hero:** card blu `#1E40AF` (eyebrow mono, H1, sub, chip cyan/lime) + stat card bianche affiancate in griglia bento
- **Timeline:** rail verticale sfumato cyan→blu→lime, nodi colorati, card bianche con tag versione in mono (metafora git sobria: v0.1…v1.0)
- **Section Order home:** 1. Hero bento, 2. Timeline percorso, 3. Card approfondimenti, 4. Outro navy "prossimi sviluppi", 5. Footer

---

## Anti-Patterns (Do NOT Use)

- ❌ Excessive animation
- ❌ Dark mode by default

### Additional Forbidden Patterns

- ❌ **Emojis as icons** — Use SVG icons (Heroicons, Lucide, Simple Icons)
- ❌ **Missing cursor:pointer** — All clickable elements must have cursor:pointer
- ❌ **Layout-shifting hovers** — Avoid scale transforms that shift layout
- ❌ **Low contrast text** — Maintain 4.5:1 minimum contrast ratio
- ❌ **Instant state changes** — Always use transitions (150-300ms)
- ❌ **Invisible focus states** — Focus states must be visible for a11y

---

## Pre-Delivery Checklist

Before delivering any UI code, verify:

- [ ] No emojis used as icons (use SVG instead)
- [ ] All icons from consistent icon set (Heroicons/Lucide)
- [ ] `cursor-pointer` on all clickable elements
- [ ] Hover states with smooth transitions (150-300ms)
- [ ] Light mode: text contrast 4.5:1 minimum
- [ ] Focus states visible for keyboard navigation
- [ ] `prefers-reduced-motion` respected
- [ ] Responsive: 375px, 768px, 1024px, 1440px
- [ ] No content hidden behind fixed navbars
- [ ] No horizontal scroll on mobile
