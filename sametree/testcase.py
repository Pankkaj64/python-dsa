import unittest

from main import TreeNode, is_same_tree


def build_tree(values):
    """
    Build a binary tree from a level-order list.
    Use None for missing nodes.
    """

    if not values:
        return None

    nodes = [
        TreeNode(v) if v is not None else None
        for v in values
    ]

    child = 1

    for i in range(len(values)):
        if nodes[i] is not None:
            if child < len(values):
                nodes[i].left = nodes[child]
                child += 1

            if child < len(values):
                nodes[i].right = nodes[child]
                child += 1

    return nodes[0]


class TestSameTree(unittest.TestCase):

    def test_same_tree(self):
        p = build_tree([1, 2, 3])
        q = build_tree([1, 2, 3])

        self.assertTrue(is_same_tree(p, q))

    def test_different_values(self):
        p = build_tree([1, 2])
        q = build_tree([1, 3])

        self.assertFalse(is_same_tree(p, q))

    def test_different_structure(self):
        p = build_tree([1, 2, None])
        q = build_tree([1, None, 2])

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


if __name__ == "__main__":
    unittest.main()