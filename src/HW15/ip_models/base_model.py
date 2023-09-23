import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///ip_location.db', echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()
session = Session()


class BaseModel(Base):
    __abstract__ = True

    id = sa.Column('id', sa.Integer, primary_key=True, autoincrement=True)
