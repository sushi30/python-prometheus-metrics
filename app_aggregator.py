# app.py
import json
import time
import logging
import os

# Ensure the log directory exists
log_dir = "/var/log/app"
os.makedirs(log_dir, exist_ok=True)

# Configure logging to write to the shared log file
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    handlers=[
        logging.FileHandler(f"{log_dir}/app.log"),
        logging.StreamHandler()  # Optional: Logs to stdout for debugging
    ]
)

def function_one():
    tags = {"function": "one", "custom_tag": "value1"}
    start_time = time.time()
    logging.info(json.dumps({
        "event": "function_start",
        "function_name": "function_one",
        "timestamp": start_time,
        "tags": tags
    }))

    # Simulate workload
    time.sleep(2)

    end_time = time.time()
    logging.info(json.dumps({
        "event": "function_end",
        "function_name": "function_one",
        "timestamp": end_time,
        "duration_seconds": end_time - start_time,
        "tags": tags
    }))

def function_two():
    tags = {"function": "two", "custom_tag": "value2"}
    start_time = time.time()
    logging.info(json.dumps({
        "event": "function_start",
        "function_name": "function_two",
        "timestamp": start_time,
        "tags": tags
    }))

    # Simulate workload
    time.sleep(3)

    end_time = time.time()
    logging.info(json.dumps({
        "event": "function_end",
        "function_name": "function_two",
        "timestamp": end_time,
        "duration_seconds": end_time - start_time,
        "tags": tags
    }))

if __name__ == '__main__':
    while True:
        function_one()
        function_two()
        time.sleep(1)