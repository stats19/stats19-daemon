from dataclasses import dataclass
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
