from .app import app
from .redis import fid_add_devices, fid_devices
from flask import request, json, g
import random
import string


@app.route('/', methods=['GET'])
@app.route('/health_check', methods=['GET'])
def health_check():
    app.logger.info('app logger info health check')
    return json.dumps({'healthy': True}), 200, {'ContentType': 'application/json'}


def random_string(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


@app.route('/redis/add', methods=['GET'])
def redis_add():
    app.logger.info('redis add endpoint')
    device = random_string()
    fid_add_devices('12345', device)
    return json.dumps({'device': device}), 200, {'ContentType': 'application/json'}


@app.route('/redis/get', methods=['GET'])
def redis_get():
    app.logger.info('redis get endpoint')
    devices = fid_devices('12345')
    response = []
    for d in devices:
        response.append(d)
    return json.dumps({'fid': devices}), 200, {'ContentType': 'application/json'}
