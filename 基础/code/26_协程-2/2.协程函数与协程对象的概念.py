# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 2.协程函数与协程对象的概念.py
# @Software: PyCharm
# @Time    : 2023/11/29 20:17

import asyncio


# 协程函数
async def func(content):
    print(content)
    await asyncio.sleep(1)  # 模拟IO操作: 耗时任务
    print('任务完成...')
    return content

# coro_obj变量接收的是一个协程对象
coro_obj = func('今天天气不错...')
# print(coro_obj)


# 一个协程对象可以被事件循环调度执行
loop = asyncio.get_event_loop()
res = loop.run_until_complete(coro_obj)
print('返回值:', res)


"""
1.协程对象不能直接运行, 需要使用事件循环对象将任务提交给事件循环并调度执行
2.如果当前协程对象任务不止一个, 那么事件循环对象本身无法接收多个任务: asyncio.wait()
"""