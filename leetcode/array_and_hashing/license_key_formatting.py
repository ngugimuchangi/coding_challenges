"""
Leetcode 482: License Key Formatting
https://leetcode.com/problems/license-key-formatting/
Approach: Reverse iteration (preferred) or forward iteration
Analysis: Time: O(n) | Space: O(n)
"""
from collections import deque
from typing import List


def licenseKeyFormatting(s: str, k: int) -> str:
    res = deque()
    s = s.replace('-', '').upper()
    count = len(s) % k or k

    for char in s:
        if not count:
            res.append('-')
            count = k
        res.append(char)
        count -= 1

    return ''.join(res)


def licenseKeyFormattingReverseIteration(s: str, k: int) -> str:
    res = ''
    count = k

    for i in range(len(s) - 1, -1, -1):
        if s[i] == '-':
            continue
        if count == 0:
            res = '-' + res
            count = k
        res = s[i].upper() + res
        count -= 1
    return res
