# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 7.事件循环对象以及创建方式.py
# @Software: PyCharm
# @Time    : 2023/11/27 21:52


import asyncio


async def work_1():
    for _ in range(5):
        print('异步任务1:', _)
        # 模拟耗时堵塞场景
        await asyncio.sleep(1)


async def work_2():
    for _ in range(5):
        print('异步任务2:', _)
        # 模拟耗时堵塞场景
        await asyncio.sleep(1)


"""
1.await关键字可以运行单个的协程任务
2.await关键字必须在协程函数内部使用
"""

"""
方式一
当前操作方式是属于python3.6以下的协程语法
    虽然这种方式属于年代久远的方式, 但是必须要掌握
"""
# 创建一个列表并保存以上两个协程函数的对象
# tasks = [work_1(), work_2()]
# 创建事件循环对象
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))


"""
方式二
    当前操作方式属于python3.7以上版本的协程语法
        也必须要掌握
        
    方式二无需自己手动创建事件循环对象
"""
tasks = [work_1(), work_2()]
asyncio.run(asyncio.wait(tasks))

