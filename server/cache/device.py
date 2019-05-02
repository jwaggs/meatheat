from server.app import app
from server.cache.user import fid_controllers
from server.cache import r


def device_controllers(device):
    app.logger.info(f'getting device controllers')
    if not r.exists(f'device:{device}:fid'):
        return []
    fid = r.get(f'device:{device}:fid')
    return fid_controllers(fid)


# TODO: Remove once application is finished. This is a shortcut for development purposes only.
def all_devices(device: str = None):
    # this is a shortcut to work around the fact that microcontrollers aren't getting paired with users yet.
    if device:
        r.sadd('all_devices', device)
    app.logger.info(f'getting all devices')
    return list(r.smembers('all_devices'))
