# Dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY app_aggregator.py app_native.py metrics_aggregator.py /app/

RUN pip install prometheus_client

# Default command to override in each service
CMD ["python", "app.py"]