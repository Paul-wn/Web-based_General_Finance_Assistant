from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float , ForeignKey , DateTime , Text , Date
from .base import Base

class GeneratedDB(Base):
    __tablename__ = "generated"
    id = Column(Integer, primary_key=True ,nullable=False)
    date = Column(Date, index=True)
    prompt = Column(Text)
    inference = Column(Text)
 
   