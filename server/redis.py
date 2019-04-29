import os
import redis
from .app import app

redis_url = os.getenv("REDIS_URL")
r = redis.from_url(redis_url, charset="utf-8", decode_responses=True)


def fid_add_device(fid, device):
    app.logger.info(f'adding device: {device} to fid: {fid}')
    r.sadd(f'fid:{fid}:devices', device)
    r.set(f'device:{device}:fid', fid)


def fid_add_controller(fid, controller):
    app.logger.info(f'adding controller: {controller} to fid: {fid}')
    r.sadd(f'fid:{fid}:controllers', controller)
    r.set(f'controller:{controller}:fid', fid)


def fid_devices(fid):
    app.logger.info(f'getting devices for fid: {fid}')
    return list(r.smembers(f'fid:{fid}:devices'))


def fid_controllers(fid):
    app.logger.info(f'getting controllers for fid: {fid}')
    return list(r.smembers(f'fid:{fid}:controllers'))


def controller_devices(controller):
    app.logger.info(f'getting controller devices')
    if not r.exists(f'controller:{controller}:fid'):
        return []
    fid = r.get(f'controller:{controller}:fid')
    return fid_devices(fid)


def device_controllers(device):
    app.logger.info(f'getting device controllers')
    if not r.exists(f'device:{device}:fid'):
        return []
    fid = r.get(f'device:{device}:fid')
    return fid_controllers(fid)


# TODO: remove this once above functionality is implemented.
def all_devices(device: str = None):
    # this is a shortcut to work around the fact that microcontrollers aren't getting paired with users yet.
    if device:
        r.sadd('all_devices', device)
    app.logger.info(f'getting all devices')
    return list(r.smembers('all_devices'))


# TODO: remove this once above functionality is implemented.
def all_controllers(controller: str = None):
    # this is a shortcut to work around the fact that microcontrollers aren't getting paired with users yet.
    if controller:
        r.sadd('all_controllers', controller)
    app.logger.info(f'getting all controllers')
    return list(r.smembers('all_controllers'))
