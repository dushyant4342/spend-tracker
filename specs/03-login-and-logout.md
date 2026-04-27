# Spec: Login and Logout

## Overview
Implements session-based authentication for returning users. `POST /login` verifies credentials and sets the session. `GET /logout` clears the session and redirects to the login page. After this step, `/profile` must redirect unauthenticated visitors to `/login`.

## Depends on
- Step 1: Database setup (`users` table must exist)
- Step 2: Registration (user accounts must be creatable to test login)

## Routes
- `GET /login` — render the login form
- `POST /login` — verify credentials, set session, redirect to `/profile`
- `GET /logout` — clear session, redirect to `/login`

## Database changes
No schema changes. Reads from the existing `users` table.

## Session
On successful login set:
```python
session['user_id']   = user['id']
session['user_name'] = user['name']
```

On logout:
```python
session.clear()
```

## Auth guard
`/profile` (and all future protected routes) must check:
```python
if not session.get('user_id'):
    return redirect(url_for('login'))
```

## Templates
- `templates/login.html` — already exists; pass errors via `render_template("login.html", error="...")`.

## Error messages
| Condition | Error string |
|---|---|
| Email not found or wrong password | `"Invalid email or password."` |

Use a single generic message for both cases to avoid leaking whether the email exists.

## Acceptance criteria
- [ ] `GET /login` renders the form with no errors
- [ ] `POST /login` with correct credentials sets the session and redirects to `/profile`
- [ ] `POST /login` with wrong password renders the form with `"Invalid email or password."`
- [ ] `POST /login` with an unknown email renders the same generic error (no email-enumeration leak)
- [ ] `GET /logout` clears the session and redirects to `/login`
- [ ] `GET /profile` while logged out redirects to `/login`
- [ ] `GET /profile` immediately after logout redirects to `/login` (session is fully cleared)
