from kafka import KafkaProducer
from time import sleep

producer = KafkaProducer(bootstrap_servers=["localhost:9093","localhost:9095"])
print(producer.bootstrap_connected())

for _ in range(1000):
    print('writing to kafka-broker...')
    producer.send('testPythonTopic', b'Test message')
    sleep(5)