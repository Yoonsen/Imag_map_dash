FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
ENV PORT=8050
ENV FRONTEND_ROOT_PATH=/helloworld/
CMD ["sh", "-c", "gunicorn --workers=2 --timeout 90 --bind 0.0.0.0:${PORT} app:app"]