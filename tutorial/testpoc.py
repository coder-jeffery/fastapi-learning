import asyncio

from fastapi import APIRouter

testpoc = APIRouter()

@testpoc.get("/hello/{number}")
async def hello(number: int):
      number  =  number + 1
      print("number ",number)
      await asyncio.sleep(1)
      print("number count",number)
      return {"number": number, "message": "Hello World!"}





