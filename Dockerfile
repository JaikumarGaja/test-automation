FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# COPY requirements first (caching trick)
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

CMD ["python", "app.py"]
