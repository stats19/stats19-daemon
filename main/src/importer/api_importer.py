import json
import logging
from urllib.error import HTTPError

import requests as rq
from dataclasses import field, dataclass
from typing import List

from main.src.importer.interface_importer import ImporterInterface
from main.src.model.api_model import LeagueApi
from main.src.utils.utils import extract_dict_value

logger = logging.getLogger(__name__)
DEFAULT_TIMEOUT = 120


@dataclass
class ApiImporter(ImporterInterface):
    url: str
    api_token: str
    timeout: int = field(init=False, default=DEFAULT_TIMEOUT)

    def import_data(self):
        logger.warning("method not implemented")

    def get_all_leagues(self) -> List[LeagueApi]:
        try:
            logger.debug(f'Get all Leagues from API')
            url = f'{self.url}leagues'
            header = {'Authorization': self.api_token}
            response = rq.get(url, headers=header)
            content = json.loads(response.content)
            league_list = []
            for x in content:
                league_list.append(extract_dict_value(x, lambda dict_: dict_['name']))

            logger.debug(league_list)
        except (rq.exceptions.RequestException, HTTPError, ConnectionError, KeyError) as e:
            logger.error(e, exc_info=True)
            return []
