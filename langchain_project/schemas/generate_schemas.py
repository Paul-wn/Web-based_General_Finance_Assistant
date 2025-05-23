from pydantic import BaseModel , Field
from datetime import date as Date
class Generate(BaseModel):
    date: Date = Field(default_factory=Date.today)
    prompt: str
    inference: str

class GenerateCreate(Generate):
    pass

class GenerateResponse(Generate):
    id: int

    class Config:
        from_attributes = True