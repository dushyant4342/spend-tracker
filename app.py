from flask import Flask, render_template, session, redirect, url_for, request
from werkzeug.security import generate_password_hash, check_password_hash
from database.db import get_db, close_db, init_db
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-secret-change-in-production'

app.teardown_appcontext(close_db)

with app.app_context():
    init_db()


@app.template_filter('fmtdate')
def format_date(value: str) -> str:
    try:
        return datetime.strptime(value, '%Y-%m-%d').strftime('%b %d, %Y')
    except (ValueError, TypeError):
        return value


# ------------------------------------------------------------------ #
# Routes                                                              #
# ------------------------------------------------------------------ #

@app.route("/")
def landing():
    return render_template("landing.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    name     = request.form.get("name", "").strip()
    email    = request.form.get("email", "").strip().lower()
    password = request.form.get("password", "")

    if not name or not email or not password:
        return render_template("register.html", error="All fields are required.")
    if len(password) < 8:
        return render_template("register.html", error="Password must be at least 8 characters.")

    db = get_db()
    if db.execute("SELECT id FROM users WHERE email = ?", (email,)).fetchone():
        return render_template("register.html", error="An account with that email already exists.")

    cursor = db.execute(
        "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
        (name, email, generate_password_hash(password)),
    )
    db.commit()

    session['user_id']   = cursor.lastrowid
    session['user_name'] = name
    return redirect(url_for('profile'))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    email    = request.form.get("email", "").strip().lower()
    password = request.form.get("password", "")

    user = get_db().execute(
        "SELECT id, name, password FROM users WHERE email = ?", (email,)
    ).fetchone()

    if not user or not check_password_hash(user['password'], password):
        return render_template("login.html", error="Invalid email or password.")

    session['user_id']   = user['id']
    session['user_name'] = user['name']
    return redirect(url_for('profile'))


@app.route("/terms")
def terms():
    return render_template("terms.html")


@app.route("/privacy")
def privacy():
    return render_template("privacy.html")


# ------------------------------------------------------------------ #
# Placeholder routes — students will implement these                  #
# ------------------------------------------------------------------ #

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route("/profile")
def profile():
    if not session.get('user_id'):
        return redirect(url_for('login'))

    user = {
        "name": "Riya Sharma",
        "email": "riya@example.com",
        "member_since": "January 2025",
    }
    stats = {
        "total_spent": 42750,
        "transaction_count": 18,
        "top_category": "Food",
    }
    categories = [
        {"name": "Food",      "amount": 15200},
        {"name": "Transport", "amount": 8400},
        {"name": "Utilities", "amount": 6100},
        {"name": "Shopping",  "amount": 13050},
    ]
    transactions = [
        {"date": "2025-04-20", "description": "Zomato",           "category": "Food",       "amount": 450},
        {"date": "2025-04-18", "description": "Ola Cab",          "category": "Transport",  "amount": 220},
        {"date": "2025-04-15", "description": "Electricity Bill", "category": "Utilities",  "amount": 1800},
        {"date": "2025-04-12", "description": "Amazon",           "category": "Shopping",   "amount": 3200},
        {"date": "2025-04-10", "description": "Swiggy",           "category": "Food",       "amount": 380},
    ]
    return render_template(
        "profile.html",
        user=user,
        stats=stats,
        categories=categories,
        transactions=transactions,
    )


@app.route("/expenses/add")
def add_expense():
    return "Add expense — coming in Step 7"


@app.route("/expenses/<int:id>/edit")
def edit_expense(id):
    return "Edit expense — coming in Step 8"


@app.route("/expenses/<int:id>/delete")
def delete_expense(id):
    return "Delete expense — coming in Step 9"


if __name__ == "__main__":
    app.run(debug=True, port=5001)
