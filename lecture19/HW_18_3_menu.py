from abc import ABC, abstractmethod
from datetime import datetime


class Dish(ABC):
    @abstractmethod
    def get_dish(self):
        pass


class Risotto(Dish):
    def get_dish(self):
        return "Risotto"


class Pasta(Dish):
    def get_dish(self):
        return "Pasta"


class Pizza(Dish):
    def get_dish(self):
        return "Pizza"


class Drink(Dish):
    def get_dish(self):
        return "Drink"


class Order:
    def __init__(self):
        self.order_items = []
        self.order_time = datetime.now()

    def add_order_item(self, order_item):
        self.order_items.append(order_item)

    def display_order(self):
        print(f"Order time: {self.order_time}")
        for item in self.order_items:
            print(item.get_dish())


class OrderPart:
    def __init__(self, dish_factory, section):
        self.dish_factory = dish_factory
        self.section = section

    def get_dish(self):
        return f"{self.section}: {self.dish_factory.get_dish()}"


if __name__ == "__main__":
    # Створення об'єктів для різних блюд та напоїв
    risotto_factory = Risotto()
    pasta_factory = Pasta()
    pizza_factory = Pizza()
    drink_factory = Drink()

    # Створення частини замовлення для кожного блюда та напою
    order_risotto = OrderPart(risotto_factory, section="Hot Dishes")
    order_pasta = OrderPart(pasta_factory, section="Hot Dishes")
    order_pizza = OrderPart(pizza_factory, section="Hot Dishes")
    order_drink = OrderPart(drink_factory, section="Drinks")

    # Створення замовлення та додавання частин замовлення
    order = Order()
    order.add_order_item(order_risotto)
    order.add_order_item(order_pasta)
    order.add_order_item(order_pizza)
    order.add_order_item(order_drink)

    # Виведення замовлення на екран
    order.display_order()
