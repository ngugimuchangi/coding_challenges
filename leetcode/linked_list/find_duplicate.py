"""
Leetcode 287: Find the Duplicate Number
"""

from typing import List


def findDuplicate(nums: List[int]) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    Algorithm: Floyd's Tortoise and Hare
        - slow pointer moves 1 step at a time
        - fast pointer moves 2 steps at a time
        - when slow and fast pointers meet, reset slow pointer to the beginning
        - move slow and fast pointers 1 step at a time until they meet again
        - the node at which they meet is the duplicate number i.e the start of the cycle
    """
    slow, fast = 0, 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow
