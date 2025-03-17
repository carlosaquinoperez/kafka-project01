# persist_mongo_consumer.py
from kafka import KafkaConsumer
from pymongo import MongoClient
import json
import time

# 1) Conectar a Mongo
mongo_client = MongoClient("mongodb://mongodb:27017/")
db = mongo_client["transport_db"]
collection = db["trains_flink_clean"]

# 2) Configurar Consumer Kafka
consumer = KafkaConsumer(
    'transport-clean',
    bootstrap_servers='kafka:29092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='mongo-consumer-group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("Esperando eventos transformados en transport-clean...")

# 3) Loop infinito recibiendo mensajes
for msg in consumer:
    event = msg.value
    print(f"Recibido en Python: {event}")

    # 4) Insertar en Mongo
    try:
        collection.insert_one(event)
        print(f"✅ Insertado en MongoDB: {event}")
    except Exception as e:
        print(f"❌ Error Mongo: {e}")

    time.sleep(0.2)  # Pequeña pausa para simular algo de procesamiento
