from .routes import *
from flask import json
from firebase_admin import credentials
import firebase_admin
import os


fir_secret = os.getenv('MEATHEAT_FIREBASE')
if not os.path.isfile(fir_secret):
    fir_secret = json.loads(fir_secret)
cred = credentials.Certificate(fir_secret)
firebase_app = firebase_admin.initialize_app(cred)
