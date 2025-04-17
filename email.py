import json

from kafka import KafkaConsumer 
from kafka import KafkaProducer 


ORDER_CONFIRMED_KAFKA_TOPIC="order_confirmed"

consumer=KafkaConsumer(
    ORDER_CONFIRMED_KAFKA_TOPIC,
    bootstrap_servers="localhost:29092"

) 

print("stat listing... ")
email_Sent_so_far=set()
while True:
    for message in consumer:
        consumed_mess=json.loads(message.value.decode())
        email_mess=consumed_mess['customer_email']
        print(f'sending email to {email_mess}')
        email_Sent_so_far.add(email_mess)
        print(f'email sending so far {len(email_Sent_so_far)} unique emails')


