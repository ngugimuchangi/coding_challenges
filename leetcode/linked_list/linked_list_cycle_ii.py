""""
LeeCode: 142. Linked List Cycle II
leetcode.com/problems/linked-list-cycle-ii/
"""

from typing import Optional
from list_node import ListNode


def detectCycle(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    Algorithm: Floyd's Tortoise and Hare
        - find if there is a cycle in the list
        - find start of cycle
    """
    slow = fast = head

    if not head:
        return None

    # find if there is a cycle in the list
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if fast == slow:
            break

    # no cycle found
    if not fast or not fast.next:
        return None

    # find start of cycle
    slow = head
    while slow != fast:
        slow, fast = slow.next, fast.next

    return slow
