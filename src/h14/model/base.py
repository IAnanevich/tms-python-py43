from sqlalchemy import Column, Integer, DateTime
from datetime import datetime
from src.h14.nastya_hw14_1 import Base


class BaseModel(Base):
    """
    The BaseModel class is a subclass of Base from SQLAlchemy's
    """
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    created_at = Column('created_at', DateTime(), default=datetime.now)
    updated_at = Column('updated_at', DateTime(), default=datetime.now, onupdate=datetime.now)
