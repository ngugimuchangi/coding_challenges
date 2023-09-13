"""
Leetcode 215: Kth Largest Element in an Array
Link: https://leetcode.com/problems/kth-largest-element-in-an-array/
"""
from typing import List
from heapq import heapify, heapreplace


def findKthLargest(nums: List[int], k: int) -> int:
    """
    Time complexity: O(nlogk)
    Space complexity: O(k)
    Approach: Min heap
        - We can use a min heap to keep track of the k largest elements
        - We can initialize the min heap with the first k elements
        - We can then iterate over the remaining elements and if the
          current element is greater than the root of the min heap, then
          we can replace the root with the current element
        - After iterating over all the elements, the root of the min heap
          will be the kth largest element
    """
    heap = nums[:k]
    heapify(heap)
    for num in nums[k:]:
        if num > heap[0]:
            heapreplace(heap, num)
    return heap[0]


def findKthLargestTwo(nums: List[int], k: int) -> int:
    """
    Time complexity: O(n) in average case, O(n^2) in worst case
    Space complexity: O(1)
    Approach: Quick select
        - The idea is to use the partition function from quick sort
        - We can use either Lomuto's partition or Hoare's partition
        - We can also use three way partition
        - The idea is to find the index of the pivot after partitioning
        - If the index of the pivot is greater than k, then we need to
          partition the left subarray
        - If the index of the pivot is less than k, then we need to
          partition the right subarray
        - If the index of the pivot is equal to k, then we have found
          the kth largest element
    """
    k = len(nums) - k

    def quick_select(l, r):
        pivot = nums[r]
        p = l
        for i in range(l, r):
            if nums[i] <= pivot:
                nums[i], nums[p] = nums[p], nums[i]
                p += 1

        nums[r], nums[p] = nums[p], nums[r]
        if p > k:
            return quick_select(l, p - 1)
        elif p < k:
            return quick_select(p + 1, r)
        else:
            return nums[p]

    return quick_select(0, len(nums) - 1)
