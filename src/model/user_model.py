from typing import Optional
from sqlmodel import SQLModel,Field,Column
from enum import Enum

class RoleEnum(str,Enum):
    admin="Admin"
    subadmin="SubAdmin"
    user="User"

class User(SQLModel,table=True):
    __tablename__ = "users"
    id:Optional[int]=Field(default=None,primary_key=True)
    name:str=Field(max_length=255)
    user_name:str=Field(unique=True)
    email:str=Field(unique=True)
    password:str=Field(min_length=6)
    role:RoleEnum=Field(default=RoleEnum.user)


class Product(SQLModel,table=True):
    id:Optional[int]=Field(default=None,primary_key=True)
    name:str=Field(max_length=255)