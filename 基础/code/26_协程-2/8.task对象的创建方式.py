# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 8.task对象的创建方式.py
# @Software: PyCharm
# @Time    : 2023/11/29 21:44


import asyncio
import threading


async def func():
    print('任务启动...')
    await asyncio.sleep(1)
    print('任务结束...')
    return 123


# futures = [asyncio.ensure_future(func()) for _ in range(3)]
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(futures))

# 推荐大家使用以下方式运行
async def main():
    tasks = [asyncio.create_task(func()) for _ in range(3)]
    future = [asyncio.ensure_future(func()) for _ in range(3)]
    await asyncio.gather(*future)
    for obj in future:
        print(obj.done())

asyncio.run(main())


"""
1.create_task方法必须在一个协程函数内部使用
2.如果想要在一个协程函数的外部创建任务列表, 则需要使用3.6版本语法
"""


"""
在写异步代码之前首先去写中文步骤注释
"""

