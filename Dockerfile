FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY hello_world.py .
ENV PORT=8050
ENV SCRIPT_NAME=/helloworld/
CMD ["sh", "-c", "gunicorn --workers=2 --timeout 90 --preload --bind 0.0.0.0:${PORT} --forwarded-allow-ips='*' hello_world:server"]