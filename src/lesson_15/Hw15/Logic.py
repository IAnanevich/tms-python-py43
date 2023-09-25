import sys
from HomeWork.Hw15.database import session
from HomeWork.Hw15.models import User

def create_record():
    # Users
    gender = input("Gender: ")
    name_first = input("First Name: ")
    name_last = input("Last Name: ")
    email = input("Email: ")
    registered_date = input("Registration Date: ")
    phone = input("Phone: ")
    user_id_name = input("Identifier Name: ")

    # BASE
    new_user = User(
        gender=gender,
        name_first=name_first,
        name_last=name_last,
        email=email,
        registered_date=registered_date,
        phone=phone,
        user_id_name=user_id_name,
    )
    session.add(new_user)
    session.commit()

    print("Record created successfully!")

# Function to read data
def read_data():
    # Read all data
    users = session.query(User).all()

    if not users:
        print("No data in the database.")
    else:
        print("\nUser Data:")
        for user in users:
            print(f"ID: {user.id}")
            print(f"Gender: {user.gender}")
            print(f"Name: {user.name_first} {user.name_last}")  # Corrected line
            print(f"Email: {user.email}")
            print(f"Registration Date: {user.registered_date}")
            print(f"Phone: {user.phone}")
            print("-----------")

# Menu
while True:
    print("\nMenu")
    print("1. Create")
    print("2. Read")
    print("0. Exit")

    choice = input("Options: ")

    if choice == '1':
        create_record()
    elif choice == '2':
        read_data()
    elif choice == '0':
        print("Exiting the program.")
        sys.exit()
    else:
        print("Wrong choice. Please select 1, 2, or 0.")