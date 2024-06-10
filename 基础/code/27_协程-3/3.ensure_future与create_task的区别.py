# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 3.ensure_future与create_task的区别.py
# @Software: PyCharm
# @Time    : 2023/12/1 20:24


"""
协程中的并发对象有两个
    task
    future

    asyncio.ensure_future方法是在python3.4版本中出现, 比较适合在3.6以下版本中使用
    asyncio.create_task方法在python3.7版本中出现, 比较适合在3.7以上版本中使用

    task对象是future对象的子类, task对象具有future对象中的所有功能
        建议之后统一使用asyncio.create_task完成并发任务!!!

    task对象和future对象可以互转
"""

import asyncio


async def func():
    print(1)
    await asyncio.sleep(1)
    print(2)


loop = asyncio.get_event_loop()
task = loop.create_task(func())

future = asyncio.ensure_future(task)  # 不要用
print(future)



