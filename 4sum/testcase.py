import unittest

from main import four_sum


class TestFourSum(unittest.TestCase):

    def test_example1(self):
        nums = [1, 0, -1, 0, -2, 2]
        target = 0

        expected = sorted([
            [-2, -1, 1, 2],
            [-2, 0, 0, 2],
            [-1, 0, 0, 1]
        ])

        self.assertEqual(sorted(four_sum(nums, target)), expected)

    def test_example2(self):
        nums = [2, 2, 2, 2, 2]
        target = 8

        expected = [[2, 2, 2, 2]]

        self.assertEqual(four_sum(nums, target), expected)

    def test_empty(self):
        self.assertEqual(four_sum([], 0), [])

    def test_not_possible(self):
        nums = [1, 2, 3]
        self.assertEqual(four_sum(nums, 6), [])

    def test_negative_target(self):
        nums = [-3, -2, -1, 0, 0, 1, 2, 3]
        target = 0

        expected = sorted([
            [-3, -2, 2, 3],
            [-3, -1, 1, 3],
            [-3, 0, 0, 3],
            [-3, 0, 1, 2],
            [-2, -1, 0, 3],
            [-2, -1, 1, 2],
            [-2, 0, 0, 2],
            [-1, 0, 0, 1]
        ])

        self.assertEqual(sorted(four_sum(nums, target)), expected)


if __name__ == "__main__":
    unittest.main()