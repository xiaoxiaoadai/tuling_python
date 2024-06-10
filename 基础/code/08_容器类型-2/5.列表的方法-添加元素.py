# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 5.列表的方法-添加元素.py
# @Software: PyCharm
# @Time    : 2023/10/25 20:20

"""
列表的元素添加方法
"""
old_names = ["张三", "李四", "王五", "赵六", "田七"]
new_names_1 = ['夏洛', '木木']
# 元素增加: append[当前方法可以添加一个元素, 并且这个元素一定是在这个列表的末端, 当前方法只能一次添加一个元素]
# 如果append添加的是一个列表对象, 则当前会把这个列表对象作为一个元素整体添加进去
old_names.append(new_names_1)
print(old_names)

# extend: 元素添加方法
# extend可以一次添加多个元素
# 添加的元素位置和append一样, 都是放在原本的列表的末尾
new_names_2 = ['百川', 'monkey']
new_names_3 = (1, 2, 3, 4)
old_names.extend(new_names_2)
old_names.extend(new_names_3)
print(old_names)

# insert: 将某一个元素插入到列表的指定位置
'''
insert方法需要两个参数
    参数1:要插入的列表索引位置
    参数2:要插入的元素本身    
'''
old_names.insert(0, '伯乐')
print(old_names)

# 如果多个列表相加则会合并成一个新列表
list_a = [1, 2]
list_b = [3, 4]
print(list_a + list_b)
print(list_a)
print(list_b)
