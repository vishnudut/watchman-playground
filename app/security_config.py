import logging

LOGGING_CONFIG = {
    'level': logging.ERROR,
    'format': '%(asctime)s - %(levelname)s - %(message)s'
}

def configure_logging():
    logging.basicConfig(**LOGGING_CONFIG)