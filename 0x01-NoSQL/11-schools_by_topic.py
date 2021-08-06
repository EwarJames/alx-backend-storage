#!/usr/bin/env python3
"""Module to list specific topics"""


def schools_by_topic(mongo_collection, topic):
    """Returns lists of schools with specific topics"""
    return mongo_collection.find({"topics": topic})
