#!/usr/bin/env python3
"""
Leetcode 217: Contains Duplicate
https://leetcode.com/problems/contains-duplicate/description/
"""

from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    Approach: Hash table
        - Use a set to store the unique numbers
        - Iterate through the numbers
        - If the number is in the set, return True
        - Otherwise, add the number to the set
        - Return False
    """
    unique_nums = set()

    for n in nums:
        if n in unique_nums:
            return True
        unique_nums.add(n)
    return False
