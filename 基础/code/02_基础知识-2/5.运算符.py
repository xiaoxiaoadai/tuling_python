# -*- coding: utf-8 -*-
# @Time    : 2023/10/18 下午8:55
# @Author  : 顾安
# @File    : 5.运算符.py
# @Software: PyCharm


"""
算术运算符:
    + - * / %(%是取余的意思) //(地板除)
赋值运算符:
    =
比较运算符:
    > < >= <= != ==
关系运算符:
    and or not
成员运算符:
    in
"""

print(1 + 1)
print(2 - 1)
print(3 * 3)
print(9 / 3)  # 除法得出的结果的类型是一个浮点
print(9 % 2)  # 获取的是余数
print(9 // 2)  # 保留整数部分
print(2 ** 3)  # 平方

"""
在计算的时候需要注意: 执行顺序
    ** > * / % // > + -
    
    如果想要提升运算符的优先级则在表达式中加()
"""

"""
赋值
    获取等号右边的值，将获取到的值赋值给等号左边的变量
"""
age = 18

# 多个参数赋值 拆包
"""
多个参数的个数必须和多个变量的个数一致
"""
num_1, num_2, pi, str_data = 1, 2, 3.14, '你好'
print(num_1, num_2, pi, str_data)

# 复合赋值运算符
int_data = 2
int_data += 3  # 变形: int_data = int_data + 3
print(int_data)

int_data -= 2  # 变形: int_data = int_data - 2
print(int_data)

"""
套路：
    等号左边的变量不动, 将变量移动到等号右边的开始位置
"""
