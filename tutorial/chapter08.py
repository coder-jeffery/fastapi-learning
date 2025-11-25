from typing import Optional

# from ctypes.macholib import framework
from datetime import time

from fastapi import APIRouter, BackgroundTasks, Depends
from starlette.background import BackgroundTask

app08 = APIRouter()

# 控制全局的API返回响应时间

# yield 依赖 退出部分会在中间件执行完成之后运行！！！！！

def bg_task(framework: str):
    with open("TEST_READ.md",mode= "a") as f:
        f.write(f"{framework} 框架学习" )

@app08.post("/exec/task01")
async def exec_task(framework: str, background_task: BackgroundTasks):
    ''' 后台任务函数'''
    background_task.add_task(bg_task, framework=framework)
    return {"message": "Task is DONE!"}


def continue_write_task(backgroup_task: BackgroundTasks, q: Optional[str] = None):
    if q:
        backgroup_task.add_task(bg_task, "这里是追加的一段内容 用来测试依赖注入")
    return q

# 后台任务

@app08.post("/exec/task02")
async def exec_task2(q: str = Depends(continue_write_task)):
    if q:
         return {"message": "Task2  is DONE!"}

