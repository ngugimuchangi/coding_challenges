"""
Leetcode 230: Kth Smallest Element in a BST
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
"""

from typing import Optional
from tree_node import TreeNode


def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(h) - h is the height of the tree
        - maximum call stack is equal to the height of the tree (height of root)
    Algorithm: DFS
        - Inorder traversal of a BST is sorted
        - Traverse the tree in inorder and decrement k
        - If k is equal to zero then return the current node value
    """
    def inorder(root):
        nonlocal k
        if not root:
            return 0

        l_val = inorder(root.left)
        k -= 1

        if l_val:
            return l_val
        if k == 0:
            return root.val

        r_val = inorder(root.right)
        return r_val or 0

    return inorder(root)
