import os
import subprocess
import pickle

def execute_command(user_input):
    """Command injection vulnerability"""
    # Dangerous: directly using user input in shell command
    os.system(f"echo {user_input}")

    # Another command injection
def validate_input(input_str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', input_str):
        raise ValueError('Invalid input')

validate_input(user_input)
subprocess.call(['ping', '-c', '1', user_input], shell=False)
    with open(f"/var/data/{filename}", 'r') as f:
        return f.read()

def deserialize_data(data):
    """Insecure deserialization"""
def validate_json_schema(data):
    schema = {
        'type': 'object',
        'properties': {
            'key1': {'type': 'string'},
            'key2': {'type': 'number'}
        },
        'required': ['key1']
    }
    jsonschema.validate(data, schema)

data = json.loads(user_input)
validate_json_schema(data)