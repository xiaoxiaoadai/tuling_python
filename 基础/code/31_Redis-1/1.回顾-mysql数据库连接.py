# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 1.回顾-mysql数据库连接.py
# @Software: PyCharm
# @Time    : 2023/12/11 20:00

# 1. pip install pymysql

import pymysql


def db_connect():
    # 创建mysql数据库的链接对象
    db = pymysql.connect(host='localhost', user='root', password='root', db='python_basic')

    # 使用链接对象创建游标对象 ----> 主要负责sql代码的执行
    cursor = db.cursor()

    # 使用游标对象执行sql
    sql = 'select version();'
    cursor.execute(sql)  # 会得到一个结果

    # 获取结果并打印 获取一条结果
    result = cursor.fetchone()  # 返回的类型是一个元组
    print(result)


db_connect()


