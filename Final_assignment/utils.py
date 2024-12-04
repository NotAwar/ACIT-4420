import logging
import time
import os

class InvalidInputError(Exception):
    pass

os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/execution_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def log_execution(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logging.info(f"{func.__name__} executed in {end_time - start_time:.2f} seconds")
        return result
    return wrapper
