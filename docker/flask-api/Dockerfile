FROM python:3.10-slim

WORKDIR /app

COPY requirements/flask_api.txt .

RUN pip install --no-cache-dir -r flask_api.txt

COPY scripts/flask_api.py .

CMD ["python", "flask_api.py"]
