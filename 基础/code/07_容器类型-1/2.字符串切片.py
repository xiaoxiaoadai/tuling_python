# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 2.字符串切片.py
# @Software: PyCharm
# @Time    : 2023/10/23 21:17

"""
所谓的切片其实就是对一串字符串进行范围截取
    切片代码格式:
        [起始位置:结束位置]
    切片不包含结束位置本身
"""

str_data = 'abcdef'
print(str_data[0:3])  # 当前切片的第二个参数不包含本身
print(str_data[:3])

print(str_data[3:5])

# 忽略结束位置: 如果结束位默认不填, 则取到字符串的最后一位
print(str_data[3:])

# 如果结束位置为-1, 则取到最后一位, 但是不包含最后一位本身
print(str_data[1: -1])

# 引入步长
print(str_data[1:5:2])

# 倒序获取 第二个参数不包含本身
print(str_data[5:1:-1])

# 不填写起始位置以及结束位置, 默认从字符串的起始位置到结束位置
print(str_data[::-1])

