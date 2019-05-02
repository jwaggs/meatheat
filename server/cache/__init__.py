import os
import redis

redis_url = os.getenv("REDIS_URL")
r = redis.from_url(redis_url, charset="utf-8", decode_responses=True)
