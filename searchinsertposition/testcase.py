import unittest

from search_insert_position import search_insert


class TestSearchInsertPosition(unittest.TestCase):

    def test_target_exists(self):
        nums = [1, 3, 5, 6]
        self.assertEqual(search_insert(nums, 5), 2)

    def test_insert_middle(self):
        nums = [1, 3, 5, 6]
        self.assertEqual(search_insert(nums, 2), 1)

    def test_insert_end(self):
        nums = [1, 3, 5, 6]
        self.assertEqual(search_insert(nums, 7), 4)

    def test_insert_beginning(self):
        nums = [1, 3, 5, 6]
        self.assertEqual(search_insert(nums, 0), 0)

    def test_single_element_found(self):
        nums = [1]
        self.assertEqual(search_insert(nums, 1), 0)

    def test_single_element_not_found(self):
        nums = [1]
        self.assertEqual(search_insert(nums, 2), 1)

    def test_empty_array(self):
        nums = []
        self.assertEqual(search_insert(nums, 5), 0)


if __name__ == "__main__":
    unittest.main()