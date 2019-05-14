from flask import request, abort, json
from server.app import app
from server.cache.pairing import controller_devices
from server.messaging import send
from server.cache.threshold import get_thresholds


@app.route('/controllers/<controller>/state/', methods=['POST'])
def meat_heat(controller):
    app.logger.info(f'meat_heat endpoint hit for controller: {controller}')
    data = request.get_json()
    if not data:
        abort(400)

    for device in controller_devices(controller):
        for probe_data in data:
            try:
                probe, temp = probe_data['probe'], probe_data['temp']
                low, high = get_thresholds(device, controller, probe)
                push_temp = None
                if temp < low or temp > high:
                    app.logger.info(f'probe {probe} temp {temp}° outside of threshold {low}° - {high}°!')
                    push_temp = temp
                send(probe_data, device, controller, push_temp)
            except Exception as e:
                app.logger.error(f'caught exception handling thresholds. {e}')

    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
