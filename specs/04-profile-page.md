# Spec: Profile Page

## Overview
This feature replaces the `/profile` stub with a fully designed profile page showing static, hardcoded data. The goal is to establish the complete UI layout: user info card, transaction history table, summary stats, and category breakdown before any real database queries are wired up in Step 5. Building the UI first lets the team validate the design in isolation and ensures the templates are ready for the backend-connection step.

## Depends on
- Step 1: Database setup (schema must exist)
- Step 2: Registration (user accounts must be creatable)
- Step 3: Login + Logout (session must be set; `/profile` must be a protected route)

## Routes
- GET `/profile` — render the profile page; logged-in only (redirect to `/login` if not authenticated)

## Database changes
No database changes. The existing `users` and `expenses` tables are sufficient.

## Templates
- `templates/profile.html` — extends `base.html`
- Sections:
  - **User info card**: name, email, member since date
  - **Summary stats**: total spent, number of transactions, top category
  - **Category breakdown**: per-category totals (hardcoded for now)
  - **Transaction history table**: date, description, category, amount (INR)

## Static data (hardcoded for Step 4)
Use the following placeholder values until Step 5 wires up real queries:

```python
user = {
    "name": "Riya Sharma",
    "email": "riya@example.com",
    "member_since": "January 2025"
}

stats = {
    "total_spent": 42750,
    "transaction_count": 18,
    "top_category": "Food"
}

categories = [
    {"name": "Food", "amount": 15200},
    {"name": "Transport", "amount": 8400},
    {"name": "Utilities", "amount": 6100},
    {"name": "Shopping", "amount": 13050},
]

transactions = [
    {"date": "2025-04-20", "description": "Zomato", "category": "Food", "amount": 450},
    {"date": "2025-04-18", "description": "Ola Cab", "category": "Transport", "amount": 220},
    {"date": "2025-04-15", "description": "Electricity Bill", "category": "Utilities", "amount": 1800},
    {"date": "2025-04-12", "description": "Amazon", "category": "Shopping", "amount": 3200},
    {"date": "2025-04-10", "description": "Swiggy", "category": "Food", "amount": 380},
]
```

## Acceptance criteria
- [ ] `/profile` redirects to `/login` when the user is not in session
- [ ] Page renders without errors when logged in
- [ ] All four sections visible: user card, stats, category breakdown, transaction table
- [ ] Amounts formatted as `₹X,XXX`
- [ ] Template extends `base.html` correctly (navbar/footer present)
