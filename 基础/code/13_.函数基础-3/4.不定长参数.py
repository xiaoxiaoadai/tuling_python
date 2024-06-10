# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 4.不定长参数.py
# @Software: PyCharm
# @Time    : 2023/11/1 21:09


"""
*args
**kwargs

可以在函数中接收不确定数量的参数

args: 可以接收不确定数量的参数, 并打包成一个元组
kwargs: 可以接收不确定数量的参数, 并打包成一个字典
"""


def func_attr(a, b, *args, **kwargs):
    print(a, type(a))
    print(b, type(b))
    print(args, type(args))
    print(kwargs, type(kwargs))


func_attr(1, 2, 3, 4, 5, name='安娜', gender='女')

"""
在函数调用的过程中如果传递的参数个数超出函数本身的新式参数则多余的参数会被args和kwargs接收
    args: 接收的是普通传参方式的多个值并打包成元组
    kwargs: 接收的是命名参数传递方式的多个值并打包成一个字典
"""

"""
在不定长参数前面的*代表的是元素值
    (1, 2, 3)

如果是**kwargs
    {name: '双双'}
"""

"""
关于不定长参数使用的注意事项
    形式参数 > 缺省参数 > *args > **kwargs
"""


def test_attr(a, *args, b=22, c=33, **kwargs):
    print(a, args, b, c, kwargs)


# 当前传参需求是a=1, b=2, c=3, args=(4,)
test_attr(1, 2, 3, 4, name='aa')


# **kwargs一定是在所有参数的最后
# def test_attr(a, *args, b=22, **kwargs, c=33):
#     print(a, args, b, c, kwargs)


# 需要在调用函数的时候确定每一个参数的具体的值
# 可以确定每一个参数的值
# 语法更严格, 每个参数必须对应一个值, 并且强制性使用命名参数
def set_attr(*, a, b, c):  # 不允许使用不定长参数
    print()


set_attr(a=1, b=2, c=3)

