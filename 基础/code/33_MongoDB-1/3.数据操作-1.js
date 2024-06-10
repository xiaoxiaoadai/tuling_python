/*
* 数据操作
* */

// 1.在名为test_2数据库之下的stu_test集合中存储数据
show dbs
use test_2
// 可以在不存在的数据库以及不存在的集合中直接插入数据, 不需要手动创建集合
db.stu_test.insert({'name': 'xiaoming', 'age': 10})
db.stu_test.insertOne({'name': 'xiaohong', 'age': 18})

// 2.查询对应集合中的数据
db.stu_test.find()


// 3.数据保存操作
db.stu_test.insertOne({_id: 10010, name: 'xiaoming', age: 30})
// db.stu_test.insertOne({_id: 10010, name: 'xiaoming', age: 40})  当前语句报错, 原因: id重复

// save方法可以覆盖id相同的数据
db.stu_test.save({_id: 10010, name: 'xiaoming', age: 40})  // 在pycharm中执行报错时需要重新在终端中执行
db.stu_test.find()


// 4.数据更新
// db.集合名称.update(<query>, <update>, {mulit: <bool>})
db.stu_test.insertOne({_id: 10011, name: 'xiaowang', age: 20})
db.stu_test.find()
db.stu_test.update({name: 'xiaowang'}, {name: 'xiaozhao'})
db.stu_test.update({name: 'xiaohong'}, {$set: {name: 'xiaolan'}})

// 修改满足名称为xiaoming的所有数据
db.stu_test.update({name: 'xiaoming'}, {$set: {name: 'xiaowang'}}, {multi: true})
// 修改满足名称为xiaowang的第一条数据
db.stu_test.update({name: 'xiaowang'}, {$set: {name: 'xiaoming'}})



