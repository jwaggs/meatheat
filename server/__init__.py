from .routes import *

import firebase_admin
from firebase_admin import credentials
import os
from flask import json

fir_secret = os.getenv('MEATHEAT_FIREBASE')
if not os.path.isfile(fir_secret):
    fir_secret = json.loads(fir_secret)
cred = credentials.Certificate(fir_secret)
firebase_app = firebase_admin.initialize_app(cred)
