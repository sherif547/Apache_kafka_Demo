import json
import time


from kafka import KafkaProducer,producer

ORDER_KAFKA_TOPIC="order_details"
ORDER_LIMIT=15

## producer every thing write in kafka
producer=KafkaProducer(bootstrap_servers='localhost:29092')

print("Going to be generating after 4 seconds")
print("will generate after 4 seconds")

for i in range(1,ORDER_LIMIT):
    data={"order_id":i,
          "user_id":f"sherif{i}",
          "total_cost":i*2,
          "items":"Burger , Cola"
          
          
          }
    
    producer.send(
        ORDER_KAFKA_TOPIC,
        json.dumps(data).encode("utf-8")
    )

    print("Done sending ...{i}")
    time .sleep(4)
