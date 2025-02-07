FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY hello_world.py .
ENV PORT=8050
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "8050"]