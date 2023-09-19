"""
Leetcode 480: Sliding Window Median
https://leetcode.com/problems/sliding-window-median/
Time: O(nlogk) - n is the length of nums, k is the size of the window
Space: O(n) - n is the length of nums
Algorithm: Sliding Window, Two Heaps
- Use two heaps to store the numbers in the window
- Use a hash map to store the numbers that are out of the window
- Use a balance variable to keep track of the balance of the two heaps
- When the window moves, we need to:
    - remove the number that is out of the window
    - add the new number to the heap
    - balance the two heaps
    - get the median of the current window
- The balance variable is used to determine which heap to pop and push
- The hash map is used to keep track of the numbers that are out of the window
"""

from collections import defaultdict
from heapq import heappush, heappop, heappushpop
from typing import List


def medianSlidingWindow(nums: List[int], k: int) -> List[float]:
    """ Get the median of each window of size k """
    res, max_heap, min_heap = [], [], []
    past_window = defaultdict(int)

    for r in range(0, k):
        # add the first k numbers to the heaps
        n = nums[r]
        heappush(min_heap, -heappushpop(max_heap, -n))
        if len(min_heap) > len(max_heap):
            heappush(max_heap, -heappop(min_heap))

    median = get_median(max_heap, min_heap, k)
    res.append(median)

    for r in range(k, len(nums)):
        n, past_n = nums[r], nums[r - k]
        past_window[past_n] += 1

        # balance = -1 if the out of window number is the in the max heap
        # balance = 1 if the out of window number is the in the min heap
        balance = -1 if past_n <= median else 1
        if n <= median:
            heappush(max_heap, -n)
            balance += 1
        else:
            heappush(min_heap, n)
            balance -= 1

        # balance = 0 if the two heaps are balanced, i.e. we removed a number
        # from and added a number back to the same heap
        if balance < 0:
            heappush(max_heap, -heappop(min_heap))
        elif balance > 0:
            heappush(min_heap, -heappop(max_heap))

        while max_heap and past_window[-max_heap[0]]:
            past_window[-max_heap[0]] -= 1
            heappop(max_heap)
        while min_heap and past_window[min_heap[0]]:
            past_window[min_heap[0]] -= 1
            heappop(min_heap)

        median = get_median(max_heap, min_heap, k)
        res.append(median)
    return res


def get_median(max_heap, min_heap, k) -> float:
    """ Get median of the current window """
    if k & 1:
        return -max_heap[0]
    return (-max_heap[0] + min_heap[0]) / 2
