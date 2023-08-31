#!/usr/bin/env python3

"""
Leetcode 69. Sqrt(x)
https://leetcode.com/problems/sqrtx/
"""


def mySqrt(x: int) -> int:
    """
    - Binary search problem
    - Time: O(log(n)) - n is the number of elements in the search space == x // 2
    - Space: O(1)
    - Algorithm:
        - Initialize l and r to 0 and x // 2
        - While l <= r:
            - Calculate mid
            - If mid * mid == x, then return mid - perfect square
            - If mid * mid < x, then move to the right half of the search space
              and update the answer to mid
            - If mid * mid > x, then move to the left half of the search space
    """
    l, r = 0, x // 2
    if x < 2:
        return x

    while l <= r:
        mid = (r + l) // 2
        if mid * mid == x:
            return mid
        if mid * mid < x:
            l = mid + 1
            ans = mid
        else:
            r = mid - 1
    return ans
