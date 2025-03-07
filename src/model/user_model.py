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
    name:str=Field(sa_column=Column(max_length=255,))
    user_name:str=Field(sa_column=Column(unique=True, nullable=False))
    email:str=Field(sa_column=Column(unique=True,nullable=False))
    password:str=Field(sa_column=Column(min_length=6,nullable=False))
    role:RoleEnum=Field(sa_column=Column(default=RoleEnum.user))


