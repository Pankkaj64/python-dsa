import unittest
from median import find_median_sorted_arrays


class TestMedian(unittest.TestCase):

    def test_odd_length(self):
        self.assertEqual(find_median_sorted_arrays([1, 3], [2]), 2)

    def test_even_length(self):
        self.assertEqual(find_median_sorted_arrays([1, 2], [3, 4]), 2.5)

    def test_one_empty(self):
        self.assertEqual(find_median_sorted_arrays([], [1]), 1)

    def test_both_empty(self):
        with self.assertRaises(IndexError):
            find_median_sorted_arrays([], [])

    def test_duplicates(self):
        self.assertEqual(find_median_sorted_arrays([1, 2], [2, 3]), 2)

    def test_negative_numbers(self):
        self.assertEqual(find_median_sorted_arrays([-5, -3], [-2, -1]), -2.5)


if __name__ == "__main__":
    unittest.main()