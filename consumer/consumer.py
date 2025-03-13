from kafka import KafkaConsumer
import json

# Crear el consumidor Kafka
consumer = KafkaConsumer(
    'api-posts',  # Nombre del topic del que leeremos
    bootstrap_servers='localhost:9092',  # Dirección del broker Kafka
    auto_offset_reset='earliest',       # Leer desde el principio si no hay offset guardado
    enable_auto_commit=True,            # Guardar automáticamente el offset después de leer
    group_id='api-posts-consumer-group', # Identificador del grupo consumidor
    value_deserializer=lambda m: json.loads(m.decode('utf-8')) # Decodifica el mensaje JSON
)

# Leer los mensajes
for message in consumer:
    print(f"Mensaje recibido: {message.value}")
