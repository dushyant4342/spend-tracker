# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

**Spendly** is a Flask + SQLite expense tracker built as a step-by-step tutorial project. Routes and database helpers are added incrementally across numbered steps. Many routes in `app.py` are intentional placeholders that students will implement.

## Commands

```bash
# Install dependencies (inside venv)
pip install -r requirements.txt

# Run the dev server (port 5001)
python app.py

# Run all tests
pytest

# Run a single test file
pytest tests/test_auth.py

# Run a single test by name
pytest -k "test_login"
```

## Architecture

- **`app.py`**: Flask application and all route definitions. Single-file for now; no blueprints.
- **`database/db.py`**: SQLite helpers (to be implemented). Three functions expected: `get_db()`, `init_db()`, `seed_db()`. `get_db()` must enable `row_factory = sqlite3.Row` and `PRAGMA foreign_keys = ON`.
- **`templates/`**: Jinja2 templates. `base.html` defines the shared navbar/footer shell; all pages extend it via `{% extends "base.html" %}`.
- **`static/css/style.css`**: All styling. No CSS framework; custom styles only.
- **`static/js/main.js`**: Client-side JS, currently empty.

## Step-by-step build order

The placeholder routes in `app.py` map to numbered implementation steps:

| Step | Feature |
|------|---------|
| 1 | Database setup (`database/db.py`) |
| 2 | Registration (POST `/register`) |
| 3 | Login/logout session handling |
| 4 | Profile page |
| 7-9 | Expense CRUD (add, edit, delete) |

When implementing a step, wire up `init_db()` in the app factory and call it on first run before adding routes.

## Key conventions

- Sessions use Flask's signed cookie session; add a `SECRET_KEY` to `app.config` before enabling auth routes.
- Passwords must be hashed with `werkzeug.security` (`generate_password_hash` / `check_password_hash`), which is already a dependency.
- All DB queries go through `get_db()`; never open a raw `sqlite3.connect()` in a route.
- Currency is INR (rupees); display amounts as `₹X,XXX`.
