# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 9.静态方法.py
# @Software: PyCharm
# @Time    : 2023/11/8 21:38


"""
在类中的方法一般包含三种类型的方法
    1.实例方法
    2.静态方法
    3.类方法

以上三种方法都可以使用实例方法完成
    实例方法可以实现类方法和静态方法的所有功能
"""


class Tool:
    def __init__(self):
        self.num_1 = 0
        self.num_2 = 1

    @staticmethod
    def print_menu():  # 当前方法有没有使用到类的实例属性？
        """
        如果类中的方法没有使用到实例属性或者实例方法的话
            则可以定义成一个静态方法
        :return:
        """
        print('计算工具:')
        print('1.加法')
        print('2.减法')
        print('3.乘法')
        print('4.除法')

    def get_nums(self):
        self.num_1 = int(input("请输入第1个数:"))
        self.num_2 = int(input("请输入第2个数:"))

    def add(self):
        print(self.num_1 + self.num_2)

    def min(self):
        print(self.num_1 - self.num_2)

    def mul(self):
        print(self.num_1 * self.num_2)

    def div(self):
        print(self.num_1 / self.num_2)

    def run(self):
        while True:
            self.print_menu()
            op = input("请输入要进行的操作:")
            if op == "1":
                self.get_nums()
                self.add()
            elif op == "2":
                self.get_nums()
                self.min()
            elif op == "3":
                self.get_nums()
                self.mul()
            elif op == "4":
                self.get_nums()
                self.div()
            elif op == "5":
                break


# tool = Tool()
# tool.run()

Tool.print_menu()  # 静态方法可以省略实例化过程直接通过类对象调用

"""
在类中的静态方法可以不需要实例对象调用, 直接用类对象调用也是可以的
实例方法必须使用实例对象进行调用

静态方法其实就是我们之前所学的函数: 当前这个函数只是和普通函数有作用域的区别
    静态方法需要通过类去调用, 普通函数可以全局调用
    
静态方法的声明方式是通过装饰器实现的
    @staticmethod
"""
