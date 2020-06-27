import logging
import os
from dataclasses import dataclass, field
from urllib.error import HTTPError

import requests as rq

from main.src.exporter.interface_exporter import ExporterInterface
from main.src.model.api_model import Player, STATUS

logger = logging.getLogger(__name__)
DEFAULT_TIMEOUT = 120
USERNAME = os.environ.get('USERNAME')
PASSWORD = os.environ.get('PASSWORD')


@dataclass
class ApiExporter(ExporterInterface):
    url: str
    url_login: str
    timeout: int = field(init=False, default=DEFAULT_TIMEOUT)
    token: str = field(init=False, default='')

    def __post_init__(self):
        try:
            logger.debug(f'Connect user to API')
            url = f'{self.url_login}login'
            body = {
                'username': USERNAME,
                'password': PASSWORD
            }
            response = rq.post(url, json=body, timeout=self.timeout)

            if response.status_code != 200:
                return
            self.token = response.headers['Authorization']

        except (rq.exceptions.RequestException, HTTPError, ConnectionError, KeyError) as e:
            logger.error(e, exc_info=True)
            return

    def save_score_to_player(self, player: Player, score: float, match_id: int) -> int:
        try:
            header = {'Authorization': self.token}
            url = f'{self.url_login}process/matches/{match_id}/players/{player.id}'
            body = {"score": "%.1f" % score}
            response = rq.put(url, headers=header, timeout=self.timeout, json=body)

            if response.status_code != 200:
                logger.error(f'Error while updating {str(player.name)} score : {score} for match {match_id}')
                return 0
        except (rq.exceptions.RequestException, HTTPError, ConnectionError, KeyError) as e:
            logger.error(e, exc_info=True)
            return 0
        return 1

    def save_average_score_to_player(self, player: Player, average_score: float) -> int:
        try:
            header = {'Authorization': self.token}
            url = f'{self.url_login}process/players/{player.id}/score'
            body = {"score": "%.1f" % average_score}
            response = rq.post(url, headers=header, timeout=self.timeout, json=body)

            if response.status_code != 200:
                logger.error(f'Error while updating player {str(player.name)} average_score : {average_score}')
                return 0
        except (rq.exceptions.RequestException, HTTPError, ConnectionError, KeyError) as e:
            logger.error(e, exc_info=True)
            return 0
        return 1

    def save_forecast(self, winner: int, match_id: int) -> int:
        try:
            header = {'Authorization': self.token}
            url = f'{self.url_login}process/matches/{match_id}'
            body = {"forecast": winner}
            response = rq.put(url, headers=header, timeout=self.timeout, json=body)

            if response.status_code != 200:
                return 0
        except (rq.exceptions.RequestException, HTTPError, ConnectionError, KeyError) as e:
            logger.error(e, exc_info=True)
            return 0
        return 1

    def save_process_status_start(self, process: str) -> int:
        return self._save_process_status(process, STATUS.STARTED.name)

    def save_process_status_failed(self, process: str) -> int:
        return self._save_process_status(process, STATUS.FAILED.name)

    def save_process_status_ended(self, process: str) -> int:
        return self._save_process_status(process, STATUS.ENDED.name)

    def save_process_status_no_status(self, process: str) -> int:
        return self._save_process_status(process, STATUS.NO_STATUS.name)

    def _save_process_status(self, process: str, status: str) -> int:
        header = {'Authorization': self.token}
        url = f'{self.url_login}process/update/{process}'
        body = {
            'status': status
        }
        logger.debug(body)
        response = rq.post(url, headers=header, json=body, timeout=self.timeout)

        if response.status_code != 200:
            return 0
        return 1
