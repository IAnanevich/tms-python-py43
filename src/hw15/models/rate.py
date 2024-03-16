"""SQLAlchemy Data Models."""
from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.types import Integer, Float, String, DateTime

from database import engine

Base = declarative_base()


class Rate(Base):
    __tablename__ = "rate"
    id = Column(Integer, primary_key=True, autoincrement="auto")
    code = Column(String(3), nullable=False)
    bank_name = Column(String(255), nullable=False)
    rate = Column(Float, nullable=False, default=0)
    updated_at = Column(DateTime, server_default=func.now())


# Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
