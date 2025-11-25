# from typing import Optional
#
# from fastapi import FastAPI
# from pydantic import BaseModel
#
# app = FastAPI()
#
# class CityInfo(BaseModel):
#     province: str
#     country: str
#     is_affected: Optional[bool] = None
#
# # @app.get('/')
# # def hello_world():
# #     return {"message": "Hello World"}
# #
# # @app.get('/city/{city}')
# # def result(city: str, query_string: Optional[str] = None):
# #     return {"city": city, "query_string": query_string}
# #
# # @app.put('/city/{city}')
# # def result(city: str, city_info: CityInfo):
# #     return {"city": city, "city_info": city_info.country, "is_affected": city_info.is_affected}
#
#
#
# @app.get('/')
# async def hello_world():
#     return {"message": "Hello World"}
#
# @app.get('/city/{city}')
# async def result(city: str, query_string: Optional[str] = None):
#     return {"city": city, "query_string": query_string}
#
# @app.put('/city/{city}')
# async def result(city: str, city_info: CityInfo):
#     return {"city": city, "city_info": city_info.country, "is_affected": city_info.is_affected}
#
# # http://127.0.0.1:8000/openapi.json
# # http://127.0.0.1:8000/redoc
#
# # http://127.0.0.1:8000/docs
# # http://127.0.0.1:8000/city/beijing?query_string=xxs
# # uvicorn hello_world:app  --reload