
# 执行测试代码 pytest

'''  执行测试代码  : pytest '''
from unittest.mock import Base

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from coronavirus.main import get_db
from run import app


# 使用内存 SQLite 数据库进行测试（隔离真实数据库）
# SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
# SQLALCHEMY_DATABASE_URL = "sqlite:///coronavirus.sqlite3"
#
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )
# TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
# # 创建测试数据库表
# Base.metadata.create_all(bind=engine)
#
# # 覆盖 get_db 依赖，使用测试数据库
# def override_get_db():
#     try:
#         db = TestingSessionLocal()
#         yield db
#     finally:
#         db.close()
#
# app.dependency_overrides[get_db] = override_get_db

''' 测试用例编写 '''
client = TestClient(app)

def test_get_city():
    response = client.get(url="/coronavirus/get_city/Shanghai")
    assert response.status_code == 200
    assert response.json() is not None
    assert response.json() == {
        "province": "Shanghai",
        "country": "China",
        "country_code": "CN",
        "country_population": 500,
        "id": 5,
        "update_at": "2025-11-21T07:05:39",
        "create_at": "2025-11-21T07:05:39"

    }

def test_get_cities():
    response = client.get(url="/coronavirus/get_cities")
    assert response.json is not None
    assert response.status_code == 200

def test_create_city():
    city_data = {
        "province": "Anqing00",
        "country": "China",
        "country_code": "CN",
        "country_population": 500,
    }
    response = client.post(url="/coronavirus/create_city",
                           # data={"city_name": "Shanghai", "city_population": 500},
                           json= city_data
                           )
    assert response.status_code == 200
    assert response.json() is not None

