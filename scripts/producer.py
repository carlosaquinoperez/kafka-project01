# scripts/producer.py
from kafka import KafkaProducer
import json
import time
import requests

# Configurar Kafka Producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# === ⚠️ DATOS REALES DESDE API TRANSPORT ===
APP_ID = '62f1444d'         # ← Reemplazar con tu App ID real
API_KEY = '30e532bf7dc8070c5e64fa2276520d39'       # ← Reemplazar con tu API Key real
station_code = 'KGX'         # Puedes cambiar la estación si deseas
url = f"https://transportapi.com/v3/uk/train/station/{station_code}/live.json?app_id={APP_ID}&app_key={API_KEY}"

# Hacer una sola consulta a la API
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    departures = data.get("departures", {}).get("all", [])
    
    if departures:
        # Enviar solo el primer tren
        train = departures[0]
        print(f"🚆 Enviando tren: {train.get('service')} hacia {train.get('destination_name')}")
        producer.send("transport-events", value=train)
        producer.flush()
        print("✅ Tren enviado al topic Kafka: transport-events")
    else:
        print("⚠️ No se encontraron trenes disponibles en la estación.")
else:
    print(f"❌ Error al consultar la API: {response.status_code} - {response.text}")
