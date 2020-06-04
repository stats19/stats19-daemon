import logging
from dataclasses import dataclass
from enum import Enum

from main.src.importer.api_importer import ApiImporter
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
    name: str

    def call_process(self) -> None:
        logger.info(f'Call process {self.name}')

        if self.force_process_execution:
            self._start_safe_process()
        else:
            self._start_safe_process()

        logger.info(f'End process {self.name}')

    def _start_safe_process(self):
        logger.info('Working')

        matches = self.importer_api.get_matches_to_predict()
        accuracy = 0
        res = DatasetService.predict_result_with_linear_model(matches)
        for i in range(0, len(res)):
            match = matches[i]
            if match.goal_away > match.goal_home:
                if res[i] == 1:
                    accuracy += 1
                print(f' Away devrais gagner, score : {match.goal_home}-{match.goal_away} mais l\'algo predit : {WHOWON(res[i]).name}')
            elif match.goal_away < match.goal_home:
                if res[i] == 0:
                    accuracy += 1
                print(f' Home devrais gagner, score : {match.goal_home}-{match.goal_away} mais l\'algo predit : {WHOWON(res[i]).name}')
            else:
                if res[i] == 2:
                    accuracy += 1
                print(f' Egalité, score : {match.goal_home}-{match.goal_away} mais l\'algo predit : {WHOWON(res[i]).name}')
        print(f'Accuracy = {accuracy/len(res)}')





