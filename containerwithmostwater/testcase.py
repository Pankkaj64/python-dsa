import unittest
from main import max_area


class TestContainerWithMostWater(unittest.TestCase):

    def test_example_case(self):
        self.assertEqual(max_area([1,8,6,2,5,4,8,3,7]), 49)

    def test_two_elements(self):
        self.assertEqual(max_area([1,1]), 1)

    def test_increasing_heights(self):
        self.assertEqual(max_area([1,2,3,4,5]), 6)

    def test_decreasing_heights(self):
        self.assertEqual(max_area([5,4,3,2,1]), 6)

    def test_same_heights(self):
        self.assertEqual(max_area([4,4,4,4]), 12)

    def test_single_peak(self):
        self.assertEqual(max_area([1,2,10,2,1]), 4)

    def test_large_edges(self):
        self.assertEqual(max_area([10,1,1,1,10]), 40)

    def test_alternating_heights(self):
        self.assertEqual(max_area([1,3,2,5,25,24,5]), 24)

    def test_empty_array(self):
        self.assertEqual(max_area([]), 0)

    def test_single_element(self):
        self.assertEqual(max_area([5]), 0)


if __name__ == "__main__":
    unittest.main()