class Menu:

    @staticmethod
    def main_menu() -> str:
        print(
            """
            Main menu:
            1. Create
            2. Read
            0. Exit
            """
        )
        return input('Choose: ')

    @staticmethod
    def create_menu() -> str:
        print(
            """
            Create menu:
            1. Create an ip_user
            """
        )
        return input('Choose: ')

    @staticmethod
    def list_menu() -> str:
        print(
            """
            Create menu:
            1. Read an ip_user
            """
        )
        return input('Choose: ')

    @staticmethod
    def exit_menu() -> str:
        print(
            """
            Create menu:
            0. Exit
            """
        )
        return input('Choose: ')
