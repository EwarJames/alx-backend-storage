#!/usr/bin/env python3
"""Web module"""
import requests


@count_calls
def get_page(url: str) -> str:
    """Gets the page"""
    req = requests.get(url)
    return req.text
