import json
import os
import time

import firebase_admin
from firebase_admin import credentials, firestore, storage


class FirebaseTool:
    def __init__(self):
        service_account_key = os.environ.get("FIREBASE_CERTIFICATE", None)
        if service_account_key is None:
            cred = credentials.Certificate("serviceAccountKey.json")
        else:
            cred = credentials.Certificate(json.loads(service_account_key))
        self.firebase_app = firebase_admin.initialize_app(cred, {
            'storageBucket': 'hidehunt-71e41.appspot.com'
        })
        self.db = firestore.client()
        self.bucket = storage.bucket()

    def start_game(self, game_id: str, action: str):
        self.db.collection(u'game_action_queue').add({
            u'timestamp': time.time(),
            u'action': action,
            u'game_id': game_id
        })
