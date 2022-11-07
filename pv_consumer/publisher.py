import pika
import json


class Publisher:
    def __init__(self, exchange: str, exchange_type="fanout"):
        """
        :param exchange: Name of exchange where messages are published to
        :param exchange_type: "topic", "fanout", "header". !Only "fanout" supported here!
        """
        self.exchange = exchange
        self.exchange_type = exchange_type
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange=self.exchange, exchange_type=self.exchange_type)
        print(f"created Publisher with exchange: {self.exchange} and exchange type: {self.exchange_type}")

    def publish_pv_value(self, meter_id: str, timestamp: int, meter_value: float, eom: bool):
        """
        :param meter_id: Unique meter id for identification
        :param timestamp: A timestamp in [s] to be published
        :param meter_value: The power value [W] to be published
        :param eom: If True, tags last message of a batch
        :return: None
        """
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