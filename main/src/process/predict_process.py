import logging
from dataclasses import dataclass
from enum import Enum

from main.src.exporter.broker_exporter import BrokerExporter
from main.src.importer.api_importer import ApiImporter
from main.src.importer.broker_importer import BrokerImporter
from main.src.process.process_interface import Process
from main.src.service.dataset_service import DatasetService

logger = logging.getLogger(__name__)
logging.getLogger('matplotlib').setLevel(logging.ERROR)


class WHOWON(Enum):
    HOMEWON = 0
    AWAYWON = 1
    EQUALITY = 2


@dataclass
class PredictProcess(Process):
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
        logger.info('Working')

        matches = self.importer_api.get_matches_to_predict()
        accuracy = 0
        if not matches:
            return
        res = DatasetService.predict_result_with_linear_model(matches)
        for i in range(0, len(res)):
            match = matches[i]
            if match.away.goals > match.home.goals:
                if res[i] == 1:
                    accuracy += 1
                logger.info(f' Away devrais gagner, score : {match.home.goals}-{match.away.goals} mais l\'algo predit : {WHOWON(res[i]).name}')
            elif match.away.goals < match.home.goals:
                if res[i] == 0:
                    accuracy += 1
                logger.info(f' Home devrais gagner, score : {match.home.goals}-{match.away.goals} mais l\'algo predit : {WHOWON(res[i]).name}')
            else:
                if res[i] == 2:
                    accuracy += 1
                logger.info(f' Egalité, score : {match.home.goals}-{match.away.goals} mais l\'algo predit : {WHOWON(res[i]).name}')
        logger.info(f'Accuracy = {accuracy/len(res)}')





