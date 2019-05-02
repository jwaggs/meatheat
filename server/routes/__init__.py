from .registration import *
from .state import *
from .webhook import *
from flask import json
from server.app import app


@app.route('/', methods=['GET'])
@app.route('/health_check/', methods=['GET'])
def health_check():
    app.logger.info('app logger info health check')
    return json.dumps({'healthy': True}), 200, {'ContentType': 'application/json'}
