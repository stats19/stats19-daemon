import logging
from dataclasses import dataclass

from main.src.importer.api_importer import ApiImporter
from main.src.process.process_interface import Process

logger = logging.getLogger(__name__)


@dataclass
class LeagueProcess(Process):
    importer_api: ApiImporter
    name: str

    def call_process(self) -> None:
        logger.info(f'Call process {self.name}')

        if self.force_process_execution:
            self.start_safe_process()
        else:
            self.start_safe_process()

        logger.info(f'End process {self.name}')

    def start_safe_process(self):
        self.importer_api.get_all_leagues()