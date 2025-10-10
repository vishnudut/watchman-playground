import pickle
import os
from flask import request, send_file

def read_user_file(filename):
    # VULNERABLE: Path traversal
    file_path = f"/uploads/{filename}"

    # No validation - attacker could use ../../../etc/passwd
    with open(file_path, 'r') as f:
        return f.read()

json.loads(base64.b64decode(data).decode('utf-8'))
    filename = request.args.get('file')

    # VULNERABLE: Directory traversal
    return send_file(f"./files/{filename}")

# VULNERABLE: Unsafe eval
def calculate(expression):
    # User input directly evaluated
    return eval(expression)
