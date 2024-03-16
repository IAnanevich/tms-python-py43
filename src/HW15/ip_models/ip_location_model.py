"""
    "key": "value",

    "ip": "161.185.160.93",
    "city": "New York City",
    "region": "New York",
    "country": "US",
    "loc": "40.7143,-74.0060",
    "org": "AS22252 The City of New York",
    "postal": "10001",
    "timezone": "America/New_York"
"""

import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from base_model import BaseModel

engine = create_engine('sqlite:///ip_location.db', echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()
session = Session()


class UserLocation(BaseModel):
    __tablename__ = 'users'

    id = sa.Column('id', sa.Integer, primary_key=True, autoincrement=True)
    ip = sa.Column(sa.String(100), nullable=False)
    city = sa.Column(sa.String(100), nullable=False)
    region = sa.Column(sa.String(100), nullable=False)
    country = sa.Column(sa.String(100), nullable=False)
    loc = sa.Column(sa.String(100), nullable=False)
    org = sa.Column(sa.String(100), nullable=False)
    postal = sa.Column(sa.Integer)
    timezone = sa.Column(sa.String(50), nullable=False)
    readme = sa.Column(sa.String(60), nullable=False)
