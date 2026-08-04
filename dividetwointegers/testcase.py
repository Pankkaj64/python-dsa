import unittest

from divide_two_integers import divide


class TestDivideTwoIntegers(unittest.TestCase):

    def test_positive_division(self):
        self.assertEqual(divide(10, 3), 3)

    def test_negative_result(self):
        self.assertEqual(divide(7, -3), -2)

    def test_both_negative(self):
        self.assertEqual(divide(-15, -3), 5)

    def test_dividend_zero(self):
        self.assertEqual(divide(0, 5), 0)

    def test_divisor_one(self):
        self.assertEqual(divide(25, 1), 25)

    def test_divisor_minus_one(self):
        self.assertEqual(divide(25, -1), -25)

    def test_overflow(self):
        self.assertEqual(divide(-2**31, -1), 2**31 - 1)

    def test_large_negative(self):
        self.assertEqual(divide(-2**31, 1), -2**31)

    def test_divisor_larger(self):
        self.assertEqual(divide(3, 5), 0)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)


if __name__ == "__main__":
    unittest.main()