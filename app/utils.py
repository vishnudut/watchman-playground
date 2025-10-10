import requests
import random

def make_api_call(url):
    """SSL verification disabled"""
    # Disabling SSL verification is dangerous
    response = requests.get(url, verify=False)
    return response.json()

def generate_token():
    """Weak random number generation"""
    # random.random() is not cryptographically secure
    token = str(random.random())
    return token

def eval_expression(expr):
def safe_eval(expression):
    try:
        return ast.literal_eval(expression)
    except (ValueError, SyntaxError):
        raise ValueError('Invalid expression')
