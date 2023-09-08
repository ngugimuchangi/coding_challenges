"""
Leetcode 951: Flip Equivalent Binary Trees
https://leetcode.com/problems/flip-equivalent-binary-trees/
"""

from typing import Optional
from tree_node import TreeNode


def flipEquiv(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    """
    Check if two binary trees are flip equivalent
    Time complexity: O(n)
    Space complexity: O(n)
    Approach:
        1. If both trees are empty, return True
        2. If one of the trees is empty, return False
        3. If the values of the roots are different, return False
        4. Check if the trees are the same or flipped
    """
    if not root1 or not root2:
        return not root1 and not root2
    if root1.val != root2.val:
        return False
    same = flipEquiv(root1.left, root2.left) and flipEquiv(
        root1.right, root2.right)
    flipped = flipEquiv(root1.left, root2.right) and flipEquiv(
        root1.right, root2.left)
    return same or flipped
