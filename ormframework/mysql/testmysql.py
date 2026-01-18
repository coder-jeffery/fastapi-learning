#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# 打开数据库连接
# db = MySQLdb.connect('localhost', 'root', 'root', 'TESTDB', charset='utf8')

db =MySQLdb.connect(
    host='127.0.0.1',
    user='root',
    passwd='root',
    db='TESTDB',
    charset='utf8',
    # unix_socket="/tmp/mysql.sock",  # 路径1：最常见
    # unix_socket="/usr/local/mysql/mysql.sock", # 路径2：官方安装包的默认路径
    port=3306
)

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 插入语句
sql = """INSERT INTO TESTDB.EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# 关闭数据库连接
db.close()
