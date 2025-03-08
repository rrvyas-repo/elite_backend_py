from typing import Optional,TYPE_CHECKING
from sqlmodel import SQLModel,Field,Column,Relationship
import sqlalchemy.dialects.postgresql as pg
from enum import Enum
import uuid
import datetime

if TYPE_CHECKING:
    from src.model.user_model import User 

class APIKey(SQLModel, table=True):  # Separate table for Subadmin API keys
    __tablename__ = "api_keys"

    uid: uuid.UUID = Field(
        sa_column=Column(pg.UUID, nullable=False, primary_key=True, default=uuid.uuid4)
    )
    key: str = Field(max_length=255)
    subadmin_id: uuid.UUID = Field(foreign_key="users.uid")  # Link only to subadmins
    issued_at: datetime.datetime = Field(default=datetime.timezone.utc)
    expires_at: datetime.datetime = Field(default=datetime.timezone.utc)
    is_active: bool = Field(default=True)

    # One-to-One Relationship (Subadmin -> Single API Key)
    subadmin: Optional["User"] = Relationship(back_populates="api_key")