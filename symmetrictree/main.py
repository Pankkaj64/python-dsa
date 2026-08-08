from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_symmetric(root: Optional[TreeNode]) -> bool:
    """
    Returns True if the binary tree is symmetric.
    """

    if root is None:
        return True

    def is_mirror(left, right):
        # Both nodes are empty
        if left is None and right is None:
            return True

        # Only one node is empty
        if left is None or right is None:
            return False

        # Values must be equal
        if left.val != right.val:
            return False

        # Compare opposite sides
        return (
            is_mirror(left.left, right.right)
            and is_mirror(left.right, right.left)
        )

    return is_mirror(root.left, root.right)