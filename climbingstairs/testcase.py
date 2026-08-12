import unittest

from main import climb_stairs


class TestClimbingStairs(unittest.TestCase):

    def test_one_stair(self):
        self.assertEqual(climb_stairs(1), 1)

    def test_two_stairs(self):
        self.assertEqual(climb_stairs(2), 2)

    def test_three_stairs(self):
        self.assertEqual(climb_stairs(3), 3)

    def test_four_stairs(self):
        self.assertEqual(climb_stairs(4), 5)

    def test_five_stairs(self):
        self.assertEqual(climb_stairs(5), 8)

    def test_ten_stairs(self):
        self.assertEqual(climb_stairs(10), 89)


if __name__ == "__main__":
    unittest.main()