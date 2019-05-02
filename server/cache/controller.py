from server.app import app
from server.cache import r
from server.cache.user import fid_devices


def controller_devices(controller):
    app.logger.info(f'getting controller devices')
    if not r.exists(f'controller:{controller}:fid'):
        return []
    fid = r.get(f'controller:{controller}:fid')
    return fid_devices(fid)


# TODO: Remove once application is finished. This is a shortcut for development purposes only.
def all_controllers(controller: str = None):
    # this is a shortcut to work around the fact that microcontrollers aren't getting paired with users yet.
    if controller:
        r.sadd('all_controllers', controller)
    app.logger.info(f'getting all controllers')
    return list(r.smembers('all_controllers'))
