#!/usr/bin/env python3
"""
Leetcode 22. Generate Parentheses
https://leetcode.com/problems/generate-parentheses/
"""
from typing import List


def generateParenthesis(n: int) -> List[str]:
    """
    - Backtracking and stack problem
    - Time complexity: O(2 ^ n) - there are two choices for each position
      either '(' or ')', leading to exponential time complexity
      in the recursive tree
    - Space complexity: O(n) - the depth of the recursive tree is n and the
        stack space is proportional to the depth of the recursive tree
    - Approach: Backtracking
        - Use a stack to store the parentheses
        - Use a recursive function to backtrack
        - Base case: when the number of opened and closed parentheses is equal
        - Recursive case:
            - If the number of opened parentheses is less than n, append '('
                to the stack and recurse
            - If the number of closed parentheses is less than the number of
                opened parentheses, append ')' to the stack and recurse
        - Pop from the stack after each recursive call
        - When the base case is reached, append the stack to the result
        - Return the result
    """
    stack = []
    res = []

    def backtrack(opened, closed):
        if opened == closed == n:
            res.append(''.join(stack))
            return
        if opened < n:
            stack.append('(')
            backtrack(opened + 1, closed)
            stack.pop()
        if closed < opened:
            stack.append(')')
            backtrack(opened, closed + 1)
            stack.pop()
    backtrack(0, 0)
    return res
