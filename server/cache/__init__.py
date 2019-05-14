import os
import redis

redis_url = os.getenv("REDIS_URL")
r = redis.from_url(redis_url, charset="utf-8", decode_responses=True)


class Keys:
    @staticmethod
    def controller_devices(controller: str):
        return f'controller:devices:{controller}'

    @staticmethod
    def device_controller_throttle(device, controller: str):
        return f'throttle:{device}:{controller}'

    @staticmethod
    def device_probe_low_threshold(device, controller, probe):
        return f'threshold:low:{device}:{controller}:{probe}'

    @staticmethod
    def device_probe_high_threshold(device, controller, probe):
        return f'threshold:high:{device}:{controller}:{probe}'
