from server.app import app
from server.cache import r
from . import Keys


def set_thresholds(device, controller, probe, low, high):
    app.logger.info(f'setting controller thresholds in cache to {low} and {high}')
    if low:
        key = Keys.device_probe_low_threshold(device, controller, probe)
        r.set(key, str(low))
    if high:
        key = Keys.device_probe_high_threshold(device, controller, probe)
        r.set(key, str(high))


def get_thresholds(device, controller, probe):
    app.logger.info(f'getting thresholds in cache')
    low, high = 0, 999
    low_key = Keys.device_probe_low_threshold(device, controller, probe)
    high_key = Keys.device_probe_high_threshold(device, controller, probe)
    if r.exists(low_key):
        low = int(r.get(low_key))
    if r.exists(high_key):
        high = int(r.get(high_key))
    app.logger.info(f'retrieved threshold. low: {low} high: {high}')
    return low, high

