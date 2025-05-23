from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker , Session
from sqlalchemy import Column, Integer, String, Float , ForeignKey

SQLALCHEMY_DATABASE_URL = "postgresql://myuser:mypassword@localhost:5432/mydatabase"
from .base import Base
from .summary import SummaryDB
from .generate import GeneratedDB

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)
    