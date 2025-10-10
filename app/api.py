import os
import subprocess
import pickle

def execute_command(user_input):
    """Command injection vulnerability"""
    # Dangerous: directly using user input in shell command
    os.system(f"echo {user_input}")

    # Another command injection
import shlex, subprocess

    # Validate input against allowed pattern
    if not re.match(r'^[a-zA-Z0-9.-]+$', user_input):
        raise ValueError('Invalid input')
    
    subprocess.call(shlex.split(f'ping -c 1 {user_input}'), shell=False, timeout=5)
def unsafe_file_read(filename):
    """Path traversal vulnerability"""
    # No validation - user can access any file
    with open(f"/var/data/{filename}", 'r') as f:
import json, jsonschema

    # Define strict schema for validation
    schema = {
        'type': 'object',
        'properties': {
            'id': {'type': 'integer'},
            'name': {'type': 'string'}
        },
        'required': ['id', 'name']
    }

    try:
        data = json.loads(serialized_data)
        jsonschema.validate(instance=data, schema=schema)
    except (json.JSONDecodeError, jsonschema.ValidationError) as e:
        logging.error(f'Deserialization Error: {e}')
        raise
def deserialize_data(data):
    """Insecure deserialization"""
    # pickle.loads() is dangerous with untrusted data
    return pickle.loads(data)

def render_template(user_data):
    """XSS vulnerability"""
    # Directly inserting user data into HTML
    html = f"<div>Welcome {user_data['name']}</div>"
    return html
