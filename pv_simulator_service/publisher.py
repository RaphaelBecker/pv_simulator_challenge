import pika
import json


class Publisher:
    def __init__(self, exchange, exchange_type):
        self.exchange = exchange
        self.exchange_type = exchange_type
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange=self.exchange, exchange_type=self.exchange_type)
        print(f"created Publisher with exchange: {self.exchange} {self.exchange_type}")

    def publish_pv_value(self, meter_id: str, timestamp: int, meter_value: float, eom: bool):
        if eom:
            message = "eom"
            print("Reached end of message batch!")
            self.channel.basic_publish(exchange=self.exchange, routing_key='', body=message)
        else:
            message = json.dumps(dict(timestamp= timestamp, meter_id= meter_id, meter_value=meter_value))
            self.channel.basic_publish(exchange=self.exchange, routing_key='', body=message)
            print("Sent: " + str(message))

    def close_connection(self):
        self.connection.close()