use python_test

db.getCollection("products").insert([{
    _id: 100,
    sku: "abc123",
    description: "Single line description"
}]);
db.getCollection("products").insert([{
    _id: 101,
    sku: "abc789",
    description: "First line\nSecond line"
}]);
db.getCollection("products").insert([{
    _id: 102,
    sku: "xyz456",
    description: "Many spaces before    line"
}]);
db.getCollection("products").insert([{
    _id: 103,
    sku: "xyz789",
    description: "Multiple\nline description"
}]);
db.getCollection("products").insert([{
    _id: 104,
    sku: "abc123",
    description: "Single line description"
}]);


db.getCollection("stu_info").insert([{
    _id: ObjectId("626ba04fce0a56f10342b6f3"),
    name: "郭靖",
    hometown: "蒙古",
    age: 20,
    gender: true
}]);
db.getCollection("stu_info").insert([{
    _id: ObjectId("626ba07cce0a56f10342b6f4"),
    name: "黄蓉",
    hometown: "桃花岛",
    age: 18,
    gender: false
}]);
db.getCollection("stu_info").insert([{
    _id: ObjectId("626ba0acce0a56f10342b6f5"),
    name: "华筝",
    hometown: "蒙古",
    age: 18,
    gender: false
}]);
db.getCollection("stu_info").insert([{
    _id: ObjectId("626ba0d2ce0a56f10342b6f6"),
    name: "黄药师",
    hometown: "桃花岛",
    age: 40,
    gender: true
}]);
db.getCollection("stu_info").insert([{
    _id: ObjectId("626ba0f1ce0a56f10342b6f7"),
    name: "段誉",
    hometown: "大理",
    age: 16,
    gender: true
}]);
db.getCollection("stu_info").insert([{
    _id: ObjectId("626ba10bce0a56f10342b6f8"),
    name: "段王爷",
    hometown: "大理",
    age: 45,
    gender: true
}]);
db.getCollection("stu_info").insert([{
    _id: ObjectId("626ba12cce0a56f10342b6f9"),
    name: "洪七公",
    hometown: "华山",
    age: 18,
    gender: true
}]);

show tables

// 数据查询
// db.集合名称.find()
db.stu_info.find()
// 查询年龄为20的学生数据
db.stu_info.find({age: 20})
// 查询年龄为18的一条学生数据
// db.stu_info.find({age:18})
db.stu_info.findOne({age: 18})
// 格式化输出查询结果 - 需要在终端中执行
db.stu_info.find().pretty()

// 比较运算符
db.stu_info.find({age: {$gte: 18}})


// 不连续的范围运算符 类似于逻辑运算符
db.stu_info.find({age: {$in: [18, 20]}})

// 逻辑运算
// 并且查询 - mongo中没有and关键字
db.stu_info.find({age: 18, hometown: '桃花岛'})
// 或查询
db.stu_info.find({$or: [{age: 20}, {hometown: '华山'}]})

// 混合查询
db.stu_info.find({
    $or: [
        {
            age: {$gte: 20}}, {hometown: {$in: ['桃花岛', '华山']}}
    ]
})

// 正则表达式查询
db.products.find({sku: /^abc/})
db.products.find({sku: {$regex: '789$'}})
db.products.find({sku:  /789$/})

// 分页查询
db.products.find()
db.products.find().limit(2)
db.products.find().skip(2)  // 忽略指定的条数继续向下查询
// 查询除了两条数据之外的剩下的两条数据
db.products.find().skip(2).limit(2)

// 自定义查询 - 自己创建js函数定义查询规则
db.stu_info.find({
    $where: function() {
        return this.age <= 18;  // JavaScript规定
    }
})

// 投影 - 类似于mysql中的指定字段查询
db.stu_info.find({age: {$gt: 18}}, {name: 1, _id: 0})


// 排序 倒序查询
// 1代表正序, -1代表倒序
db.stu_info.find().sort({age: -1})
db.stu_info.find().sort({age: -1, gender: -1})
db.stu_info.find({age: {$gt: 18}}).sort({age: -1})

// 记录统计
// 统计学生个数
db.stu_info.find()
db.stu_info.find().count()
db.stu_info.find({age: {$gt: 18}}).count()

// 需要在终端中执行
db.stu_info.count()

// 去重
db.stu_info.distinct('hometown')
// 查询年龄大于20的学生的出生地信息并去重
db.stu_info.distinct('hometown', {age: {$gt: 20}})

// 聚合操作
// 分组
db.stu_info.aggregate({
    $group: {_id: '$gender', counter: {$sum: 1}}
})

// 根据性别进行分组, 获取不同分组的统计人数以及平均年龄
db.stu_info.aggregate({
    $group: {_id: '$gender', '统计人数': {'$sum': 1}, '平均年龄': {$avg: '$age'}}
})

// 没有指定分组字段的情况
db.stu_info.aggregate({
    $group: {_id: null, '统计人数': {'$sum': 1}, '平均年龄': {$avg: '$age'}}
})


// 对字段名取别名
db.stu_info.aggregate({
    $project: {_id: 0, name: 1, age: 1}
})

// 查询性别数据、人数统计、平均年龄并以中文显示
db.stu_info.aggregate(
    {$group: {_id: '$gender', counter: {$sum: 1}, avg_age: {$avg: '$age'}}},
    {$project: {'学生性别': '$_id', '人数统计': '$counter', '平均年龄': '$avg_age', _id: 0}}
)

// 数据过滤
// 查询年龄大于20的学生
db.stu_info.aggregate({
    $match: {age: {$gt: 20}}
})

// 查询年龄大于20的男生人数、女生人数并使用中文输出
db.stu_info.aggregate(
    {
        $match: {age: {$gt: 20}}
    },
    {
        $group: {_id: '$gender', counter: {$sum: 1}}
    },
    {
        $project: {'性别': '$_id', '统计人数': '$counter', _id: 0}
    }
)


db.stu_info.aggregate(
  {
    $match:
    {
      $or:
        [
          {
            age: {$gt: 20}
          },
          {
            hometown: {$in: ["蒙古", "大理"]}
          }
        ]
    },
  },

  {
    $group: {_id: "$gender", counter: {$sum: 1}}
  },

  {
    $project: {"性别": "$_id", "统计人数": "$counter", _id: 0}
  }
)


// 排序管道
db.stu_info.aggregate({
    $sort: {age: 1}
})

db.stu_info.aggregate(
    {
        $group: {_id: '$gender', counter: {$sum: 1}}
    },
    {
        $sort: {counter: -1}
    }
)

// 分页管道
db.stu_info.aggregate({$skip: 2})
// 获取除了第一个学生之外的第一个学生
db.stu_info.aggregate({$skip: 1}, {$limit: 1})