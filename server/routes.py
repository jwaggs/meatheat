from .app import app
from flask import request, json, g


@app.route('/health_check', methods=['GET'])
def health_check():
    app.logger.info('health check')
    return json.dumps({'healthy': True}), 200, {'ContentType': 'application/json'}
