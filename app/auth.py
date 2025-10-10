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
    """Using weak hashing algorithm"""
    # MD5 is cryptographically broken
salt = os.urandom(16)
password_hash = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
