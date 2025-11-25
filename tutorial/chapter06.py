import hashlib
from typing import Optional
from urllib.request import Request

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

app06 = APIRouter()

'''FastAPI 常见配置项'''



oauth2_schema = OAuth2PasswordBearer(tokenUrl="/chapter06/token")

@app06.get("/oauth2_pass_bearer")
async def oauth2_pass_bearer(token: str = Depends(oauth2_schema)):
    return token

'''基于 pwd和bearer token的oauth2 认证'''


fake_users_db = {
    "admin": {
        "username": "admin",
        "full_name": "admin",
        "email": "admin@citi.com",
        "hashed_password": "admin123456",
        "disabled": False,
    },
    "root": {
            "username": "root",
            "full_name": "root",
            "email": "root@citi.com",
            "hashed_password": "admin123",
            "disabled": False,
        },
}


def fake_hash_pwd(pwd: str):
    # print("输入密码", pwd)
    return "admin"+ pwd
    # print(fake_hash_pwd("123"))

from fastapi import HTTPException

class User(BaseModel):
    username: str
    # password: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

class UserInDB(User):
    hashed_password: str

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)



def fake_decode_token(token: str):
    user = get_user(fake_users_db, token)
    return user

#获取当前用户
def get_current_user(token: str = Depends(oauth2_schema)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(status_code=404,
                            detail="Not found",
                            headers={"WWW-Authenticate": "Bearer"}
                            )
    return user

# 获取活跃用户
def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400,
                            detail="Not authorized",
                            headers={"WWW-Authenticate": "Bearer"})
    return current_user


@app06.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # 查看用户
    user_dict = fake_users_db[form_data.username]
    if not user_dict:
        raise HTTPException(status_code=400,
                            detail="Incorrect username or password",
                            headers={"WWW-Authenticate": "Bearer"})
    # 构造用户对象
    user = UserInDB(**user_dict)
    # 验证密码
    if fake_hash_pwd(form_data.password) != user.hashed_password:

        raise HTTPException(status_code=400,
                            detail="Incorrect username or password",
                            headers={"WWW-Authenticate": "Bearer"})
    # 返回token
    return {"access_token": user.username, "token_type": "bearer"}
