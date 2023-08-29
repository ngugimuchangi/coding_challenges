#!/usr/bin/env python3
"""
Leetcode 739. Daily Temperatures
https://leetcode.com/problems/daily-temperatures/
"""
from typing import List


def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    """
    - Stack problem
    - Time complexity: O(n) - n is the number of temperatures
    - Space complexity: O(n) - n is the number of temperatures
    - Approach: Stack
        - Use a stack to store the indices of the temperatures
        - Elements in the stack are in descending order - monotonically decreasing stack
        - When encountering a temperature, pop from the stack while the top of
          the stack is less than the current temperature
        - The difference between the current index and the top of the stack is
          the number of days until a warmer temperature
        - Push the current index to the stack
        - Return the result
    """
    t_stack = []
    res = [0] * len(temperatures)

    for i in range(len(temperatures)):
        t = temperatures[i]
        while t_stack and temperatures[t_stack[-1]] < t:
            res[t_stack[-1]] = i - t_stack[-1]
            t_stack.pop()
        t_stack.append(i)
    return res
