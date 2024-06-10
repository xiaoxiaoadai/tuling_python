# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 8.绑定回调.py
# @Software: PyCharm
# @Time    : 2023/12/1 21:19


import asyncio


async def work(content):
    print('信息内容:', content)
    return f'返回值为: {content}'


# 将协程函数转为一个协程对象
coro_obj = work('双双胖三斤...')

# 手动创建一个事件循环
loop = asyncio.get_event_loop()
task = loop.create_task(coro_obj)


# 创建一个回调函数, 当任务执行完成后自动调用该函数
def callback(task_obj):
    print('回调函数打印的返回值为:', task_obj.result())


# 将回调函数添加到task对象中
task.add_done_callback(callback)

loop.run_until_complete(task)


"""
1.回调函数的作用是当一个任务完成之后会自动触发回调函数任务
2.回调函数是一个普通函数
3.需要使用task对象或者future对象内部的add_done_callback方法将回调函数引用进行传递
"""