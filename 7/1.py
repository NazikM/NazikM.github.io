from abc import ABC, abstractmethod


class Product(ABC):
    """
    Each distinct product of a product family should have a base
    interface. All variants of the product must implement this interface.
    """

    def __init__(self):
        self.dish = None

    @abstractmethod
    def cook(self) -> str:
        pass


class FettuccineAlfredo(Product):
    def __init__(self):
        self.dish = "Fettuccine Alfredo"

    def cook(self) -> str:
        print("Italian main course prepared: " + self.dish)


class Tiramisu(Product):
    def __init__(self):
        self.dish = "Tiramisu"

    def cook(self) -> str:
        print("Italian dessert prepared: " + self.dish)


class DuckALOrange(Product):
    def __init__(self):
        self.dish = "Duck À L'Orange"

    def cook(self) -> str:
        print("French main course prepared: " + self.dish)


class CremeBrulee(Product):
    def __init__(self):
        self.dish = "Crème brûlée"

    def cook(self) -> str:
        print("French dessert prepared: " + self.dish)


class Factory(ABC):
    """
    The Abstract Factory interface declares a set of methods
    that return different abstract products. These products
    are called a family and are related by a high-level theme
    or concept. Products of one family are usually able
    to collaborate among themselves. A family of products
    may have several variants, but the products of one variant
    are incompatible with products of another.
    """
    @abstractmethod
    def get_dish(self, type_of_meal):
        pass


class ItalianDishesFactory(Factory):
    def get_dish(self, type_of_meal) -> Product:
        if type_of_meal == "main":
            return FettuccineAlfredo()
        else:
            return Tiramisu()


class FrenchDishesFactory(Factory):
    def get_dish(self, type_of_meal) -> Product:
        if type_of_meal == "main":
            return DuckALOrange()
        else:
            return CremeBrulee()


class FactoryProducer:
    def get_factory(self, type_of_factory):
        if type_of_factory == "italian":
            return ItalianDishesFactory()
        return FrenchDishesFactory()

fp = FactoryProducer()
fac = fp.get_factory("italian")
main_dish = fac.get_dish("main")
main_dish.cook()

dessert = fac.get_dish("dessert")
dessert.cook()