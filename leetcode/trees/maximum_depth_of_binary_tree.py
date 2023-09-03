#!/usr/bin/env python3
from typing import Optional
from tree_node import TreeNode


def maxDepth(root: Optional[TreeNode]) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(n) - worst case for skewed tree
    Approach: DFS
        - Recursively find the maximum depth of the left and right subtrees
        - Return the maximum depth of the current node
    """
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))
