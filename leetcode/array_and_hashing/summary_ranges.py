"""
Leetcode 228: Summary Ranges
https://leetcode.com/problems/summary-ranges/
"""
from typing import List


def summaryRanges(nums: List[int]) -> List[str]:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    Approach:
        1. Use two pointers to keep track of the start and end of the range
        2. If the next number is not the next number in the range, append the range to the result
        3. Update the start pointer to the next number
    """
    lookup, res = set(nums), []
    l = 0
    for r in range(len(nums)):
        if nums[r] + 1 not in lookup:
            num_range = f'{nums[l]}->{nums[r]}' if r - l else f'{nums[r]}'
            res.append(num_range)
            l = r + 1
    return res
