#!/usr/bin/env python3
"""
LeetCode: 225. Implement Stack using Queues
https://leetcode.com/problems/implement-stack-using-queues/
"""

from collections import deque


class MyStack:

    def __init__(self):
        self.__stack = deque()
        self.__size = 0

    def push(self, x: int) -> None:
        self.__stack.appendleft(x)
        self.__size += 1

    def pop(self) -> int:
        if self.__size > 0:
            self.__size -= 1
            return self.__stack.popleft()

    def top(self) -> int:
        if self.__size > 0:
            return self.__stack[0]

    def empty(self) -> bool:
        return not self.__size
