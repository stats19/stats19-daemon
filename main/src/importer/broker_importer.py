import json

import pika
import logging

from dataclasses import dataclass

from main.src.importer.interface_importer import ImporterInterface

logger = logging.getLogger(__name__)


@dataclass
class BrokerImporter(ImporterInterface):
    username: str
    password: str
    queue: str
    port: int
    host: str

    def receive(self):
        credentials = pika.PlainCredentials(self.username, self.password)
        connection = pika.BlockingConnection(pika.ConnectionParameters(self.host, self.port, '/', credentials))

        channel = connection.channel()

        channel.queue_declare(queue=self.queue)

        channel.basic_consume(queue=self.queue, auto_ack=True, on_message_callback=self._callback)
        logger.info('To stop process press CTRL + C')
        logger.info('Start listenning ...')

        channel.start_consuming()

    @staticmethod
    def _callback(channel, method, properties, body):
        logger.debug(f'Received {body}')
        content = json.loads(body)
        logger.debug(f'Received {content}')

        logger.debug(f'Launche process {content["process"]}')



        return body


