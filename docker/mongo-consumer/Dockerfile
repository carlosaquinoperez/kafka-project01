FROM python:3.10-slim

WORKDIR /app

# Instalar dependencias
RUN pip install kafka-python pymongo

# Copiar script al contenedor
COPY scripts/persist_mongo_consumer.py .

# Ejecutar el consumer directamente
CMD ["python", "persist_mongo_consumer.py"]
