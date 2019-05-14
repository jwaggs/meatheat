from server.app import app
from server.cache import r
from . import Keys


def pair(device, controller: str):
    app.logger.info(f'pair_device_controller in cache for device: {device} controller: {controller}')
    r.sadd(Keys.controller_devices(controller), device)


def controller_devices(controller):
    app.logger.info(f'getting controller devices from cache')
    return r.smembers(Keys.controller_devices(controller))
