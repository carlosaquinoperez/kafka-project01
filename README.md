# Proyecto de Ingesta y Procesamiento de Eventos con Kafka, Apache Flink y MongoDB

## 🌟 Objetivo del Proyecto
Implementar un pipeline de procesamiento de datos en tiempo real utilizando tecnologías open-source modernas:
- **Kafka** para la ingesta de eventos.
- **Apache Flink** para el procesamiento y transformación de los eventos.
- **MongoDB** para la persistencia final.
- **Flask API** para exponer los datos en tiempo real.

Este flujo se basa en eventos provenientes de la API de TransportAPI (trenes en vivo en Reino Unido).

---

## 📊 Arquitectura General
```
+-------------+         +-----------+         +-------------+         +---------+         +-----------+
|  Transport  | --> --> |  Producer | ----->  |  Kafka       | ----->  |  Flink  | ----->  |  MongoDB  |
|   API (UK)  |         |  (Python) |         |   Broker     |         | Transform|         |  Database |
+-------------+         +-----------+         +-------------+         +---------+         +-----------+
                                                        
                                                             \                                
                                                              \                              
                                                                \---> Flask API (visualización)
```

---

## ⚙️ Tecnologías Utilizadas
- **Apache Kafka** (Confluent Platform 7.5)
- **Apache Flink 1.17**
- **MongoDB 6.0**
- **Python 3.10**
- **Flask** (API Rest)
- **Docker & Docker Compose**

---

## 📄 Estructura del Proyecto
```
kafka-project01/
├── docker/
│   └── flink-jobrunner/
│       └── Dockerfile
├── jars/
│   ├── flink-connector-kafka-1.17.0.jar
│   └── kafka-clients-3.4.0.jar
├── scripts/
│   ├── producer.py
│   ├── transform_flink_job.py
│   ├── persist_mongo_consumer.py
│   └── flask_api.py
├── requirements.txt
└── docker-compose.yml
```

---

## ⚡ Instalación y Ejecución Paso a Paso

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu_usuario/kafka-project01.git
cd kafka-project01
```

### 2. Configurar credenciales de TransportAPI
Edita `scripts/producer.py` e inserta tu `APP_ID` y `API_KEY` reales.

### 3. Construir contenedores Docker
```bash
docker-compose build
```

### 4. Levantar toda la infraestructura
```bash
docker-compose up -d
```

### 5. Ejecutar el Producer manualmente (API real)
```bash
python scripts/producer.py
```

### 6. Verificar datos en MongoDB
```bash
docker exec -it mongodb mongosh
use transport_db
db.trains_flink_clean.find().pretty()
```

### 7. Acceder a la API Flask
```
http://localhost:5000/trains
```

---

## 🎓 Notas Adicionales
- Puedes cambiar la estación consultada desde la API editando el `station_code` en `producer.py`.
- Flink y el Consumer están dockerizados y corren automáticamente.
- La arquitectura es extensible y podría incluir dashboards (ej. Power BI o Grafana).

---

## 📚 Aprendizajes Clave
- Conceptos de arquitecturas orientadas a eventos.
- Uso de Kafka como sistema de mensajería.
- Transformaciones con Apache Flink.
- Persistencia de datos con MongoDB.
- Visualización RESTful con Flask.

---

## 🌟 Autor
Carlos - Ingeniero de Datos

---

## 🎓 Futuras Mejoras
- Procesamiento por ventanas de tiempo en Flink.
- Visualización en tiempo real con dashboards.
- Autenticación y seguridad para la API REST.

