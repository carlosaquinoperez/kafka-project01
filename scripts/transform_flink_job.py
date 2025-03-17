from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors import FlinkKafkaConsumer, FlinkKafkaProducer
from pyflink.common.serialization import SimpleStringSchema
from pyflink.common.typeinfo import Types
import json

def transform_event(value: str) -> str:
    data = json.loads(value)
    data["transformed"] = True
    return json.dumps(data)

env = StreamExecutionEnvironment.get_execution_environment()

consumer_props = {
    'bootstrap.servers': 'kafka:29092',
    'group.id': 'flink-transform-group'
}
consumer = FlinkKafkaConsumer(
    topics='transport-events',
    deserialization_schema=SimpleStringSchema(),
    properties=consumer_props
)

producer_props = {
    'bootstrap.servers': 'kafka:29092'
}
producer = FlinkKafkaProducer(
    topic='transport-clean',
    serialization_schema=SimpleStringSchema(),
    producer_config=producer_props
)

# IMPORTANTE: Usa Types.STRING() con paréntesis
data_stream = env.add_source(
    consumer,
    type_info=Types.STRING()
)

# También output_type=Types.STRING() con paréntesis
transformed_stream = data_stream.map(
    transform_event,
    output_type=Types.STRING()
)

# Opcional para debug
transformed_stream.print()

transformed_stream.add_sink(producer)

env.execute("Flink Transform Job")
