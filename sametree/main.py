from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    # If both nodes are None, trees are identical up to this point
    if p is None and q is None:
        return True

    # If one node is None and the other isn't
    if p is None or q is None:
        return False

    # If values don't match
    if p.val != q.val:
        return False

    # Recursively compare left and right subtrees
    return (
        is_same_tree(p.left, q.left)
        and is_same_tree(p.right, q.right)
    )