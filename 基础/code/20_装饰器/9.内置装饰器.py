# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 9.内置装饰器.py
# @Software: PyCharm
# @Time    : 2023/11/15 21:57


"""
@property
可以将类中的函数作为一个属性去使用
"""


class Foo:
    def func(self):
        pass

    @property
    def prop(self):
        return 1


foo = Foo()
foo.func()

value = foo.prop
print(value)


"""
1.@property装饰器在装饰实例方法时, 当前这个实例方法只能有一个参数: self
2.在调用函数时无需加括号
"""
