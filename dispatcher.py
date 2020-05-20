from queue import Queue
from typing import Dict

from firebase_repo import FirebaseRepo
from proto import CatchEvent_pb2, LocationEvent_pb2, Location_pb2
from referee import Referee
import paho.mqtt.client as mqtt
from mqtt_helper import connect_mqtt_with_credentials


class Dispatcher:
    def __init__(self):
        self.games: Dict[str, Referee] = {}
        self.action_queue = Queue()
        self.game_repo = FirebaseRepo(self.action_queue)
        self.running = False

        self.mqtt_client = mqtt.Client()
        self.mqtt_client.on_message = self.on_message
        connect_mqtt_with_credentials(self.mqtt_client)

    def run(self):
        self.mqtt_client.loop_start()
        self.running = True
        while self.running:
            action = self.action_queue.get()
            self.perform_action(action)
        self.mqtt_client.loop_stop()

    def perform_action(self, action: Dict):
        try:
            {
                'start_game': lambda: self.on_new_game(action['game_id'])
            }[action['action']]()
        except KeyError:
            print("Invalid action")

    def on_new_game(self, game_id: str):
        self.games[game_id] = Referee(game_id, self.mqtt_client, self.game_repo, self.on_game_stop)

    def on_game_stop(self, game_id: str):
        self.games.pop(game_id, None)

    def on_message(self, client: mqtt.Client, obj, msg: mqtt.MQTTMessage):
        topic = msg.topic.split("/")
        game = self.games[topic[0]]
        if topic[1] == "catch":
            event = CatchEvent_pb2.CatchEvent()
            event.ParseFromString(msg.payload)
            game.on_catch(event)
        else:
            event = LocationEvent_pb2.LocationEvent()
            event.playerID = topic[1]
            event.location = Location_pb2.Location()
            event.location.ParseFromString(msg.payload)
            game.on_location(event)
