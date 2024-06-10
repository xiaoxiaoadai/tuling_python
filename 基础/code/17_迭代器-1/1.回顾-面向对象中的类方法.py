# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 1.回顾-面向对象中的类方法.py
# @Software: PyCharm
# @Time    : 2023/11/10 20:01


class Tool1:
    tools_num = 0

    def __init__(self, name):
        self.name = name
        # print(id(self))
        # Tool.tools_num += 1  # 重新生成了一个新的实例属性: tools_num

    def print_info(self):  # 通过实例方法中self参数是可以访问一个类属性的
        print(id(self))
        # print(id(Tool))
        print('工具的总数为: ', self.tools_num)  # 不是创建, 查询是否有tools_num变量

    # 定义一个类方法
    @classmethod
    def cls_print_info(cls):
        print('工具的总数为: ', cls.tools_num)

    # @staticmethod
    # def static_print_info():
    #     print('工具的总数为: ', Tool.tools_num)


# 电钻 = Tool('电钻')
# 铁锹 = Tool('铁锹')
# 锄头 = Tool('锄头')
# 锄头.print_info()

# 实例对象是可以直接调用类方法的
# 锄头.cls_print_info()

# 通过类对象调用类方法
Tool1.cls_print_info()


"""
类方法中的cls参数一个是任意一个类的名字
    cls不会受到修改类名的影响, 如果类名修改也可以通过cls找到修改后的类对象地址
"""