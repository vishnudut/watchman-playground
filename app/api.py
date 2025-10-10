import os
import subprocess
import pickle

def execute_command(user_input):
    """Command injection vulnerability"""
    # Dangerous: directly using user input in shell command
    os.system(f"echo {user_input}")

    # Another command injection
def sanitize_input(user_input):
    if not re.match(r'^[\w.-]+$', user_input):
        raise ValueError('Invalid input')
    return user_input

sanitized_input = sanitize_input(user_input)
subprocess.call(['ping', '-c', '1', sanitized_input], shell=False)

def unsafe_file_read(filename):
    """Path traversal vulnerability"""
    # No validation - user can access any file
def safe_json_load(serialized_data):
    try:
        data = json.loads(serialized_data)
        # Add schema validation if needed
        return data
    except json.JSONDecodeError:
        raise ValueError('Invalid JSON data')

data = safe_json_load(serialized_data)
        return f.read()

def deserialize_data(data):
    """Insecure deserialization"""
    # pickle.loads() is dangerous with untrusted data
    return pickle.loads(data)

def render_template(user_data):
    """XSS vulnerability"""
    # Directly inserting user data into HTML
    html = f"<div>Welcome {user_data['name']}</div>"
    return html
