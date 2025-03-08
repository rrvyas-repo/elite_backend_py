from typing import Optional, List,TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship, Column
import sqlalchemy.dialects.postgresql as pg
from enum import Enum
import uuid
import datetime

if TYPE_CHECKING:
    from src.model.api_model import APIKey

class RoleEnum(str, Enum):
    admin = "Admin"
    subadmin = "SubAdmin"
    user = "User"

class User(SQLModel, table=True):
    __tablename__ = "users"

    uid: uuid.UUID = Field(
        sa_column=Column(pg.UUID, nullable=False, primary_key=True, default=uuid.uuid4)
    )
    name: str = Field(max_length=255)
    user_name: str = Field(unique=True)
    email: str = Field(unique=True)
    password: str = Field(min_length=6)
    role: RoleEnum = Field(default=RoleEnum.user)

    # One-to-One Relationship (Subadmin -> Single API Key)
    api_key: Optional["APIKey"] = Relationship(back_populates="subadmin")