"""
Leetcode 2: Add Two Numbers
https://leetcode.com/problems/add-two-numbers/
"""

from typing import Optional
from list_node import ListNode


def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    Algorithm: 3 steps
        1. Compute sum and carry
        2. Create new node for sum
        3. Update pointers
    """
    carry = 0
    res = curr = ListNode()

    while l1 or l2 or carry:
        # computer sum and new carry
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        curr_sum = val1 + val2 + carry
        carry = curr_sum // 10

        # new node
        curr.next = ListNode(curr_sum % 10)

        # update pointers
        curr = curr.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return res.next
