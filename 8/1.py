import unittest


class Product:
    def __init__(self, name, price, count):
        if not isinstance(name, str):
            raise ValueError("Name cannot be not string value.")
        if not (isinstance(price, int) or isinstance(price, float)):
            raise ValueError("Price cannot be not numeric value.")
        if not (isinstance(count, int) or isinstance(count, float)):
            raise ValueError("Count cannot be not numeric value.")
        if price < 0:
            raise ValueError("Price cannot be minus numeric value.")
        if count < 0:
            raise ValueError("Count cannot be minus numeric value.")
        if not (name and price and count):
            raise ValueError("All fields must be filled")
        self.name = name
        self.price = price
        self.count = count
        if self.count > 20:
            self.discount = 0.5
        elif self.count == 20:
            self.discount = 0.7
        elif self.count >= 10:
            self.discount = 0.8
        elif self.count >= 7:
            self.discount = 0.9
        elif self.count >= 5:
            self.discount = 0.95
        else:
            self.discount = 1
        self.total_price = self.price * self.discount * self.count


class Cart:
    def __init__(self, products):
        self.products = products
        self.__total_price = 0
        if products:
            for product in products:
                self.__total_price += product.total_price

    def get_total_price(self):
        return self.__total_price


class CartTest(unittest.TestCase):
    def test_valid_card(self):
        products = (Product('p1', 10, 4),
                    Product('p2', 100, 5),
                    Product('p3', 200, 6),
                    Product('p4', 300, 7),
                    Product('p5', 400, 9),
                    Product('p6', 500, 10),
                    Product('p7', 1000, 20))
        cart = Cart(products)
        expected = 24785.0
        actual = cart.get_total_price()
        return self.assertEquals(actual, expected)
