-- 单行注释
-- 如果使用pycharm链接了mysql那么我们就不需要重新编写登录指令
-- mysql -uroot -p

-- 查询当前mysql中的所有数据库
show databases;

-- 查询指定数据库之下的数据表之前, 需要进入到这个数据库中
use py_spider;

-- 查询指定数据库之下的所有的数据表
show tables;

-- 查询当前位于哪个数据库之下
select database();

-- 查询mysql软件版本
select version();

-- 创建数据库, 在创建时需要指定当前数据库的编码集
-- create database 数据库名称 charset=编码集;
create database python_basic charset=utf8mb4;

-- 重新查询数据库
show databases;

-- 删除数据库 - 慎用
-- drop database 要删除的数据库名称;
drop database python_basic;
show databases;