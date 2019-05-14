from flask import json
from server.app import app
from server.cache.pairing import pair


@app.route('/pair/device/<device>/controller/<controller>/', methods=['POST'])
# @authenticate
def pair_device_controller(device, controller):
    app.logger.info(f'pair endpoint. device: {device} controller: {controller}')
    pair(device, controller)
    return json.dumps({'registered': controller}), 200, {'ContentType': 'application/json'}
