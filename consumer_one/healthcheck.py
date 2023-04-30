import pika
import time

sleepTime = 20
time.sleep(sleepTime)

print('Connecting to server ...')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='health_check', durable=True)

def callback(ch, method, properties, body):
    print("Health Check ACK ")
    ch.basic_ack(delivery_tag=method.delivery_tag)
    return "Health check ACK"


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='health_check', on_message_callback=callback)
channel.start_consuming()