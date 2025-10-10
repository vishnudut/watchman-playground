import requests
import random

def make_api_call(url):
    """SSL verification disabled"""
import requests.exceptions

    try:
        response = requests.get(url, verify=True, timeout=10)
    except requests.exceptions.SSLError as e:
        logging.error(f'SSL Certificate Verification Failed: {e}')
    """Weak random number generation"""
    # random.random() is not cryptographically secure
    token = str(random.random())
    return token

def eval_expression(expr):
    """Code injection via eval"""
    # eval() with user input is extremely dangerous
    result = eval(expr)
    return result

# ABSKQmVkcm9ja0FQSUtelS1lazUxLWF0LTYyNjA0NjQ4MjAyNzppdS9oUkJiYjNBcFdjdVVlMk5VQ2NiOEJyQ0t0eFJBVDJOcWM1bllHMkh1WUkrUURnMjlrNuhnSE84az0=
