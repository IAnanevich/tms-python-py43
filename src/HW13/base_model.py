from datetime import datetime
import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///bookshop.db', echo=True)
Session = sessionmaker(bind=engine)  # metaclass
Base = declarative_base()
session = Session()


class BaseModel(Base):
    __tablename__ = 'genres'
    # __table_args__ = {'extend_existing': 'name'}
    # __mapper_args__ = {'polymorphic_on': 'name'}
    id = sa.Column('id', sa.Integer, primary_key=True, autoincrement=True)
    created_at = sa.Column('Created time', sa.DateTime(), default=datetime.now)
    update_at = sa.Column('Update time', sa.DateTime(), default=datetime.now, onupdate=datetime.now)
