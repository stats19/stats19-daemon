import logging
from dataclasses import dataclass

from main.src.exporter.api_exporter import ApiExporter
from main.src.importer.api_importer import ApiImporter
from main.src.process.process_interface import Process

logger = logging.getLogger(__name__)


@dataclass
class LeaguesProcess(Process):
    importer_api: ApiImporter
    exporter_api: ApiExporter
    name: str

    def call_process(self) -> None:
        logger.info(f'Call process {self.name}')

        self.exporter_api.save_process_status_start(self.name)

        if self.force_process_execution:
            self._start_safe_process()
        else:
            self._start_safe_process()

        logger.info(f'End process {self.name}')

        self.exporter_api.save_process_status_ended(self.name)

    def _start_safe_process(self):
        leagues = self.importer_api.get_all_leagues()
