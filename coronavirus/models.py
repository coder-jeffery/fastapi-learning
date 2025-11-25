

from sqlalchemy import Column, Integer, String, ForeignKey, BigInteger, DateTime, func
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Date

from coronavirus.database import Base


class City(Base):
    __tablename__ = "city"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    province = Column(String(100), unique=True, nullable=False, comment="省份/直辖市")
    country = Column(String(100), nullable=True, comment="国家")
    country_code = Column(String(100), nullable=True, comment="国家代码")
    country_population = Column(BigInteger, nullable=True)

    data = relationship("Data", back_populates="city")
    create_at = Column(DateTime, server_default= func.now())
    update_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    # __mapper_args__ = {"order_by": country_code}

    def __repr__(self):
        return f'{self.province} {self.country}'

class Data(Base):
    __tablename__ = "data"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    city_id = Column(Integer, ForeignKey("city.id"))
    date = Column(Date, nullable=False)
    confirmed = Column(BigInteger,  nullable= False)
    recoverd = Column(BigInteger, nullable=False)
    deaths = Column(BigInteger, nullable=False)
    province = Column(String(100), nullable=True)
    city = relationship("City", back_populates="data")

    create_at = Column(DateTime, server_default=func.now())
    update_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    # __mapper_args__ = {"order_by": date.desc()}

    def __repr__(self):
        return f'{self.city} {self.date}'

