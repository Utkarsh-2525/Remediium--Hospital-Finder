import firebase_admin
from csvjson import hps
from firebase_admin import credentials

from firebase_admin import firestore



cred = credentials.Certificate("./serviceKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
for i in hps:
    update_time, city_ref = db.collection(u'Hospitals').add(i)
    print(f'Added document with id {city_ref.id}')
