-- use py_spider;

-- show tables;

-- 查询某一个数据表中的所有数据
-- * 代表的是通配符 匹配所有的字段名称
-- select * from ali_work;

-- 查询指定的部分字段中的数据 id 
-- select id, work_name from ali_work;


-- 创建测试数据库与数据表
show databases;
use python_basic;
show tables;
desc student_info;

-- 数据插入
-- 全字段插入
insert into student_info values (0, '安娜', 18, 176.53, '女', 1);
insert into student_info values (null, '双双', 20, 168.53, '女', 1);
insert into student_info values (default, '夏洛', 24, 172.53, '男', 2);

select * from student_info;

-- 部分字段插入
desc student_info;
insert into student_info (id, name) values (0, '木木');
select * from student_info;

-- 全字段数据批量插入
insert into student_info values (0, '惊蛰', 19, 173.87, '男', 1), (0, '何老师', 25, 174.54, '未知', 2);
select * from student_info;

-- 部分字段批量插入
insert into student_info (id, name) values (0, '南枫'), (0, '柏川');
select * from student_info;

-- 数据修改
-- select * from student_info;
-- update 表名 set 字段1, 字段2 where id=id值;
update student_info set age=17 where id=2;
select * from student_info;

update student_info set age=20, height=178.91, gender='人妖' where id=7;
select * from student_info;

-- update student_info set cls_id=3; -- 影响表中的所有行, 在开发中不要这样操作
-- select * from student_info;

-- 数据删除
-- 物理删除 当执行以下语句则直接从磁盘中将指定的数据抹除
delete from student_info where id=8;
select * from student_info;

-- 逻辑删除
-- 所谓的逻辑删除其实是判断某一个条件是否成立, 如果成立则显示数据, 如果不成立则隐藏数据
alter table student_info add is_delete bit default 0;
select * from student_info;
update student_info set is_delete=1 where id=4;
select * from student_info where is_delete=0;  -- 只是隐藏了
