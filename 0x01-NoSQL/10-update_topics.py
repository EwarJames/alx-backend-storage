#!/usr/bin/env python3
"""Module that Changes all topics in a document"""


def update_topics(mongo_collection, name, topics):
    """Üpdates all topics based on name"""
    val = {"name": name}
    new_val = {"$set": {"topics": topics}}
    mongo_collection.update_many(val, new_val)
