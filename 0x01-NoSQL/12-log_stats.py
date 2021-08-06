#!/usr/bin/env python3
"""Python module that provides stats on logs"""
from pymongo import MongoClient


def log_stats():
    """"Provides some stats about Ngnix logs stored in Mongodb"""
    client = MongoClient("https://127.0.0.1:27017")
    logs_list = client.logs.nginx
    all_logs = logs_list.count_documents({})
    get = logs_list.count_documents({"method": "GET"})
    post = logs_list.count_documents("method": "POST")
    delete = logs_list.count_documents("method": "DELETE")
    put = logs_list.count_documents("method": "PUT")
    patch = logs_list.count_documents("method": "PATCH")
    path = logs_list.count_documents({
        "method": "GET", "path": "/status"})
    print(f"{all_logs} logs")
    print("Methods")
    print(f"\tmethod GET: {get}")
    print(f"\tmethod POST: {post}")
    print(f"\tmethod PUT: {put}")
    print(f"\tmethod PATCH: {patch}")
    print(f"\tmethod DELETE: {delete}")
    print(f"{path} status check")

    if __name__ == "__main__":
        log_stats()
