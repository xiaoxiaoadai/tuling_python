# -*- coding: utf-8 -*-
# @Time    : 2023/10/20 下午9:51
# @Author  : 顾安
# @File    : 5.练习题.py
# @Software: PyCharm


"""
*
* *
* * *
* * * *
* * * * *
"""

# i = 1
# while i <= 5:
#     # j参数需要通过外层循环完成重置
#     j = 1
#     while j <= i:
#         print('* ', end='')
#         j += 1
#
#     i += 1
#     print('\n')


# i = 1
# while i <= 5:
#     j = 1
#     while j <= i:
#         print('X*Y=Z ', end='')
#         j += 1
#
#     i += 1
#     print('\n')

# i = 1
# while i <= 5:
#     j = 1
#     while j <= i:
#         print(f'{j} * {i} = Z ', end='')
#         j += 1
#     i += 1
#     print('\n')


i = 1
while i <= 5:
    j = 1
    while j <= i:
        print(f'{j} * {i} = {j * i} ', end='')
        j += 1
    i += 1
    print('\n')
