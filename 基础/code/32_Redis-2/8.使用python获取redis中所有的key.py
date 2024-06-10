# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 8.使用python获取redis中所有的key.py
# @Software: PyCharm
# @Time    : 2023/12/13 20:54


from redis import Redis


redis_client = Redis()
result = redis_client.keys()
print(result)  # 返回的是一个列表类型
