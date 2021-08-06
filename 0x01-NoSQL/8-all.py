#!/usr/bin/env python3
"""Python Module for using pymong"""
import pymongo


def list_all(mongo_collection):
    """Lists all documents in a collection"""
    doc = mongo_collection.find()
    return [i for i in doc]
