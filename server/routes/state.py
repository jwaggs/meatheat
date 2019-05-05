from flask import request, abort, json
from server.app import app
from server.cache.device import all_devices
from server.messaging import send_data_to_device, send_push_to_device
from server.cache.threshold import get_thresholds

@app.route('/controllers/<controller>/state/', methods=['POST', 'GET'])  # TODO: remove GET from methods
def meat_heat(controller):
    app.logger.info(f'meat_heat endpoint hit for controller: {controller}')
    data = request.get_json()
    if not data:
        abort(400)

    for key, value in data.items():
        app.logger.info(f'{key}: {value}')

    # TODO: change to controller_devices.
    for device in all_devices():
        send_data_to_device(data, device)
        try:
            temp = data['temp']
            low, high = get_thresholds()
            if temp < low or temp > high:
                app.logger.info(f'temp {temp} outside of threshold {low} - {high}!')
                send_push_to_device(device, temp, low, high)
        except:
            app.logger.error('caught exception handling thresholds.')

    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
