class Menu:

    @staticmethod
    def main_menu() -> str:
        print(
            """
            Main menu:
            1. Make order
            2. Create
            3. Check all records
            4. Update some records
            5. Delete some records
            0. Exit
            """
        )
        return input('Choose: ')

    @staticmethod
    def create_menu() -> str:
        print(
            """
            Create menu:
            1. Create an user
            2. Create a book
            3. Create genre
            0. Go to back
            """
        )
        return input('Choose: ')

    @staticmethod
    def list_menu() -> str:
        print(
            """
            List menu:
            1. Get all users
            2. Get all books
            3. Get all orders
            4. Get all genres
            5. Ger all orders
            0. Go to back
            """
        )
        return input('Choose: ')

    @staticmethod
    def update_menu() -> str:
        print(
            """
            Update menu
            1. Update user
            2. Update book
            3. Update genre
            0. Go to back
            """
        )
        return input('Choose: ')

    @staticmethod
    def delete_menu() -> str:
        print(
            """
            Delete menu
            1. Delete user
            2. Delete book
            3. Delete genre
            0. Go to back
            """
        )
        return input('Choose: ')
