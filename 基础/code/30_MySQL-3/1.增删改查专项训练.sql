use python_test_1;
show tables;
select * from students;


-- 统计学生总数
select count(*) from students;

-- 获取当前年龄最大/最小的学生
select max(age) from students;
select min(age) from students;

-- 求和
select sum(age) from students;

-- 平均年龄
select sum(age)/count(*) from students;
select avg(age) from students;

-- 分组查询
select gender from students group by gender;
select gender, group_concat(name) from students group by gender;
select gender, group_concat(id) from students group by gender;

select gender, avg(age) from students group by gender;
select gender, count(*) from students group by gender;

-- 在分组查询中如果携带条件则不能使用where, 通过having完成条件查询
select gender, count(*) from students group by gender having count(*) > 2;

-- with rollup
select gender,count(*) from students group by gender with rollup;
select gender,group_concat(age) from students group by gender with rollup;


-- 分页查询
-- select * from 表名 limit start, count
select * from students limit 0, 3;
select * from students limit 2; -- 如果忽略limit中的第一个参数则默认为0

select * from students limit 0, 5;
select * from students limit 5, 5;

-- 完成翻页功能, 要求每一页显示2条数据, 将当前表中的数据全部显示出来
select * from students limit 0, 2;
select * from students limit 2, 2;
select * from students limit 4, 2;
select * from students limit 6, 2;
select * from students limit 8, 2;
select * from students limit 10, 3;
select * from students limit 13, 2; -- 如果返回的数量不够则不会报错, 有多少取多少

-- select * from students limit(12 - 1), 1;
-- select * from students limit 10, 2 order by age desc;
select * from students order by height desc limit 10, 2;  -- limit需要放在最后
select * from students where gender=2 order by height desc limit 0, 10;


-- 链接查询
-- 内链接
-- select * from 表1 inner join 表2 on 表1.列=表2.列;
select * from students inner join classes on students.cls_id=classes.id;
select * from students as 学生表 inner join classes as 班级表 on 学生表.cls_id=班级表.id;

-- 左/右连接
select * from students as 学生表 right join classes as 班级表 on 学生表.cls_id=班级表.id;
select 学生表.name as 学生信息, 班级表.name as 班级名称 from students as 学生表 inner join classes as 班级表 on 学生表.cls_id=班级表.id;

-- 自关联查询的准备工作
create table tb_areas(
  aid int primary key,
  atitle varchar(20),
  pid int
);
desc tb_areas;

-- 查询一共有多少个省
select count(*) from tb_areas where pid is null;

-- 查询某个省的所有城市 -- 湖南省
# select aid from tb_areas where atitle='湖南省';
# select atitle from tb_areas where pid=430000;

select 城市信息.* from tb_areas as 城市信息 inner join tb_areas as 省信息 on 城市信息.pid=省信息.aid
              where 省信息.atitle='湖南省';


select 区县信息.* from tb_areas as 区县信息 inner join tb_areas as 城市信息 on 区县信息.pid=城市信息.aid
              where 城市信息.atitle='长沙市';


-- 子查询 - 不建议使用[查询速度慢]
-- 查询年龄大于平均年龄的所有学生
-- 可以将一段单独查询语句作为另外一个查询语句的条件
select * from students where age > (select avg(age) from students);

-- 查询对应班级中包含的所有学生: inner join?
select name from students where cls_id in (select id from classes where name='python_01期');


-- 视图 - 创建视图的视图时为了可以和表做区分需要在视图名称前加v_前缀
create view v_select_city as select 城市信息.* from tb_areas as 城市信息 inner join tb_areas as 省信息 on 城市信息.pid=省信息.aid
              where 省信息.atitle='湖南省';

-- 除了表信息可以显示之外也可以显示创建的视图
show tables;
select * from v_select_city; -- 查询视图的方式运行之前写的自关联语句

-- 删除视图
drop view v_select_city;
show tables;


-- 事务
-- 开启事务
-- begin;

-- 提交事务
-- commit;

-- 回滚
-- rollback;

