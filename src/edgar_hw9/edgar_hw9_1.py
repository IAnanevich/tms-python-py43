from datetime import datetime
from edgar_hw9_3 import Years


class Auto:
    def __init__(self, name: str, model: str, years: Years) -> None:
        """

        :param name:
        :param model:
        :param years:
        """
        self.name = name
        self.model = model
        self.years = years

    @staticmethod
    def example() -> None:
        """

        :return:
        """
        print("Example auto")

    @property
    def notification(self) -> str:
        """

        :return:
        """
        return f"Поставка авто --> n\Модель: {self.name}, n\сделано в: {self.model}"

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
        return f"Автомобиль : {self.name}"

    @staticmethod
    def _protected() -> str:
        """

        :return:
        """
        return "скрытые функции"


class Truck(Auto):
    def __init__(self, name, model, years, color) -> None:
        """

        :param name:
        :param model:
        :param years:
        :param color:
        """
        super().__init__(name, model, years)
        self.color = color

    @staticmethod
    def example() -> None:
        """

        :return:
        """
        print("Example auto")

    @property
    def notification(self) -> str:
        """

        :return:
        """
        return f"Марка Авто: {self.name}, \nЦвет: {self.color}"


class ElectroCars(Auto):
    def __init__(self, name, model, years) -> None:
        """

        :param name:
        :param model:
        :param years:
        """
        super().__init__(name, model, years)

    @staticmethod
    def example() -> None:
        """

        :return:
        """
        print("Example auto")

    def notification(self) -> str:
        """

        :return:
        """
        return f"Марка Авто: {self.name}, \nГод Выпуска: {self.years}"


auto_1 = Auto(name="Lexus", model="SRX", years=2023)
truck_1 = Truck(name="MAN", model="SuperTruck", years=2023, color="blue")
elect_1 = ElectroCars(name="Tesla", model="X", years=2022)

print(auto_1.old_years())
print(auto_1.example())
print(auto_1.__repr__())
print(auto_1._protected())
print(auto_1.notification)

print(1 * "-")

print(truck_1.old_years())
print(truck_1.example())
print(truck_1.__repr__())
print(truck_1._protected())
print(truck_1.notification)

print(1 * "-")

print(elect_1.old_years())
print(elect_1.example())
print(elect_1.__repr__())
print(elect_1._protected())
print(elect_1.notification)
