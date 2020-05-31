import json

import requests
from typing import List
from unittest import TestCase
from importlib import resources
from unittest.mock import MagicMock, Mock

import test.resources as test_resources_folder

from main.src.importer.api_importer import ApiImporter
from main.src.model.api_model import LeagueApi


class ApiImporterTest(TestCase):
    api_importer: ApiImporter
    leagues: List[LeagueApi]

    @classmethod
    def setUpClass(cls) -> None:
        with resources.open_text(test_resources_folder, 'api_get_leagues_items.json') as get_api_items_response:
            api_get_leagues_response = Mock()
            api_get_leagues_response.content = get_api_items_response.read()
            api_get_leagues_response.status_code = 200
            requests.get = MagicMock(return_value=api_get_leagues_response)
            cls.api_importer = ApiImporter('')
            cls.leagues = cls.api_importer.get_all_leagues()

    def test_get_leagues_response_1(self) -> None:
        print(self.leagues)
        self.assertEqual(self.leagues[0].name, 'Premiere league')

    def test_get_leagues_response_2(self) -> None:
        self.assertEqual(self.leagues[1].name, 'Deuxieme league')

    def test_get_leagues_response_length(self) -> None:
        self.assertEqual(len(self.leagues), 2)
