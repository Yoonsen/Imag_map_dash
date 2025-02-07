FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
ENV PORT=8050
ENV SCRIPT_NAME=/helloworld/
CMD ["python", "app.py"]