


from sqlalchemy.orm import Session
from coronavirus import models, schemas

def get_city(db: Session, city_id: int):
    return db.query(models.City).filter(models.City.id == city_id).first()


def get_city_by_name(db: Session, name: str):
    return db.query(models.City).filter(models.City.province == name).first()

def get_cities(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.City).offset(skip).limit(limit).all()

def create_city(db: Session, city: schemas.CreateCity):
    try:
        db_city = models.City(**city.dict())
        db.add(db_city)  # 提交
        db.commit()
        db.refresh(db_city)
    except Exception as error:
        raise error
    return db_city

def get_data(db: Session, city: str=None, skip: int = 0, limit: int = 100):
    if city:
        try:
            return db.query(models.Data).filter(models.Data.city.has(province=city))
        except Exception as error:
            raise error

    return db.query(models.Data).offset(skip).limit(limit).all()


def create_city_data(db: Session, data: schemas.CreateData, city_id: int):
    # db_data = models.Data(**data.dict(), city_id = city_id)
    # ✅ Pydantic V2 用 model_dump(
    try:
        # db_data = models.Data(**data.dict(), city_id=city_id)
        db_data = models.Data(**data.model_dump(), city_id=city_id)
        db.add(db_data)
        db.commit()
        db.refresh(db_data)
    except Exception as e:
        db.rollback()
        raise e

    print("打印：Type of return value:", type(db_data))
    print("打印 Attributes:", dir(db_data))

    return db_data
