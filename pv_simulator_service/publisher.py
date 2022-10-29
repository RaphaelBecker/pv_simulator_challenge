#!/usr/bin/env python
import pika
import sys
from pv_generator.solar_pannel import SolarPanel


class Publisher:
    def __init__(self, solar_panel: SolarPanel):
        self.solar_panel = solar_panel
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange='logs', exchange_type='fanout')

    def publish_pv_values(self):
        message = ' '.join(sys.argv[1:]) or "info: Hello World!"
        self.channel.basic_publish(exchange='logs', routing_key='', body=message)
        print(" [x] Sent %r" % message)

    def close_connection(self):
        self.connection.close()