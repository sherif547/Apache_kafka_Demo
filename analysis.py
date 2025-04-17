import json


from kafka import KafkaConsumer


ORDER_CONFIRMED_KAFKA_TOPIC="order_confirmed"

Consumer=KafkaConsumer(ORDER_CONFIRMED_KAFKA_TOPIC,
                       bootstrap_servers="localhost:29092"
)

total_Revenue=0
total_orders=0
print('start listing..')
while True:
    for message in Consumer:
        mess=json.loads(message.value.decode())
        Revenue=mess['total_cost']
        total_orders+=1
        total_Revenue+=Revenue
        print(f'we sold {total_orders} orders ,till now the total Revenue is {total_Revenue}')


