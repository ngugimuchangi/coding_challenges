#!/usr/bin/env python3
"""
Leetcode 224. Basic Calculator
https://leetcode.com/problems/basic-calculator/
"""


def calculate(s: str) -> int:
    """
    - Stack problem
    - Time: O(n) - n is the length of the string - linear traversal of the string
    - Space: O(n) - stack can grow upto n/2
    - Note that `solve` function is recursive and it returns the sum of the numbers
        in the current parenthesis and the index of the closing parenthesis
        - The use of index is to skip the characters in the current parenthesis
          and avoid increasing time and space complexity due to slicing. This keeps
          the time and space complexity linear.
    - Algorithm:
        - Iterate over the string
        - If the character is a digit, then keep adding it to the number
        - If the character is an operator, then add the number to the stack
          based on the previous operator
        - If the character is an opening parenthesis, then call the `solve` function
          recursively to get the sum of the numbers in the current parenthesis
        - If the character is a closing parenthesis, then return the sum of the
          numbers in the current parenthesis and the index of the closing parenthesis
        - At the end, add the last number to the stack based on the previous operator
        - Return the sum of the numbers in the stack

    """
    def solve(s, l, r):
        num_stack, op = [], '+'
        num = 0
        while l <= r:
            c = s[l]
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in '-+':
                num_stack.append(num if op == '+' else -num)
                num, op = 0, c
            elif c in '(':
                num, l = solve(s, l + 1, r)
            elif c == ')':
                num_stack.append(num if op == '+' else -num)
                return sum(num_stack), l
            l += 1

        num_stack.append(num if op == '+' else -num)
        return sum(num_stack)

    return solve(s, 0, len(s) - 1)
