from kafka import KafkaConsumer

consumer = KafkaConsumer('pageview',
                         auto_offset_reset='earliest',
                         group_id='pageview-group1',
                         bootstrap_servers=['localhost:9092'])
for message in consumer:
    print(f"""
        topic     => {message.topic}
        partition => {message.partition}
        offset    => {message.offset}
        key={message.key} value={message.value}
    """)