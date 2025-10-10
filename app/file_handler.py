import pickle
import os
from flask import request, send_file

def read_user_file(filename):
    # VULNERABLE: Path traversal
    file_path = f"/uploads/{filename}"

    # No validation - attacker could use ../../../etc/passwd
    with open(file_path, 'r') as f:
        return f.read()

try:
    data = json.loads(file_contents)
except json.JSONDecodeError:
    raise ValueError('Invalid JSON data')
    filename = request.args.get('file')

    # VULNERABLE: Directory traversal
    return send_file(f"./files/{filename}")

# VULNERABLE: Unsafe eval
def calculate(expression):
    # User input directly evaluated
    return eval(expression)
