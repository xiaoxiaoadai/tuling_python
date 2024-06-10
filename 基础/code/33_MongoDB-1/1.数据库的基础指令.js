/*
* mongodb没有表的概念, 但是有集合的概念
*   可以把mysql中的表理解成mongodb中所谓的集合
*   mysql的表必须有表结构, mongodb不需要结构
*
* mongodb和mysql都有数据库的概念
* */

// 1. 查询mongodb中所有的数据库
show dbs

// 2. 切入到指定数据库
use local

// 3.删除数据库 - 慎用
use py_spider
db.dropDatabase()