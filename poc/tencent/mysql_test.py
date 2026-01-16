
import pymysql
import re
import json

def main(
        host: str = '127.0.0.1',
        port: int = 3306,
        user: str = 'root',
        password: str = 'root',
        database: str = 'dify',
        sql: str = 'select id,name,age from dify.students'
):
    """
    参数：
    host: 数据库主机地址（默认：127.0.0.1）
    port: 数据库端口（默认：3306）
    user: 数据库用户名（默认：root）
    password: 数据库密码（默认：root）
    database: 数据库名称（默认：dify）
    sql: 要执行的SELECT语句（必需）

    返回：
    - 总是返回 {"result": "完整字符串"} 格式
    """

    # 校验必填参数
    if not sql.strip():
        return {"result": "SQL语句不能为空"}

    # 严格校验SQL类型
    cleaned_sql = re.sub(r'[\s\t\n]+', ' ', sql.strip().lower())
    if not cleaned_sql.startswith("select"):
        return {"result": "仅允许执行SELECT查询语句"}

    # 阻止危险操作
    forbidden_keywords = ['insert', 'update', 'delete', 'drop', 'alter', 'create', 'truncate']
    if any(keyword in cleaned_sql for keyword in forbidden_keywords):
        return {"result": "检测到非查询操作语句"}

    try:
        # 建立数据库连接
        connection = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            cursorclass=pymysql.cursors.DictCursor
        )

        with connection:
            with connection.cursor() as cursor:
                # 执行SQL
                cursor.execute(sql)
                result = cursor.fetchall()

                # 将结果转换为完整字符串
                if not result:
                    result_str = "查询成功，但结果为空"
                else:
                    # 将结果转换为格式化的JSON字符串
                    result_str = json.dumps(result, indent=2, ensure_ascii=False)
                    result_str = f"查询成功，结果如下：\n{result_str}"
                print(result_str)
                return {"result": result_str}


    except pymysql.Error as err:
        return {"result": f"数据库错误: {str(err)}"}
    except Exception as e:
        return {"result": f"未知错误: {str(e)}"}

# 测试结果
print(main('127.0.0.1', 3306, user='root', password='root', database='dify', sql='select id,name,age from dify.students'))
# print(main('127.0.0.1', 3306))
