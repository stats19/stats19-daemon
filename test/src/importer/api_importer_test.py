import json

import requests
from typing import List
from unittest import TestCase
from importlib import resources
from unittest.mock import MagicMock, Mock

import test.resources as test_resources_folder

from main.src.importer.api_importer import ApiImporter
from main.src.model.api_model import LeagueApi
from main.src.utils.utils import extract_dict_value


class ApiImporterTest(TestCase):
    api_importer: ApiImporter
    leagues: List[LeagueApi]

    @classmethod
    def setUpClass(cls) -> None:
        with resources.open_text(test_resources_folder, 'api_get_leagues_items.json') as get_api_items_response:
            api_get_leagues_response = Mock()
            api_get_leagues_response.content = get_api_items_response.read()
            league_list = []
            for x in json.loads(api_get_leagues_response.content):
                league_list.append(extract_dict_value(x, lambda dict_: dict_['name']))
            print(league_list)
            requests.get = MagicMock(return_value=api_get_leagues_response)
            cls.api_importer = ApiImporter(None, None)
            cls.leagues = cls.api_importer.get_all_leagues()

    def test_get_leagues_response_1(self) -> None:
        self.assertEqual(self.leagues[0].name, 'Premier League')

    def test_get_leagues_response_2(self) -> None:
        self.assertEqual(self.leagues[1].name, 'Deuxieme League')

    def test_get_leagues_response_length(self) -> None:
        self.assertEqual(len(self.leagues), 2)
