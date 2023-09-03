#!/usr/bin/env python3
"""
Leetcode 543. Diameter of Binary Tree
https://leetcode.com/problems/diameter-of-binary-tree/
"""

from typing import Optional
from tree_node import TreeNode


def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    Approach: DFS
        - Recursively find the height of the left and right subtrees
        - Update the diameter if the sum of the heights of the left and right subtrees
          is greater than the current diameter
        - Note the diameter is the number of edges between the two farthest nodes
          and we add two to the sum of the heights of the left and right subtrees
          to account for the edges between current node and its left and right subtrees
        - Return the height of the current node

    """
    res = 0

    def dfs(root):
        nonlocal res
        if not root:
            return -1
        l = dfs(root.left)
        r = dfs(root.right)
        res = max(res, l + r + 2)
        return 1 + max(l, r)

    dfs(root)
    return res
