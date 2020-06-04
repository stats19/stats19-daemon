import logging
from dataclasses import dataclass
from typing import List

from main.src.importer.api_importer import ApiImporter
from main.src.model.api_model import Player
from main.src.process.process_interface import Process

logger = logging.getLogger(__name__)

GOAL_KEEPER = 'GOAL KEEPER'
DEFENDER = 'DEFENDER'
MID_FIELDER = 'MID FIELDER'
FORWARD = 'FORWARD'


@dataclass
class ScoreProcess(Process):
    importer_api: ApiImporter
    name: str

    def call_process(self) -> None:
        logger.info(f'Call process {self.name}')

        if self.force_process_execution:
            self.start_safe_process()
        else:
            self.start_safe_process()

        logger.info(f'End process {self.name}')

    def start_safe_process(self):
        logger.info('score')
        matches = self.importer_api.get_matches_DTO()

        for match in matches:
            # print(match)
            self._set_score_of_a_team(match.home_players)
            self._set_score_of_a_team(match.away_players)

    def _set_score_of_a_team(self, playerlist: List[Player]):
        for player in playerlist:
            logger.debug(f'{str(player)}')
            post = self._get_post_of_player(player)
            if post == GOAL_KEEPER:
                score = self._create_score_of_goal_keep(player)
            elif post == DEFENDER:
                score = self._create_score_of_defender(player)
            elif post == MID_FIELDER:
                score = self._create_score_of_mid_fielder(player)
            else:
                score = self._create_score_of_forward(player)
            self.importer_api.save_score_to_player(player, score)

    @staticmethod
    def _get_post_of_player(player: Player) -> str:
        if player.position_y in [1]:
            return GOAL_KEEPER
        elif player.position_y in [2, 3, 4]:
            return DEFENDER
        elif player.position_y in [5, 6, 7, 8]:
            return MID_FIELDER
        elif player.position_y in [9, 10, 11]:
            return FORWARD

    def _create_score_of_goal_keep(self, player: Player) -> int:
        return 1

    def _create_score_of_defender(self, player: Player) -> int:
        return 1

    def _create_score_of_mid_fielder(self, player: Player) -> int:
        return 1

    def _create_score_of_forward(self, player: Player) -> int:
        return 1

