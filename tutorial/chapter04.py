
from importlib.resources import contents
from pickle import FALSE
from typing import Optional, Union, List

from fastapi import APIRouter, status, Form, File, UploadFile
from pydantic import BaseModel, EmailStr

''' 响应模型 '''
app04 = APIRouter()


class UserIn(BaseModel):
    username: str
    password: str
    mobile: str = "10086"
    email: EmailStr
    full_name: Optional[str] = None

class UserOut(BaseModel):
    username: str
    mobile: str = "13951253492"
    email: EmailStr
    full_name: Optional[str] = None
    email: EmailStr
    mobile: str
    full_name: Optional[str] = None


users = {
    "user01": UserIn(
        username="user01",
        password="123",
        mobile="110",
        email="1238@citi.com",
    ),
    "user02": UserIn(
            username="user02",
            password="234",
            mobile="119",
            email="1239@citi.com",
        )
}

@app04.post("/user", response_model=UserOut, status_code=200,response_model_exclude_unset=False)
async def get_user_info(user: UserIn):
    print(user.dict())
    return user


@app04.post("/status_code", status_code=status.HTTP_200_OK)
async def status_code():
    print(type(status.HTTP_200_OK))
    return {"status_code": status.HTTP_200_OK}


@app04.post("/response_model/attributes01",
            response_model=Union[UserIn, UserOut],
            status_code=200)
async def get_user_info(user: UserIn):
    del user.password
    print(user.dict())
    return user



@app04.post("/response_model/attributes02",
            response_model=UserOut,
            # response_model=List[UserOut],
            response_model_include=["username"],
            response_model_exclude=["mobile", "email"])
async def get_user_info(user: UserIn):
    del user.password
    print(user.dict())
    return user



'''表单处理'''
@app04.post("/login")
async def login(username: str = Form(...),
                password: str = Form(...) ):
    print(username, password)
    return {"username": username, "password": password}


'''文件上传'''
# 单个文件上传
@app04.post("/file/upload")
async def file_upload(file: bytes = File(...)):
    return {"file": file, "file size": len(file)}

# 多个文件上传
@app04.post("/file/batch/upload")
async def file_upload(file: List[bytes] = File(...)):
    return {"file": file, "file size": len(file)}

# 多个大文件上传
'''大文件保存内存 。不会出现内存爆表 会放到磁盘 
    适合图片 视频大文件
'''
@app04.post("/file/batch/bigfile")
async def file_upload(files: List[UploadFile] = File(...) ):

    for file in files:
        contents = await file.read()
        print(type(contents))
        print(contents)

    return {"filesname": files[0], "file size": len(files)}


''' FastAPI 项目静态文件配置'''

'''Handing Errors 错误处理'''

@app04.post("/system/exception")
async def http_exception(city: str):
    if city != "Beijing":
        from fastapi import HTTPException
        raise HTTPException(status_code = 404, detail="city not found" )
    return {"city": city}


@app04.post("/customized/exception/city")
async def http_exception(city_id: int):
    if city_id != 1:
        from fastapi import HTTPException
        raise HTTPException(status_code = 404, detail="city not found")
    return {"city": city_id}

