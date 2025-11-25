import datetime
from email.policy import default
from enum import Enum
from typing import Optional, List
from fastapi import APIRouter, Path, Query, Cookie, Header
from pydantic import BaseModel
from pydantic.v1 import Field
from datetime import date

app03 = APIRouter()


class CityName(str, Enum):
    Beijing = "Beijing"
    Shanghai = "Shanghai"
    Shenzhen = "Shenzhen"

@app03.get("/03")
def hello_world():
    return {"message": "Hello World"}


@app03.get("/enum/{city}")
def enum_city(city: CityName):
    if city == CityName.Beijing:
        return {"city_name": city}
    elif city == CityName.Shanghai:
        return {"city_name": city}
    elif city == CityName.Shenzhen:
        return {"city_name": city}


@app03.get("/file/{file_path:path}")
def file_path(file_path: str):
    return f"file_path is {file_path}"


@app03.get("/path/{num}")
def path_params_validate(
        num: int = Path(ge =1 , le =10, title="number", description="描述")
):
    return num

@app03.get("/query")
def page_limit(page: int =1, limit:Optional[int] = None):
    if limit:
        return {"page": page, "limit": limit}
    return {"page": page}

@app03.get("/query/bool/conversion")
def type_conversion(param: bool = False):
    return {"param": param}


@app03.get("/query/validator")
def type_params_validator(
    value: str  = Query(..., min_length=8, max_length=16,regex="^a"),
    values: List[str] = Query(default=["v1","v2"], alias="alias_name")
    ):
    return { "value": value,"values": values}


'''  请求体和字段'''
class CitiInfo(BaseModel):
    name: str = Field(..., example="Beijing")
    country: str
    country_code: str = None
    country_population: int = Field(default =100, title="人口数量",
                                    description="country population")
    class Config:
        schema_extra = {
            "example": {
                "name": "LA",
                "country":"US",
                "country_code":"US",
                "country_population":100,
            }
        }

@app03.get("/request_body/city")
def request_body_city(city: CitiInfo):
    print(city.name, city.country, city.country_code, city.country_population)
    return  city.dict()

@app03.put("/request_body/cities")
def mix_city_info(
        name: str,
        citi01: CitiInfo,
        citi02: CitiInfo,
        confirmed: int = Query(default=0, ge=0, description="确诊"),
        death: int = Query(ge=0, description="死亡", default=0),
):
    if name == "Shanghai":
        return {"Shanghai", {"confirmed": confirmed, "death": death}}
    return citi01.dict(), citi02.dict(), {"confirmed": confirmed, "death": death}


class Data(BaseModel):
    citi: List[CitiInfo] = None
    date: date
    confirmed: int = Field(ge=0, description="qz", default=0)
    death: int = Field(ge=0, description="dead", default=0)
    recovered: int = Field(ge=0, description="qy", default=0)

# 嵌套定义
'''
{
  "citi": [
    {
      "name": "Shanghai",
      "country": "Shanghai",
      "country_code": "1",
      "country_population": 20
    }, {
      "name": "Beijjing",
      "country": "Beijjing",
      "country_code": "2",
      "country_population": 10
    }

  ],

  "date": "2025-11-20",
  "confirmed": 10,
  "death": 0,
  "recovered": 10
}
'''
@app03.put("/request_body/nested")
def request_body_date(data: Data):
    return data


@app03.put("/cookie")  # 需要postman使用 非浏览器使用
def cookie(cookie_id : Optional[str] = Cookie(None)):
    return {"cookie": cookie_id}


@app03.get("/header")
def header(user_agent: Optional[str] =Header(None), convert_underscore: bool = False, x_token: Optional[str] = Header(None)):
    return {"user_agent": user_agent, "x_token": x_token}

