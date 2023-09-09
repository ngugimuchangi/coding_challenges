"""
Leetcode 347: Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/description/
"""
from collections import Counter
from typing import List


def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    """
    Time complexity: O(n)
        - Iteration over the array occurs linearly in the
        - original nums array and frequencies array
    Space complexity: O(n)
        - Maximum size allocated to frequencies array is n
    Approach: Bucket Sort
        - Get count of elements
        - Create a frequencies array whose indices reflect
        - maximum number of frequencies of an element === array length
          in the case where all elements are unique
        - maximum frequency of an element is n (array length) in the case
          where all elements are the same hence the array of size n + 1
        - Iterate over the original array and add the elements
          to the frequencies array
        - Iterate over the frequencies array in reverse adding
          values to result array until k is 0


    """
    res = []
    nums_count = Counter(nums)
    len_nums = len(nums)
    freq = [[] for _ in range(len_nums + 1)]

    for key, value in nums_count.items():
        freq[value].append(key)

    i = len_nums
    while i > 0 and k > 0:
        for num in freq[i]:
            res.append(num)
            k -= 1
        i -= 1
    return res
