#!/usr/bin/env python3
"""
Leetcode 98. Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/
"""

from typing import Optional
from tree_node import TreeNode


def isValidBST(root: Optional[TreeNode]) -> bool:
    """
    Time complexity: O(n)
    Space complexity: O(n) - worst case for skewed tree
    Approach: DFS
        - Check if the current node is within the min and max range
        - Recursively check if the left and right subtrees meet the above conditions
        - Note: The min and max range is updated for each node
            - If exploring left subtree, update max range to current node value - 1
            - If exploring right subtree, update min range to current node value + 1
    """
    left = right = root

    if not root:
        return False
    while left.left:
        left = left.left
    while right.right:
        right = right.right
    return is_bst(root, left.val, right.val)


def is_bst(root: Optional[TreeNode], min_val: int, max_val: int) -> bool:
    """
    Check if tree is bst by check min and max range for of values for a particular node
    """
    if not root:
        return True
    if root.val < min_val or root.val > max_val:
        return False
    return (is_bst(root.left, min_val, root.val - 1) and
            is_bst(root.right, root.val + 1, max_val))
