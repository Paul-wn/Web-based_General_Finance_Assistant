from pydantic import BaseModel, Field
from datetime import date as Date

class Summary(BaseModel):
    date: Date = Field(default_factory=Date.today)
    summary: str

class SummaryCreate(Summary):
    pass

class SummaryResponse(Summary):
    id: int

    class Config:
        from_attributes = True
