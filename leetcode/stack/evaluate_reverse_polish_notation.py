#!/usr/bin/env python3
"""
Leetcode 150. Evaluate Reverse Polish Notation
https://leetcode.com/problems/evaluate-reverse-polish-notation/
"""


def evalRPN(self, tokens: list[str]) -> int:
    """
    - Stack problem
    - Time complexity: O(n) - n is the number of tokens
    - Space complexity: O(n) - n is the number of tokens
    - Approach: Stack
        - Use a stack to store the numbers
        - When encountering an operator, pop two numbers from the stack and
          perform the operation
        - Push the result back to the stack
        - Return the top of the stack
    """
    t_stack = []

    for t in tokens:
        if t not in ('+-*/'):
            t_stack.append(int(t))
        else:
            num_1 = t_stack.pop()
            num_2 = t_stack.pop()
            if t == '+':
                res = num_2 + num_1
            if t == '-':
                res = num_2 - num_1
            if t == '*':
                res = int(num_2 * num_1)
            if t == '/':
                res = int(num_2 / num_1)
            t_stack.append(res)
    res = t_stack.pop()
    return res
