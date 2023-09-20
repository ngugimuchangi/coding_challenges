"""
Leetcode 39: Combination Sum
https://leetcode.com/problems/combination-sum/
    
- Approach: Backtracking
    - Use a helper function to backtrack the possible combinations
    - The helper function takes in the index of the candidate to be considered
      and the current combination
    - For each candidate, we have 2 choices: either we use it or we don't
    - If we use it, we add it to the current combination and subtract it from
      the target. Then we recursively call the helper function with the same
      index and the new target
    - If we don't use it, we just call the helper function with the next index
      and the same target
    - We need to make sure that the target is non-negative and that the index
      is within the range of the candidates

- Analysis:
    - Time complexity: O(n^target) - n is the number of candidates
    - Space complexity: O(target)
"""
from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    res = []

    def backtrack(index, combination, target):

        if target == 0:
            res.append(combination.copy())
            return
        if target < 0 or index >= len(candidates):
            return

        candidate = candidates[index]
        next_target = target - candidate
        combination.append(candidate)
        backtrack(index, combination, next_target)
        combination.pop()
        backtrack(index + 1, combination, target)

    backtrack(0, [], target)
    return res


def combinationSumIterative(candidates: List[int], target: int) -> List[List[int]]:
    """ Iterative solution """
    res = []
    end = len(candidates)

    def backtrack(start, combination, target):

        if target == 0:
            res.append(combination)
            return
        if target < 0:
            return
        for i in range(start, end):
            candidate = candidates[i]
            if candidate <= target:
                next_target = target - candidate
                backtrack(i, combination + [candidate], next_target)

    backtrack(0, [], target)
    return res
