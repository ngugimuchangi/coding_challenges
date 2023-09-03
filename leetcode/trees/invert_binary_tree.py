#!/usr/bin/env python3
"""
Leetcode 226. Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/
"""
from typing import Optional
from tree_node import TreeNode


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    Swap left and right nodes pre-orderly
    Time complexity: O(n)
    Space complexity: O(log(n)) for balanced tree, O(n) for skewed tree
    Approach: DFS
        - Swap left and right nodes pre-orderly
    """
    if not root:
        return
    temp = root.left
    root.left = root.right
    root.right = temp

    invertTree(root.left)
    invertTree(root.right)
    return root
