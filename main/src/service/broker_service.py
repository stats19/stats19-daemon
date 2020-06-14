import json

import pika
import logging

from dataclasses import dataclass


logger = logging.getLogger(__name__)




@dataclass
class BrokerService:
    username: str
    password: str
    queue: str
    port: int
    host: str

    def send(self, message: dict):
        message = json.dumps(message)
        credentials = pika.PlainCredentials(self.username, self.password)
        connection = pika.BlockingConnection(pika.ConnectionParameters(self.host, self.port, '/', credentials))
        properties = pika.BasicProperties(content_type='application/json',
                                          content_encoding='UTF-8',
                                          delivery_mode=1)
        channel = connection.channel()

        channel.queue_declare(queue=self.queue)

        channel.basic_publish(exchange='',
                              routing_key=self.queue,
                              body=message, properties=properties)
        logger.debug(f'Send {message}')
        print(f'Send {message}')

        connection.close()

    def receive(self):
        credentials = pika.PlainCredentials(self.username, self.password)
        connection = pika.BlockingConnection(pika.ConnectionParameters(self.host, self.port, '/', credentials))

        channel = connection.channel()

        channel.queue_declare(queue=self.queue)

        channel.basic_consume(queue=self.queue, auto_ack=True, on_message_callback=self._callback)
        channel.start_consuming()

    @staticmethod
    def _callback(channel, method, properties, body):
        logger.debug(f'Received {body}')
        print(f'Received {body}')
        return body


