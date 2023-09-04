# Реализовать любой класс на свой выбор. В нем сделать:
# конструктор несколько методов (один обязательно статикметод,
# один классметод, один обычный) переопределить один любой из
# магических методов (__lt__ и тд) сделать один метод протектед
#
# Сделать два класса дочерних. В этих классах переопределить все
# методы и конструктор, которые можете (один метод должен быть переопределен
# ТОЛЬКО ОДИН раз в любом классе ребенке)
#
# Сделать проверку, что все работает (создать обьекты от классов)

from datetime import datetime
from katya_9_3 import Years


class OfficeEquipment:
    def __init__(self, name: str, make: str, years: Years) -> None:
        """

        :param name:
        :param make:
        :param years:
        """
        self.name = name
        self.make = make
        self.years = years

    @staticmethod
    def thanks() -> None:
        """

        :return:
        """
        print("Спасибо, что выбрали нас")

    @property
    def sms(self) -> str:
        """

        :return:
        """
        return f"Добавляем на склад --> \nМодель: {self.name}, \nсделано в: {self.make}"

    def old_years(self) -> int:
        """

        :return:
        """
        current_datetime = datetime.now()
        return current_datetime.year - self.years

    def __repr__(self) -> str:
        """

        :return:
        """
        return f"Техника : {self.name}"

    @staticmethod
    def _protected() -> str:
        """

        :return:
        """
        return "секретная информация"


class Printer(OfficeEquipment):
    def __init__(self, name, make, years, color) -> None:
        """

        :param name:
        :param make:
        :param years:
        :param color:
        """
        super().__init__(name, make, years)
        self.color = color

    @staticmethod
    def thanks() -> str:
        """

        :return:
        """
        return "Спасибо, что выбрали данный принтер"

    @property
    def sms(self) -> str:
        """

        :return:
        """
        return f"Модель принтера: {self.name}, \nцвет: {self.color}"


class Skan(OfficeEquipment):
    def __init__(self, name, make, years) -> None:
        """

        :param name:
        :param make:
        :param years:
        """
        super().__init__(name, make, years)

    @staticmethod
    def thanks() -> str:
        """

        :return:
        """
        return "Спасибо, что выбрали данный сканер"

    @property
    def sms(self) -> str:
        """

        :return:
        """
        return f"Модель сканера: {self.name}, \nгод выпуска: {self.years}"


office_1 = OfficeEquipment(name="xiaomi", make="china", years=2022)
printer_1 = Printer(name="hp", make="china", years=2020, color="black")
skan_1 = Skan(name="sony", make="china", years=2019)

print(office_1.old_years())
print(office_1.sms)
print(office_1.__repr__())
print(office_1._protected())
print(office_1.thanks())

print(20 * "-")

print(printer_1.old_years())
print(printer_1.sms)
print(printer_1.__repr__())
print(printer_1._protected)
print(printer_1.thanks())

print(20 * "-")

print(skan_1.old_years())
print(skan_1.sms)
print(skan_1.__repr__())
print(skan_1._protected)
print(skan_1.thanks())
