"""
driver for sanic-redis
"""
import redis


class RedisDriver:
    def __init__(self):
        self.host = '0.0.0.0'
        self.password = 'Password123'
        self.port = 6379

    def _connect_redis(self):
        return redis.Redis(connection_pool=redis.ConnectionPool(
            host=self.host, password=self.password, port=self.port, db=0))

    def set(self, key, value):
        rd = self._connect_redis()
        rd.set(key, value)

    def get(self, key):
        rd = self._connect_redis()
        return rd.get(key)

    def expire(self, key, second):
        rd = self._connect_redis()
        return rd.expire(key, second)

    def exists(self, key):
        rd = self._connect_redis()
        return rd.exists(key)

    def delete(self, key):
        rd = self._connect_redis()
        return rd.expire(key, 0)

    def rename(self, old_key, new_key):
        rd = self._connect_redis()
        return rd.rename(old_key, new_key)


rd = RedisDriver()
