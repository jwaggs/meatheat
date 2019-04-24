import os
import redis
from .app import app

redis_url = os.getenv("REDIS_URL")
r = redis.from_url(redis_url, charset="utf-8", decode_responses=True)


def fid_add_device(fid, device):
    app.logger.info(f'adding device: {device} to fid: {fid}')
    r.sadd(fid, device)
    r.sadd('all_devices', device)


def fid_devices(fid):
    app.logger.info(f'getting devices for fid: {fid}')
    return list(r.smembers(fid))


def all_devices():
    # this is a shortcut to work around the fact that microcontrollers aren't getting paired with users yet.
    app.logger.info(f'getting all devices')
    return list(r.smembers('all_devices'))
