# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 3.使用循环对列表进行遍历.py
# @Software: PyCharm
# @Time    : 2023/10/25 20:09


stu_names = ["张三", "李四", "王五", "赵六", "田七"]

# for name in stu_names:
#     print(name)


# 如果使用while循环遍历则需要获取到当前这个列表的长度
list_length = len(stu_names)
i = 0  # 当前这个i是列表的下标值, 默认为0
while i < list_length:
    print(stu_names[i])
    i += 1

