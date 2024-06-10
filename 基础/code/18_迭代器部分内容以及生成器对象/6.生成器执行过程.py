# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 6.生成器执行过程.py
# @Software: PyCharm
# @Time    : 2023/11/13 21:18


def my_range(number):
    print('开始迭代...')
    i = 0
    while i < number:
        print('迭代中...')
        yield i  # 在第一次取值的时候 while循环执行到yield关键字的地方的时候 -- 暂停

        print('迭代结束...')
        i += 1


my_ = my_range(3)
print(next(my_))  # next() 方法是python帮我们封装好的一种接口
print(next(my_))

my_.__next__()


"""
yield生成器机制:
    惰性加载: python解释器遇到yield会暂停代码, 当第二次执行时, 会从之前暂停的地方继续向下执行
    
    为了节约内存
    
上面的函数能不能用return?
    因为return会结束函数的执行
"""