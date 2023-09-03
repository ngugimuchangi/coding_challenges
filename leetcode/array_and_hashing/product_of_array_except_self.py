#!/usr/bin/env python3
"""
Leetcode 238: Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/description/
"""

from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    """
    Time complexity: O(n)

    Space complexity: O(1) - considering answer array
    doesn't account for extra space

    Approach: Prefix and postfix products
    - Prefix and suffix can be computed in their own arrays but
      would lead to O(n) space complexity. If the answer memory doesn't
      account for time complexity, we can use it for all operations:
    - computing the prefixes first by iterating over nums array forwards, then
    - multiplying prefixes with postfixes by iterating over the nums array in reverse

    """
    answer = [1] * len(nums)
    prefix = 1
    postfix = 1

    # compute prefixes and store them in answer array
    for i in range(len(nums)):
        answer[i] = prefix
        prefix *= nums[i]

    # compute postfix and multiply it by prefix in answer array
    for i in range(len(nums) - 1, -1, -1):
        answer[i] *= postfix
        postfix *= nums[i]

    return answer
