"""
Leetcode 105: Construct Binary Tree from Preorder and Inorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""

from typing import List, Optional
from tree_node import TreeNode


def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    Algorithm:
        - The first element in preorder is the root of the tree
        - Find the root in inorder and split the inorder into left and right subtrees
        - The length of the left subtree is equal to the index of the root in inorder
          and the length of the right subtree is equal to the length of inorder minus
          the index of the root in inorder minus one
        - Recursively call buildTree on the left and right subtrees
    """
    if not preorder or not inorder:
        return None
    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    root.left = self.buildTree(preorder[1: mid + 1], inorder[:mid])
    root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
    return root
