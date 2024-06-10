# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 5.使用python获取redis保存的字符串.py
# @Software: PyCharm
# @Time    : 2023/12/13 20:49


import redis


redis_client = redis.Redis()
result = redis_client.get('name')
print(result.decode())