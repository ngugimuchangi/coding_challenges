"""
Leetcode 78: Subsets
https://leetcode.com/problems/subsets/
- Approach: Backtracking
    - For each element, we have two choices: either we include it in the subset or we don't
    - We can use backtracking to generate all subsets
    - We can use a helper function to generate all subsets
    - The helper function takes in the start index, end index, and the current subset
    - The start index is the index of the element we are currently considering
    - The end index is the index of the last element in the array
    - The current subset is the subset we have generated so far
    - We append the current subset to the result
    - Then we iterate through the array starting from the start index
    - For each element, we call the helper function with the start index incremented by 1
    - The end index is the same
    - The current subset is the current subset plus the current element
    - This is the case where we include the current element in the subset
    - Then we backtrack by removing the current element from the subset
    - This is the case where we don't include the current element in the subset
    
- Analysis:
    - Time complexity: O(2^n) where n is the length of the array
    - Space complexity: O(n) - the maximum depth of the recursion stack is n
        - subset size is unaccounted for because it is a result
"""
from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    res = []

    def backtrack(start, end, subset):
        res.append(subset)
        for i in range(start, end):
            backtrack(i + 1, end, subset + [nums[i]])
    backtrack(0, len(nums), [])
    return res
