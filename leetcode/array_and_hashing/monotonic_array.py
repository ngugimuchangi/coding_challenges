from typing import List
"""
Leetcode 896: Monotonic Array
https://leetcode.com/problems/monotonic-array/
Approach: One pass
    - Iterate through the array and check if the direction
      is increasing or decreasing
    - If the direction is 0, then we don't know the direction
      yet, so we set the direction
    - If the direction is 1, then we check if the current
      element is less than the previous element
    - If the direction is -1, then we check if the current
      element is greater than the previous element
Analysis: Time: O(n) | Space: O(1)
"""


def isMonotonic(nums: List[int]) -> bool:
    if len(nums) < 2:
        return True

    direction = 0
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            if direction == 0:
                direction = 1
            elif direction == -1:
                return False
        elif nums[i] > nums[i - 1]:
            if direction == 0:
                direction = -1
            elif direction == 1:
                return False

    return True


def isMonotonicAlt(nums: List[int]) -> bool:
    """
    Suboptimal solution using stacks
    - We use two stacks, one for ascending and one for descending
    - We iterate through the array and check if the current element
      is less than the top of the ascending stack or greater than
      the top of the descending stack
    - If it is, then we pop the stack until we find the correct place
        to insert the element
    - We check if the length of the ascending stack is equal to the length of the
        array or the length of the descending stack is equal to the length of the array
    """
    asc_stack, desc_stack = [], []
    for num in nums:
        while asc_stack and asc_stack[-1] > num:
            asc_stack.pop()
        while desc_stack and desc_stack[-1] < num:
            desc_stack.pop()
        asc_stack.append(num)
        desc_stack.append(num)

    return len(asc_stack) == len(nums) or len(desc_stack) == len(nums)
