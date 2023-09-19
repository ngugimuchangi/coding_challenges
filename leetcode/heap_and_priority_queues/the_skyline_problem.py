"""
Leetcode 218: The Skyline Problem
https://leetcode.com/problems/the-skyline-problem/
Priority Queue and Sweep Line Problem
Approach:
    1. Create a list of events, each event is a tuple of (x, -height, right)
    2. Sort the events by x, then height, then right
    3. Create a heap, heap[0] is the current max height and heap[1] is the right boundary
    4. Iterate through the events, if the event is a left boundary,
       push the height and right boundary to the heap
    5. If the event is a right boundary, pop the right boundary from the heap
    6. If the current max height is different from the previous max height,
       append the current max height to the result
    7. Return the result
Analysis:
- Time Complexity: O(nlogn) - n is the number of buildings in the input
    - O(nlogn) for sorting the events
    - O(nlogn) for iterating through the events and pushing/popping from the heap
- Space Complexity: O(n) - n is the number of buildings in the input

"""

from typing import List
from heapq import heappush, heappop


def getSkyline(buildings: List[List[int]]) -> List[List[int]]:
    res, events = [], []
    heap = [(0, float('inf'))]

    for left, right, height in buildings:
        events.append((left, -height, right))
        events.append((right, 0, 0))
    events.sort()

    for pos, height, right in events:
        while heap[0][1] <= pos:
            heappop(heap)
        if height:
            heappush(heap, (height, right))
        if not res or res[-1][1] != -heap[0][0]:
            res.append([pos, -heap[0][0]])
    return res
