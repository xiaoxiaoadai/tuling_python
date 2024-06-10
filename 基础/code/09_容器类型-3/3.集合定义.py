# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 3.集合定义.py
# @Software: PyCharm
# @Time    : 2023/10/25 21:57

# 集合是一种无序的容器类型
# 集合可以用来进行数据去重
int_set = {1, 2, 3, 4, 5, 5, 2, 4}
print(int_set)

# 集合是可以遍历的
for item in int_set:
    print(item)

# 能否使用索引的方式获取集合中的元素: 不能, 因为元素无序, 无法确定元素索引值
# print(int_set[0])


# 声明一个列表
"""
python中可以使用关键字定义容器类型
    str
    list
    dict
    set
    tuple    
"""
int_list = [1, 2, 1, 3, 4, 1, 3, 5, 9, 4, 8, 9, 2]
# 去重
int_set = set(int_list)
# print(int_set)
# 完成去重后排序
int_list = list(int_set)
int_list.sort(reverse=True)
print(int_list)

int_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
int_set = set(int_tuple)
print(tuple(int_set))

"""
列表, 元组, 集合是可以互转的
"""

# 当前有一串字符串, 能否转为一个列表?
# 是可以的
str_data = 'abcdef'
print(list(str_data))


str_data_2 = 'aabbccddeeff'
print(set(str_data_2))


"""
集合运算
    交并差运算
"""




