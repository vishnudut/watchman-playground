import pickle
import os
from flask import request, send_file

def read_user_file(filename):
    # VULNERABLE: Path traversal
    file_path = f"/uploads/{filename}"

    # No validation - attacker could use ../../../etc/passwd
    with open(file_path, 'r') as f:
        return f.read()

def deserialize_data(data):
    # VULNERABLE: Arbitrary code execution via pickle
    return pickle.loads(base64.b64decode(data))

def download_file():
    filename = request.args.get('file')

    # VULNERABLE: Directory traversal
    return send_file(f"./files/{filename}")

# VULNERABLE: Unsafe eval
def safe_evaluate(expression):
    try:
        return ast.literal_eval(expression)
    except (ValueError, SyntaxError):
        raise ValueError('Invalid expression')

result = safe_evaluate(user_input)