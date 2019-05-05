from flask import request, abort, json
from server.app import app
from server.cache.threshold import set_threshold


# TODO: set threshold on a controller basis. Global just for short term testing.
@app.route('/threshold/', methods=['POST'])
def threshold():
    app.logger.info(f'threshold endpoint hit.')
    data = request.get_json()
    if not data:
        abort(400)

    low, high = None, None
    if 'low' in data:
        low = data['low']
    if 'high' in data:
        high = data['high']

    set_threshold(low, high)

    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
