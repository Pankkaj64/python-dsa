import unittest
from hcf import hcf


class TestHCF(unittest.TestCase):

    def test_common_numbers(self):
        self.assertEqual(hcf(12, 18), 6)

    def test_prime_numbers(self):
        self.assertEqual(hcf(13, 17), 1)

    def test_same_numbers(self):
        self.assertEqual(hcf(20, 20), 20)

    def test_one_zero(self):
        self.assertEqual(hcf(0, 15), 15)

    def test_both_zero(self):
        self.assertEqual(hcf(0, 0), 0)

    def test_negative_numbers(self):
        self.assertEqual(hcf(-12, 18), 6)

    def test_large_numbers(self):
        self.assertEqual(hcf(100, 80), 20)


if __name__ == "__main__":
    unittest.main()