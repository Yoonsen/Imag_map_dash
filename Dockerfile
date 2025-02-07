FROM python:3.12-slim

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY hello_world.py ./

# Expose the correct port for Cloud Run
ENV PORT=8050

# Use Gunicorn for Cloud Run
CMD ["sh", "-c", "gunicorn --workers=2 --timeout 90 --log-level debug hello_world:server --bind 0.0.0.0:${PORT}"]
