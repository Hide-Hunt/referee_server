import threading

import paho.mqtt.client as mqtt

from GameInfo import GameInfo
from proto import LocationEvent_pb2, CatchEvent_pb2


class Referee:
    def __init__(self, game_id: str, mqtt_client: mqtt.Client, repo):
        self.mqtt_client = mqtt_client
        self.info = GameInfo(game_id, repo)
        self.running = True
        
        self.mqtt_client.subscribe(self.info.id + "/catch")
        for player in self.info.players:
            self.mqtt_client.subscribe(self.info.id + "/" + str(player.id))

        self.info.set_started()

        self.timeout_thread = threading.Timer(self.info.duration, self.stop)
        self.timeout_thread.start()
        self.stop_lock = threading.Lock()

    def stop(self):
        self.stop_lock.acquire()
        if self.running:
            self.running = False
            self.timeout_thread.cancel()
            self.mqtt_client.unsubscribe(self.info.id + "/catch")
            for player in self.info.players:
                self.mqtt_client.unsubscribe(self.info.id + "/" + str(player.id))
            self.info.set_stopped()
            self.info.upload_log()
        self.stop_lock.release()

    def on_catch(self, event: CatchEvent_pb2.CatchEvent):
        self.info.log.events.append(event)
        self.info.alive_preys.remove(event.preyID)
        self.info.dead_preys.append(event.preyID)
        if self.is_over():
            self.stop()

    def on_location(self, event: LocationEvent_pb2.LocationEvent):
        self.info.log.events.append(event)
        self.info.players[event.playerID].location = event.location

    def is_over(self) -> bool:
        return not self.info.alive_preys
