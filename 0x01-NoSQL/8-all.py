#!usr/bin/env python3
""""Python Module for using pymongo"""


def list_all(mongo_collection):
    """Lists all documents in a collection"""
    d_list = []
    doc = mongo_collection.find()
    for i in doc:
        d_list.append(i)
    return d_list
