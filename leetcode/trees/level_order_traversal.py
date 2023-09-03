#!/usr/bin/env python3
"""
Leetcode 102. Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/
"""
from typing import List, Optional
from collections import deque
from tree_node import TreeNode


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Level order traversal of tree
    Time complexity: O(n)
    Space complexity: O(log(n))
    Approach:
        - Uses a queue
        - Add element to a queue
        - Retrieve all elements of a specific level from the queue
        - Clear queue
        - Add children of all retrieved elements to the queue
        - Add the vals of retrieved element to an array of values
        - Append the arr of level values to the result array
        - Repeat until there are no more elements to add to the queue i.e. queue is empty
    """
    nodes_queue = deque([root]) if root else deque([])
    res = []
    while (nodes_queue):
        nodes_arr = list(nodes_queue)
        vals_arr = []
        nodes_queue.clear()
        for node in nodes_arr:
            if node.left:
                nodes_queue.append(node.left)
            if node.right:
                nodes_queue.append(node.right)
            vals_arr.append(node.val)
        res.append(vals_arr)
    return res
