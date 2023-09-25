from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from HomeWork.Hw15.database import Base, engine


class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True, autoincrement=True)
    gender = Column(String)
    name_title = Column(String),
    name_first = Column(String)
    name_last = Column(String)
    email = Column(String)
    registered_date = Column(Integer)
    phone = Column(String)
    user_id_name = Column(String)


# Create Table BASE
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()
