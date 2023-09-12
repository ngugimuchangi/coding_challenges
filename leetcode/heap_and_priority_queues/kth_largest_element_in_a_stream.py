"""
Leetcode 703: Kth Largest Element in a Stream
https://leetcode.com/problems/kth-largest-element-in-a-stream/
"""

from heapq import heapify, heappush, heappop
from typing import List


class KthLargest:
    """
    Time: O(nlogk) - initialization of heap is O(nlogk) and add is O(logk)
    Space: O(k)
    """

    def __init__(self, k: int, nums: List[int]):
        """Initialize the heap with the first k elements"""
        self.min_heap = nums
        self.k = k
        heapify(nums)
        for i in range(len(nums) - k):
            heappop(self.min_heap)

    def add(self, val: int) -> int:
        """
        - Add a new element to the heap.
        - If the heap is full, pop the smallest element.
        - Return the root of the heap.
        """
        heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heappop(self.min_heap)
        return self.min_heap[0]
