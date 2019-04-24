from .app import app
from .redis import fid_add_device, fid_devices, all_devices
from .messaging import send_to_device
from flask import request, json, g
import random
import string


@app.route('/', methods=['GET'])
@app.route('/health_check/', methods=['GET'])
def health_check():
    app.logger.info('app logger info health check')
    return json.dumps({'healthy': True}), 200, {'ContentType': 'application/json'}


@app.route('/user/<fid>/devices/<device>/', methods=['POST', 'GET'])  # TODO: remove GET from methods
def register_device(fid, device):
    app.logger.info(f'register_device endpoint. fid: {fid} device: {device}')
    fid_add_device(fid, device)
    return json.dumps({'registered': device}), 200, {'ContentType': 'application/json'}


@app.route('/user/<fid>/devices/', methods=['GET'])
def get_devices(fid):
    app.logger.info(f'get_devices endpoint. fid: {fid}')
    devices = fid_devices(fid)
    return json.dumps({fid: devices}), 200, {'ContentType': 'application/json'}


@app.route('/state/', methods=['POST', 'GET'])  # TODO: need a good way to associate microcontroller with user account. this spews to all.
def meat_heat():
    app.logger.info(f'meat_heat endpoint')
    for device in all_devices():
        send_to_device(device)

