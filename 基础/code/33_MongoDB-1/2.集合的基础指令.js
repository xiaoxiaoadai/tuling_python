// 关于mongodb中的集合基础操作

// 1.进入到一个不存在的数据库
show dbs
use test_1 // 如果当前数据库不存在, mongodb会临时创建一个数据库
/*
* mongodb可以进入到一个不存在的数据库中, 如果在这个不存在的数据库中存入了数据
* 则mongodb会真正的创建这个数据库, 如果没有存储数据, 当退出mongo时则这个临时数据库会清空
* */

// 2.在临时数据库中创建集合
// db.createCollection(set_name, options)
db.createCollection('stu')

// 参数capped: 默认值为false表示不设置上限，值为true表示设置上限
// 参数size: 当capped值为true时，需要指定此参数，表示上限大小。
// 当文档达到上限时，会将之前的数据覆盖，单位为字节。
db.createCollection('sub', {capped: true, size: 10})

// 3.在当前数据库中显示所有的集合
show tables

// 4.删除集合
db.sub.drop()