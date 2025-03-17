from kafka import KafkaConsumer
from pymongo import MongoClient
import json

# 🔸 Configurar conexión a MongoDB
mongo_client = MongoClient("mongodb://localhost:27017/")
db = mongo_client["transport_db"]
collection = db["trains"]

# 🔸 Configurar Kafka Consumer
consumer = KafkaConsumer(
    'transport-events',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='mongo-consumer-group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("Esperando mensajes de Kafka...")

# 🔸 Leer mensajes y guardarlos en MongoDB
for message in consumer:
    event = message.value
    print(f"Guardando en MongoDB: {event}")
    collection.insert_one(event)
