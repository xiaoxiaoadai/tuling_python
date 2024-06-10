# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 3.字典的常用方式.py
# @Software: PyCharm
# @Time    : 2023/10/27 20:23


stu_info = {
    'name': '安娜',
    'age': 18,
    'gender': '女',
    'address': '长沙'
}


print(stu_info['name'])
# 如果现在获取到的value在字典中不存在，那么就会报错
# print(stu_info['height'])

# 如何避免获取的key不存在而产生报错的情况
print(stu_info.get('height'))  # 如果指定的key不存在, 则get方法默认返回一个
"""
None也是python中的一种数据结构
    代表的是空
    None在全局中只有一份 *
"""
# 如果key不存在则返回一个自定义的信息
"""
get可以传递两个参数
    1.你要获取的值所对应的key
    2.如果key不存在需要设置的返回值 可选*
"""
print(stu_info.get('height', '当前数据不存在...'))


"""
数据修改
"""
stu_info['name'] = '双双'
print(stu_info)

"""
在字典中添加新元素
    通过以下方式添加的新数据在字典的结尾
"""
stu_info['height'] = 170
print(stu_info)


"""
数据删除
"""

# del stu_info  # 看情况使用, 因为当前方法会删除整个对象
# print(stu_info)

del stu_info['height']
print(stu_info)

# clear: 当前方法可以清空字典中的所有数据
stu_info.clear()
print(stu_info)


# 如何定义一个空字典？
# str_dict = {}  # 容易让人误解: 会让别人觉得你定义的是一个空集合
# print(type(str_dict))
str_data = dict()
print(type(str_data))

