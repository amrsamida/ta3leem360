from pydantic import BaseModel

class Center(BaseModel):
    id: int
    name: str
    city: str
    from pydantic import BaseModel, Field

class Center(BaseModel):
    id: int = Field(..., example=1)
    name: str = Field(..., example="Future Academy")
    city: str = Field(..., example="Cairo")