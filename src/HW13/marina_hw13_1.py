from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from menu_file import Menu

# создаем сессию для работы с БД
engine = create_engine("sqlite:///test_hw13.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

while True:
    if not Menu.main_menu(session=session):
        print("Goodbye!")
        break
