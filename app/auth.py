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
import secrets

def hash_password(password, salt=None):
    if salt is None:
        salt = secrets.token_bytes(16)
    return hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 250000, dklen=32).hex(), salt.hex()