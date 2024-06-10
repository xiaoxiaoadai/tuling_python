# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 6.断言.py
# @Software: PyCharm
# @Time    : 2023/11/17 20:17


import requests

response = requests.get('https://www.baidu.com')

assert response.status_code != 200, StopIteration