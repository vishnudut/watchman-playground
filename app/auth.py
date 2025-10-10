import sqlite3
import hashlib

def login_user(username, password):
    """Vulnerable to SQL injection"""
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # SQL Injection vulnerability - user input directly in query
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)

    user = cursor.fetchone()
    conn.close()
    return user

def weak_hash_password(password):
def hash_password(password):
    # Use bcrypt with high work factor for secure password hashing
    salt = bcrypt.gensalt(rounds=12)
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')