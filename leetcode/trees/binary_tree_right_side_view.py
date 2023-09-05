"""
Leetcode 199: Binary Tree Right Side View
https://leetcode.com/problems/binary-tree-right-side-view/
"""

from collections import deque
from tree_node import TreeNode
from typing import List, Optional


def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    Algorithm: BFS
        - Traverse the tree level by level
        - For each level, add the last node to the result
    """
    q = deque([root]) if root else deque()
    res = []

    while q:
        visible = q[-1]
        res.append(visible.val)
        for _ in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return res
