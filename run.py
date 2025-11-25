import time
from doctest import debug
from urllib.request import Request


# class Name:
#     pass


# def get_name_with_age(name: Name, age: int):
#     print(name, age)

# get_name_with_age(name= [], age=1)

# from typing import List, Set, Tuple, Dict
#
# def process_time(items: Dict[str, float]):
#     for item in items:
#         print(item)

import uvicorn
from fastapi import FastAPI, Depends
from starlette.staticfiles import StaticFiles

from tutorial import app03, app04, app05, app06, app07, app08, testpoc

from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from fastapi.exceptions import HTTPException
from starlette.exceptions import HTTPException as StarletteHTTPException

from tutorial.chapter05 import verify_token, verify_key

from coronavirus import app_coronavirus

# 跨域的组件包
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="FastAPI 后端服务框架开发",
    description="miaoshu",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    # 全局依赖配置
    # dependencies=[Depends(verify_token), Depends(verify_key)]
)

# 重新http异常处理器
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    print("打印日志 StarletteHTTPException: ",exc)
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

# 重新异常处理器
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    print("打印日志 RequestValidationError: ",exc)
    return PlainTextResponse(str(exc), status_code=400)


app.mount("/static",StaticFiles(directory="./static"), name="static")

# 中间件 控制全局的API返回响应时间
@app.middleware('http')
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

#跨域资源 实现资源共享方式
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1",
        "http://127.0.0.1:8000",
    ],
    allow_credentials=True,
    # allow_methods=["GET", "POST"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(app03, prefix="/chapter03", tags=[" 请求参数和验证"])
app.include_router(app04, prefix="/chapter04", tags=[" 响应参数"])
app.include_router(app05, prefix="/chapter05", tags=["05 创建 导入声明和依赖注入 难点！！"])
app.include_router(app06, prefix="/chapter06", tags=["安全 认证 授权"])
app.include_router(app07, prefix="/chapter07", tags=["07 数据库操作 目录文件结构设计"])
app.include_router(app08, prefix="/chapter08", tags=["中间件设计"])
app.include_router(app_coronavirus, prefix="/coronavirus", tags=["增查改删数据管理"])

app.include_router(testpoc, prefix="/testpoc", tags=["测试POC CODE 代码"])

if __name__ == "__main__":
    uvicorn.run('run:app', host="0.0.0.0", port=8000, reload=True, workers=1)


