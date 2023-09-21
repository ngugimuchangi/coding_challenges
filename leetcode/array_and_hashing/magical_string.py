"""
Leetcode 481: Magical String
https://leetcode.com/problems/magical-string/
- The magic string is a self descriptive string
  like the Kolakoski sequence
- Approach: Iterative
    - Use an array to store the string
    - Add the first 3 numbers to the array
    - Use a variable to keep track of the previous number, which starts at 2
    - Iterate from 2 to n
        - Add 1 if the previous number is 2, otherwise add 2, to the array
          string[i] times, i is the current index
        - Update the count if the number is 1
        - Update the previous number
- Analysis:
    - Time: O(n) - n is the length of the string
    - Space: O(n) - n is the length of the string
"""


def magicalString(n: int) -> int:
    string, prev, count = [1, 2, 2], 2, 1

    for i in range(2, n):
        string.extend([1 if prev == 2 else 2] * string[i])
        count += (1 if string[i] == 1 else 0)
        prev = 1 if prev == 2 else 2
    return count
