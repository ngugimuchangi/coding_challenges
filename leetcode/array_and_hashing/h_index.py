"""
Leetcode 274: H-Index
https://leetcode.com/problems/h-index/
Approach: Counting Sort
    - Create an array of size max_citation + 1
    - Iterate through citations and increment the count at the index of the citation
    - Iterate through the count array from the end
        - If the current count is greater than the current index, return the index
    - Return 0 if no h-index is found
Analysis: Time: O(n) | Space: O(n) - n is the maximum citation count
"""
from typing import List


def hIndex(citations: List[int]) -> int:
    max_citation = max(citations)
    count = [0] * (max_citation + 1)

    for citation in citations:
        count[citation] += 1

    for i in range(max_citation, -1, -1):
        if i < max_citation:
            count[i] += count[i + 1]
        if count[i] >= i:
            return i
    return 0
