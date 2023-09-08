"""
Leetcode 2385: Amount of Time for Binary Tree to be Deleted
https://leetcode.com/discuss/interview-question/1002813/Amazon-or-OA-2021-or-Amount-of-Time-for-Binary-Tree-to-be-Deleted
"""

from collections import defaultdict, deque
from tree_node import TreeNode
from typing import Optional


def amountOfTime(root: Optional[TreeNode], start: int) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    Approach:
        1. Build a graph from the tree
        2. Perform BFS from the start node
    """
    burned, graph, time = set(), defaultdict(list), 0
    queue = deque([(root, None)])

    while queue:
        node, parent = queue.popleft()
        if parent:
            graph[parent.val].append(node.val)
            graph[node.val].append(parent.val)
        if node.left:
            queue.append((node.left, node))
        if node.right:
            queue.append((node.right, node))

    burned.add(start)
    queue.append(start)
    while queue:
        for _ in range(len(queue)):
            u = queue.popleft()
            for v in graph[u]:
                if v not in burned:
                    burned.add(v)
                    queue.append(v)
        time += 1

    return time - 1
