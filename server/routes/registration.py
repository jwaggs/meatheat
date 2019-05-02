from flask import json
from server.app import app
from server.cache.user import fid_add_device, fid_add_controller
from server.cache.device import all_devices


@app.route('/user/<fid>/devices/<device>/', methods=['POST', 'GET'])  # TODO: remove GET from methods
# @authenticate
def register_device(fid, device):
    app.logger.info(f'register_device endpoint. fid: {fid} device: {device}')
    fid_add_device(fid, device)
    return json.dumps({'registered': device}), 200, {'ContentType': 'application/json'}


@app.route('/user/<fid>/controllers/<controller>/', methods=['POST', 'GET'])  # TODO: remove GET from methods
# @authenticate
def register_controller(fid, controller):
    app.logger.info(f'register_controller endpoint. fid: {fid} controller: {controller}')
    fid_add_controller(fid, controller)
    return json.dumps({'registered': controller}), 200, {'ContentType': 'application/json'}


# TODO: for development purposes only.... remove this route once application finished.
@app.route('/devices/<device>/', methods=['POST'])
def register_device_to_all(device):
    app.logger.info(f'add_device_to_all endpoint. device: {device}')
    all_devices(device)
    return json.dumps({'registered': device}), 200, {'ContentType': 'application/json'}
