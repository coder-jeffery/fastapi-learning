from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str = "John"
    signup_ts: Optional[datetime] = None
    friends: List[int] = []

external_data ={
    "id": "123",
    "signup_ts": "2021-09-22",
    "friends": [1, 2, 3],
}

user = User(**external_data)
print(user.id, user.friends)

print(user.signup_ts, user.friends)
print(user.signup_ts)
print(user.dict())
