import json
import time
import random
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

products = ['Laptop', 'Phone', 'Tablet', 'Headphones', 'Camera']
countries = ['Morocco', 'France', 'Spain', 'Germany', 'USA']

print("Sending orders...")
while True:
    order = {
        'order_id': random.randint(1000, 9999),
	'product': random.choice(products),
        'price': round(random.uniform(50, 1500), 2),
        'country': random.choice(countries),
        'status': random.choice(['completed', 'pending', 'cancelled'])
    }
    producer.send('ecommerce-orders', order)
    print("Sent: " + str(order))
    time.sleep(1)
