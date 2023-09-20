"""
Leetcode 40: Combination Sum II
https://leetcode.com/problems/combination-sum-ii/
Approach: Backtracking
- Use a helper function to backtrack the possible combinations
- The helper function takes in the index of the candidate to be considered
  and the current combination
- For each candidate, we have 2 choices: either we use it or we don't
- If we use it, we add it to the current combination and subtract it from
  the target. Then we recursively call the helper function with the next
  index and the new target, i.e. we don't consider the same candidate again
- Due to the duplicates in the candidates, we need to skip the duplicates
  when we are considering the same candidate again
Analysis:
- Time complexity: O(2^n) - n is the number of candidates
- Space complexity: O(n)
"""
from typing import List


def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    """ Recursive solution """
    res = []
    candidates.sort()

    def backtrack(index, combination, target):
        if target == 0:
            res.append(combination.copy())
            return
        if target < 0 or index >= len(candidates):
            return

        candidate = candidates[index]

        next_target = target - candidate
        combination.append(candidate)
        backtrack(index + 1, combination, next_target)
        combination.pop()
        i = index + 1
        while i < len(candidates) and candidates[i] == candidates[index]:
            i += 1
        backtrack(i, combination, target)
    backtrack(0, [], target)
    return res


def combinationSum2Iterative(candidates: List[int], target: int) -> List[List[int]]:
    """ Iterative solution """
    res = []
    candidates.sort()

    def backtrack(index, combination, target):
        if target == 0:
            res.append(combination)
            return
        if target < 0 or index >= len(candidates):
            return
        prev = -1
        for i in range(index, len(candidates)):
            candidate = candidates[i]
            if candidate == prev:
                continue
            if candidate <= target:
                backtrack(i + 1, combination + [candidate], target - candidate)
            prev = candidate
    backtrack(0, [], target)
