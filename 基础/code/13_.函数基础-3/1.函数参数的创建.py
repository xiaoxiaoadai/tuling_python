# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 1.函数参数的创建.py
# @Software: PyCharm
# @Time    : 2023/11/1 20:40

# 形式参数: a和b只是一个没有绑定值的变量, 在使用时需要传递一个具体的值
# 可以理解为一种占位符, python允许当前这种占位符在真正使用之前没有绑定一个具体的值
def test(a, b):
    return a + b


print(test(11, 22))


# 缺省参数
def work(name, work_obj='正在做饭'):  # 如果函数中的参数存在默认值则运行调用时可以不用传递参数
    print(name)
    print(work_obj)


work('安娜', '正在遛狗')

