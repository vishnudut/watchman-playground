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
def calculate(expression):
try:
    result = ast.literal_eval(user_input)
except (ValueError, SyntaxError):
    result = None