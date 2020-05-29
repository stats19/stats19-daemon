import json
import logging
import os
from urllib.error import HTTPError
import requests as rq
from dataclasses import field, dataclass
from typing import List

from main.src.importer.interface_importer import ImporterInterface
from main.src.model.api_model import LeagueApi

logger = logging.getLogger(__name__)
DEFAULT_TIMEOUT = 120
API_TOKEN = os.environ.get('API_TOKEN')


@dataclass
class ApiImporter(ImporterInterface):
    url: str
    timeout: int = field(init=False, default=DEFAULT_TIMEOUT)

    def import_data(self):
        logger.warning("method not implemented")

    def get_all_leagues(self) -> List[LeagueApi]:
        try:
            logger.debug(f'Get all Leagues from API')
            url = f'{self.url}leagues'
            header = {'Authorization': API_TOKEN}
            response = rq.get(url, headers=header)

            if response.status_code != 200:
                return []

            content = json.loads(response.content)
            league_list = []
            for x in content:
                league = LeagueApi(x['leagueId'], x['name'], x['country'], x['matches'], x['teams'])
                league_list.append(league)
            logger.debug(league_list)
            return league_list
        except (rq.exceptions.RequestException, HTTPError, ConnectionError, KeyError) as e:
            logger.error(e, exc_info=True)
            return []
