# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 11.关于实例属性创建的三种方式.py
# @Software: PyCharm
# @Time    : 2023/11/3 21:48


"""
1.使用实例对象动态创建
2.使用__init__方法创建实例属性
3.使用实例方法创建实例属性
"""


class Test_1:
    pass


test_1 = Test_1()
test_1.name = '顾安'


class Test_2:
    def __init__(self, name='安娜'):
        # 当前代码将参数的值获取之后由重新赋值给了属性
        self.name = name


test_2 = Test_2()
print(test_2.name)


class Test_3:
    # 使用普通实例方法完成实例属性的创建
    def set_attr(self, value):
        self.name = value


test_3 = Test_3()  # 类的实例化并产生一个对象赋值给了test_3变量
test_3.set_attr('双双')
print(test_3.name)



