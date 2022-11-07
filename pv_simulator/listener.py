import pika
import threading


class Listener:
    def __init__(self, exchange: str, exchange_type="fanout"):
        """
        :param exchange: Name of exchange where to listen to
        :param exchange_type: "topic", "fanout", "header". !Only "fanout" supported here!
        """
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
        self.receiving = False

    def callback(self, ch, method, properties, body):
        if body.decode() == "eom":
            self.receiving = False
        else:
            self.receiving = True
            self.received_messages.append(body)

    def listen_for_packages(self):
        self.channel.basic_consume(
            queue=self.queue_name, on_message_callback=self.callback, auto_ack=True)
        receiver_thread = threading.Thread(target=self.channel.start_consuming)
        receiver_thread.daemon = True
        receiver_thread.start()
        receiver_thread.join(0)
        print(f"started consuming thread. Waiting for messages on exchange: {self.exchange} exchange_type: "
              f"{self.exchange_type}. To exit press CTRL+C)")

    def delete_messages(self):
        self.received_messages = []