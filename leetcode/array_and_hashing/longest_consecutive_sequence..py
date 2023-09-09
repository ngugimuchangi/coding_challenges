"""
Leetcode 128: Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence/description/
"""

from typing import List


def longestConsecutive(self, nums: List[int]) -> int:
    """
    Time complexity: O(n) - n is the number of elements in nums
    Space complexity: O(n) - n is the number of elements in nums
    Approach: Hash table
        - Use a set to store the numbers
        - Iterate through the numbers
        - If the number - 1 is not in the set, it is the start of a sequence
        - Iterate through the numbers starting from the current number
        - If the number is in the set, increment the count
        - Otherwise, break
        - Update the longest sequence
    """
    lookup = set(nums)
    longest = 0

    for n in nums:
        if n - 1 not in lookup:
            count = 0
            while n + count in lookup:
                count += 1
            longest = max(longest, count)
    return longest
