import unittest
from add import add


class TestAdd(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(add(1, 2, 3), 6)

    def test_negative_numbers(self):
        self.assertEqual(add(-1, -2, -3), -6)

    def test_mixed_numbers(self):
        self.assertEqual(add(-1, 2, 3), 4)

    def test_zero(self):
        self.assertEqual(add(0, 0, 0), 0)

    def test_float_numbers(self):
        self.assertEqual(add(1.5, 2.5, 3.0), 7.0)


if __name__ == "__main__":
    unittest.main()