
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine


SQLALCHEMY_DATABASE_URI = 'sqlite:///coronavirus.sqlite3'

engine = create_engine(
    SQLALCHEMY_DATABASE_URI,
    # encoding="utf-8",   #  python sqlilte3.0 默认是utf-8
    echo=True,
    connect_args={"check_same_thread": False}
)


SessionLocal = sessionmaker(expire_on_commit=True ,autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base(bind = e
#
#
# ngine, name= 'Base') 。
# #declarative_base 不再接收参数绑定 。只需要创建base类
Base = declarative_base()