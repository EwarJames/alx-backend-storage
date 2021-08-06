#!/usr/bin/env python3
"""Python module using pymongo"""


def top_students(mongo_collection):
    """"Returns all students sorted by average score"""
    return list(mongo_collection.find())
