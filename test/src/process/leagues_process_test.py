from typing import List
from unittest import TestCase
from unittest.mock import Mock, MagicMock

from main.src.model.api_model import LeagueApi
from main.src.process.league_process import LeagueProcess


class LeaguesProcessTest(TestCase):
    result: List[LeagueApi]

    @classmethod
    def _side_effect_get_all_leagues(cls):
        cls.result = [LeagueApi(1, 'Premier League', 'France', 'url', []),
                      LeagueApi(2, 'Deuxieme League', 'France', 'url', [])]

    @classmethod
    def setUpClass(cls) -> None:
        api_importer = Mock()
        api_importer.get_all_leagues = MagicMock(side_effect=cls._side_effect_get_all_leagues)

        process = LeagueProcess(use_asyncio=False,
                                force_process_execution=False,
                                name='Process League',
                                importer_api=api_importer)

        process.call_process()

    def test_nb_result(self) -> None:
        self.assertEqual(2, len(self.result))

    def test_get_leagues_response_1(self) -> None:
        self.assertEqual(self.result[0].name, 'Premier League')

    def test_get_leagues_response_2(self) -> None:
        self.assertEqual(self.result[1].name, 'Deuxieme League')