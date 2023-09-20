from sqlalchemy import Column, String, Integer, Float

from src.edgar_hw13.models.base_model import BaseModel


class User(BaseModel):
    """
    The UserModel class is a subclass of the BaseModel class and represents
    a model for storing user information in a database.
    """
    __tablename__ = 'users'

    first_name = Column('first_name', String(20), nullable=False)
    last_name = Column('last_name', String(30), nullable=False)
    email = Column('email', String(50), unique=True, nullable=False)
    age = Column('age', Integer, nullable=False)
    balance = Column('balance', Float, nullable=False, default=0)
