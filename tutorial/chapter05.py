from typing import Optional
from urllib.request import Request
from fastapi import APIRouter, HTTPException
from fastapi.params import Depends, Header
from pydantic import BaseModel
from starlette import status

app05 = APIRouter()


'''路径操作配置 '''

class UserIn(BaseModel):
    name: str
    age: int
    address: str

class UserOut(BaseModel):
    name: str
    age: int
    address: str

@app05.post("/path_operation_config",
            response_model= UserOut,
            tags=["Path", "Operation", "Configuration"],
            description="desc",
            summary="desc",
            # deprecated=True,
            status_code=status.HTTP_200_OK)
async def path_operation_config(user: UserIn):
    return user


'''创建导入声明和依赖'''
'''函数依赖'''
async def common_parameters(q: Optional[str] =None,
                            page: int = 1,
                            limit: int = 10):
    return {"q": q, "page": page, "limit": limit}

@app05.get("/dependency01")
async def dependency01(commons: dict = Depends(common_parameters)):
    return commons

@app05.get("/dependency02")
def dependency02(commons: dict = Depends(common_parameters)):
    return commons



# @app05.get("/dependency03_1")
#     pass
# @app05.get("/dependency03_2")


dummy_code =[{"item_name":"Foo"},{"item_name":"Bar"},{"item_name":"Baz"}]

'''类依赖'''
class CommonQueryParams:
    def __init__(self, q: Optional[str] = None,  page: int = 1, limit: int = 10):
        self.q = q
        self.page = page
        self.limit = limit

@app05.get("/dependency03_3")
# async def dependency03_1(params: CommonQueryParams = Depends(CommonQueryParams)):
# async def dependency03_2(params: CommonQueryParams = Depends()):
async def class_as_dependency03_3(commons = Depends(CommonQueryParams)):
    response ={}
    if commons.q:
        response.update({"q": commons.q})
    items = dummy_code[commons.page: commons.page + commons.limit]
    response.update({"items": items})
    return response

'''子依赖关系'''

def query(q: Optional[str] = None):
    print("打印信息 query", q)
    return q
    # return {"q", q}

# q: Optional[str]= Depends(query)
def sub_query(q: Optional[str]= Depends(query), last_query: Optional[str] = None):
    if not q:
        print("打印 not q", q)
        return last_query
    print("打印  q", q)
    return q

@app05.get("/sub_dependency")
async def sub_dependency(final_query: Optional[str] = Depends(sub_query)): #use_cache=True
    print("打印参数 final_query", final_query)
    return {"sub_query": final_query}



'''路径操作器 添加多个依赖'''
async def verify_token(x_token: str = Header):
    if x_token != "fake-token":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="x_token token is not  invalid")
    return x_token

async def verify_key(x_key: str = Header):
    if x_key != "fake-key":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="x_key token is not invalid")
    return x_key


@app05.get("/dependency_in_path_operation", dependencies=[Depends(verify_token), Depends(verify_key)])
async def dependency_in_path_operation():
    return [{"user":"user01"}, {"user":"user02"}]


'''依赖注入系统
特性：
    提高代码复用
    共享数据库连接
    增强安全 认证 角色管理
FastAPI
    关系型数据库 支撑NoSQL
    第三方包和API
    认证和授权
    响应数据和注入系统
'''


''' 全局依赖使用 '''

# app05 = APIRouter( dependencies=[Depends(verify_token), Depends(verify_key)])

''' yield依赖关键字作用'''












