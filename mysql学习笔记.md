# mysql 学习日记

## 清空表中数据（truncate 、 delete）

> 删除表信息的方式有两种方法：truncate与delete
>
    truncate table table_name;
    delete * from table_name;
    注 : truncate操作中的table可以省略，delete操作中的*可以省略

### truncate、delete 清空表数据的区别

1. truncate 是整体删除 (速度较快)，delete是逐条删除 (速度较慢)
2. truncate 不写服务器 log，delete 写服务器 log，也就是 truncate 效率比 delete高的原因
3. truncate 不激活trigger (触发器)，但是会重置Identity (标识列、自增字段)，相当于自增列会被置为初始值，又重新从1开始记录，而不是接着原来的 ID数。而 delete 删除以后，identity 依旧是接着被删除的最近的那一条记录ID加1后进行记录。如果只需删除表中的部分记录，只能使用 DELETE语句配合 where条件.


## mysql limit用法

使用查询语句需要显示前几条，或者中间几条时常用到limit


```sql
SELECT * FROM table LIMIT [offset,] rows | rows OFFSET offset
```

LIMIT 子句可以被用于强制 SELECT 语句返回指定的记录数。LIMIT 接受一个或两个数字参数。参数必须是一个整数常量。
- 如果给定两个参数，第一个参数指定第一个返回记录行的偏移量，第二个参数指定返回记录行的最大数目。初始记录行的偏移量是 0(而不是 1)： 为了与 PostgreSQL 兼容，MySQL 也支持句法： LIMIT # OFFSET #。
- 如果给定一个参数，则表示返回的最大数目，即LIMIT n 等价于 LIMIT 0,n 

```sql

--  检索记录行 6-15
mysql> SELECT * FROM table LIMIT 5,10;
  
-- 为了检索从某一个偏移量到记录集的结束所有的记录行，可以指定第二个参数为 -1：  
mysql> SELECT * FROM table LIMIT 95,-1; // 检索记录行 96-last.
  
-- 如果只给定一个参数，它表示返回最大的记录行数目：
mysql> SELECT * FROM table LIMIT 5; //检索前 5 个记录行
  
-- 换句话说，LIMIT n 等价于 LIMIT 0,n。  

```

