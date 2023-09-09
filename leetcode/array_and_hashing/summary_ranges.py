"""
Leetcode 228: Summary Ranges
https://leetcode.com/problems/summary-ranges/
"""
from typing import List


def summaryRanges(nums: List[int]) -> List[str]:
    lookup, res = set(nums), []
    l = 0
    for r in range(len(nums)):
        if nums[r] + 1 not in lookup:
            num_range = f'{nums[l]}->{nums[r]}' if r - l else f'{nums[r]}'
            res.append(num_range)
            l = r + 1
    return res
