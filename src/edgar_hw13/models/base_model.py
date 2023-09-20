from datetime import datetime

from src.edgar_hw13.db import Base

from sqlalchemy import Column, Integer, DateTime


class BaseModel(Base):
    """
    The BaseModel class is a subclass of Base from SQLAlchemy's ORM module.
    It represents a base model for other models in the application.
    """
    __abstract__ = True

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    created_at = Column('created_at', DateTime, default=datetime.now)
    updated_at = Column('updated_at', DateTime, default=datetime.now, onupdate=datetime.now)
