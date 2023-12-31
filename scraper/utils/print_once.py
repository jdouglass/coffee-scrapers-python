from config.config import USE_DATABASE
from config.logger_config import logger


def print_once():
    if not hasattr(print_once, "_printed"):
        logger.info("Database operations are disabled via USE_DATABASE flag.")
        print_once._printed = True


def check_use_database(func):
    def wrapper(*args, **kwargs):
        if not USE_DATABASE:
            print_once()
            return
        return func(*args, **kwargs)
    return wrapper
