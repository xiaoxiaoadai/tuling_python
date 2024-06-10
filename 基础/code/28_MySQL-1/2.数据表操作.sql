-- 数据表操作

-- 查询所有的数据库
show databases;

-- 进入到指定数据库之下
use py_spider;

-- 查询所有的表
show tables;

-- 查询指定的表结构 查询的是这张表中的字段以及字段对应的类型以及约束
desc ali_work;

-- 新建数据库
create database python_basic charset=utf8mb4;

-- 进入到指定数据库
use python_basic;

-- 在指定数据库中创建表
-- create table 表名称(字段名以及类型和约束, 字段名以及类型和约束...);
create table cls_info(
    -- auto_increment: 可以让主键完成自增长的功能, 默认为1, 新增一条数据则id + 1
    id int primary key auto_increment,
    cls_name varchar(10)
);

create table student_info(
    id int primary key auto_increment,
    name varchar(20) not null,
    -- unsigned: 声明整数无负数
    age tinyint unsigned default 0,
    height decimal(5,2),
    -- enum: 枚举类型, 可以在给定的值中选择一个作为当前字段的值
    gender enum('男', '女', '人妖', '未知'),
    cls_id int unsigned default 0
);

-- 查询对应数据库中的所有的表
show tables;

-- 结构查询
desc student_info;


-- 当表创建完成, 发现少写了一个字段, 如何解决？
-- 在原有表中添加新字段
-- alter table 表名 add 字段名 字段类型 [约束];
alter table student_info add birthday datetime;
desc student_info;

-- 修改原有字段
-- change 修改字段时需要更改原有字段的名称
alter table student_info change birthday birth date not null;
desc student_info;

-- 修改字段类型以及约束并不修改字段名称
alter table student_info modify birth time;
desc student_info;

-- 删除多余字段
alter table student_info drop birth;
desc student_info;

-- 删除表 - 慎用
drop table cls_info;
show tables;

-- 查询表的创建过程 列出创建表的sql语句
show create table student_info;



