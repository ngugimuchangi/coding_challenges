#!/usr/bin/env python3
"""
Leetcode 155. Min Stack
https://leetcode.com/problems/min-stack/
"""
from collections import deque


class MinStack:
    """
    - Stack problem
    - Time complexity: O(1) - all operations are constant time
    - Space complexity: O(n) - n is the number of elements in the stack
    - Approach: Stack
        - Use two stacks, one for the actual stack and one for the minimum
        - When pushing, push the value to the actual stack and the minimum
          of the value and the top of the minimum stack to the minimum stack
        - When popping, pop from both stacks
        - When getting the minimum, return the top of the minimum stack
    """

    def __init__(self):
        self.__stack = deque()
        self.__min_stack = deque()

    def push(self, val: int) -> None:
        self.__stack.append(val)
        min_val = min(val, self.__min_stack[-1] if self.__min_stack else val)
        self.__min_stack.append(min_val)

    def pop(self) -> None:
        self.__min_stack.pop()
        return self.__stack.pop()

    def top(self) -> int:
        return self.__stack[-1]

    def getMin(self) -> int:
        return self.__min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
