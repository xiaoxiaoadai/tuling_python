show dbs
use test_2
show tables
db.stu_test.find()

// 删除一条数据
db.stu_test.remove({name:'xiaolan'}, {justOne: true})
// 删除所有符合规定的数据
db.stu_test.remove({name: 'xiaoming'})
