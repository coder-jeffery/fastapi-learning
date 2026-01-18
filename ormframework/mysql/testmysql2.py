# main.py 或 app 初始化处
import pymysql

from ormframework.mysql.testmysql import cursor

pymysql.install_as_MySQLdb()

# 然后正常使用 SQLAlchemy 或其他 ORM
from sqlalchemy import create_engine
engine = create_engine("mysql://root:root@127.0.0.1/testdb")

engine.connect()
# cursor.execute("select * from testdb.employee")