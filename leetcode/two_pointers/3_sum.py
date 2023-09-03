#!/usr/bin/env python3
"""
Leetcode 15: 3Sum
https://leetcode.com/problems/3sum/description/
"""

from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    """
    Time complexity - O(n^2) - n is the number of elements in nums
        - O(nlogn) for sorting
        - O(n^2) for the nested while loop
    Space complexity - O(1)
    Approach: Two pointers
        - Sort the array
        - Use 3 pointers, i, l, r
        - Iterate through the array
        - For each element, use two pointers, l and r
        - If the sum of the three elements is greater than 0, move the right pointer
          to a lower value
        - If the sum of the three elements is less than 0, move the left pointer
          to a higher value
        - If the sum of the three elements is 0, append the three elements to the result
          and move the left pointer to a higher value
        - If the element is the same as the previous element, skip it
        - If the left pointer is greater than the right pointer, break
    """
    res = []
    l_idx = len(nums) - 1
    nums.sort()

    for i, n in enumerate(nums):
        if i > 0 and n == nums[i - 1]:
            continue

        l, r = i + 1, l_idx
        while l < r:
            curr_sum = n + nums[l] + nums[r]
            if curr_sum > 0:
                r -= 1
            elif curr_sum < 0:
                l += 1
            else:
                res.append([n, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return res
