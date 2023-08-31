#!/usr/bin/env python3
"""
Leetcode 74. Search a 2D Matrix
https://leetcode.com/problems/search-a-2d-matrix/
"""

from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    """
    - Binary search problem
    - Time: O(log(mn)) - m is the number of rows and n is the number of columns
    - Space: O(1)
    - Algorithm:
        - Search for the right row
        - Search for target in the row
    """

    m, n = len(matrix), len(matrix[0])
    t, b = 0, m - 1

    while t <= b:
        r = t + (b - t) // 2
        if target < matrix[r][0]:
            b = r - 1
        elif target > matrix[r][-1]:
            t = r + 1
        else:
            break

    s, e = 0, n - 1
    while s <= e:
        c = s + (e - s) // 2
        if target == matrix[r][c]:
            return True
        if target > matrix[r][c]:
            s = c + 1
        else:
            e = c - 1
    return False
