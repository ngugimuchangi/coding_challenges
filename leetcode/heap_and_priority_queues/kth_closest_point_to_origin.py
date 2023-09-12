"""
Leetcode 973: K Closest Points to Origin
https://leetcode.com/problems/k-closest-points-to-origin/
"""
from typing import List
from math import sqrt, pow
from heapq import heapify, heappop, nsmallest


def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    """
    Time: O(klogn)
    Space: O(k)
    Approach: Use a min heap to keep track of the k closest points.
        - Use nsmallest to get the k closest points.
    """
    def get_distance(coordinates: List[List[int]]):
        """
        - Get the distance of a point from the origin.
        """
        x, y = coordinates
        return sqrt(pow(x, 2) + pow(y, 2))
    return nsmallest(k, points, key=get_distance)


def kClosestTwo(points: List[List[int]], k: int) -> List[List[int]]:
    """
    - Detailed approach
    - Time: O(klogn)
    - Space: O(n)
    - Approach: Use a min heap to keep track of the k closest points.
        - Push all points onto the heap.
        - Pop k times from the heap.
    """
    res, min_heap = [], []
    for x, y in points:
        distance = sqrt(pow(x, 2) + pow(y, 2))
        min_heap.append([distance, x, y])
    heapify(min_heap)

    while k:
        _, x, y = heappop(min_heap)
        res.append([x, y])
        k -= 1
    return res
