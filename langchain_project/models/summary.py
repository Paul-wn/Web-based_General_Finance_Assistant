from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float , ForeignKey , DateTime , Text , Date
from .base import Base

class SummaryDB(Base):
    __tablename__ = "summary"
    id = Column(Integer, primary_key=True ,nullable=False)
    date = Column(Date, index=True)
    summary = Column(Text)
