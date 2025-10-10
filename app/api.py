import os
import subprocess
import pickle

def execute_command(user_input):
    """Command injection vulnerability"""
    # Dangerous: directly using user input in shell command
    os.system(f"echo {user_input}")

    # Another command injection
def validate_ip_input(input_str):
    import ipaddress
    try:
        ipaddress.ip_address(input_str)
        return input_str
    except ValueError:
        raise ValueError("Invalid IP address")

valid_ip = validate_ip_input(user_input)
subprocess.call(["ping", "-c", "1", valid_ip], shell=False, timeout=5)
    with open(f"/var/data/{filename}", 'r') as f:
import json

def safe_json_load(serialized_data):
    try:
        return json.loads(serialized_data)
    except json.JSONDecodeError as e:
        logging.error(f"JSON Parsing Error: {e}")
        raise ValueError("Invalid JSON data")

data = safe_json_load(serialized_data)
    # pickle.loads() is dangerous with untrusted data
    return pickle.loads(data)

def render_template(user_data):
    """XSS vulnerability"""
    # Directly inserting user data into HTML
    html = f"<div>Welcome {user_data['name']}</div>"
    return html
