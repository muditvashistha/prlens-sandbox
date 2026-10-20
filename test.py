import sqlite3

def get_user(conn, username):
    query = "SELECT * FROM users WHERE name = ?"
    return conn.execute(query, (username,)).fetchone()

def average(values):
    if not values:
        raise ValueError("values must not be empty")
    return sum(values) / len(values)
