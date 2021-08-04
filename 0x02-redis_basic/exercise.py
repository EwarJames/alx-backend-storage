#!/usr/bin/env python3
""""Python Module for redis database"""
import redis
from uuid import uuid4
from typing import Union, Callable, Optional
from sys import byteorder
from functools import wraps


def replay(method: Callable):
    """Does the replay"""
    key = method.__qualname__
    i = "".join([key,":inputs"])
    o = "".join([key, ":outputs"])
    count = method.__self__.get(key)
    i_list = method.__self__._redis.lrange(i, 0, -1)
    o_list = method.__self__._redis.lrange(o, 0, -1)
    queue = list(zip(i_list, o_list))
    print(f"{key} was called {decode_utf8(count)} times:"
    for k, v in queue:
          k = decode_utf8(k)
          v = decode_utf8(v)
          print(f"{key}({*k})-> {v}")

def count_calls(method: Callable) -> Collable:
    """Counts number of calls to a class method"""
    key = method.__qualname__

@wraps(method)
def wrapper(self, *args, **kwargs):
    """wraps method"""
    self._redis.incr(key)
    return method(self, *args, **kwargs)
return wrapper


class Cache:
    """"Operate a caching system"""
    def __init__(self):
        """Instance of the redis database"""
        self._redis = redis.Redis()
        self._redis.flushdb

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Creates which is stored with data"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None)\
            -> Union[str, bytes, int, float]:
        """"Return data converted to desired format"""
        data = self._redis.get(key)
        if fn:
            data = fn(data)
        return data

    def get_str(self, data: bytes) -> str:
        """Converts bytes to string"""

        return data.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        """"Converts bytes to int"""
        return int.from_bytes(data, byteorder)
