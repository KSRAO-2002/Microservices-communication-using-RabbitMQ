import pika
import time
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
import socket
import certifi
import pymongo
from pymongo.mongo_client import MongoClient

app = Flask(__name__)
uri = "mongodb+srv://sujanraor2002:RDJ200218341@cluster0.daiqnjt.mongodb.net/test"
client = MongoClient(uri,tlsCAFile=certifi.where())
db = client['studentdb']
collection = db["student"]
sleepTime = 20
time.sleep(sleepTime)
print('Consumer_three connecting to server ...')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='delete_record', durable=True)

def callback(ch, method, properties, body):
    b = body.decode()
    collection.delete_one({"SRN":b})
    ch.basic_ack(delivery_tag=method.delivery_tag)
    return "Student deleted successfully!"
    
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='delete_record', on_message_callback=callback)
channel.start_consuming()