#!/usr/bin/env python3
"""Python module that provides stats on logs"""
from pymongo import


client = MongoClient()
stat = client.logs.nginx

all_logs = stat.count_documents({})
get = stat.count_documents({"method": "GET"})
post = stat.count_documents({"method": "POST"})
delete = stat.count_documents({"method": "DELETE"})
put = stat.count_documents({"method": "PUT"})
patch = stat.count_documents({"method": "PATCH"})
path = stat.count_documents({"method": "GET", "path": "/status"})


if __name__ == "__main__":
    print(f"{all_logs} logs")
    print("Methods")
    print(f"\tmethod GET: {get}")
    print(f"\tmethod POST: {post}")
    print(f"\tmethod PUT: {put}")
    print(f"\tmethod PATCH: {patch}")
    print(f"\tmethod DELETE: {delete}")
    print(f"{path} status check")
