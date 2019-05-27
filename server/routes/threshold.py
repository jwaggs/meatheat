from flask import request, abort, json
from server.app import app
from server.cache.threshold import set_thresholds
from server.cache.throttle import set_push_throttle


@app.route('/threshold/', methods=['POST'])
def threshold():
    app.logger.info(f'threshold endpoint hit.')
    data = request.get_json()
    if not data:
        abort(400)

    controller = data['controller']
    probe = data['probe']
    device = data['device']

    low, high = None, None
    if 'low' in data:
        low = data['low']
    if 'high' in data:
        high = data['high']

    # set low and high thresholds in redis cache
    set_thresholds(device, controller, probe, low, high)
    # give 30 seconds before notifying of being outside of new thresholds
    set_push_throttle(device, controller, 30)

    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
