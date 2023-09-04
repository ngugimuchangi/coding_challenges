#!/usr/bin/env python3
"""
Problem: Flipping the Matrix
https://www.hackerrank.com/challenges/flipping-the-matrix/problem
"""


def flippingMatrix(matrix):
    """
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    Approach:
        - We only need to look at the top left quadrant of the matrix
        - We can find the max of the 4 numbers that are symmetric to the
          current number
        - We can iterate through the top left quadrant and find the max
          of the 4 numbers
    """
    res = 0
    q_size = len(matrix) // 2

    for r in range(q_size):
        for c in range(q_size):
            num = matrix[r][c]
            t_right = matrix[r][q_size * 2 - c - 1]
            b_right = matrix[q_size * 2 - r - 1][q_size * 2 - c - 1]
            b_left = matrix[q_size * 2 - r - 1][c]
            res += max(num, t_right, b_right, b_left)
    return res
