import random
import time
import json
from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')
while True:

    random_number = str(random.randrange(999))
    value_dict= {
        "URL": f"URL{random_number}"
    }
    value = json.dumps(value_dict)
    producer.send(
        topic='pageview',
        key=f"{random.randrange(999)}".encode(),
        value=value.encode(),
    )
    print(f"produced value: {value}")
    time.sleep(1)
