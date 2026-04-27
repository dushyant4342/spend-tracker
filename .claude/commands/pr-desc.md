---
description: Generate a pull request description from changed files or a summary
argument-hint: [optional: brief summary of what changed]
allowed-tools: Bash(git diff:*), Bash(git log:*), Bash(git status:*)
---

Generate a pull request description for the current branch.

$ARGUMENTS

## Instructions

**Step 1 — Gather context**

Run these commands to understand what changed:

```bash
git log main..HEAD --oneline
git diff main..HEAD --stat
git diff main..HEAD
```

If `$ARGUMENTS` was provided, treat it as extra context or a manual summary — combine it with the git data.

**Step 2 — Infer the PR type**

- Bug fix → changes fix broken behavior
- Feature → new functionality added
- Refactor → no behavior change, code quality improvement
- Chore → deps, config, infra, CI changes
- Docs → documentation only

**Step 3 — Output the PR description in this exact format**

---

## [Title]
[Verb-first, max 10 words. E.g.: "Add cross-encoder reranker to RAG retrieval pipeline"]

---

### Type
- [ ] Feature
- [ ] Bug Fix
- [ ] Refactor
- [ ] Chore
- [ ] Docs

*(check the correct one with `[x]`)*

---

### What changed
[2-4 sentences. What was added, removed, or fixed. Be specific — mention file names, functions, or modules if relevant.]

---

### Why
[1-2 sentences. The motivation or problem this solves.]

---

### How to test
- [ ] [Step 1 — specific, runnable]
- [ ] [Step 2]
- [ ] [Step 3 — expected result]

---

### Files changed
[Auto-generated from `git diff --stat`. List key files with a one-line note on what changed in each.]

---

### Notes for reviewer *(optional)*
[Anything the reviewer should pay special attention to: tricky logic, known limitations, follow-up tickets, etc. Omit this section if nothing notable.]

---

## Rules
- Title must start with a verb: Add, Fix, Refactor, Migrate, Integrate, Remove, etc.
- "How to test" steps must be runnable — not "verify it works"
- If diff is too large to summarize cleanly, focus on the most impactful changes
- Never include secrets, tokens, or internal URLs in the output
- If no git data is available and no $ARGUMENTS given, ask the user for a summary before proceeding