#!/usr/bin/env python3
"""
Leetcode 143: Reorder List
https://leetcode.com/problems/reorder-list/
"""
from typing import Optional
from list_node import ListNode


def reorderList(head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    Time complexity: O(n)
    Space complexity: O(1)
    Algorithm: 3 steps
        1. Find the middle of the list
        2. Reverse the second half of the list
        3. Merge the two lists
    """
    slow, fast, prev = head, head.next, None

    while fast and fast.next:
        slow, fast = slow.next, fast.next.next,

    second, slow.next = slow.next, None
    while second:
        second.next, prev, second = prev, second, second.next

    first, second = head, prev
    while first and second:
        first.next, second.next, first, second = second, first.next, first.next, second.next

    return head
