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

> `tests/` does not exist yet — it is created as part of the tutorial. `pytest` will report "no tests ran" on a fresh clone.

## Architecture

- **`app.py`**: Flask application and all route definitions. Single-file; no blueprints. Placeholder routes return plain strings and are replaced step by step.
- **`database/db.py`**: SQLite helpers stub. Three functions expected: `get_db()`, `init_db()`, `seed_db()`. `get_db()` must set `row_factory = sqlite3.Row` and `PRAGMA foreign_keys = ON`.
- **`templates/`**: Jinja2 templates. `base.html` is the shell (navbar, footer, CSS/JS links). All pages extend it. The navbar is currently hardcoded to unauthenticated links (Sign in / Get started) and must be updated once session auth is wired up.
- **`static/css/style.css`**: Global styles shared by all pages.
- **`static/css/landing.css`**: Landing-page-only styles, loaded via `{% block head %}` in `landing.html`. Use the same per-page `{% block head %}` pattern for any page that needs its own stylesheet.
- **`static/js/main.js`**: Client-side JS, currently empty.
- **`specs/`**: Step-level feature specs (e.g. `04-profile-page.md`). Consult the relevant spec before implementing a step.

## Step-by-step build order

| Step | Feature |
|------|---------|
| 1 | Database setup (`database/db.py`) |
| 2 | Registration (POST `/register`) |
| 3 | Login/logout session handling |
| 4 | Profile page UI (static/hardcoded data) |
| 5 | Connect profile to real DB queries |
| 6 | Expense list / dashboard |
| 7 | Add expense (POST `/expenses/add`) |
| 8 | Edit expense (POST `/expenses/<id>/edit`) |
| 9 | Delete expense (POST `/expenses/<id>/delete`) |

When implementing a step, call `init_db()` inside an `app.before_request` or app-factory pattern before adding the new routes.

## Key conventions

- Sessions use Flask's signed cookie session; `SECRET_KEY` must be set in `app.config` before any auth route is enabled.
- Passwords must be hashed with `werkzeug.security` (`generate_password_hash` / `check_password_hash`).
- All DB queries go through `get_db()`; never open a raw `sqlite3.connect()` in a route.
- Auth templates receive errors via a template variable named `error` (e.g. `render_template("register.html", error="...")`), not via `flask.flash`.
- Currency is INR; display amounts as `₹X,XXX`.
