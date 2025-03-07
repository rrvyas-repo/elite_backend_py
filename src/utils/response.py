from typing import Generic, TypeVar, Optional
from pydantic import BaseModel

T = TypeVar("T")

class ResponseModel(BaseModel, Generic[T]):
    success: bool
    status_code: int
    data: Optional[T] = None
    error: Optional[str] = None
    error_code: Optional[str] = None