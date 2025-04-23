#pip install confluent-kafka --no-cache-dir
from confluent_kafka import Consumer, KafkaError

# Kafka broker configuration
bootstrap_servers = 'sandbox-hdf.hortonworks.com:6667'
topic = 'iot-data-topic'
group_id = 'iot-consumer-group'

# Create Kafka consumer configuration
conf = {
    'bootstrap.servers': bootstrap_servers,
    'group.id': group_id,
    'auto.offset.reset': 'earliest'
}

# Create Kafka consumer instance
consumer = Consumer(conf)

# Subscribe to the Kafka topic
consumer.subscribe([topic])

# Main consumer loop
while True:
    try:
        # Poll for Kafka messages
        message = consumer.poll(timeout=1.0)

        if message is None:
            continue

        if message.error():
            if message.error().code() == KafkaError._PARTITION_EOF:
                # Reached end of Kafka partition
                continue
            else:
                # Error occurred
                print(f"Error occurred: {message.error().str()}")
                continue

        # Process the consumed message
        value = message.value().decode('utf-8')
        print(f"Consumed message: {value}")

    except KeyboardInterrupt:
        # Break the loop if the script is interrupted
        break

# Close the Kafka consumer
consumer.close()
