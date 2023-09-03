#!/usr/bin/env python3
"""
Leetcode 167: Two Sum II - Input array is sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
"""
from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:
    """
    - Time complexity: O(n)
    - Space complexity: O(1)
    - Approach:
        - Use 2 pointers
        - if left plus right is greater than target
          move the right pointer backwards (towards the left)
          to a lower value
        - if left plus right is less than target move the left
          pointer forwards to a higher value
    """
    l, r = 0, len(numbers) - 1
    while l < r:
        res = numbers[l] + numbers[r]
        if res > target:
            res -= 1
        elif res < target:
            l += 1
        else:
            return [l + 1, r + 1]
