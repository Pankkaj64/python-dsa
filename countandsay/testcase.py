import unittest
from main import Solution


class TestCountAndSay(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_case_1(self):
        self.assertEqual(self.sol.countAndSay(1), "1")

    def test_case_2(self):
        self.assertEqual(self.sol.countAndSay(2), "11")

    def test_case_3(self):
        self.assertEqual(self.sol.countAndSay(3), "21")

    def test_case_4(self):
        self.assertEqual(self.sol.countAndSay(4), "1211")

    def test_case_5(self):
        self.assertEqual(self.sol.countAndSay(5), "111221")

    def test_case_6(self):
        self.assertEqual(self.sol.countAndSay(6), "312211")


if __name__ == "__main__":
    unittest.main()