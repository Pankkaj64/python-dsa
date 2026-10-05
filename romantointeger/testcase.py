import unittest

from main import roman_to_int


class TestRomanToInteger(unittest.TestCase):

    def test_basic_numerals(self):
        self.assertEqual(roman_to_int("I"), 1)
        self.assertEqual(roman_to_int("III"), 3)
        self.assertEqual(roman_to_int("V"), 5)
        self.assertEqual(roman_to_int("M"), 1000)

    def test_subtractive_notation(self):
        self.assertEqual(roman_to_int("IV"), 4)
        self.assertEqual(roman_to_int("IX"), 9)
        self.assertEqual(roman_to_int("XL"), 40)
        self.assertEqual(roman_to_int("XC"), 90)
        self.assertEqual(roman_to_int("CD"), 400)
        self.assertEqual(roman_to_int("CM"), 900)

    def test_general_numerals(self):
        self.assertEqual(roman_to_int("LVIII"), 58)
        self.assertEqual(roman_to_int("MCMXCIV"), 1994)
        self.assertEqual(roman_to_int("MMXXIV"), 2024)
        self.assertEqual(roman_to_int("MMMCMXCIX"), 3999)

    def test_invalid_numerals(self):
        with self.assertRaises(ValueError):
            roman_to_int("")

        with self.assertRaises(ValueError):
            roman_to_int("ABC")

        with self.assertRaises(ValueError):
            roman_to_int("iv")


if __name__ == "__main__":
    unittest.main()
