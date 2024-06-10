# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 2.字典的内置方法.py
# @Software: PyCharm
# @Time    : 2023/10/27 20:12

stu_info = {
    'name': '安娜',
    'age': 18,
    'gender': '女',
    'address': '长沙'
}

# 字典也是可以被遍历的
for item in stu_info:
    # 如果直接对字典进行遍历, 则只能获取到字典中的key
    print(item)

print('-' * 30)

# 使用for循环获取字典中的value
print(stu_info.values())  # 当前values方法返回的数据类型是dict_values类型, 可以使用list进行列表转换
for item in stu_info.values():
    print(item)

print('-' * 30)

# 使用for循环对列表进行遍历, 并使用keys方法获取字典中的key
print(stu_info.keys())  # 当前keys方法返回的数据类型是dict_keys类型, 可以使用list进行列表转换
for item in stu_info.keys():
    print(item)

print('-' * 30)

# 使用for循环获取字典中的key和value
print(stu_info.items())  # 当前items方法返回的数据类型是dict_items类型, 可以使用list进行列表转换
for item in stu_info.items():
    print(item)

# 拆包
for key, value in stu_info.items():
    print(key, value)





