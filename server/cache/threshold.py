from server.app import app
from server.cache import r
from server.cache.user import fid_devices


def set_threshold(low, high: int):
    app.logger.info(f'setting threshold in cache')
    if low:
        r.set('templow', str(low))
    if high:
        r.set('temphigh', str(high))


def get_thresholds():
    app.logger.info(f'getting threshold in cache')
    low, high = 0, 999
    if r.exists('templow'):
        low = int(r.get('templow'))
    if r.exists('temphigh'):
        high = int(r.get('temphigh'))
    app.logger.info(f'retrieved threshold. low: {low} high: {high}')
    return low, high

