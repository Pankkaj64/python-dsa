import unittest

from valid_parentheses import is_valid


class TestValidParentheses(unittest.TestCase):

    def test_valid_cases(self):
        self.assertTrue(is_valid("()"))
        self.assertTrue(is_valid("()[]{}"))
        self.assertTrue(is_valid("{[]}"))
        self.assertTrue(is_valid("({[]})"))
        self.assertTrue(is_valid(""))

    def test_invalid_cases(self):
        self.assertFalse(is_valid("(]"))
        self.assertFalse(is_valid("([)]"))
        self.assertFalse(is_valid("("))
        self.assertFalse(is_valid("]"))
        self.assertFalse(is_valid("((("))
        self.assertFalse(is_valid("(()"))
        self.assertFalse(is_valid(")("))
        self.assertFalse(is_valid("{[}]"))


if __name__ == "__main__":
    unittest.main()