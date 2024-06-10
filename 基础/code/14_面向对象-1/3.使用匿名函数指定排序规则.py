# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 3.使用匿名函数指定排序规则.py
# @Software: PyCharm
# @Time    : 2023/11/3 20:19


students = [
    {"name": "顾安", "age": 18},
    {"name": "夏洛", "age": 19},
    {"name": "木木", "age": 17}
]


# print('排序前:', students)
# students.sort(key=lambda x: x['age'])
# print('排序后:', students)


"""
1.sort对以上列表进行遍历
2.sort根据匿名函数所返回的字典的value进行正序排序
"""


# 使用普通方式完成
def sort_by_age(student):
    return student['age']


sorted_data = sorted(students, key=sort_by_age)
print(sorted_data)

