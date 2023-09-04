#!/usr/bin/env python3
"""
Leetcode 19: Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""

from typing import Optional
from list_node import ListNode


def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    Algorithm: 2 pointers
        - fast pointer moves n steps ahead of slow pointer
        - when fast pointer reaches the end, slow pointer is at the nth node from the end
        - keep track of the previous node of the slow pointer
        - remove the nth node from the end
    """
    fast, slow, prev = head, head, None

    for n in range(1, n):
        fast = fast.next

    while fast.next:
        fast, prev, slow = fast.next, slow, slow.next

    if prev:
        prev.next = slow.next
    else:
        head = slow.next
    slow = None
    return head
