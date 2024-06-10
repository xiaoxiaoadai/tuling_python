# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 4.使用python创建redis测试数据.py
# @Software: PyCharm
# @Time    : 2023/12/13 20:42


"""
需要使用python链接redis并在redis中生成测试数据
1. 需要下载链接redis的python驱动: redis
    pip install redis
2. 导包
    from redis import Redis
"""

from redis import Redis


if __name__ == '__main__':
    redis_client = Redis()
    result = redis_client.set('name', '安娜')
    print(result)


