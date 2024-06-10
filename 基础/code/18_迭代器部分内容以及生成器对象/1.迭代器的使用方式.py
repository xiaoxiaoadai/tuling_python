# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 1.迭代器的使用方式.py
# @Software: PyCharm
# @Time    : 2023/11/13 20:06


nums = [1, 2, 3, 4, 5]

iter_obj = iter(nums)
print(iter_obj.__next__())
print(iter_obj.__next__())
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))

print(next(iter_obj))  # 元素下标越界
"""
后面会学习到异常处理
    异常是可以避免程序直接崩溃的
    
    
总结
    列表 字典 集合等一些容器类型是一种迭代对象

如果想要对当前这些迭代对象进行迭代取值, 需要将迭代对象转为一个迭代器
    iter()就可以将一个迭代对象转为一个迭代器

    迭代器底层包含了一个__next__方法, 这个方法运行一次取出一个值
        从左到右，迭代器不能回头取到前面一个值
"""




