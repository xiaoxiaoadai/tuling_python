# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 7.使用python删除redis中保存的数据.py
# @Software: PyCharm
# @Time    : 2023/12/13 20:52


import redis


redis_client = redis.Redis()
result = redis_client.delete('name')
print(result)
