import logging
from dataclasses import dataclass
from typing import List

from main.src.exporter.broker_exporter import BrokerExporter
from main.src.importer.api_importer import ApiImporter
from main.src.importer.broker_importer import BrokerImporter
from main.src.model.api_model import Player, CARD
from main.src.process.process_interface import Process

logger = logging.getLogger(__name__)

GOAL_KEEPER = 'GOAL KEEPER'
DEFENDER = 'DEFENDER'
MID_FIELDER = 'MID FIELDER'
FORWARD = 'FORWARD'
OTHER = 'OTHER'
SCORE = 5


@dataclass
class ScoreProcess(Process):
    importer_api: ApiImporter

    importer_broker: BrokerImporter
    exporter_broker: BrokerExporter
    name: str

    def call_process(self) -> None:
        logger.info(f'Call process {self.name}')

        self.exporter_broker.send({
            "process": self.name,
            "status": 'RUNNING',
        })

        if self.force_process_execution:
            self._start_safe_process()
        else:
            self._start_safe_process()

        logger.info(f'End process {self.name}')

        self.exporter_broker.send({
            "process": self.name,
            "status": 'ENDED',
        })

    def _start_safe_process(self):
        matches = self.importer_api.get_all_matches_to_note()
        for match in matches:
            logger.debug(match.match_id)
            match.home.players, match.away.players = self.importer_api.get_player_in_match(match.home.players_url)

            home_shot_ratio = self._get_shot_ratio_of_a_team(match.home.players)
            away_shot_ratio = self._get_shot_ratio_of_a_team(match.away.players)

            logger.debug(f'Home : {str(match.home.name)}')
            self._set_score_of_a_team(match.home.players, home_shot_ratio, away_shot_ratio, match.match_id)
            logger.debug(f'Away : {str(match.away.name)}')
            self._set_score_of_a_team(match.away.players, home_shot_ratio, away_shot_ratio, match.match_id)

    def _set_score_of_a_team(self, playerlist: List[Player],
                             home_shot_ratio: float,
                             away_shot_ratio: float,
                             match_id: int):
        for player in playerlist:
            if player and player.id is not None:
                logger.debug(f'{str(player.name)}')
                post = self._get_post_of_player(player)
                if post == GOAL_KEEPER:
                    score = self._create_score_of_goal_keep(player, away_shot_ratio)
                elif post == DEFENDER:
                    score = self._create_score_of_defender(player, away_shot_ratio)
                elif post == MID_FIELDER:
                    score = self._create_score_of_mid_fielder(player, home_shot_ratio)
                elif post == FORWARD:
                    score = self._create_score_of_forward(player, home_shot_ratio)
                else:
                    score = self._create_score_of_other(player, home_shot_ratio)
                self.importer_api.save_score_to_player(player, score, match_id)

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
        return OTHER

    def _create_score_of_goal_keep(self, player: Player, away_shot_ratio: float) -> float:
        score = SCORE
        score -= sum([2 for x in player.fouls if self._get_card_value(x.card) == 1])
        score -= sum([4 for x in player.fouls if self._get_card_value(x.card) == 2])
        score += sum([3 for x in player.shots if x.scored])
        score += away_shot_ratio * 5
        score += len(player.assists)

        return self._is_score_good(score)

    def _create_score_of_defender(self, player: Player, away_shot_ratio: float) -> float:
        score = SCORE
        score -= sum([1 for x in player.fouls if self._get_card_value(x.card) == 1])
        score -= sum([4 for x in player.fouls if self._get_card_value(x.card) == 2])
        score += sum([2 for x in player.shots if x.scored])
        score += len(player.assists)
        score += away_shot_ratio * 3
        return self._is_score_good(score)

    def _create_score_of_mid_fielder(self, player: Player, home_shot_ratio: float) -> float:
        score = SCORE
        score += len([2 for x in player.assists])
        score += sum([0.1 for x in player.crosses])
        score += sum([1.5 for x in player.shots if x.scored])
        score -= sum([1 for x in player.fouls if self._get_card_value(x.card) == 1])
        score -= sum([4 for x in player.fouls if self._get_card_value(x.card) == 2])
        score -= home_shot_ratio
        return self._is_score_good(score)

    def _create_score_of_forward(self, player: Player, home_shot_ratio: float) -> float:
        score = SCORE
        score += len(player.assists)
        score += sum([2 for x in player.shots if x.scored])
        score += sum([.5 if x.on_target else -0.5 for x in player.shots])
        score -= sum([2 for x in player.fouls if self._get_card_value(x.card) == 1])
        score -= sum([4 for x in player.fouls if self._get_card_value(x.card) == 2])
        score -= home_shot_ratio
        return self._is_score_good(score)

    def _create_score_of_other(self, player: Player, home_shot_ratio: float) -> float:
        score = SCORE
        score += len([2 for x in player.assists])
        score += sum([0.1 for x in player.crosses])
        score += sum([1.5 for x in player.shots if x.scored])
        score -= sum([1 for x in player.fouls if self._get_card_value(x.card) == 1])
        score -= sum([4 for x in player.fouls if self._get_card_value(x.card) == 2])
        score -= home_shot_ratio
        return self._is_score_good(score)

    @staticmethod
    def _get_card_value(card: str) -> int:
        if card == 'NO_CARD':
            return CARD.NO_CARD.value
        elif card == 'YELLOW_CARD':
            return CARD.YELLOW_CARD.value
        else:
            return CARD.RED_CARD.value

    @staticmethod
    def _is_score_good(score: float) -> float:
        if score < 0:
            return 0
        elif score > 10:
            return 10
        else:
            return score

    @staticmethod
    def _get_shot_ratio_of_a_team(players: List[Player]) -> float:
        goals = 0
        shots = 0
        for player in players:
            if player:
                for shot in player.shots:
                    if shot.on_target:
                        shots += 1
                    if shot.on_target and shot.scored:
                        goals += 1

        return goals / shots if shots != 0 else 0
