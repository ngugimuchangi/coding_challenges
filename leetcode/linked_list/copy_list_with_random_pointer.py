"""
Leetcode 138: Copy List with Random Pointer
https://leetcode.com/problems/copy-list-with-random-pointer/
"""
from typing import Optional


class Node:
    # Definition for a Node.
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copyRandomList(head: 'Optional[Node]') -> 'Optional[Node]':
    """
    Time complexity: O(n)
    Space complexity: O(n)
    Algorithm: 2 passes
        - first pass: create a copy of each node and store it in a dictionary
        - second pass: set the next and random pointers of each node
    """
    node_lookup = {None: None}
    curr = head

    while curr:
        node_lookup[curr] = Node(curr.val)
        curr = curr.next
    curr = head

    while curr:
        copy = node_lookup[curr]
        copy.next = node_lookup[curr.next]
        copy.random = node_lookup[curr.random]
        curr = curr.next

    return node_lookup[head]
