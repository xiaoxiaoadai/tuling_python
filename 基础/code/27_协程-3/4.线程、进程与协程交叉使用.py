# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 4.线程、进程与协程交叉使用.py
# @Software: PyCharm
# @Time    : 2023/12/1 20:35

import asyncio
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def work():
    print(1)
    time.sleep(2)
    return '这是一个返回值'


async def main():
    loop = asyncio.get_running_loop()  # 获取一个正在运行的
    with ProcessPoolExecutor(max_workers=2) as pool:
        # run_in_executor方法会默认创建线程池, 可以指定池的类型
        # run_in_executor可以传递两个参数
        # 1.池对象
        # 2.任务
        result = await loop.run_in_executor(pool, work)
    print(result)


# 可以将当前普通任务放入到一个特殊的线程池中调度运行

if __name__ == '__main__':
    loop = asyncio.get_event_loop()  # 创建一个事件循环对象
    loop.run_until_complete(main())

