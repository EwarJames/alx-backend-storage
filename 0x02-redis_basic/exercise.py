#!/usr/bin/env python3
""""Python Module for redis database"""
import redis
from uuid import uuid4
from typing import Union, Collable, Optional
from sys import byteorder
from functools import wraps


def count_calls(method: Collable) -> Collable:
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

    def get(self, key: str, fn: Optional[Collable] = None)\
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
