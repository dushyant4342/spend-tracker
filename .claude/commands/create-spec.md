---
description: Generate a step spec file in specs/ for a Spendly tutorial step
argument-hint: <step number and feature name, e.g. "05 connect profile to DB">
---

Create a spec file in `specs/` for the following step:

$ARGUMENTS

---

## Instructions

**Step 1 — Determine the filename**

Format: `NN-slug.md` where `NN` is the zero-padded step number and `slug` is a short kebab-case name.
Example: `05-connect-profile-to-db.md`

**Step 2 — Read context**

Before writing, read:
- `CLAUDE.md` — for project conventions, step order, and key rules
- Any existing specs in `specs/` — to match format and avoid overlap
- Relevant source files (`app.py`, `database/db.py`, templates) — to reflect what already exists vs. what needs to be added

**Step 3 — Write the spec**

Use exactly this structure:

```
# Spec: <Feature Name>

## Overview
[2-3 sentences: what this step adds, why it exists, and what it unblocks.]

## Depends on
- Step N: <name> (<one-line reason>)

## Routes
- METHOD /path — description; auth requirement if applicable

## Database changes
[Table changes with column name, type, constraints. If none: "No schema changes."]

## Templates
[List new or modified templates and their sections. If none: omit this section.]

## Validation rules
[Table of field, rule pairs. Omit if no form input.]

## Session / State
[What gets set or cleared. Omit if not applicable.]

## Error messages
[Table of condition, exact error string. Omit if no errors to surface.]

## Acceptance criteria
- [ ] [Specific, testable criterion]
- [ ] [Each criterion maps to one observable behavior]
```

---

## Rules

- Acceptance criteria must be independently testable — not "it works" or "looks correct"
- Error message strings must be exact — they are used verbatim in `render_template(..., error="...")`
- Omit sections that don't apply to this step (don't leave empty headers)
- Do not describe implementation details unless they are constraints (e.g. "must use `werkzeug.security`")
- After writing the file, print the full path of the created spec
