import threading
import time
from typing import Callable

import paho.mqtt.client as mqtt

from GameInfo import GameInfo
from proto import GameEvent_pb2


class Referee:
    def __init__(self, game_id: str, mqtt_client: mqtt.Client, repo, stop_callback: Callable[[str], None]):
        self.mqtt_client = mqtt_client
        self.stop_callback = stop_callback
        self.info = GameInfo(game_id, repo)
        self.timeout_thread = threading.Timer(self.info.duration, self.stop)
        self.stop_lock = threading.Lock()
        self.start_time = time.time()
        self.running = True
        
        self.mqtt_client.subscribe(self.info.id + "/catch", 2)
        for player in self.info.players.values():
            self.mqtt_client.subscribe(self.info.id + "/" + str(player.id), 2)
        self.info.set_started()
        self.timeout_thread.start()
        print("Referee for game {} ready".format(self.info.id))

    def stop(self):
        with self.stop_lock:
            if self.running:
                print("Stopping referee for game {}".format(self.info.id))
                self.running = False
                self.timeout_thread.cancel()
                self.mqtt_client.unsubscribe(self.info.id + "/catch")
                game_duration = time.time() - self.start_time
                for player in self.info.players.values():
                    self.mqtt_client.unsubscribe(self.info.id + "/" + str(player.id))
                    if player.id in self.info.alive_preys:
                        player.score = game_duration
                self.info.set_stopped()
                self.info.upload_log()
                self.stop_callback(self.info.id)

    def on_catch(self, catch_payload):
        # Append event to game log
        game_event = GameEvent_pb2.GameEvent()
        game_event.timestamp = int(time.time())
        game_event.catch_event.ParseFromString(catch_payload)
        self.info.log.events.append(game_event)
        # Update prey state
        event = game_event.catch_event
        self.info.alive_preys.remove(event.preyID)
        self.info.dead_preys.append(event.preyID)
        # Update players' score
        self.info.players[event.predatorID].score += 1
        self.info.players[event.preyID].score = time.time() - self.start_time
        # Check game over condition
        if self.is_over():
            self.stop()

    def on_location(self, player_id: int, location_payload):
        # Append event to game log
        game_event = GameEvent_pb2.GameEvent()
        game_event.timestamp = int(time.time())
        game_event.location_event.playerID = player_id
        game_event.location_event.location.ParseFromString(location_payload)
        self.info.log.events.append(game_event)
        # Update player's location
        self.info.players[player_id].location = game_event.location_event.location
        # Check game over condition
        if self.is_over():
            self.stop()

    def is_over(self) -> bool:
        return not self.info.alive_preys
