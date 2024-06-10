# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 5.回顾-数据更新.py
# @Software: PyCharm
# @Time    : 2023/12/11 20:56


import pymysql


def update_data():
    db = pymysql.connect(host='localhost', user='root', password='root', db='python_basic')
    cursor = db.cursor()

    sql = """
        update employee set age=age+1 where first_name='双';
    """

    try:
        cursor.execute(sql)
        db.commit()
        print('数据更新成功...')
    except Exception as e:
        print('数据更新失败:', e)
        db.rollback()
    finally:
        cursor.close()
        db.close()


update_data()

