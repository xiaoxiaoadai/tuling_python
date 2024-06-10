# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : insert_start_url.py
# @Software: PyCharm
# @Time    : 2023/12/12 21:58


import redis

redis_client = redis.Redis(host='192.168.70.82', port=6379)
redis_client.lpush('top250:start_urls', 'https://movie.douban.com/top250?start=0&filter=')
print('插入完成...')
redis_client.close()