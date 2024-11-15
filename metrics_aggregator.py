# metrics_aggregator.py
from prometheus_client import start_http_server, Summary
import time
import json

# Initialize Prometheus metric with a generic label for tags
function_duration = Summary('function_duration_seconds', 'Duration of my_function executions', ['function', 'tags'])

def process_log_line(log_line):
    try:
        log_data = json.loads(log_line)
        if log_data["event"] == "function_end":
            # Extract and record duration in Prometheus metric
            duration = log_data["duration_seconds"]
            tags = log_data.get("tags", {})
            function_name = tags.pop("function", "unknown")
            tags_json = json.dumps(tags)
            function_duration.labels(function=function_name, tags=tags_json).observe(duration)
    except json.JSONDecodeError:
        pass

if __name__ == '__main__':
    # Start Prometheus HTTP server on  sport 8001
    start_http_server(8001)

    # Continuously read log data from the app log file
    log_file = "/var/log/app/app.log"
    with open(log_file, 'r') as f:
        f.seek(0, 2)  # Start at the end of the file for new logs
        while True:
            line = f.readline()
            if line:
                process_log_line(line)
            else:
                time.sleep(0.1)