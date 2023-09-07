"""
Leetcode 92: Reverse Linked List II
https://leetcode.com/problems/reverse-linked-list-ii/
"""

from typing import Optional
from list_node import ListNode


def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    """
    - Time complexity: O(n)
    - Space complexity: O(1)
    - Approach: Iterative
        - Find the left node and the node before the left node
        - Reverse the nodes between left and right
        - Connect the left node to the right node
    """
    dummy = ListNode(0, head)  # dummy node to handle edge case
    curr, prev_left = dummy, None
    right = right - left + 1

    while curr and left:
        prev_left, curr = curr, curr.next
        left -= 1

    l_node, prev = curr, None
    while curr and right:
        curr.next, prev, curr = prev, curr, curr.next
        right -= 1

    prev_left.next, l_node.next = prev, curr
    return dummy.next
