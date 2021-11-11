import unittest


class TriangleNotExistException(Exception):
    def __str__(self):
        return "Can`t create triangle with this arguments"


class TriangleNotValidArgumentException(Exception):
    def __str__(self):
        return "Not valid arguments"


class Triangle:
    def __init__(self, sides):
        if not isinstance(sides, tuple):
            raise TriangleNotValidArgumentException()
        if len(sides) != 3:
            raise TriangleNotValidArgumentException()
        for side in sides:
            if not (isinstance(side, int) or isinstance(side, float)):
                raise TriangleNotValidArgumentException()
        if sides[0] >= sides[1] + sides[2] or \
                sides[1] >= sides[0] + sides[2] or \
                sides[2] >= sides[0] + sides[1]:
            raise TriangleNotExistException()
        self.a = sides[0]
        self.b = sides[1]
        self.c = sides[2]

    def get_area(self):
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5


class TriangleTest(unittest.TestCase):
    def test_valid(self):
        expected = 6.0
        actual = Triangle((3, 4, 5)).get_area()
        self.assertEqual(actual, expected)

    def test_not_valid(self):
        self.assertRaises(TriangleNotExistException, Triangle, (-7, 7, 7))

    def test_not_valid_arguments(self):
        self.assertRaises(TriangleNotValidArgumentException, Triangle, ('3', 4, 5))