"""
Leetcode 124: Binary Tree Maximum Path Sum
https://leetcode.com/problems/binary-tree-maximum-path-sum/
"""

from typing import Optional
from tree_node import TreeNode


def maxPathSum(root: Optional[TreeNode]) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    Algorithm: DFS
        - At each node, we calculate the maximum path sum that goes through the node
        - We update the max_sum if the current path sum is greater than the max_sum
        - We return the maximum path sum that goes through the node
    """
    max_sum = float('-inf')

    def dfs(root):
        nonlocal max_sum
        if not root:
            return 0
        left = dfs(root.left)
        right = dfs(root.right)
        path_sum = root.val + left + right
        child_sum = root.val + max(left, right)
        max_sum = max(max_sum, root.val, path_sum, child_sum)
        return max(root.val, child_sum)
    dfs(root)
    return max_sum
