import asyncio
import json
import logging
from dataclasses import dataclass
from threading import Thread
from typing import Any, Dict

import pika

from main.src.importer.interface_importer import ImporterInterface
from main.src.run_server import get_env_level, get_force

logger = logging.getLogger(__name__)


def launch_process(content: Dict[Any, Any]) -> None:
    logger.debug(f'Received {content}')

    logger.debug(f'Launch process {content["process"]}')

    process = content['process']
    environment = content['environment']
    force = content['force']

    env_level = get_env_level(environment)
    force_level = get_force(force, env_level)

    from main.src.service.process_launcher import ProcessLauncher

    launcher = ProcessLauncher(process_name=process,
                               force_process_execution=force_level,
                               environment=env_level)
    launcher.build_process()
    if launcher.process is not None and launcher.process.use_asyncio:
        coroutine = launcher.async_start()
        asyncio.run(coroutine)
    else:
        launcher.start()


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
        content = json.loads(body)

        thread = Thread(target=launch_process, args=(content,))

        thread.start()
        return body
