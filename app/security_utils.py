import json
import bcrypt
import ast

def validate_input(input_data, expected_type=dict):
    try:
        parsed_data = json.loads(input_data)
        if not isinstance(parsed_data, expected_type):
            raise ValueError('Invalid input type')
        return parsed_data
    except json.JSONDecodeError:
        raise ValueError('Invalid JSON input')