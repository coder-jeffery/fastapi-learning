FastAPI:
    https://fastapi.tiangolo.com/zh/
特性：
    精简编码 代码重复率低
    自带API交互文档
    API开发标准化

启动方式： uvicorn main:app --reload

http://127.0.0.1:8000/hello/tim

Starlette, Pydantic FastAPI的关系
    Python的类型提示 Type hints
FAST API：
    Pydantic基于Python类型的提示来定义数据验证，序列化和文档库
    Starlette 轻量级ASGI框架工具包 构建高性能Asyncio服务
    python3.6+

ASGI：
    unicorn
    hypercorn
    daphne
WSGI：
    uWsgi
    Gunicorn
提示词学习：
    https://github.com/JushBJJ/Mr.-Ranedeer-AI-Tutor
    https://github.com/liaogx
依赖问题：
    yield依赖

OAuah2.0
    授权码授权模式
    隐式授权模式
    密码授权模式
        Client Application- > 
    客户端凭证授权模式


pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

依赖问题
安全认证 授权 
数据库操作
模型类问题


yield

中间件编写：
    # yield执行退出模块会在中间件执行结束之后运行
    # 跨域问题
    协议+端口+域名

后台任务 执行：

查询SQL：
    SELECT data.id AS data_id, data.city_id AS data_city_id, data.date AS data_date, data.confirmed AS data_confirmed, data.recoverd AS data_recoverd, data.deaths AS data_deaths, data.province AS data_province, data.create_at AS data_create_at, data.update_at AS data_update_at
    FROM data
    WHERE EXISTS (SELECT 1
    FROM city
    WHERE city.id = data.city_id AND city.province = 'Shanghai')
    