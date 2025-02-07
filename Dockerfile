FROM python:3.12-slim
# Install system dependencies
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     gcc \
#     && rm -rf /var/lib/apt/lists/*
# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Copy application code
COPY hello_world.py ./
# COPY place_exploded.db ./
# COPY corpus.db ./
# Expose the port
# Ensure the correct port is exposed
ENV PORT=8050

# Use Gunicorn to serve the Dash app
CMD ["gunicorn", "-b", "0.0.0.0:8050", "hello_world:server"]
