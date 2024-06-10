# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 7.关于协程并发的代码示例.py
# @Software: PyCharm
# @Time    : 2023/11/29 21:27


import random
import asyncio


async def work():
    print(1)
    await asyncio.sleep(random.randint(1, 3))
    print(2)
    return '123'


# 规范写法: 如果存在多个协程任务则需要单独定义一个协程函数完成task对象的转换
async def main():
    tasks = [asyncio.create_task(work()) for _ in range(3)]
    # done, pending = await asyncio.wait(tasks)
    # print(done)  # 保存已经完成的任务状态
    # print(pending)  # 保存未完成的任务

    # done是一个集合
    # for res in done:
    #     print(res.result())

    results = await asyncio.gather(*tasks)
    print(results)


asyncio.run(main())


"""
如果使用asyncio.wait进行任务调度, 则当前所有任务的返回值存储在done集合中
    需要对done集合进行迭代并使用result()方法获取每个任务的返回值
    pending集合返回的是未完成的任务


asyncio.gather也是可以完成多个任务的并发并获取多个任务的返回值
    1.gather无法获取任务的状态
    2.gather是收集所有任务的返回值, 必须要等待所有任务全部完成之后才能返回所有的结果
    3.gather如果接收的是一个迭代对象那么必须进行一次拆包
"""