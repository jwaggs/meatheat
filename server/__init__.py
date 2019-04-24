from .routes import *

import firebase_admin
from firebase_admin import credentials
import os


firebase_json_file = os.getenv('MEATHEAT_FIREBASE')
cred = credentials.Certificate(firebase_json_file)
firebase_app = firebase_admin.initialize_app(cred)

print(firebase_app.name)
