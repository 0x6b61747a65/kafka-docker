from kafka import KafkaConsumer

consumer = KafkaConsumer('testPythonTopic',
                            client_id='simple-consumer',
                            auto_offset_reset='latest',
                            bootstrap_servers=["localhost:9093", "localhost:9095"])

print(consumer.bootstrap_connected())

for message in consumer:
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))