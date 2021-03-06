import threading
from queue import Queue
from typing import Dict

from firebase_repo import FirebaseRepo
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
        self.mqtt_client.on_connect = self.on_mqtt_connect
        self.mqtt_client.on_disconnect = self.on_mqtt_disconnect
        self.mqtt_client.on_message = self.on_message
        connect_mqtt_with_credentials(self.mqtt_client)
        self.mqtt_barrier = threading.Barrier(2)

    def run(self):
        print("Starting dispatcher")
        self.mqtt_client.loop_start()
        print("Waiting for MQTT connection...")
        self.mqtt_barrier.wait()
        self.running = True
        print("Dispatcher running: waiting for action to be queued")
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
        try:
            print("Starting game with id {}".format(game_id))
            self.games[game_id] = Referee(game_id, self.mqtt_client, self.game_repo, self.on_game_stop)
        except ReferenceError:
            print("Invalid game ID {}".format(game_id))

    def on_game_stop(self, game_id: str):
        print("Game {} has stopped".format(game_id))
        self.games.pop(game_id, None)

    def on_mqtt_connect(self, client: mqtt.Client, obj, flags, rc):
        print("MQTT connected")
        self.mqtt_barrier.wait()

    @staticmethod
    def on_mqtt_disconnect(client: mqtt.Client, obj, rc):
        print("MQTT disconnected")

    def on_message(self, client: mqtt.Client, obj, msg: mqtt.MQTTMessage):
        print("Processing message with topic {}".format(msg.topic))
        topic = msg.topic.split("/")
        try:
            referee = self.games[topic[0]]
        except KeyError:
            print("Invalid MQTT message (wrong game ID)")
            return

        if topic[1] == "catch":
            referee.on_catch(msg.payload)
        else:
            referee.on_location(int(topic[1]), msg.payload)
