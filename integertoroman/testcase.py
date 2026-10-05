import unittest

from main import int_to_roman


class TestIntegerToRoman(unittest.TestCase):

    def test_basic_numbers(self):
        self.assertEqual(int_to_roman(1), "I")
        self.assertEqual(int_to_roman(2), "II")
        self.assertEqual(int_to_roman(3), "III")

    def test_subtractive_notation(self):
        self.assertEqual(int_to_roman(4), "IV")
        self.assertEqual(int_to_roman(9), "IX")
        self.assertEqual(int_to_roman(40), "XL")
        self.assertEqual(int_to_roman(90), "XC")
        self.assertEqual(int_to_roman(400), "CD")
        self.assertEqual(int_to_roman(900), "CM")

    def test_general_numbers(self):
        self.assertEqual(int_to_roman(58), "LVIII")
        self.assertEqual(int_to_roman(1994), "MCMXCIV")
        self.assertEqual(int_to_roman(2024), "MMXXIV")
        self.assertEqual(int_to_roman(3999), "MMMCMXCIX")

    def test_invalid_numbers(self):
        with self.assertRaises(ValueError):
            int_to_roman(0)

        with self.assertRaises(ValueError):
            int_to_roman(-5)

        with self.assertRaises(ValueError):
            int_to_roman(4000)


if __name__ == "__main__":
    unittest.main()