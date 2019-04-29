from .redis import *
from .messaging import send_data_to_device
from .middleware import authenticate
from flask import request, json, abort
from .app import app


@app.route('/', methods=['GET'])
@app.route('/health_check/', methods=['GET'])
def health_check():
    app.logger.info('app logger info health check')
    return json.dumps({'healthy': True}), 200, {'ContentType': 'application/json'}


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


@app.route('/controllers/<controller>/state/', methods=['POST', 'GET'])  # TODO: remove GET from methods
def meat_heat(controller):
    app.logger.info(f'meat_heat endpoint hit for controller: {controller}')
    data = request.get_json()
    if not data:
        abort(400)

    # TODO: change to controller_devices.
    for device in all_devices():
        send_data_to_device(data, device)

    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


# TODO: remove this entirely. A quick hack to get ios client working.
@app.route('/devices/<device>/', methods=['POST'])
def add_device_to_all(device):
    app.logger.info(f'add_device_to_all endpoint. device: {device}')
    all_devices(device)
    return json.dumps({'registered': device}), 200, {'ContentType': 'application/json'}