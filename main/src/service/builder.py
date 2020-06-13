import logging
from dataclasses import dataclass
from typing import Any, Dict

from main.src.importer.api_importer import ApiImporter
from main.src.importer.interface_importer import ImporterInterface

logger = logging.getLogger(__name__)


@dataclass
class SourceBuilder:
    source_config: Dict[Any, Any]

    def build_importer(self) -> ImporterInterface:
        pass


@dataclass
class ApiSourceBuilder(SourceBuilder):

    def build_importer(self) -> ApiImporter:
        logger.debug('Build importer for API')

        url = self.source_config['url']
        url_login = self.source_config['url_login']
        return ApiImporter(url=url, url_login=url_login)

