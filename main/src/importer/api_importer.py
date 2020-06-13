import json
import logging
import os
from urllib.error import HTTPError
import requests as rq
from dataclasses import field, dataclass
from typing import List, Any

from main.src.importer.interface_importer import ImporterInterface
from main.src.model.api_model import LeagueApi, FullMatch, Player


logger = logging.getLogger(__name__)
DEFAULT_TIMEOUT = 120
USERNAME = os.environ.get('USERNAME')
PASSWORD = os.environ.get('PASSWORD')


@dataclass
class ApiImporter(ImporterInterface):
    url: str
    url_login: str
    timeout: int = field(init=False, default=DEFAULT_TIMEOUT)

    def login(self) -> str:
        try:
            logger.debug(f'Connect user to API')
            url = f'{self.url_login}login'
            body = {
                    'username': USERNAME,
                    'password': PASSWORD
                }
            response = rq.post(url, json=body, timeout=self.timeout)

            if response.status_code != 200:
                return ''
            return response.headers['Authorization']

        except (rq.exceptions.RequestException, HTTPError, ConnectionError, KeyError) as e:
            logger.error(e, exc_info=True)
            return ''

    def import_data(self):
        logger.warning("method not implemented")

    def get_all_leagues(self) -> List[LeagueApi]:
        try:
            logger.debug(f'Get all Leagues from API')
            url = f'{self.url}leagues'
            header = {'Authorization': self.login()}
            response = rq.get(url, headers=header, timeout=self.timeout)

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

    def get_all_matches(self) -> List[FullMatch]:
        try:
            logger.debug(f'Get all Matches from API')
            url = f'{self.url}matches?played=1'
            header = {'Authorization': self.login()}
            response = rq.get(url, headers=header, timeout=self.timeout)

            if response.status_code != 200:
                return []
            content = json.loads(response.content)
            match_list = []
            for x in content:
                match = FullMatch(
                    match_id=x['matchId'],
                    team_home_id=x['home']['teamId'],
                    team_away_id=x['away']['teamId'],
                    goal_home=x['home']['goals'],
                    goal_away=x['away']['goals']
                )
                match_list.append(match)
            return match_list
        except (rq.exceptions.RequestException, HTTPError, ConnectionError, KeyError) as e:
            logger.error(e, exc_info=True)
            return []

    def get_matches_to_predict(self) -> List[FullMatch]:
        try:
            logger.debug(f'Get all Matches to predict from API')
            url = f'{self.url}matches?played=0'
            header = {'Authorization': self.login()}
            response = rq.get(url, headers=header, timeout=self.timeout)

            if response.status_code != 200:
                return []
            content = json.loads(response.content)
            match_list = []
            for x in content:
                match = FullMatch(
                    match_id=x['matchId'],
                    team_home_id=x['home']['teamId'],
                    team_away_id=x['away']['teamId'],
                    goal_home=x['home']['goals'],
                    goal_away=x['away']['goals']
                )
                match_list.append(match)
            return match_list
        except (rq.exceptions.RequestException, HTTPError, ConnectionError, KeyError) as e:
            logger.error(e, exc_info=True)
            return []

    def get_matches_DTO(self) -> List[Any]:
        # try:
        #     logger.debug(f'Get all Leagues from API')
        #     url = f'{self.url}leagues'
        #     header = {'Authorization': API_TOKEN}
        #     response = rq.get(url, headers=header)
        #
        #     if response.status_code != 200:
        #         return []
        #
        #     content = json.loads(response.content)
        #     league_list = []
        #     for x in content:
        #         league = LeagueApi(x['leagueId'], x['name'], x['country'], x['matches'], x['teams'])
        #         league_list.append(league)
        #     logger.debug(league_list)
        #     return league_list
        # except (rq.exceptions.RequestException, HTTPError, ConnectionError, KeyError) as e:
        #     logger.error(e, exc_info=True)
        #     return []
        return createMatchDTO()

    def save_score_to_player(self, player: Player, score: int) -> int:
        # update player where id = player.id
        logger.debug(f'Update player {str(player)}')
        return 1