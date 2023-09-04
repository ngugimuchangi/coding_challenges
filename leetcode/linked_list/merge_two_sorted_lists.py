#!/usr/bin/env python3
"""
Leetcode 21: Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/
"""

from typing import Optional
from list_node import ListNode


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    l1, l2 = list1, list2
    res = curr = ListNode()

    while l1 and l2:
        if l1.val < l2.val:
            curr.next, l1 = l1, l1.next
        else:
            curr.next, l2 = l2, l2.next
        curr = curr.next

    # edge case - if one list is empty
    if l1:
        curr.next = l1
    else:
        curr.next = l2

    return res.next
