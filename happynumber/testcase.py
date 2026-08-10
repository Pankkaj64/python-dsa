import unittest

from main import is_happy


class TestHappyNumber(unittest.TestCase):

    def test_happy_number(self):
        self.assertTrue(is_happy(19))
        self.assertTrue(is_happy(1))
        self.assertTrue(is_happy(7))
        self.assertTrue(is_happy(10))

    def test_unhappy_number(self):
        self.assertFalse(is_happy(2))
        self.assertFalse(is_happy(3))
        self.assertFalse(is_happy(4))
        self.assertFalse(is_happy(20))

    def test_large_happy_number(self):
        self.assertTrue(is_happy(100))

    def test_single_digit_numbers(self):
        self.assertTrue(is_happy(1))
        self.assertFalse(is_happy(2))
        self.assertFalse(is_happy(3))
        self.assertFalse(is_happy(4))
        self.assertFalse(is_happy(5))
        self.assertFalse(is_happy(6))
        self.assertTrue(is_happy(7))
        self.assertFalse(is_happy(8))
        self.assertFalse(is_happy(9))


if __name__ == "__main__":
    unittest.main()