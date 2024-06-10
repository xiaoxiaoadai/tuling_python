# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 6.使用python修改redis中保存的数据.py
# @Software: PyCharm
# @Time    : 2023/12/13 20:50


import redis


redis_client = redis.Redis()

redis_client.set('name', '双双')
result = redis_client.get('name')
print(result.decode())
