"""
Leetcode 47: Permutations II
https://leetcode.com/problems/permutations-ii/
- Approach: Backtracking
    - Same approach as permutations I, but we need to account for duplicates
    - We can sort the array first
    - Then we can skip over duplicates
    - We can keep track of the previous element
    - If the current element is equal to the previous element, we skip it
    - We also keep track of the indices of the elements we have visited
    - If the current index is in the set of visited indices for the
      current element, we skip it
    - Otherwise, we backtrack

- Analysis:
    - Time complexity: O(n * n!)
        - there are n! permutations i.e nPr = n!/(n-r)! in this case n = r
        - Each level the branching factor is n - i where i is the current level, leading to n! leaves
        - The maximum depth of the tree is n, hence n * n!
    - Space complexity: O(n * n!)
        - the maximum depth of the recursion stack is n,
          but we also have n! permutations each of length n
"""
from collections import defaultdict
from typing import List


def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    res, visited, max_count = [], defaultdict(set), len(nums)
    nums.sort()

    def backtrack(permutation, count):
        if count == max_count:
            res.append(permutation)
            return
        prev = float('inf')
        for i, num in enumerate(nums):
            if i in visited[num] or prev == num:
                continue
            visited[num].add(i)
            backtrack(permutation + [num], count + 1)
            visited[num].remove(i)
            prev = num

    backtrack([], 0)
    return res
