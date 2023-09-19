"""Database & session creation."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE = "d:\\Program Files\\djangoProject\\db\\library.db"
engine = create_engine('sqlite:///library.db', echo=False)
#engine = create_engine(DATABASE, echo=True)

Session = sessionmaker(bind=engine)
session = Session()
