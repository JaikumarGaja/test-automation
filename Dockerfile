FROM python:3.9-slim

# This tells Python: "Print immediately!"
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY app.py .
CMD ["python", "app.py"]
