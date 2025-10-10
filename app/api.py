import os
import subprocess
import pickle

def execute_command(user_input):
    """Command injection vulnerability"""
    # Dangerous: directly using user input in shell command
    os.system(f"echo {user_input}")

import shlex

    # Validate and sanitize user input
    sanitized_input = shlex.quote(user_input)
    result = subprocess.run([sanitized_input], shell=False, capture_output=True, text=True, check=True)
    with open(f"/var/data/{filename}", 'r') as f:
        return f.read()

def deserialize_data(data):
    """Insecure deserialization"""
import json

    try:
        data = json.loads(untrusted_input)
    except json.JSONDecodeError as e:
        logging.error(f'Invalid JSON input: {e}')
    html = f"<div>Welcome {user_data['name']}</div>"
    return html
