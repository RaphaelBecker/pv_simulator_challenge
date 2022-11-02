#!/usr/bin/env python
import pika
import json


class Publisher:
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange='logs', exchange_type='fanout')

    def publish_pv_value(self, meter_id, timestamp, meter_value):
        message = dict(timestamp= timestamp, meter_id= meter_id, meter_value=meter_value)
        self.channel.basic_publish(exchange='logs', routing_key='', body=json.dumps(message))
        print(f" [x] Sent - meter_id: {message['meter_id']}, timestamp: {message['timestamp']}, meter_value: {message['meter_value']}")

    def close_connection(self):
        self.connection.close()