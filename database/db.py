import sqlite3
import os
from flask import g

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'spendly.db')


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON")
    return g.db


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_db():
    db = sqlite3.connect(DB_PATH)
    db.execute("PRAGMA foreign_keys = ON")
    db.executescript("""
        CREATE TABLE IF NOT EXISTS users (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            name         TEXT    NOT NULL,
            email        TEXT    NOT NULL UNIQUE,
            password     TEXT    NOT NULL,
            created_at   TEXT    NOT NULL DEFAULT (datetime('now'))
        );

        CREATE TABLE IF NOT EXISTS expenses (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id      INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
            date         TEXT    NOT NULL,
            description  TEXT    NOT NULL,
            category     TEXT    NOT NULL,
            amount       REAL    NOT NULL,
            created_at   TEXT    NOT NULL DEFAULT (datetime('now'))
        );
    """)
    db.commit()
    db.close()


def seed_db():
    from werkzeug.security import generate_password_hash

    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row

    if db.execute("SELECT COUNT(*) FROM users").fetchone()[0] > 0:
        db.close()
        return

    cursor = db.execute(
        "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
        ("Riya Sharma", "riya@example.com", generate_password_hash("password123")),
    )
    user_id = cursor.lastrowid

    expenses = [
        (user_id, "2025-04-20", "Zomato",           "Food",       450),
        (user_id, "2025-04-18", "Ola Cab",           "Transport",  220),
        (user_id, "2025-04-15", "Electricity Bill",  "Utilities",  1800),
        (user_id, "2025-04-12", "Amazon",            "Shopping",   3200),
        (user_id, "2025-04-10", "Swiggy",            "Food",       380),
        (user_id, "2025-04-08", "Metro Card",        "Transport",  500),
        (user_id, "2025-04-05", "Grocery",           "Food",       1200),
        (user_id, "2025-04-03", "Netflix",           "Utilities",  649),
        (user_id, "2025-04-01", "Myntra",            "Shopping",   1850),
        (user_id, "2025-03-28", "Blinkit",           "Food",       740),
    ]
    db.executemany(
        "INSERT INTO expenses (user_id, date, description, category, amount) VALUES (?, ?, ?, ?, ?)",
        expenses,
    )
    db.commit()
    db.close()
