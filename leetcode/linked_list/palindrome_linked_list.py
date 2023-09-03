#!/usr/bin/env python
"""
Leetcode 234. Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/

"""
from typing import Optional
from list_node import ListNode


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        Check if linked list is palindrome
        Time complexity: O(n)
        Space complexity: O(1)
        Approach: Reverse half of linked list
         - Use Floyd's tortoise and hare algorithm to get mid points
         - Reverse the second half of the linked list
         - Compare the first half and the second half

        """
        slow, fast, prev = head, head, None

        # Get mid points
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        # Reverse half of linked list and adjust pointers
        while (slow):
            slow.next, prev, slow = prev, slow, slow.next

        # Check if list is palindrome with two pointers
        slow, fast = head, prev
        while fast:
            if slow.val != fast.val:
                return False
            slow, fast = slow.next, fast.next
        return True
