# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 3.字符串方法.py
# @Software: PyCharm
# @Time    : 2023/10/23 21:42


# replace: 替换
# replace方法是没有返回值的
str_data = 'welcome to www.tulingxueyuan.com'
print(str_data.replace('w', 'W', 1))

# split: 字符串分割
print(str_data.split(" ", 1))


# strip: 删除字符串两端空格
str_data_ = '   welcome to www.tulingxueyuan.com   '
print(str_data_.strip())

# join: 字符串拼接
# 对列表中的元素进行了遍历, 遍历出一个元素在这个元素的后面添加一个-
str_format = '-'
str_list = ['welcome', 'to', 'www.tulingxueyuan.com']
print(str_format.join(str_list))



