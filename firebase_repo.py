import json
import os
from queue import Queue

import firebase_admin
from firebase_admin import credentials, firestore, storage


class FirebaseRepo:
    def __init__(self, action_queue: Queue):
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
        self.action_queue = action_queue
        action_query = self.db.collection(u'game_action_queue').order_by(u'timestamp')
        self.action_watch = action_query.on_snapshot(self.__on_action_snapshot)

    def __on_action_snapshot(self, col_snapshot, changes, read_time):
        for change in changes:
            if change.type.name == 'ADDED':
                action = change.document.to_dict()
                change.document.reference.delete()
                self.action_queue.put(action)

    def get_game(self, game_id: str) -> [dict, None]:
        doc = self.db.collection(u'games').document(game_id).get()
        if doc.exists:
            return doc.to_dict()
        else:
            return None

    def set_game_started(self, game_id: str):
        self.db.collection(u'games').document(game_id).update({
            u'state': u'STARTED',
            u'startDate': firestore.SERVER_TIMESTAMP
        })

    def set_game_ended(self, game_id: str):
        self.db.collection(u'games').document(game_id).update({
            u'state': u'ENDED',
            u'endDate': firestore.SERVER_TIMESTAMP
        })

    def upload_log(self, game_id: str, content: bytes):
        blob = self.bucket.blob('replays/'+game_id+'.game')
        blob.upload_from_string(content, content_type='application/octet-stream')
