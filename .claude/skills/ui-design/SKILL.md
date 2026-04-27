# Skill: ui-design

Use this skill when building or modifying any HTML template or CSS for the Spendly project.

---

## Design tokens (from `static/css/style.css`)

```css
--ink: #0f0f0f          /* primary text */
--ink-soft: #2d2d2d     /* secondary text */
--ink-muted: #6b6b6b    /* labels, captions */
--ink-faint: #a0a0a0    /* timestamps, hints */
--paper: #f7f6f3        /* page background */
--paper-warm: #f0ede6   /* section backgrounds */
--paper-card: #ffffff   /* card surfaces */
--accent: #1a472a       /* primary green */
--accent-light: #e8f0eb /* green tint bg */
--accent-2: #c17f24     /* amber accent */
--accent-2-light: #fdf3e3
--danger: #c0392b
--border: #e4e1da
--border-soft: #eeebe4
--radius-sm: 6px  --radius-md: 12px  --radius-lg: 20px
--max-width: 1200px
--font-display: 'DM Serif Display', Georgia, serif   /* headings */
--font-body: 'DM Sans', system-ui, sans-serif        /* everything else */
```

---

## Rules

- **Never use a CSS framework.** All styles go in `static/css/style.css` (global) or a per-page file loaded via `{% block head %}`.
- Use `var(--token)` exclusively — no hardcoded hex values except for one-off badge colors not in the token set.
- Cards: `background: var(--paper-card); border: 1px solid var(--border); border-radius: var(--radius-md); padding: 1.75rem 2rem`.
- Headings use `font-family: var(--font-display)`. Body/labels use `var(--font-body)`.
- Buttons: `.btn-primary` (dark fill, hover to accent) and `.btn-ghost` (outlined) are already defined — reuse them.
- Amounts are INR, always formatted as `₹X,XXX` using Jinja2: `₹{{ "{:,}".format(amount) }}`.
- Responsive breakpoint: collapse grids to single column at `max-width: 900px`.

## Template conventions

- All pages: `{% extends "base.html" %}`, define `{% block title %}` and `{% block content %}`.
- Per-page CSS: `{% block head %}<link rel="stylesheet" href="{{ url_for('static', filename='css/page.css') }}">{% endblock %}`.
- Errors in auth forms: `{% if error %}<div class="auth-error">{{ error }}</div>{% endif %}` — no `flask.flash`.
- Internal links: always `{{ url_for('view_name') }}`, never hardcoded paths.

## Existing reusable classes

| Class | Purpose |
|---|---|
| `.btn-primary` / `.btn-ghost` | CTA buttons |
| `.auth-section`, `.auth-card`, `.auth-error` | Login/register layout |
| `.form-group`, `.form-input`, `.btn-submit` | Form elements |
| `.profile-card`, `.profile-card-title` | Content cards |
| `.stat-card`, `.stat-label`, `.stat-value` | Metric tiles |
| `.txn-table`, `.txn-badge` | Transaction tables |
| `.breakdown-bar-track`, `.breakdown-bar` | Horizontal bar charts |
