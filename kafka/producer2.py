#pip install confluent-kafka --no-cache-dir
from confluent_kafka import Producer
import random
import time

# Kafka broker configuration
bootstrap_servers = 'sandbox-hdf.hortonworks.com:6667'
topic = 'iot-data-topic'

# Create Kafka producer configuration
conf = {
    'bootstrap.servers': bootstrap_servers,
    'client.id': 'iot-producer'
}

# Create Kafka producer instance
producer = Producer(conf)

# Function to generate random IoT data
def generate_iot_data():
    temperature = random.uniform(20, 30)
    humidity = random.uniform(40, 60)
    wind = random.uniform(0, 10)
    return {
        'temperature': temperature,
        'humidity': humidity,
        'wind': wind
    }

# Main producer loop
while True:
    try:
        # Generate IoT data
        iot_data = generate_iot_data()

        # Convert data to string format
        message_value = f"Temperature: {iot_data['temperature']}, Humidity: {iot_data['humidity']}, Wind: {iot_data['wind']}"

        # Produce message to Kafka topic
        producer.produce(topic=topic, value=message_value)

        # Flush producer to ensure message delivery
        producer.flush()

        # Print produced message
        print(f"Produced message: {message_value}")

        # Wait for 1 second before sending the next message
        time.sleep(1)

    except KeyboardInterrupt:
        # Break the loop if the script is interrupted
        break

# Close the Kafka producer
producer.flush()
producer.close()
