"""
Leetcode: 11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/
"""
from typing import List


def maxArea(height: List[int]) -> int:
    """
    - Time complexity: O(n)
    - Space complexity: O(1)
    - Approach:
        - use two pointers
        - compare area between the two pointers and previous
            max area and store the maximum
        - adjust pointers based on height, the pointer with
            lowest height moves in respective direction
        - return max area
    """
    max_area = 0
    l, r = 0, len(height) - 1

    while l < r:
        area = min(height[l], height[r]) * (r - l)
        max_area = max(max_area, area)
        # move the pointer with the lowest height
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return max_area
