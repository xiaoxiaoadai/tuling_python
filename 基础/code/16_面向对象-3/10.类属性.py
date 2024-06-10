# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 10.类属性.py
# @Software: PyCharm
# @Time    : 2023/11/8 21:55


"""
类属性相当于在类中定义的变量, 声明方式:
    class Test:
        name = 'ABC'  # 类属性
"""


class Tool:
    tools_num = 0

    def __init__(self, name):
        self.name = name
        print(id(self))
        Tool.tools_num += 1  # 重新生成了一个新的实例属性: tools_num

    @classmethod  # 类方法
    def print_info(cls):  # 类属性
        print(id(cls))
        print(id(Tool))
        print('工具的总数为: ', cls.tools_num)  # 不是创建, 查询是否有tools_num变量


电钻 = Tool('电钻')
铁锹 = Tool('铁锹')
锄头 = Tool('锄头')
锄头.print_info()


"""
类属性和实例属性的区别
    类属性是一种全局属性, 保存的地址为类对象的地址
        当前类属性只有一个, 无论多少个实例对象去访问类属性, 访问的都是同一个
        
    
    实例属性是一种局部属性, 保存的地址为实例对象的地址
        每一个实例对象中都有属于自己的实例属性
        
类属性的访问权限:
    实例对象和类对象都可以访问并操作
"""



