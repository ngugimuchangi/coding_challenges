#!/usr/bin/env python3
"""
Leetcode 84. Largest Rectangle in Histogram
https://leetcode.com/problems/largest-rectangle-in-histogram/
"""
from typing import List


def largestRectangleArea(heights: List[int]) -> int:
    """
    - Stack problem
    - Time complexity: O(n) - n is the number of heights
    - Space complexity: O(n) - n is the number of heights - the stack can contain all the heights
    - Approach: Stack
        - Use a stack to store the indices of the heights and the heights
        - Elements in the stack are in ascending order - monotonically increasing stack
        - When encountering a height, pop from the stack while the top of the
          stack is greater than the current height and calculate the area - the width is the
          difference between the current index and the top of the stack and the height is the
          height of the top of the stack
        - Note that if top element at top of the stack is greater than the current height, the
          height at the top can no longer be extended to the right but the current height can
          be extended to the left upto the index of the top of the stack
        - Push the current index and height to the stack
        - Return the result
    """
    res = 0
    h_stack = []
    max_width = len(heights)

    for i, h in enumerate(heights):
        index = i
        while h_stack and h_stack[-1][1] > h:
            index, height = h_stack.pop()
            area = (i - index) * height
            res = max(res, area)
        h_stack.append((index, h))

    while h_stack:
        i, h = h_stack.pop()
        area = (max_width - i) * h
        res = max(res, area)

    return res
