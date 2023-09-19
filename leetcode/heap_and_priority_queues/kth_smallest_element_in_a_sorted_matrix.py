"""
Leetcode 378: Kth Smallest Element in a Sorted Matrix
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
Approach: Max Heap
    - We can use a max heap to keep track of the k smallest elements
    - We can iterate through the matrix and add each element to the heap
    - If the heap size is greater than k, we can pop the largest element
    - At the end, we can return the largest element in the heap
Analysis:
    - Time Complexity: O(n(log(k)))
    - Space Complexity: O(k)
"""

from typing import List
from heapq import heappush, heappushpop


def kthSmallest(matrix: List[List[int]], k: int) -> int:
    """ Finds the kth smallest element in a sorted matrix """
    min_heap = []
    for row in matrix:
        for num in row:
            if len(min_heap) < k:
                heappush(min_heap, -num)
            else:
                heappushpop(min_heap, -num)
    return -min_heap[0]
