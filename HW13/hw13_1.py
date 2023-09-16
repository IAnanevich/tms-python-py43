from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from menu import Menu

engine = create_engine("sqlite:///dz13.db", echo=True)
Sessions = sessionmaker(bind=engine)
session = Sessions()
current_menu = "Главное"

while True:
    Menu.draw_menu(menu_name=current_menu)
    current_menu = Menu.some_input(session=session, menu_name=current_menu, choose_input=input(">>>"))
    if current_menu == "Exit":
        break
