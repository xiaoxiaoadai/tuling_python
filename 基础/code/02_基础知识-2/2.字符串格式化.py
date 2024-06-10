# -*- coding: utf-8 -*-
# @Time    : 2023/10/18 下午8:11
# @Author  : 顾安
# @File    : 2.字符串格式化.py
# @Software: PyCharm


"""
格式化
    根据一定的格式进行字符串的输出
"""

"""
通过一行print可以打印任意年龄
"""
print('我今年10岁')
print('我今年11岁')
print('我今年12岁')

age = 20
# %d是字符串占位符的一种，专门负责占位整型类型数据的
print('我今年%d岁' % age)

"""
常用的占位符号有三个
    %s: 用于字符串占位
    %d: 用户整型占位
    %f: 用于浮点占位
"""

name = '顾安'
print('我的名字是: %s' % name)

float_data = 3.1455926
print('圆周率的值为: %f' % float_data)  # 默认保留6位小数
print('圆周率的值为: %.2f' % float_data)  # %f具有四舍五入的特性

print('我的名字是: %s, 年龄是: %d' % (name, age))

# 通过字符串format内置方法完成字符串格式化
name_1 = '安娜'
age_1 = 18
print('我的名字是: {}, 年龄为: {}'.format(name_1, age_1))

# F表达式: python3.6推出的全新的格式化语法
stu_name = '夏洛'
stu_age = 20
stu_address = '长沙'
stu_money = 30.561111
print(f'学生姓名:{stu_name} 学生年龄:{stu_age} 学生住址:{stu_address} 学生金额余额: {stu_money}')

