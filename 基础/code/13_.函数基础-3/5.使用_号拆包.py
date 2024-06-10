# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 5.使用*号拆包.py
# @Software: PyCharm
# @Time    : 2023/11/1 21:52


def set_list_attr(*args):
    print(*args)


nums = [1, 2, 3]
set_list_attr(*nums)


def set_dict_attr(name, gender):
    print(name, gender)


info = {
    'name': '安娜',
    'gender': '女'
}


set_dict_attr(**info)

