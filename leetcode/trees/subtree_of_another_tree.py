#!/usr/bin/env python3
"""
Leetcode 572. Subtree of Another Tree
https://leetcode.com/problems/subtree-of-another-tree/
"""
from typing import Optional
from tree_node import TreeNode


def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    """
    Recursively establish whether a given tree is a subtree of another tree
    Time complexity: O(n * m)
        - n is the number of nodes in main tree
        - m is the number of nodes in subtree
    Space complexity: O(n * m)
    """
    if not root or not subRoot:
        return False
    if is_same(root, subRoot):
        return True
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)


def is_same(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """
    Find similarity between two nodes
    """
    if p and q:
        return p.val == q.val and is_same(p.left, q.left) and is_same(p.right, q.right)
    return p is q
