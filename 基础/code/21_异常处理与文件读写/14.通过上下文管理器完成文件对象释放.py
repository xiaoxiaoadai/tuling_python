# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 14.通过上下文管理器完成文件对象释放.py
# @Software: PyCharm
# @Time    : 2023/11/17 21:17


file_name = '测试文件.txt'

# with关键字的作用是: 开启一个上下文管理器
# 当开启一个上下文管理器的时候, open函数返回的文件对象通过as f进行接收
with open(file_name, 'r') as f:
    result = f.read()
    print(result)
    # 不需要自己手动关闭文件对象的
    # f.close()

"""
什么是上下文管理器, 实现原理是什么？
    在一段代码作用域中完成代码逻辑
"""


class MyFileOpen:
    def __init__(self):  # 当类被实例化时自动触发__init__方法
        self.file_obj = None

    def __enter__(self):  # 当开启了一个上下文管理时自动触发__enter__方法
        print(1)

    def __exit__(self, exc_type, exc_val, exc_tb):  # 如果执行到管理器最后一段代码时即将退出则触发__exit__方法
        print(2)


with MyFileOpen() as f:
    pass
