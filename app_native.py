# app.py
import json
import time
import logging
import os
from prometheus_client import start_http_server, Summary

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

# Initialize Prometheus metrics
function_duration = Summary('function_duration_seconds', 'Duration of function executions', ['function', 'custom_tag'])

def log_and_record(function_name, custom_tag, duration):
    tags = {"function": function_name, "custom_tag": custom_tag}
    logging.info(json.dumps({
        "event": "function_end",
        "function_name": function_name,
        "timestamp": time.time(),
        "duration_seconds": duration,
        "tags": tags
    }))
    function_duration.labels(function=function_name, custom_tag=custom_tag).observe(duration)

def function_one():
    start_time = time.time()
    # Simulate workload
    time.sleep(2)
    duration = time.time() - start_time
    log_and_record("function_one", "value1", duration)

def function_two():
    start_time = time.time()
    # Simulate workload
    time.sleep(3)
    duration = time.time() - start_time
    log_and_record("function_two", "value2", duration)

if __name__ == '__main__':
    # Start Prometheus HTTP server on port 8000
    start_http_server(8000)
    while True:
        function_one()
        function_two()
        time.sleep(1)