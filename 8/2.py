import unittest


def divide(num_1, num_2):
    return float(num_1)/num_2


class DivideTest(unittest.TestCase):
    def test_positive_divide(self):
        expected = 5.0
        actual = divide(10, 2)
        self.assertEqual(actual, expected)

    def test_negative_divide(self):
        expected = -2.0
        actual = divide(10, -5)
        self.assertEqual(actual, expected)

    def test_raise_error(self):
        self.assertRaises(ZeroDivisionError, divide, 10, 0)