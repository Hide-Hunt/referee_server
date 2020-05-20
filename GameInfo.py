from dataclasses import dataclass
from typing import Dict

from proto import Game_pb2, Location_pb2


@dataclass
class Player:
    id: int
    faction: str
    score: int = 0
    location: Location_pb2.Location = None

    @staticmethod
    def from_dict(p_id: int, p_dict: Dict) -> 'Player':
        return Player(p_id, p_dict['faction'])


class GameInfo:
    def __init__(self, game_id: str, repo):
        self.id = game_id
        self.repo = repo
        game_data = self.repo.get_game(self.id)
        sorted_participation = enumerate(sorted(game_data['participation'], key=lambda p: p['userID']))

        self.duration = game_data['duration']
        self.players: Dict[Player] = dict(map(lambda p: (p[0], Player.from_dict(p[0], p[1])), sorted_participation))
        self.preys = list(map(lambda p: p.id, filter(lambda p: p.faction is 'PREY', self.players)))
        self.predators = list(map(lambda p: p.id, filter(lambda p: p.faction is 'PREDATOR', self.players)))
        self.alive_preys = self.preys.copy()
        self.dead_preys = []

        self.log = Game_pb2.Game()
        self.log.id = game_id

    def set_started(self):
        self.repo.set_game_started(self.id)

    def set_stopped(self):
        self.repo.set_game_ended(self.id)

    def upload_log(self):
        self.repo.upload_log(self.id, self.log.SerializeToString())
