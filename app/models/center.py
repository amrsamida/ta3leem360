from pydantic import BaseModel

class Center(BaseModel):
    id: int
    name: str
    city: str


class CenterCreate(BaseModel):
    name: str
    city: str


class CenterUpdate(BaseModel):
    name: str | None = None
    city: str | None = None