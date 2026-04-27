# Spec: Database Setup

## Overview
Implements the SQLite database layer that all subsequent steps depend on. The goal is to create `database/db.py` with three functions: `get_db()` for per-request connections, `init_db()` to create the schema, and `seed_db()` for development data. No routes or templates are added in this step.

## Depends on
None. This is the foundation step.

## Routes
No new routes.

## Database changes

### `users`
| Column | Type | Constraints |
|---|---|---|
| `id` | INTEGER | PRIMARY KEY AUTOINCREMENT |
| `name` | TEXT | NOT NULL |
| `email` | TEXT | NOT NULL UNIQUE |
| `password` | TEXT | NOT NULL (hashed) |
| `created_at` | TEXT | DEFAULT `datetime('now')` |

### `expenses`
| Column | Type | Constraints |
|---|---|---|
| `id` | INTEGER | PRIMARY KEY AUTOINCREMENT |
| `user_id` | INTEGER | NOT NULL, FK → `users(id)` ON DELETE CASCADE |
| `date` | TEXT | NOT NULL |
| `description` | TEXT | NOT NULL |
| `category` | TEXT | NOT NULL |
| `amount` | REAL | NOT NULL |
| `created_at` | TEXT | DEFAULT `datetime('now')` |

## Implementation notes

`database/db.py` must expose exactly these three functions:

```python
def get_db() -> sqlite3.Connection:
    # Store connection in Flask g; set row_factory and PRAGMA foreign_keys = ON

def init_db() -> None:
    # CREATE TABLE IF NOT EXISTS for both tables

def seed_db() -> None:
    # Insert sample users and expenses for development (optional but recommended)
```

`close_db(e=None)` should also be defined and registered with `app.teardown_appcontext`.

`init_db()` must be called once on app startup. Wire it up in `app.py`:
```python
with app.app_context():
    init_db()
```

## Acceptance criteria
- [ ] `spendly.db` is created in the project root when `python app.py` is run for the first time
- [ ] `users` and `expenses` tables exist with the correct columns and constraints
- [ ] `get_db()` returns a connection with `row_factory = sqlite3.Row` and foreign keys enabled
- [ ] Calling `init_db()` twice does not raise an error (idempotent — uses `CREATE TABLE IF NOT EXISTS`)
- [ ] `close_db()` is registered so the connection closes at the end of each request
- [ ] No raw `sqlite3.connect()` calls exist outside `database/db.py`
