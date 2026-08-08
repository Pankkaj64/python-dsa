import unittest

from symmetric_tree import TreeNode, is_symmetric


def build_tree(values):
    """
    Build a binary tree from a level-order list.

    None represents a missing node.

    Example:
        [1, 2, 2, 3, 4, 4, 3]

              1
             / \
            2   2
           / \ / \
          3  4 4  3
    """

    if not values:
        return None

    nodes = [
        TreeNode(value) if value is not None else None
        for value in values
    ]

    for i in range(len(nodes)):
        if nodes[i] is not None:
            left = 2 * i + 1
            right = 2 * i + 2

            if left < len(nodes):
                nodes[i].left = nodes[left]

            if right < len(nodes):
                nodes[i].right = nodes[right]

    return nodes[0]


class TestSymmetricTree(unittest.TestCase):

    def test_symmetric_tree(self):
        root = build_tree([1, 2, 2, 3, 4, 4, 3])

        self.assertTrue(is_symmetric(root))

    def test_not_symmetric(self):
        root = build_tree([1, 2, 2, None, 3, None, 3])

        self.assertFalse(is_symmetric(root))

    def test_single_node(self):
        root = build_tree([1])

        self.assertTrue(is_symmetric(root))

    def test_empty_tree(self):
        root = build_tree([])

        self.assertTrue(is_symmetric(root))

    def test_two_equal_children(self):
        root = build_tree([1, 2, 2])

        self.assertTrue(is_symmetric(root))

    def test_two_different_children(self):
        root = build_tree([1, 2, 3])

        self.assertFalse(is_symmetric(root))

    def test_complex_symmetric_tree(self):
        root = build_tree([
            1,
            2, 2,
            3, 4, 4, 3,
            5, 6, 7, 8, 8, 7, 6, 5
        ])

        self.assertTrue(is_symmetric(root))


if __name__ == "__main__":
    unittest.main()