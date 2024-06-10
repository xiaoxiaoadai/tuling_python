# -*- coding: utf-8 -*-
# @Time    : 2023/10/20 下午8:30
# @Author  : 顾安
# @File    : 5.if嵌套.py
# @Software: PyCharm


"""
if 判断条件1:
    满足条件执行的代码...
    if 判断条件2:
        满足条件执行的代码...
    else:
        不满足...
else:
    不满足...
"""

ticket = True
knife_length = 10

if ticket:
    print('已购买车票, 进站安检...')
    if knife_length < 10:
        print('通过安检...')
    else:
        print('超出管制刀具的长度规定...')
else:
    print('未购买车票, 无法安检...')


"""
如何查看代码的执行流程
    断点: 一种代码调试的功能
    
    当完成断点之后启动方式由原来的run改为run debug
    
    
1.如果外层的if条件成立则判断内部的if条件
2.如果内部if条件成立则运行成立代码块否则运行else代码块
3.如果外层的if条件不成立则直接运行外层的else, 不会执行内部的判断语句
"""

