import unittest

from same_tree import TreeNode, is_same_tree


def build_tree(values):
    """
    Builds a binary tree from a level-order list.
    Example:
    [1,2,3] =>
          1
         / \
        2   3
    """

    if not values:
        return None

    nodes = [TreeNode(v) if v is not None else None for v in values]

    for i in range(len(values)):
        if nodes[i] is not None:
            left = 2 * i + 1
            right = 2 * i + 2

            if left < len(values):
                nodes[i].left = nodes[left]

            if right < len(values):
                nodes[i].right = nodes[right]

    return nodes[0]


class TestSameTree(unittest.TestCase):

    def test_example1(self):
        p = build_tree([1, 2, 3])
        q = build_tree([1, 2, 3])

        self.assertTrue(is_same_tree(p, q))

    def test_example2(self):
        p = build_tree([1, 2])
        q = build_tree([1, None, 2])

        self.assertFalse(is_same_tree(p, q))

    def test_example3(self):
        p = build_tree([1, 2, 1])
        q = build_tree([1, 1, 2])

        self.assertFalse(is_same_tree(p, q))

    def test_both_empty(self):
        self.assertTrue(is_same_tree(None, None))

    def test_one_empty(self):
        p = build_tree([1])

        self.assertFalse(is_same_tree(p, None))

    def test_large_same_tree(self):
        p = build_tree([5, 3, 8, 1, 4, 7, 9])
        q = build_tree([5, 3, 8, 1, 4, 7, 9])

        self.assertTrue(is_same_tree(p, q))

    def test_large_different_tree(self):
        p = build_tree([5, 3, 8, 1, 4, 7, 9])
        q = build_tree([5, 3, 8, 1, 6, 7, 9])

        self.assertFalse(is_same_tree(p, q))


if __name__ == "__main__":
    unittest.main()