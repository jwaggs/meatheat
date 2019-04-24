import os
import redis
from .app import app

r = redis.from_url(os.environ.get("REDIS_URL"))


def fid_add_devices(fid, device):
    app.logger.info(f'adding device: {device} to fid: {fid}')
    res = r.sadd(device, fid)
    app.logger.info(f'added device: {device} to fid: {fid} with result {res}')


def fid_devices(fid):
    app.logger.info(f'getting devices for fid: {fid}')
    devices = r.smembers(fid)
    app.logger.info(f'fid: {fid} devices: {devices}')
