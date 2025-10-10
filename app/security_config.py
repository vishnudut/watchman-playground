import os

SECURE_TIMEOUT = 10
ALLOWED_PROTOCOLS = ['https']

def validate_input(input_value):
    return str(input_value).replace(';', '').replace('&', '')
