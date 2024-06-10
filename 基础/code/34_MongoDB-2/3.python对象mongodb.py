# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 3.python对象mongodb.py
# @Software: PyCharm
# @Time    : 2023/12/15 21:41


import pymongo

# 创建链接对象
mongo_client = pymongo.MongoClient()
# 创建集合对象
collection = mongo_client['mongo_data_info']['spider_test']

# 插入一条数据
# dict_data = {
#     'name': '安娜',
#     'gender': '女'
# }
#
# result = collection.insert_one(dict_data)


# 插入多条数据
# dict_data_list = [
#     {'name': '双双', 'gender': '女'},
#     {'name': '夏洛', 'gender': '男'}
# ]
#
# result = collection.insert_many(dict_data_list)

# 如果没有定义条件则返回集合中的第一条数据
# search_data_one = collection.find_one()
# 如果有条件则返回符合条件的出现的第一条数据
# search_data_one = collection.find_one({'name': '双双'})
# print(search_data_one)

# search_data_many = collection.find()
# print(search_data_many)  # 如果查询的多条数据则返回的是游标对象, 返回的游标对象是一种迭代对象
# for temp in search_data_many:
#     print(temp)

# print(list(search_data_many))


# 更新一条数据
# collection.insert_one({'name': '双双', 'age': 20})
# collection.insert_one({'name': '双双', 'age': 18})
# collection.update_one({'name': '双双'}, {'$set': {'name': '木木'}})
# collection.update_many({'name': '双双'}, {'$set': {'gender': '女'}})

# 删除数据
# collection.insert_one({'name': '双双', 'gender': '女', 'age': 22})
# collection.delete_one({'name': '双双'})
# collection.delete_many({'name': '双双'})