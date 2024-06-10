# -*- coding: utf-8 -*-
# @Author  : 顾安
# @File    : 2.回顾-数据表的创建.py
# @Software: PyCharm
# @Time    : 2023/12/11 20:13

import pymysql


def create_table():
    db = pymysql.connect(host='localhost', user='root', password='root', db='python_basic')
    cursor = db.cursor()

    # 编辑sql脚本
    sql = """
        create table if not exists employee(
            first_name varchar(20) not null,
            last_name varchar(20),
            age tinyint,
            gender varchar(2),
            income float,
            create_time datetime
        );
    """

    # 使用异常捕获的方式去运行数据库的增删改查
    try:
        cursor.execute(sql)
        print('数据表创建成功...')
    except Exception as e:
        print('数据表创建失败:', e)
        # 事务只能在数据的增删改中使用
    finally:
        cursor.close()
        db.close()

create_table()
