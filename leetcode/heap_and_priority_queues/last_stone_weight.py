"""
Leetcode 1046: Last Stone Weight
https://leetcode.com/problems/last-stone-weight/
"""
from heapq import heapify, heappop, heappush
from typing import List


def lastStoneWeight(stones: List[int]) -> int:
    """
    Time: O(nlogn) - heapify is O(nlogn) and each heappop is O(logn)
    Space: O(n)
    Approach: Use a max heap to keep track of the largest stones.
        - Pop the two largest stones from the heap.
        - If the two stones are not equal, add the difference back to the heap.
    """
    stones = [-weight for weight in stones]
    heapify(stones)

    while len(stones) > 1:
        first = heappop(stones)
        second = heappop(stones)
        if second > first:
            heappush(stones, first - second)
    stones.append(0)
    return abs(stones[0])
