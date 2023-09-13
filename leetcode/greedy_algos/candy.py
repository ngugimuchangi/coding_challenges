"""
Leetcode 135: Candy
https://leetcode.com/problems/candy/
"""
from typing import List


def candy(ratings: List[int]) -> int:
    """
    - Greedy algorithm
    - Time complexity: O(n)
        - n is the number of elements in ratings
    - Space complexity: O(n)
    - Algorithm: Two passes
        - First pass: Give each child 1 candy
            - If the child to the left has a higher rating, give the child
              1 more candy than the child to the left
        - Second pass: Give each child 1 more candy than the child to the right if the
          child to the right has a higher rating
    """
    candies = [1] * len(ratings)
    for i in range(1, len(ratings)):

        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    for i in range(len(ratings) - 2, -1, -1):
        if ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
            candies[i] += (candies[i + 1] - candies[i] + 1)
    return sum(candies)
