from pydantic import BaseModel
from typing import Optional


# Schema اللي بيرجع في الـ responses
class Center(BaseModel):
    id: int
    name: str
    city: str
    description: Optional[str] = None

    class Config:
        from_attributes = True   # مهم جدًا مع SQLAlchemy


# Schema لإنشاء مركز جديد
class CenterCreate(BaseModel):
    name: str
    city: str
    description: Optional[str] = None


# Schema للتعديل
class CenterUpdate(BaseModel):
    name: Optional[str] = None
    city: Optional[str] = None
    description: Optional[str] = None