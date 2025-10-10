import re

def validate_input(input_string):
    if not re.match(r'^[a-zA-Z0-9.-]+$', input_string):
        raise ValueError('Invalid input characters')