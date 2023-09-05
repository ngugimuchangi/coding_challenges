"""
Leetcode 25: Reverse Nodes in k-Group
https://leetcode.com/problems/reverse-nodes-in-k-group/
"""

from typing import Optional
from list_node import ListNode


def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    Algorithm: Iterative reverse
        - find kth node
        - reverse current group upto kth node
        - link previous group to kth node
        - link 1st node of current group to next group
        - repeat until there is no more group
    """
    res = ListNode(0, head)
    prev_group = res

    while True:
        kth = self.find_kth(prev_group, k)
        if not kth:
            break
        next_group = kth.next
        prev, curr = kth.next, prev_group.next

        while curr != next_group:
            curr.next, prev, curr = prev, curr, curr.next

        prev_group.next, prev_group = kth, prev_group.next

    return res.next


def find_kth(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """
    Find kth node
    """
    curr = head
    while curr and k:
        curr = curr.next
        k -= 1
    return curr
