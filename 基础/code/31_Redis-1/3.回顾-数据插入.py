# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 3.回顾-数据插入.py
# @Software: PyCharm
# @Time    : 2023/12/11 20:24


import pymysql
import datetime


def insert_data():
    # pymysql使用完毕之后需要释放连接对象
    with pymysql.connect(host='localhost', user='root', password='root', db='python_basic') as db:
        with db.cursor() as cursor:
            sql = """
                insert into employee (first_name, last_name, age, gender, income, create_time) values (
                    %s, %s, %s, %s, %s, %s
                );
            """

            try:
                # cursor.execute(sql, ('安', '娜', 18, '女', 18000, datetime.datetime.now()))
                cursor.execute(sql, ('双', '双', 20, '女', 32000, datetime.datetime.now()))
                # 增删改操作必须要通过链接对象进行事务提交
                db.commit()
                print('数据插入成功...')
            except Exception as e:
                print('数据插入失败:', e)
                # 如果数据插入异常需要通过链接对象进行数据回滚
                db.rollback()


insert_data()
