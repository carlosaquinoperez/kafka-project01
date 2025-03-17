FROM apache/flink:1.17-scala_2.12

# Instalar Python y pip
RUN apt-get update && apt-get install -y python3.10 python3-pip curl unzip && \
    pip3 install apache-flink==1.17 pymongo requests && \
    ln -s /usr/bin/python3.10 /usr/bin/python

# Mover a la carpeta /opt/flink/lib
WORKDIR /opt/flink/lib

# Copiar tus .jar del conector Kafka (como parte del build context root)
COPY jars/flink-connector-kafka-1.17.0.jar ./
COPY jars/kafka-clients-3.4.0.jar ./

# Scripts Flink en /opt/flink/jobs
WORKDIR /opt/flink/jobs
COPY scripts/transform_flink_job.py ./
COPY scripts/persist_mongo_consumer.py ./
# (copia todos los scripts que necesites)

# final
