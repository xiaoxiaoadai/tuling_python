# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 6.队列的使用.py
# @Software: PyCharm
# @Time    : 2023/11/24 21:17


from queue import Queue

# 1.创建队列对象
queue_1 = Queue()

# 2.上传
queue_1.put(1)

# 3.获取
print('队列1:', queue_1.get())  # 在队列中取一个值少一个值, 直到取完为止

# 4.如果队列中没有值, 则get会发生堵塞, 直到队列中重新添加值为止
# queue.get_nowait()  # 如果队列中没有值并且不想等待队列重新添加值则使用get_nowait方法

# 4.如何判断队列是否为空
print(queue_1.empty())

# 5.设置队列最大保存长度
queue_2 = Queue(3)
queue_2.put(1)
queue_2.put(2)
queue_2.put(3)
queue_2.put_nowait(4)

# 6.判断队列中的元素是否满足最大长度
print(queue_2.full())
print('队列2:', queue_2.get())
print(queue_2.full())

"""
1.上传值: put
2.获取值: get [如果队列为空则一直等待, 会造成线程/进程阻塞]
3.判断队列是否为空: empty
4.判断队列元素个数是否满足队列最大长度: full

5.如果队列已满上传不等待直接抛出异常: put_nowait
6.如果队列为空取值不等待直接抛出异常: get_nowait
"""

