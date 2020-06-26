import logging
from dataclasses import dataclass
from enum import Enum

from main.src.exporter.api_exporter import ApiExporter
from main.src.importer.api_importer import ApiImporter
from main.src.process.process_interface import Process
from main.src.service.dataset_service import DatasetService

logger = logging.getLogger(__name__)
logging.getLogger('matplotlib').setLevel(logging.ERROR)


class WHOWON(Enum):
    HOMEWON = 0
    EQUALITY = 1
    AWAYWON = 2


@dataclass
class PredictProcess(Process):
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
        matches = self.importer_api.get_matches_to_predict()
        accuracy = 0
        if not matches:
            return
        res = DatasetService.predict_result_with_linear_model(matches)
        for i in range(0, len(res)):
            match = matches[i]
            if match.away.goals > match.home.goals:
                if res[i] == 2:
                    accuracy += 1
                logger.debug(
                    f' Away devrais gagner, score : {match.home.goals}-{match.away.goals} mais l\'algo predit : {WHOWON(res[i]).name}')
            elif match.away.goals < match.home.goals:
                if res[i] == 0:
                    accuracy += 1
                logger.debug(
                    f' Home devrais gagner, score : {match.home.goals}-{match.away.goals} mais l\'algo predit : {WHOWON(res[i]).name}')
            else:
                if res[i] == 1:
                    accuracy += 1
                logger.debug(
                    f' Egalité, score : {match.home.goals}-{match.away.goals} mais l\'algo predit : {WHOWON(res[i]).name}')

            self.exporter_api.save_forecast(WHOWON(res[i]).value, match.match_id)
        logger.info(f'Accuracy = {accuracy / len(res)}')
