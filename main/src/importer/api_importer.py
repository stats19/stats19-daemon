import json
import logging
import os
from urllib.error import HTTPError
import requests as rq
from dataclasses import field, dataclass
from typing import List, Any, Union, Tuple

from main.src.importer.interface_importer import ImporterInterface
from main.src.model.api_model import LeagueApi, Player, FullMatch, TeamMatch, Corner, Cross, Foul, Shot, Assist, \
    build_player, build_fullmatch

logger = logging.getLogger(__name__)
DEFAULT_TIMEOUT = 120
USERNAME = os.environ.get('USERNAME')
PASSWORD = os.environ.get('PASSWORD')


@dataclass
class ApiImporter(ImporterInterface):
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

    def import_data(self):
        logger.warning("method not implemented")

    def get_all_leagues(self) -> List[LeagueApi]:
        try:
            logger.debug(f'Get all Leagues from API')
            url = f'{self.url}leagues'
            header = {'Authorization': self.token}
            response = rq.get(url, headers=header, timeout=self.timeout)

            if response.status_code != 200:
                return []

            content = json.loads(response.content)
            league_list = []

            for x in content:
                league = LeagueApi(x['leagueId'], x['name'], x['country'], x['matches'], x['teams'])
                league_list.append(league)
            return league_list
        except (rq.exceptions.RequestException, HTTPError, ConnectionError, KeyError) as e:
            logger.error(e, exc_info=True)
            return []

    def get_all_matches(self) -> List[FullMatch]:
        try:
            logger.debug(f'Get all Matches from API')
            url = f'{self.url}matches?played=1'
            header = {'Authorization': self.token}
            response = rq.get(url, headers=header, timeout=self.timeout)

            if response.status_code != 200:
                return []
            content = json.loads(response.content)
            match_list = []
            for x in content:
                match = build_fullmatch(x)
                match_list.append(match)
            return match_list
        except (rq.exceptions.RequestException, HTTPError, ConnectionError, KeyError) as e:
            logger.error(e, exc_info=True)
            return []

    def get_matches_to_predict(self) -> List[FullMatch]:
        try:
            logger.debug(f'Get all Matches to predict from API')
            url = f'{self.url}matches?played=0'
            header = {'Authorization': self.token}
            response = rq.get(url, headers=header, timeout=self.timeout)

            if response.status_code != 200:
                return []
            content = json.loads(response.content)
            match_list = []
            for x in content:
                match = build_fullmatch(x)
                match_list.append(match)
            return match_list
        except (rq.exceptions.RequestException, HTTPError, ConnectionError, KeyError) as e:
            logger.error(e, exc_info=True)
            return []

    def save_score_to_player(self, player: Player, score: float) -> int:
        # update player where id = player.id
        logger.debug(f'Update player {str(player.name)} score : {score}')
        return 1

    def get_player_in_match(self, url: str) -> Tuple[List[Player], List[Player]]:
        header = {'Authorization': self.token}
        response = rq.get(url, headers=header, timeout=self.timeout)

        if response.status_code != 200:
            return [], []
        home = []
        away = []
        content = json.loads(response.content)
        for home_player in content['home']:
            home.append(build_player(home_player))
        for away_player in content['away']:
            away.append(build_player(away_player))
        return home, away

