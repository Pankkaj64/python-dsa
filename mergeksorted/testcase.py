import unittest

from merge_k_sorted_lists import ListNode, merge_k_lists


def build_linked_list(values):
    dummy = ListNode(0)
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def linked_list_to_list(head):
    result = []

    while head:
        result.append(head.val)
        head = head.next

    return result


class TestMergeKSortedLists(unittest.TestCase):

    def test_example1(self):
        lists = [
            build_linked_list([1, 4, 5]),
            build_linked_list([1, 3, 4]),
            build_linked_list([2, 6])
        ]

        result = merge_k_lists(lists)

        self.assertEqual(
            linked_list_to_list(result),
            [1, 1, 2, 3, 4, 4, 5, 6]
        )

    def test_empty_lists(self):
        self.assertIsNone(merge_k_lists([]))

    def test_all_empty(self):
        lists = [None, None]
        self.assertIsNone(merge_k_lists(lists))

    def test_single_list(self):
        lists = [build_linked_list([1, 2, 3])]
        result = merge_k_lists(lists)

        self.assertEqual(
            linked_list_to_list(result),
            [1, 2, 3]
        )

    def test_duplicates(self):
        lists = [
            build_linked_list([1, 1, 1]),
            build_linked_list([1, 1]),
            build_linked_list([1])
        ]

        result = merge_k_lists(lists)

        self.assertEqual(
            linked_list_to_list(result),
            [1, 1, 1, 1, 1, 1]
        )


if __name__ == "__main__":
    unittest.main()