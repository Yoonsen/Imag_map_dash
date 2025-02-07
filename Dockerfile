FROM python:3.12-slim

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY hello_world.py ./

# Expose the correct port for Cloud Run
ENV PORT=8050
ENV SCRIPT_NAME=/helloworld  

# Run Gunicorn with SCRIPT_NAME support
CMD ["sh", "-c", "gunicorn --workers=2 --timeout 90 --log-level debug --bind 0.0.0.0:${PORT} hello_world:server --env SCRIPT_NAME=${SCRIPT_NAME}"]
