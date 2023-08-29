#!/usr/bin/env python3
"""
Leetcode 227. Basic Calculator II
https://leetcode.com/problems/basic-calculator-ii/
"""


def calculate(s: str) -> int:
    """
    - Stack problem
    - Time complexity: O(n) - n is the length of the string
    - Space complexity: O(n) - n is the length of the string
    - Approach: Stack
        - Use a stack to store the numbers
        - When encountering an operator, perform the operation with the top of
          the stack and the current number
        - Note that the current number is not pushed to the stack until the
          next operator is encountered
        - If the operator is + or -, push the number to the stack with the
          appropriate sign
        - If the operator is * or /, pop the top of the stack, perform the
        - Push the result back to the stack
        - Return the sum of the stack
    """

    op_stack, num, op, length = [], 0, '+', len(s)
    for i, c in enumerate(s):
        if c.isdigit():
            num = num * 10 + int(c)
        if (not c.isspace() and not c.isdigit()) or i == length - 1:
            if op == '+':
                op_stack.append(num)
            elif op == '-':
                op_stack.append(-num)
            elif op == '*':
                op_stack.append(op_stack.pop() * num)
            else:
                op_stack.append(int(op_stack.pop() / num))
            op, num = c, 0
    print(op_stack)
    return sum(op_stack)
