"""
Leetcode 725: Split Linked List in Parts
https://leetcode.com/problems/split-linked-list-in-parts/
"""

from typing import Optional, List
from list_node import ListNode


def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
    """
    - Time complexity: O(n)
    - Space complexity: O(1)
    - Approach: Iterative
        - Find the length of the linked list
        - Calculate the base length and the remainder
            - remainder represents the number of lists
              that should have an extra node
        - Split the linked list into k parts
    """
    curr, length, res = head, 0, []

    while curr:
        length += 1
        curr = curr.next

    base_length, remainder = length // k, length % k
    curr = head
    for _ in range(k):
        res.append(curr)
        for i in range(1, base_length + (1 if remainder else 0)):
            if not curr:
                break
            curr = curr.next
        remainder -= (1 if remainder else 0)
        if curr:
            curr.next, curr = None, curr.next
    return res
