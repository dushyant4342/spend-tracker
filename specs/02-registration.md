# Spec: Registration

## Overview
Implements user account creation via `POST /register`. Reads name, email, and password from the form, validates input, hashes the password, inserts the user into the database, and starts a session. On success the user is redirected to `/profile` already logged in.

## Depends on
- Step 1: Database setup (`users` table must exist)

## Routes
- `GET /register` — render the registration form
- `POST /register` — validate input, create account, set session, redirect to `/profile`

## Database changes
No schema changes. Inserts a row into the existing `users` table.

## Validation rules
| Field | Rule |
|---|---|
| `name` | Required, non-empty after strip |
| `email` | Required, normalised to lowercase |
| `password` | Required, minimum 8 characters |
| Duplicate email | Reject with an error message |

## Session
On successful registration set:
```python
session['user_id']   = user.id
session['user_name'] = user.name
```

`SECRET_KEY` must be set in `app.config` before this route is enabled.

## Templates
- `templates/register.html` — already exists; pass errors via `render_template("register.html", error="...")`.

## Error messages
| Condition | Error string |
|---|---|
| Any field empty | `"All fields are required."` |
| Password too short | `"Password must be at least 8 characters."` |
| Email already taken | `"An account with that email already exists."` |

## Acceptance criteria
- [ ] `GET /register` renders the form with no errors
- [ ] Submitting valid details creates a row in `users` with a hashed password (not plaintext)
- [ ] User is redirected to `/profile` after successful registration and the session is set
- [ ] Submitting a duplicate email renders the form with the duplicate-email error message
- [ ] Submitting a password shorter than 8 characters renders the form with the length error message
- [ ] Password is stored using `werkzeug.security.generate_password_hash` — never plaintext
