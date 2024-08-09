from confluent_kafka import Producer
import socket

conf = {'bootstrap.servers': 'kafka:9092'}

producer = Producer(conf)
topic = "purchases"

producer.produce(topic, key="key", value="value")