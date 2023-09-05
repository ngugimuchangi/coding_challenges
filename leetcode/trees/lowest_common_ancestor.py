"""
Leetcode 235: Lowest Common Ancestor of a Binary Search Tree
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
"""

from tree_node import TreeNode


def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    Algorithm: Iterative
        - Traverse the tree until we find a node that is between p and q
        - If the current node is greater than both p and q, then we know
          that the LCA is in the left subtree
        - If the current node is less than both p and q, then we know that
          the LCA is in the right subtree
        - If the current node is not greater than p and q and not less than p and q,
          then we know that the current node is the LCA
    """
    curr = root

    while curr:
        if p.val < curr.val and q.val < curr.val:
            curr = curr.left
        elif p.val > curr.val and q.val > curr.val:
            curr = curr.right
        else:
            return curr
