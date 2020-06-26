import json
import logging
from dataclasses import dataclass

import pika

from main.src.exporter.interface_exporter import ExporterInterface

logger = logging.getLogger(__name__)


@dataclass
class BrokerExporter(ExporterInterface):
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

        connection.close()
