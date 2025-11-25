from datetime import datetime, date as date_

from pydantic import BaseModel
from pydantic.config import ConfigDict


class CreateData(BaseModel):
    date: date_
    confirmed: int=0
    deaths: int=0
    recoverd: int=0
    province: str

class CreateCity(BaseModel):
    province: str
    country: str
    country_code: str
    country_population: int


class ReadData(CreateData):
    id: int
    city_id: int
    update_at: datetime
    create_at: datetime
    province: str

    # 旧方式写法
    model_config = {"from_attributes": True}
    # class Config:
    #     orm_mode = True

    # 新方式写法
    # model_config = ConfigDict(
    #     json_schema_extra={
    #         "example": {
    #             "city": {
    #                 "id": 1,
    #                 "city_id": 0,
    #                 "created_at": datetime.now(),
    #                 "updated_at": datetime.now(),
    #             }
    #         }
    #     }
    # )
    # model_config = ConfigDict(from_attributes=True)

class ReadCity(CreateCity):
    id: int
    update_at: datetime
    create_at: datetime

    # model_config = ConfigDict(
    #     json_schema_extra={
    #         "example": {
    #             "id": 1,
    #             # "city_id": 1,
    #             "updated_at": date_.today(),
    #             "created_at": date_.today(),
    #         }
    #     }
    # )

    # 旧写法
    # class Config:
    #     from_attributes = True
    model_config = {"from_attributes": True}
    # class Config:
        # orm_mode = True

    # model_config = ConfigDict(from_attributes=True)
    # model_config = {
    #     "json_schema_extra": {
    #         "examples": [
    #             {
    #                 "id": 1,
    #                 "city_id": 1,
    #                 "updated_at": date_.today(),
    #             }
    #         ]
    #     }
    # }

