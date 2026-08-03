import unittest
from combination_sum import Solution


class TestCombinationSum(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def normalize(self, ans):
        return sorted([sorted(x) for x in ans])

    def test_case_1(self):
        candidates = [2, 3, 6, 7]
        target = 7
        expected = [[2, 2, 3], [7]]
        self.assertEqual(
            self.normalize(self.sol.combinationSum(candidates, target)),
            self.normalize(expected)
        )

    def test_case_2(self):
        candidates = [2, 3, 5]
        target = 8
        expected = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        self.assertEqual(
            self.normalize(self.sol.combinationSum(candidates, target)),
            self.normalize(expected)
        )

    def test_case_3(self):
        candidates = [2]
        target = 1
        expected = []
        self.assertEqual(
            self.normalize(self.sol.combinationSum(candidates, target)),
            self.normalize(expected)
        )

    def test_case_4(self):
        candidates = [1]
        target = 2
        expected = [[1, 1]]
        self.assertEqual(
            self.normalize(self.sol.combinationSum(candidates, target)),
            self.normalize(expected)
        )

    def test_case_5(self):
        candidates = [8, 7, 4, 3]
        target = 11
        expected = [[3, 4, 4], [3, 8], [4, 7]]
        self.assertEqual(
            self.normalize(self.sol.combinationSum(candidates, target)),
            self.normalize(expected)
        )


if __name__ == "__main__":
    unittest.main()