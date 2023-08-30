# Реализовать любой класс на свой выбор. В нем сделать:
# конструктор
# несколько методов (один обязательно статикметод, один классметод, один обычный)
# переопределить один любой из магических методов (__lt__ и тд)
# сделать один метод протектед
# Сделать два класса дочерних. В этих классах переопределить все методы и конструктор,
# которые можете (один метод должен быть переопределен ТОЛЬКО ОДИН раз в любом классе ребенке)
# Сделать проверку, что все работает (создать обьекты от классов)
from maxim_hw9_2 import RegistryMeta
from maxim_hw9_3 import Lot


class Tender(metaclass=RegistryMeta):
    TOTAL_OBJECTS = 0

    def __init__(self,
                 number: str,
                 unp: str,
                 contact: str,
                 date_made: str,
                 date_end: str,
                 value: int | float,
                 lots: list,
                 docs: bytes) -> None:
        self.number = number
        self.unn = unp
        self.contact = contact
        self.date_made = date_made
        self.date_end = date_end
        self.value = value
        self.lots = self.__get_struct_lot(lots)
        self.docs = docs
        Tender.TOTAL_OBJECTS += 1

    def __lt__(self, other) -> bool:
        if isinstance(other, Tender):
            return self.value < other.value
        elif isinstance(other, int | float):
            return self.value < other
        else:
            return NotImplemented

    def __le__(self, other) -> bool:
        if isinstance(other, Tender):
            return self.value <= other.value
        elif isinstance(other, int | float):
            return self.value <= other
        else:
            return NotImplemented

    @staticmethod
    def functional_test() -> None:
        """ Do functional test

        :return: None
        """
        print("Don't worry, I know my work.")

    @classmethod
    def total_objects(cls) -> None:
        """ Print total objects of class

        :return: None
        """
        print(f"Total objects: {cls.TOTAL_OBJECTS}")

    @property
    def get_lots(self) -> list:
        """ Return tender lots

        :return: list of classes Lot
        """
        return self.lots

    def check_unp(self) -> bool:
        """ Checks unp of organization

        :return: True if length string 9
        """
        return len(self.unn) == 9

    @staticmethod
    def __get_struct_lot(lots: list) -> list:
        """ Converts a list of dictionaries to a list of the class Lot

        :param lots: list of dictionaries of lots
        :return: list of classes Lot
        """
        return [Lot(**lot) for lot in lots]


class Operator1(Tender):
    TOTAL_OBJECTS = 0

    def __init__(self,
                 number: str,
                 unp: str,
                 contact: str,
                 date_made: str,
                 date_end: str,
                 value: int | float,
                 lots: list,
                 docs: bytes,
                 operator: str = "operator_1") -> None:
        super().__init__(
            number,
            unp,
            contact,
            date_made,
            date_end,
            value,
            lots,
            docs
        )
        self.operator = operator
        Operator1.TOTAL_OBJECTS += 1

    @staticmethod
    def functional_test() -> None:
        """ Do functional test

        :return: None
        """
        print("Don't worry, operator_1 works.")


class Operator2(Tender):
    TOTAL_OBJECTS = 0

    def __init__(self,
                 number: str,
                 unp: str,
                 contact: str,
                 date_made: str,
                 date_end: str,
                 value: int | float,
                 lots: list,
                 docs: bytes,
                 operator: str = "operator_2") -> None:
        super().__init__(
            number,
            unp,
            contact,
            date_made,
            date_end,
            value,
            lots,
            docs
        )
        self.operator = operator
        Operator2.TOTAL_OBJECTS += 1

    @staticmethod
    def functional_test() -> None:
        """ Do functional test

        :return: None
        """
        print("Don't worry, operator_2 works.")


if __name__ == "__main__":
    tend = Tender(
        "250",
        "123456789",
        "Gayazovs brothers, +375291100000",
        "30.08.2023",
        "04.09.2023",
        3120,
        [
            {
                "number_lot": 1,
                "subject_of_purchase": "Lada 2109 (Malinovaya)",
                "quantity": 1,
                "value": 1560,
                "status": "Cancelled"},
            {
                "number_lot": 2,
                "subject_of_purchase": "Lada vesta",
                "quantity": 1,
                "value": 1560,
                "status": "Cancelled"}
        ],
        b""
    )

    tend1 = Operator1(
        "0001362942",
        "100650172",
        "Tony Stark Ironmanovich, +375297777777",
        "30.08.2023",
        "31.08.2023",
        3800,
        [{
            "number_lot": 1,
            "subject_of_purchase": "Translational amplifier",
            "quantity": 2,
            "value": 3800,
            "status": "Cancelled"}],
        b""
    )

    tend2 = Operator2(
        "1086334",
        "500043292",
        "Miley Cyrus, +375291100739",
        "30.08.2023",
        "04.09.2023",
        1,
        [{
            "number_lot": 1,
            "subject_of_purchase": "Flowers",
            "quantity": 29,
            "value": 1,
            "status": "Cancelled"}],
        b""
    )
    print(tend1 > tend2)
    tend.functional_test()
    tend1.functional_test()
    tend2.functional_test()
    print(tend.get_lots)
    print(tend1.get_lots)
    print(tend2.get_lots)
    tend.total_objects()
    tend1.total_objects()
    tend2.total_objects()
    print(RegistryMeta.registry)
