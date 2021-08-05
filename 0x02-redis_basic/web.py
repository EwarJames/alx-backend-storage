#!/usr/bin/env python3
"""Web module"""
import requests
import redis
from typing import Callable
from functools import wraps


r = redis.Redis()


def count_calls(method: Callable) -> Collable:
    """Defines number of calls"""

    @wraps(method)
    def wrapper(url):
        """"wrapper decorator"""
        r.incr(f"count:{url}")
        cached_html = r.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode("utf-8")
        html = method(url)
        r.setex(f"cached:{url}", 10, html)
    return wrapper


def get_page(url: str) -> str:
    """Gets the page"""
    req = requests.get(url)
    return req.text
