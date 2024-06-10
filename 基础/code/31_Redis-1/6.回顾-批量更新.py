# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 6.回顾-批量更新.py
# @Software: PyCharm
# @Time    : 2023/12/11 21:02

import pymysql
import datetime


def insert_many_data():
    with pymysql.connect(host='localhost', user='root', password='root', db='python_basic') as db:
        with db.cursor() as cursor:
            sql = """
                insert into employee values (%s, %s, %s, %s, %s, %s);
            """

            try:
                cursor.executemany(sql, [
                    ('木', '木', 16, '女', 17000, datetime.datetime.now()),
                    ('夏', '洛', 22, '男', 27000, datetime.datetime.now())
                ])
                db.commit()
                print('数据批量插入成功...')
            except Exception as e:
                print('数据批量插入失败:', e)
                db.rollback()


insert_many_data()
