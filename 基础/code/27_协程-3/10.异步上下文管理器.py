# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 10.异步上下文管理器.py
# @Software: PyCharm
# @Time    : 2023/12/1 21:39


import asyncio


class AsyncContextManager:
    def __init__(self, conn=None):
        print(1)
        self.conn = conn

    async def do_something(self):
        print(3)
        return '模拟数据库异步增删改查操作...'

    async def __aenter__(self):
        print(2)
        self.conn = await asyncio.sleep(1, result='db_obj')  # 模拟数据库连接耗时
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print(4)
        """
        在上下文管理器中运行到最后一段代码会自动执行当前方法
        """

        # 异步关闭数据库连接
        await asyncio.sleep(1)


async def main():
    async with AsyncContextManager() as fp:
        result = await fp.do_something()
        print(result)


asyncio.run(main())