# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 6.将同步任务改写为异步任务.py
# @Software: PyCharm
# @Time    : 2023/11/29 20:52


import asyncio


async def others():
    print('开始任务...')
    await asyncio.sleep(10)
    print('任务结束...')
    return 123


async def main():
    print('正在执行main函数中的内部代码...')
    # coro_list = [others(), others()]  3.11不支持将协程对象列表提交给wait方法, 需要手动将协程对象打包成task
    task_list = [asyncio.create_task(others()) for _ in range(2)]
    await asyncio.wait(task_list)
    print('main函数即将结束...')

asyncio.run(main())


"""
await关键字只能调度三种对象:
    1.协程对象
    2.task对象
    3.future对象
以上三个对象有一个统一的名称: 可等待对象


多个协程的任务切换问题
    事件循环存在多个任务的情况下, 如果其中一个任务存在耗时任务(await) 那么事件循环会检索其他任务的状态并进行任务切换
        直到所有任务的状态都是运行态则等待所有任务的返回值
        
        
协程任务规定只要是耗时任务必须使用await
    看当前任务是否是一个协程函数
"""
