import logging
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Any

logger = logging.getLogger(__name__)


@dataclass
class LeagueApi:
    leagueId: int
    name: str
    country: str
    matches: str
    teams: List


@dataclass
class Corner:
    id: int
    player_name: str
    player: str
    elapsed: int
    elapsed_plus: int
    type: str


@dataclass
class Cross:
    id: int
    player_name: str
    player: str
    elapsed: int
    elapsed_plus: int
    type: str


@dataclass
class Foul:
    id: int
    culprit_name: str
    culprit: str
    victim_name: str
    victim: str
    elapsed: int
    elapsed_plus: int
    card: str
    type: str


@dataclass
class Shot:
    id: int
    scorer_name: str
    shooter: str
    assist_name: str
    assist: str
    elapsed: int
    elapsed_plus: int
    type: str
    goal_type: str
    scored: bool
    on_target: bool


@dataclass
class Assist:
    shot_id: int
    scorer_name: str
    shooter: str
    assist_name: str
    assist: str
    elapsed: int
    elapsed_plus: int
    scored: bool
    on_target: bool
    type: str
    goal_type: str


@dataclass
class Player:
    id: int
    name: str
    player: str
    team_name: str
    team: str
    position_x: int
    position_y: int
    first_team: bool
    corners: List[Corner]
    crosses: List[Cross]
    fouls: List[Foul]
    shots: List[Shot]
    assists: List[Assist]


# @dataclass
# class Match:
#     match_id: int
#     team_home_id: int
#     team_away_id: int
#     goal_home: int
#     goal_away: int


@dataclass
class TeamMatch:
    team_id: int
    team: str
    name: str
    players_url: str
    players: List[Player] = field(init=False)
    goals: int
    possession: int
    home: bool


@dataclass
class FullMatch:
    match_id: int
    match_fifa_id: int
    season: str
    stage: int
    date: str
    home: TeamMatch
    away: TeamMatch


@dataclass
class MatchDTO:
    match_id: int
    home_team_id: int
    away_team_id: int
    home_goal: int
    away_goal: int
    home_players: List[Player]
    away_players: List[Player]


class CARD(Enum):
    NO_CARD = 0
    YELLOW_CARD = 1
    RED_CARD = 2


def build_fullmatch(match: Any) -> FullMatch:
    return FullMatch(
                    match_id=match['matchId'],
                    match_fifa_id=match['matchFifaId'],
                    season=match['season'],
                    stage=match['stage'],
                    date=match['date'],
                    home=TeamMatch(
                        team_id=match['home']['teamId'],
                        team=match['home']['team'],
                        name=match['home']['name'],
                        players_url=match['home']['players'],
                        goals=match['home']['goals'],
                        possession=match['home']['possession'],
                        home=match['home']['home']
                    ),
                    away=TeamMatch(
                        team_id=match['away']['teamId'],
                        team=match['away']['team'],
                        name=match['away']['name'],
                        players_url=match['away']['players'],
                        goals=match['away']['goals'],
                        possession=match['away']['possession'],
                        home=match['away']['home']
                    )
                )


def build_player(player: Player) -> Player:
    corners: List[Corner] = []
    crosses: List[Cross] = []
    fouls: List[Foul] = []
    shots: List[Shot] = []
    assists: List[Assist] = []
    for corner in player['corners']:
        corners.append(Corner(
            id=corner['cornerId'],
            player_name=corner['playerName'],
            player=corner['player'],
            elapsed=corner['elapsed'],
            elapsed_plus=corner['elapsedPlus'],
            type=corner['type'],
        ))

    for cross in player['crosses']:
        crosses.append(Cross(
            id=cross['crossId'],
            player_name=cross['playerName'],
            player=cross['player'],
            elapsed=cross['elapsed'],
            elapsed_plus=cross['elapsedPlus'],
            type=cross['type'],

        ))

    for foul in player['fouls']:
        fouls.append(Foul(
            id=foul['foulId'],
            culprit_name=foul['culpritName'],
            culprit=foul['culprit'],
            victim_name=foul['victimName'],
            victim=foul['victim'],
            elapsed=foul['elapsed'],
            elapsed_plus=foul['elapsedPlus'],
            card=foul['card'],
            type=foul['type'],

        ))

    for shot in player['shots']:
        shots.append(Shot(
            id=shot['shotId'],
            scorer_name=shot['scorerName'],
            shooter=shot['shooter'],
            assist_name=shot['assistName'],
            assist=shot['assist'],
            elapsed=shot['elapsed'],
            elapsed_plus=shot['elapsedPlus'],
            type=shot['type'],
            goal_type=shot['goalType'],
            scored=shot['scored'],
            on_target=shot['onTarget'],
        ))

    for assist in player['assists']:
        assists.append(Assist(
            shot_id=assist['shotId'],
            scorer_name=assist['scorerName'],
            shooter=assist['shooter'],
            assist_name=assist['assistName'],
            assist=assist['assist'],
            elapsed=assist['elapsed'],
            elapsed_plus=assist['elapsedPlus'],
            scored=assist['scored'],
            on_target=assist['onTarget'],
            type=assist['type'],
            goal_type=assist['goalType'],
        ))
    return Player(
            id=player['playerId'],
            name=player['name'],
            player=player['player'],
            team_name=player['teamName'],
            team=player['team'],
            position_x=player['positionX'],
            position_y=player['positionY'],
            first_team=player['firstTeam'],
            corners=corners,
            crosses=crosses,
            fouls=fouls,
            shots=shots,
            assists=assists
        )
