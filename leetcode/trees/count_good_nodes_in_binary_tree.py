"""
Leetcode 1448: Count Good Nodes in Binary Tree
https://leetcode.com/problems/count-good-nodes-in-binary-tree
"""
from tree_node import TreeNode


def goodNodes(root: TreeNode) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    Algorithm: DFS
        - Keep track of the max value from root to current node
        - If current node value is greater than or equal to max value, increment count
        - Recursively call dfs on left and right children
    """

    def dfs(node: TreeNode, max_val: int):
        if not node:
            return 0
        count = 0 if node.val < max_val else 1
        max_val = max(max_val, node.val)
        count += dfs(node.left, max_val)
        count += dfs(node.right, max_val)
        return count
    return dfs(root, root.val)
