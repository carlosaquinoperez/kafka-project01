from kafka import KafkaProducer
import requests
import json
import time

# CONFIGURA TUS CREDENCIALES AQUÍ
APP_ID = '62f1444d'
API_KEY = '30e532bf7dc8070c5e64fa2276520d39'

# Define la estación de tren que quieres consultar (ej: King's Cross)
station_code = 'KGX'  # Puedes cambiar por otra si deseas

# Armamos la URL del endpoint
url = f"https://transportapi.com/v3/uk/train/station/{station_code}/live.json?app_id={APP_ID}&app_key={API_KEY}"

# Configuramos el Kafka Producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Loop de consulta en tiempo real (puedes dejarlo ejecutando continuo)
while True:
    try:
        print("Consultando Transport API...")
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            # Enviar datos completos del tren (puedes también enviar tren por tren si prefieres)
            for train in data.get("departures", {}).get("all", []):
                print(f"Enviando tren: {train.get('service')} hacia {train.get('destination_name')}")
                producer.send("transport-events", value=train)
                time.sleep(1)  # Simula flujo continuo de mensajes

        else:
            print(f"Error en la API: Código {response.status_code}")

    except Exception as e:
        print(f"Error durante la consulta/envío: {e}")

    # Espera unos segundos antes de hacer la próxima consulta
    time.sleep(10)
