"""
Leetcode 295: Find Median from Data Stream
https://leetcode.com/problems/find-median-from-data-stream/
Analysis:
1. addNum
- Time complexity: O(log(n))
    - n is the number of elements in the data stream
    - O(log(n)) is the time complexity of heappush and heappop
- Space complexity: O(n)
    - n is the number of elements in the data stream
    - O(n) is the space complexity of the heaps 
2. findMedian
- Time complexity: O(1)
"""

from heapq import heappush, heappop, heappushpop


class MedianFinder:
    """
    MedianFinder class that allows users to add numbers to a data stream
    and find the median of the data stream.
    """

    def __init__(self):
        """ Instantiate a MedianFinder object """
        self.small_vals = []  # max heap of smaller values
        self.large_vals = []  # min heap of larger values

    def addNum(self, num: int) -> None:
        """ Add new number to data stream """
        largest_left = heappushpop(self.small_vals, -num)
        heappush(self.large_vals, -largest_left)

        if len(self.small_vals) < len(self.large_vals):
            smallest_right = heappop(self.large_vals)
            heappush(self.small_vals, -smallest_right)

    def findMedian(self) -> float:
        """ Find median of data stream """
        if len(self.small_vals) > len(self.large_vals):
            return -self.small_vals[0]
        return (-self.small_vals[0] + self.large_vals[0]) / 2
