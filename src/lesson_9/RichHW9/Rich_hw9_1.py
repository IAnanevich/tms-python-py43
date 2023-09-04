# Реализовать любой класс на свой выбор. В нем сделать:
# конструктор, несколько методов (один обязательно static, один class, один обычный),
# переопределить один любой из магических методов (__lt__ и тд), сделать один метод protected.
# Сделать два класса дочерних. В этих классах переопределить все методы и конструктор,
# которые можете (один метод должен быть переопределен ТОЛЬКО ОДИН раз в любом классе ребенке)
# Сделать проверку, что все работает (создать объекты от классов).

class Item:
    def __init__(self, name: str, price: float):
        """
        :param name: name
        :param price: price
        """
        self.name = name
        self.price = price

    @staticmethod
    def is_expensive(price: float) -> bool:
        """
        :param price: float
        :return: many price
        """
        return price > 1000

    @classmethod
    def _print_info(cls):
        """
        :return: name class
        """
        print(f"This is a {cls.__name__}")

    def change_price(self, new_price: float):
        """
        :param new_price: float
        :return: item change
        """
        self.price = new_price

    def __str__(self):
        """
        :return: f str
        """
        return f"Item: {self.name}, Price: ${self.price:.2f}"

    def __lt__(self, other):
        """
        :param other: price < price?
        :return: true / false
        """
        if self.price < other.price:
            print(f"{self.name} is cheaper than {other.name}.")
            return True
        else:
            print(f"{self.name} is not cheaper than {other.name}.")
            return False


# Создаем объекты
item1 = Item("Laptop", 80000)
item2 = Item("Phone", 9123)

# Проверяем методы и вывод информации
print(item1)
print(f"Is it expensive? {Item.is_expensive(item1.price)}")
item1._print_info()

print(item2)
print(f"Is it expensive? {Item.is_expensive(item2.price)}")
item2._print_info()

# Изменяем цену предмета
item1.change_price(1500)
print(item1)


class ExpensiveItem(Item):
    def __init__(self, name: str, price: float, category: str):
        super().__init__(name, price)
        self.category = category

    def __str__(self):
        return f"Expensive Item: {self.name}, Price: ${self.price:.2f}, Category: {self.category}"


class CheapItem(Item):
    def __init__(self, name: str, price: float, discount: float):
        super().__init__(name, price)
        self.discount = discount

    def calculate_discounted_price(self) -> float:
        return self.price * (1 - self.discount / 100)

    def __str__(self):
        return f"Cheap Item: {self.name}, Price: ${self.price:.2f}, Discount: {self.discount}%"


# Создаем объекты дочерних классов
expensive_item = ExpensiveItem("High-end Laptop", 6000, "Electronics")
cheap_item = CheapItem("Budget Phone", 200, 10)

# Проверяем методы и вывод информации о дочерних классах
print(expensive_item)
print(cheap_item)

# Проверяем метод calculate_discounted_price у CheapItem
discounted_price = cheap_item.calculate_discounted_price()
print(f"Discounted Price: ${discounted_price:.2f}")
