"""
Leetcode 1: Two Sum
https://leetcode.com/problems/two-sum/description/
"""
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    Approach: Hash table
        - Use a dictionary to store the numbers and their indices
        - Iterate through the numbers
        - If the complement of the number is in the dictionary, return the
          indices
        - Otherwise, add the number to the dictionary
    """
    lookup = {}

    for i, n in enumerate(nums):
        c = target - n
        if c in lookup:
            return [lookup[c], i]
        lookup[n] = i
