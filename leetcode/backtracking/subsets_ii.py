"""
Leetcode 90: Subsets II
https://leetcode.com/problems/subsets-ii/
- Approach: Backtracking
    - Same approach as subsets I, but we need to account for duplicates
    - We can sort the array first
    - Then we can skip over duplicates
    - We can keep track of the previous element
    - If the current element is equal to the previous element, we skip it
    - Otherwise, we backtrack
- Analysis:
    - Time complexity: O(2^n) where n is the length of the array
    - Space complexity: O(n) - the maximum depth of the recursion stack is n
        - subset size is unaccounted for because it is a result
"""
from typing import List


def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()

    def backtrack(start, end, subset):
        res.append(subset)
        prev = float('inf')
        for i in range(start, end):
            if prev != nums[i]:
                backtrack(i + 1, end, subset + [nums[i]])
            prev = nums[i]
    backtrack(0, len(nums), [])
    return res
