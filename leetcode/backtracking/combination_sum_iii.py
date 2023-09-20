"""
Leetcode 216: Combination Sum III
https://leetcode.com/problems/combination-sum-iii/
- Approach: Backtracking
    - Use a helper function to backtrack the possible combinations
    - The helper function takes in the index of the candidate to be considered
    and the current combination
    - For each candidate, we have 2 choices: either we use it or we don't
    - If we use it, we add it to the current combination and subtract it from
    the target. Then we recursively call the helper function with the next
    index and the new target, i.e. we don't consider the same candidate again
    - If we don't use it, we just call the helper function with the next index
- Analysis:
    - Time complexity: O(9^k) - k is the number of candidates
    - Space complexity: O(k)
"""
from typing import List


def combinationSum3(k: int, n: int) -> List[List[int]]:
    res = []
    candidates = [i for i in range(1, 10)]

    def backtrack(index, combination, target):
        if target == 0 and len(combination) == k:
            res.append(combination.copy())
            return
        if target < 0 or len(combination) > k or index >= len(candidates):
            return

        candidate = candidates[index]
        next_target = target - candidate
        combination.append(candidate)
        backtrack(index + 1, combination, next_target)
        combination.pop()
        backtrack(index + 1, combination, target)

    backtrack(0, [], n)
    return res


def combinationSum3Iterative(k: int, n: int) -> List[List[int]]:
    """ Iterative solution """
    res = []

    def backtrack(start, combination, target):
        if target == 0 and len(combination) == k:
            res.append(combination)
            return
        if target < 0 or len(combination) > k:
            return
        for candidate in range(start, 10):
            if candidate <= target:
                backtrack(candidate + 1, combination +
                          [candidate], target - candidate)

    backtrack(1, [], n)
    return res
