"""
Leetcode 118: Pascal's Triangle
https://leetcode.com/problems/pascals-triangle/
"""
from typing import List


def generate(numRows: int) -> List[List[int]]:
    n = numRows
    pascal_triangle = []
    for row in range(n):
        new_row = []
        for col in range(row + 1):
            if col == 0 or col == row:
                new_row.append(1)
            else:
                new_row.append(prev_row[col - 1] + prev_row[col])
        prev_row = new_row
        pascal_triangle.append(new_row)
    return pascal_triangle
