#!/usr/bin/env python3
"""
Leetcode 141: Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/
"""

from typing import Optional
from list_node import ListNode


def hasCycle(head: Optional[ListNode]) -> bool:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    Algorithm: Floyd's Tortoise and Hare
    """
    if not head:
        return False
    slow, fast = head, head.next

    while fast and fast.next:
        if fast == slow:
            return True
        fast, slow = fast.next.next, slow.next
    return False
