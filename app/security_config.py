import re

DEFAULT_INPUT_REGEX = r'^[a-zA-Z0-9.-]+$'
def validate_input(input_string, pattern=DEFAULT_INPUT_REGEX):
    return re.match(pattern, input_string) is not None
