from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime
from pydantic.types import conint

"""User Schemas"""
class UserCreate(BaseModel):
    email : EmailStr
    password : str

#Response
class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at : datetime
    
    class Config:
        orm_mode=True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

#JWT Token
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None


"""Posts Schemas"""
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

#Response
class Post(PostBase):
    id : int
    created_at : datetime
    owner_id: int
    owner: UserOut

    class Config:
        orm_mode=True

class PostCreate(PostBase):
    pass

class UpdatePost(PostBase):
    pass

"""Vote Schemas"""
class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)

class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode=True