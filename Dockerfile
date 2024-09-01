FROM python:3.9-slim

WORKDIR /app

COPY main.py .
COPY src/ ./src

CMD ["python", "-u", "main.py"]
