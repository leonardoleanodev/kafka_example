from confluent_kafka import Producer
import socket

# 'client.id': socket.gethostname()

conf = {'bootstrap.servers': 'localhost:9102',
        'client.id': socket.gethostname()}

producer = Producer(conf)

def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))

topic="pageview"
producer.produce(topic, key="key", value="value", callback=acked)
producer.flush()
