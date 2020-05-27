from dataclasses import dataclass
from typing import List


@dataclass
class LeagueApi:
    leagueId: int
    name: str
    country: str
    matches: str
    teams: List
