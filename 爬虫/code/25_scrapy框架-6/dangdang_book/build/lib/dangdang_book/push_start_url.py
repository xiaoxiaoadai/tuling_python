# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : push_start_url.py
# @Software: PyCharm
# @Time    : 2023/12/14 20:42


import redis

redis_client = redis.Redis(host='192.168.70.82', port=6379, db=0)
redis_client.lpush('dd_book:start_url', 'http://search.dangdang.com/?key=python&act=input&page_index=1')
redis_client.close()