import datetime
import pika



class Listener:
    def __init__(self, exchange, exchange_type):
        self.received_messages = []
        self.exchange = exchange
        self.exchange_type = exchange_type
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange=self.exchange, exchange_type=self.exchange_type)
        result = self.channel.queue_declare(queue='', exclusive=True)
        self.queue_name = result.method.queue
        self.channel.queue_bind(exchange=self.exchange, queue=self.queue_name)
        print(f"Exchange created: {self.exchange}")

    def callback(self, ch, method, properties, body):
        print(" [x] %r" % body)
        self.received_messages.append(body)
        print(self.received_messages)

    def listen_for_packages(self):
        print(f"[*] Waiting for messages on exchange: {self.exchange} exchange_type: {self.exchange_type}. To exit press CTRL+C")
        self.channel.basic_consume(
            queue=self.queue_name, on_message_callback=self.callback, auto_ack=True)
        self.channel.start_consuming()
        print("started consuming")
