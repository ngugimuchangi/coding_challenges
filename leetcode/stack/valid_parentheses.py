#!/usr/bin/env python3
"""
Leetcode 20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/
"""


def isValid(s: str) -> bool:
    """
    - Stack problem
    - Time complexity: O(n) - n is the length of the string
    - Space complexity: O(1) - constant space
    - Approach: Stack
        - If the current character is a closing bracket,
        check if the top of the stack is the corresponding
        opening bracket
        - If not, return False
        - If stack is empty, return True else False
    """
    b_stack = []
    b_pairs = {'}': '{', ')': '(', ']': '['}

    for c in s:
        if c == '(' or c == '{' or c == '[':
            b_stack.append(c)
        elif b_stack and b_pairs[c] == b_stack[-1]:
            b_stack.pop()
        else:
            return False
    return not b_stack
