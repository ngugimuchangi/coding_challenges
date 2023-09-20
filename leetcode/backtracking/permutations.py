"""
Leetcode 46: Permutations
https://leetcode.com/problems/permutations/
- Approach: Backtracking
    - We can use backtracking to generate all permutations
    - We can use a helper function to generate all permutations
    - The helper function takes in the current permutation and the current count
    - The current permutation is the permutation we have generated so far
    - The current count is the number of elements in the current permutation
    - If the current count is equal to the length of the array, we append the current permutation to the result
    - Otherwise, we iterate through the array
    - For each element, we check if it is in the current permutation
    - If it is, we skip it
    - Otherwise, we add it to the current permutation
    - Then we call the helper function with the current permutation and the current count incremented by 1
    - Then we backtrack by removing the current element from the current permutation
Analysis:
        - Time complexity: O(n * n!)
        - there are n! permutations i.e nPr = n!/(n-r)! in this case n = r
        - Each level the branching factor is n - i where i is the current level, leading to n! leaves
        - The maximum depth of the tree is n, hence n * n!
    - Space complexity: O(n * n!)
        - the maximum depth of the recursion stack is n,
          but we also have n! permutations each of length 
"""

from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    res, visited, max_count = [], set(), len(nums)

    def backtrack(permutation, count):
        if count == max_count:
            res.append(permutation)
            return
        for num in nums:
            if num in visited:
                continue
            visited.add(num)
            backtrack(permutation + [num], count + 1)
            visited.remove(num)
    backtrack([], 0)
    return res
