from flask import request, abort, json
from server.app import app
from server.cache.device import all_devices
from server.messaging import send_data_to_device


@app.route('/controllers/<controller>/state/', methods=['POST', 'GET'])  # TODO: remove GET from methods
def meat_heat(controller):
    app.logger.info(f'meat_heat endpoint hit for controller: {controller}')
    data = request.get_json()
    if not data:
        abort(400)

    app.logger.info(f'temp: {data["probe_temp"]} internal {data["probe_internal"]}')
    # TODO: change to controller_devices.
    for device in all_devices():
        send_data_to_device(data, device)

    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}