#!/usr/bin/env python3
"""Web module"""
import requests
#import redis
#from typing import Callable
#from functools import wraps


#r = redis.Redis()

def get_page(url: str) -> str:
    """Gets the page"""
    req = requests.get(url)
    return req.text
