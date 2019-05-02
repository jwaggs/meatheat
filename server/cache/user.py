from server.app import app
from server.cache import r


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
