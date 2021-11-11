import unittest


def quadratic_equation(a, b, c):
    D = b**2 - 4*a*c
    if not a or not b:
        raise ValueError
    if D > 0:
        return ((-b + D ** 0.5) / (2 * a)), ((-b - D ** 0.5) / (2 * a))
    elif D < 0:
        return None
    else:
        return -b / 2 * a


class QuadraticEquationTest(unittest.TestCase):
    def test_with_d_z(self):
        expected = (1, -6)
        actual = quadratic_equation(1, 5, -6)
        self.assertEqual(actual, expected)

    def test_with_zeroes(self):
        self.assertRaises(ValueError, quadratic_equation, 0, 0, 0)

    def test_with_d_p(self):
        expected = (1, -2.25)
        actual = quadratic_equation(4, 5, -9)
        self.assertEqual(actual, expected)

    def test_with_d_m(self):
        expected = None
        actual = quadratic_equation(4, 5, 9)
        self.assertEqual(actual, expected)