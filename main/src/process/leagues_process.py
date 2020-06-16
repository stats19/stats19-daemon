import logging
from dataclasses import dataclass

from main.src.exporter.broker_exporter import BrokerExporter
from main.src.importer.api_importer import ApiImporter
from main.src.importer.broker_importer import BrokerImporter
from main.src.process.process_interface import Process

logger = logging.getLogger(__name__)


@dataclass
class LeaguesProcess(Process):
    importer_api: ApiImporter
    importer_broker: BrokerImporter
    exporter_broker: BrokerExporter
    name: str

    def call_process(self) -> None:
        logger.info(f'Call process {self.name}')

        self.exporter_broker.send({
            "process": self.name,
            "status": 'RUNNING',
        })

        if self.force_process_execution:
            self._start_safe_process()
        else:
            self._start_safe_process()

        logger.info(f'End process {self.name}')

        self.exporter_broker.send({
            "process": self.name,
            "status": 'ENDED',
        })

    def _start_safe_process(self):
         leagues = self.importer_api.get_all_leagues()
