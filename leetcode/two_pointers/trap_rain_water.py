"""
Leetcode: 42. Trapping Rain Water
https://leetcode.com/problems/trapping-rain-water/
"""

from typing import List


def trap(height: List[int]) -> int:
    """
    Time complexity: O(n) - linear time to go through each boundary
    Space complexity: O(1) - same list
    Approach:
        - Move through list of boundaries from the start going forwards and from the back in reverse
        - Determine the maximum boundary. Not that the boundaries at indices 0 and length - 1 cannot
          hold any water on their own since they are at the edge, and require other boundaries
        - Move the pointer with the lowest boundary 
        - Determine the new maximum bound, either left or right depending on the pointer moved
        - Calculate the units of water that can be help at that poisition by deducting the boundary
          height from the respective maximum height
        - Add the water units to the previous water units
    """
    if not height:
        return 0
    water_units = 0
    # max left and right boundaries
    max_left, max_right = height[0], height[-1]
    # left and right boundaries pointer
    l, r = 0, len(height) - 1

    while l < r:
        # adjust position of the pointer with the lower boundary
        if max_left < max_right:
            l += 1
            max_left = max(max_left, height[l])
            water_units += max_left - height[l]
        else:
            r -= 1
            max_right = max(max_right, height[r])
            water_units += max_right - height[r]

    return water_units


def trapTwo(height: List[int]) -> int:
    """
    Time complexity: O(n) - linear time to go through each boundary
    Space complexity: O(n) - additional list of max heights
    Approach: 
        - Create a list of maximum heights from the left
        - Iterate through the list of heights from the right
        - Determine the maximum boundary. Not that the boundaries at indices 0 and length - 1 cannot
          hold any water on their own since they are at the edge, and require other boundaries
        - Also compute the maximum boundary from the right
        - Calculate the units of water that can be help at that position by deducting the boundary
          height from the respective maximum height
        - Add the water units to the previous water units
    - This can also be done with a monotonically decreasing deque, but will take more space
    """
    len_height, max_heights = len(height), []
    max_h = water_units = 0

    for i, h in enumerate(height):
        max_heights.append(max_h)
        max_h = max(max_h, h)

    max_h = 0
    for i in range(len_height - 1, -1, -1):
        h = height[i]
        units = min(max_heights[i], max_h) - h
        water_units = water_units + units if units > 0 else water_units + 0
        max_h = max(max_h, h)

    return water_units
