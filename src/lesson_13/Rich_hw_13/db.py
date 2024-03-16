from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///Bookshop.db', echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()
session = Session()
