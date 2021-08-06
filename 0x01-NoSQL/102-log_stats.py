#!/usr/bin/env python3
"""Python module that provides stats on logs"""
from pymongo import MongoClient


def log_stats():
    """Log stats in mongodb"""
    client = MongoClient('mongodb://127:0.0.1:27017')
    stat = client.logs.nginx
    all_logs = stat.count_documents({})
    get = stat.count_documents({"method": "GET"})
    post = stat.count_documents({"method": "POST"})
    put = stat.count_documents({"method": "PUT"})
    patch = stat.count_documents({"method": "PATCH"})
    delete = stat.count_documents({"method": "DELETE"})
    path = stat.count_documents({"method": "GET", "path": "/status"})
    print(f"{all_logs} logs")
    print("Methods:")
    print(f"\tmethod GET: {get}")
    print(f"\tmethod POST: {post}")
    print(f"\tmethod PUT: {put}")
    print(f"\tmethod PATCH: {patch}")
    print(f"\tmethod DELETE: {delete}")
    print(f"{path} status check")
    print("IPs:")
    sorted_ips = stats.aggregate(
        [{"$group": {"_id": "$ip", "count": {$"sum": 1}}},
         {"$sort": {"count": -1}}])
    i = 0
    for t in sorted_ips:
        if i == 10:
            break
        print(f"\t{t.get('_id')}: {t.get('count')}")
        i += 1


if __name__ == "__main__":
    log_stats()
