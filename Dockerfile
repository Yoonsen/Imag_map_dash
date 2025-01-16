FROM python:3.12-slim
# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*
# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Copy application code
COPY sqlite_code.py ./
COPY place_exploded.db ./
COPY corpus.db ./
# Expose the port
EXPOSE 8050
CMD python sqlite_code.py