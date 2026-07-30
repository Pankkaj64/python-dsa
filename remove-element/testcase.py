import unittest

from main import remove_element


class TestRemoveElement(unittest.TestCase):

    def test_example1(self):
        nums = [3, 2, 2, 3]
        k = remove_element(nums, 3)

        self.assertEqual(k, 2)
        self.assertEqual(sorted(nums[:k]), [2, 2])

    def test_example2(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        k = remove_element(nums, 2)

        self.assertEqual(k, 5)
        self.assertEqual(sorted(nums[:k]), [0, 0, 1, 3, 4])

    def test_no_occurrence(self):
        nums = [1, 2, 3]
        k = remove_element(nums, 4)

        self.assertEqual(k, 3)
        self.assertEqual(nums[:k], [1, 2, 3])

    def test_all_occurrences(self):
        nums = [5, 5, 5]
        k = remove_element(nums, 5)

        self.assertEqual(k, 0)

    def test_empty_array(self):
        nums = []
        k = remove_element(nums, 1)

        self.assertEqual(k, 0)


if __name__ == "__main__":
    unittest.main()