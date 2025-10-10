import re
import json
import certifi

# Centralized security configuration
SECURITY_CONFIG = {
    'input_validation_patterns': {
        'basic_sanitization': r'^[\w.-]+$',
        'strict_alphanumeric': r'^[A-Za-z0-9]+$'
    },
    'timeout_defaults': {
        'network_request': 10,
        'subprocess_timeout': 5
    }
}