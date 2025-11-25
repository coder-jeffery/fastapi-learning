from http import HTTPStatus
from typing import List
from fastapi import APIRouter, Depends, HTTPException, FastAPI
from sqlalchemy.orm import Session
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT
from coronavirus import crud, schemas
from coronavirus.database import engine, Base, SessionLocal
from coronavirus.models import City, Data

app_coronavirus = APIRouter()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app_coronavirus.post("/create_city", response_model=schemas.ReadCity)
def create_city(city: schemas.CreateCity, db: Session = Depends(get_db)):
    db_city = crud.get_city_by_name(db = db, name= city.province)
    # ✅ 用 city.name 查询城市是否已存在
    if db_city:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST,
                            detail=f"City '{city.name}' already exists"
                            )
    return crud.create_city(db=db, city=city)


@app_coronavirus.get("/get_city/{city}", response_model= schemas.ReadCity)
def get_city(city: str, db: Session = Depends(get_db)):
    db_city = crud.get_city_by_name(db= db, name=city)
    if db_city is None:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST,
                            detail="city does not exist")
    return db_city

# 返回参数用List接收 。List[schemas.ReadCity]
@app_coronavirus.get("/get_cities", response_model=List[schemas.ReadCity])
def get_cities(skip: int=0, limit: int=100, db: Session = Depends(get_db)):
    cities = crud.get_cities(db=db, skip=skip, limit=limit)
    return cities


@app_coronavirus.post("/create_data/{city}", response_model=schemas.ReadData)
def create_data_for_city(city: str, data: schemas.CreateData, db: Session = Depends(get_db)):
    db_city = crud.get_city_by_name(db= db, name= city)
    # 判断db_city是否为空
    if not db_city:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST,
                            detail="city does not exist")

    data = crud.create_city_data(db=db, data=data, city_id=db_city.id)
    return data

# 返回参数用List接收 。List[schemas.ReadData]
@app_coronavirus.post("/get_data", response_model= List[schemas.ReadData])
def get_data(city: str= None, skip: int =0, limit:int=100, db:Session= Depends(get_db)):
    data = crud.get_data(db=db, city= city,skip=skip, limit=limit)
    return data

