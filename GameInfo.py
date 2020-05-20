from proto import Game_pb2


class GameInfo:
    def __init__(self, game_id: str, repo):
        self.id = game_id
        self.repo = repo
        # TODO Fetch real game data from firebase

        self.duration = 60
        self.players = {}
        self.preys = []
        self.predators = []
        self.alive_preys = list(map(lambda p: p.id, self.preys))
        self.dead_preys = []

        self.log = Game_pb2.Game()
        self.log.id = game_id

    def set_started(self):
        self.repo.set_game_started(self.id)

    def set_stopped(self):
        self.repo.set_game_ended(self.id)

    def upload_log(self):
        self.repo.upload_log(self.id, self.log.SerializeToString())
