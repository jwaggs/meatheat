from flask import Flask
import logging
import sys


app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))  # necessary for app.logger to show in heroku logs.
app.logger.setLevel(logging.INFO)
