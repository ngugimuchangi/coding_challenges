#!/usr/bin/env python3
from typing import Optional
from list_node import ListNode


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverse linked list
    Time complexity: O(n)
    Space complexity: O(1)
    Approach: Iterative
        - Use three pointers to reverse the linked list
        - prev, curr, next / temp
        - prev = None, curr = head
        - while curr:
            - next = curr.next
            - curr.next = prev
            - prev = curr
            - curr = next
        - head = prev
        - return head
    """
    curr, prev = head, None
    while curr:
        curr.next, prev, curr, = prev, curr, curr.next
    head = prev
    return head


def reverseListRecursive(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Time complexity: O(n) - linear traversal of linked list
    Space complexity 0(n) - stack grows linear with size of linked list
    Approach:
        - Reverse the direction of each next pointer to point to the previous value
        - Base case: if head is None, return None
        - Recursive case:
            - new_head = reverseList(head.next)
            - head.next.next = head - reverse the direction of the next pointer of
              the next node to point to the current node
            - head.next = None - set the next pointer to None - this is the new tail
            - return new_head
    """
    if not head:
        return None
    new_head = head
    if head.next:
        new_head = reverseList(head.next)
        head.next.next = head
    head.next = None
    return new_head
