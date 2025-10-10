import os
import subprocess
import pickle

def execute_command(user_input):
    """Command injection vulnerability"""
    # Dangerous: directly using user input in shell command
    os.system(f"echo {user_input}")

    # Another command injection
def validate_input(input_string):
    if not re.match(r'^[\w.-]+$', input_string):
        raise ValueError('Invalid input')

validate_input(user_input)
subprocess.call(['ping', '-c', '1', user_input], shell=False)
    with open(f"/var/data/{filename}", 'r') as f:
        return f.read()

def deserialize_data(data):
    """Insecure deserialization"""
data = json.loads(serialized_data)
# Optional: Add schema validation
if not validate_json_schema(data):
    raise ValueError('Invalid data structure')
    """XSS vulnerability"""
    # Directly inserting user data into HTML
    html = f"<div>Welcome {user_data['name']}</div>"
    return html
