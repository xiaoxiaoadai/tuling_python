# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 4.回顾-数据查询.py
# @Software: PyCharm
# @Time    : 2023/12/11 20:41

import pymysql


def select_data():
    with pymysql.connect(host='127.0.0.1', user='root', password='root', db='python_basic') as db:
        with db.cursor() as cursor:
            sql = """
                select * from employee;
            """

            try:
                cursor.execute(sql)
                result_1 = cursor.fetchone()
                # print(result_1)  # 返回的类型是一个元组, 一个元组是一条数据

                # result_2 = cursor.fetchall()  # 返回的是一个大元组, 大元组中的元组元素是一条数据
                # print(result_2[0])

                # result_3 = cursor.fetchmany(2)
                # print(result_3)

                info = dict()
                info['first_name'] = result_1[0]
                info['last_name'] = result_1[1]
                info['age'] = result_1[2]
                info['gender'] = result_1[3]
                info['income'] = result_1[4]
                info['create_time'] = result_1[5]
                print(info)
            except Exception as e:
                print('查询失败:', e)


select_data()
