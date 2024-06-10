# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : get_redis_info.py
# @Software: PyCharm
# @Time    : 2023/12/14 20:57

import json
import redis


redis_client = redis.Redis(host='192.168.70.82', port=6379, db=0)

for temp in redis_client.lrange('book:items', 0, -1):
    print(json.loads(temp))

redis_client.close()