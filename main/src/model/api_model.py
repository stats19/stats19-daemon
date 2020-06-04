from dataclasses import dataclass, field
from typing import List


@dataclass
class LeagueApi:
    leagueId: int
    name: str
    country: str
    matches: str
    teams: List


@dataclass
class FullMatch:
    match_id: int
    team_home_id: int
    team_away_id: int
    goal_home: int
    goal_away: int


@dataclass
class Player:
    id: int
    name: str
    position_x: int
    position_y: int


@dataclass
class MatchDTO:
    match_id: int
    home_team_id: int
    away_team_id: int
    home_goal: int
    away_goal: int
    home_players: List[Player]
    away_players: List[Player]
