import random
import time

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

keys = ["naver", "kakao", "viva", "coupang", "corca"]
values = [100, 200, 300, 400, 500]

try:
    while True:
        key_choice = random.choice(keys)
        value_choice = random.choice(values)
        producer.send("streaming", key=bytes(key_choice, 'utf-8'), value=bytes(str(value_choice), 'utf-8'))
        time.sleep(1)
except KeyboardInterrupt:
    print('finished!')
