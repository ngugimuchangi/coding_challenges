#!/usr/bin/env python3
"""
Leetcode 100. Same Tree
https://leetcode.com/problems/same-tree/
"""

from typing import Optional
from tree_node import TreeNode


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """
    Time complexity: O(n)
    Space complexity: O(n) - worst case for skewed tree
    Approach: DFS
        - Check if the values of the current nodes are equal or both nodes are None
        - Recursively check if the left and right subtrees meet the above conditions

    """
    if p and q:
        return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    return p is q
