"""Реализовать любой метакласс"""


class Meta(type):
    def __new__(cls, name, bases, attrs, *args, **kwargs):
        for key, value in attrs.items():
            if not callable(value) and ' ' in value: #как сделать проверку на третье слово?
                print(f'patronymic does not exist for {value}')
        return super().__new__(cls, name, bases, attrs, *args, **kwargs)


class FullName(metaclass=Meta):
    """
    FullName class created using metaclass
    Methods: __init__, write_full_name, write_name_surname
    Attributes: name, surname, patronymic
    """
    def __init__(self, name: str, surname: str, patronymic: None = str) -> None:
        """
        Initializes an instance of class
        :param name: name
        :param surname: surname
        :param patronymic: patronymic
        """
        self.name = name
        self.surname = surname
        self.patronymic = patronymic

    def write_full_name(self) -> None:
        """
        The function prints a string with the surname and name and patronymic
        :return: None
        """
        print(f'{self.name} {self.surname} {self.patronymic}')

    def write_name_surname(self) -> None:
        """
        The function prints a string with the surname and name
        :return: None
        """
        print(f'{self.name} {self.surname}')


person_1 = FullName('Yaroslava', 'Grek')
person_2 = FullName('Daria', 'Konankova', 'Sergeevna')
person_2.write_full_name()
person_1.write_name_surname()
