# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 4.在爬虫代码中使用mongodb进行数据保存.py
# @Software: PyCharm
# @Time    : 2023/12/15 22:05


import requests
import pymongo


url = 'http://www.cninfo.com.cn/new/disclosure'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

from_data = {
    "column": "szse_latest",
    "pageNum": "1",
    "pageSize": "30",
    "sortName": "",
    "sortType": "",
    "clusterFlag": "true"
}

response = requests.post(url, headers=headers, data=from_data).json()['classifiedAnnouncements']
# print(response[0])

mongo_client = pymongo.MongoClient()
collection = mongo_client['py_spider']['jc_info']
for temp in response:
    jc_info_dict = dict()
    jc_info_dict['secCode'] = temp[0]['secCode']
    jc_info_dict['secName'] = temp[0]['secName']
    collection.insert_one(jc_info_dict)




