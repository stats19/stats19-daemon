import logging
import os
from dataclasses import dataclass
from typing import Any, Dict

from main.src.exporter.api_exporter import ApiExporter
from main.src.exporter.broker_exporter import BrokerExporter
from main.src.exporter.interface_exporter import ExporterInterface
from main.src.importer.api_importer import ApiImporter
from main.src.importer.broker_importer import BrokerImporter
from main.src.importer.interface_importer import ImporterInterface

logger = logging.getLogger(__name__)


@dataclass
class SourceBuilder:
    source_config: Dict[Any, Any]

    def build_importer(self) -> ImporterInterface:
        pass


@dataclass
class DestinationBuilder:
    destination_config: Dict[Any, Any]

    def build_exporter(self) -> ExporterInterface:
        pass


@dataclass
class ApiSourceBuilder(SourceBuilder):

    def build_importer(self) -> ApiImporter:
        logger.debug('Build importer for API')

        url = self.source_config['url']
        url_login = self.source_config['url_login']
        return ApiImporter(url=url, url_login=url_login)


@dataclass
class ApiDestinationBuilder(DestinationBuilder):

    def build_exporter(self) -> ApiExporter:
        logger.debug('Build exporter for API')

        url = self.destination_config['url']
        url_login = self.destination_config['url_login']
        return ApiExporter(url=url, url_login=url_login)


@dataclass
class BrokerSourceBuilder(SourceBuilder):

    def build_importer(self) -> BrokerImporter:
        logger.debug('Build importer for Broker')

        host = os.getenv('SOURCE_BROKER_HOST')
        port = int(os.getenv('SOURCE_BROKER_PORT'))
        username = os.getenv('SOURCE_BROKER_USERNAME')
        password = os.getenv('SOURCE_BROKER_PASSWORD')
        queue = os.getenv('SOURCE_BROKER_QUEUE')
        vhost = os.getenv('SOURCE_BROKER_VHOST')
        return BrokerImporter(host=host, port=port, password=password, username=username, queue=queue, vhost=vhost)


@dataclass
class BrokerDestinationBuilder(SourceBuilder):

    def build_exporter(self) -> BrokerExporter:
        logger.debug('Build exporter for Broker')

        host = os.getenv('DESTINATION_BROKER_HOST')
        port = int(os.getenv('DESTINATION_BROKER_PORT'))
        username = os.getenv('DESTINATION_BROKER_USERNAME')
        password = os.getenv('DESTINATION_BROKER_PASSWORD')
        queue = os.getenv('DESTINATION_BROKER_QUEUE')
        vhost = os.getenv('DESTINATION_BROKER_VHOST')

        return BrokerExporter(host=host, port=port, password=password, username=username, queue=queue, vhost=vhost)
