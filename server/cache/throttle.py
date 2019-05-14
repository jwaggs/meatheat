from server.app import app
from server.cache import r
from datetime import datetime, timedelta
from . import Keys


def should_throttle_push(device, controller: str):
    app.logger.info(f'checking if push_throttle_has_expired')
    key = Keys.device_controller_throttle(device, controller)
    if r.exists(key):
        throttle_string = str(r.get(key))
        throttle_date = datetime.strptime(throttle_string, '%m/%d/%Y, %H:%M:%S')
        if datetime.now() < throttle_date:
            return True
    return False


def set_push_throttle(device, controller: str, seconds: int):
    app.logger.info(f'setting push notification throttle for {device} to {seconds} seconds')
    key = Keys.device_controller_throttle(device, controller)
    throttle_date = datetime.now() + timedelta(seconds=seconds)
    throttle_string = throttle_date.strftime('%m/%d/%Y, %H:%M:%S')
    r.set(key, throttle_string)