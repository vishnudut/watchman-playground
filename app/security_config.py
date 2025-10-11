import re
import jsonschema
import certifi

# Centralized security configuration
SECURITY_CONFIG = {
    'input_validation_patterns': {
        'hostname': r'^[a-zA-Z0-9.-]+$',
        'username': r'^[a-zA-Z0-9_-]{3,20}$'
    },
    'allowed_protocols': ['https']
}