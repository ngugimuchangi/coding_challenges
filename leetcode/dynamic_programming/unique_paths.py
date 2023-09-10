"""
Leetcode 62: Unique Paths
https://leetcode.com/problems/unique-paths/
"""


def uniquePaths(m: int, n: int) -> int:
    """
    - Dynamic programming problem
    - Time complexity: O(n.m) - n is the number of rows and m is the number of columns
    - Space complexity: O(n.m)
        - The space complexity of the memoization table is O(n.m)
    - Approach: Dynamic programming - Memoization
        - Use a dictionary to store the number of unique paths to reach a cell
        - The key is the cell and the value is the number of unique paths
        - The number of unique paths to reach a cell is the sum of the number of unique paths
            to reach the cell above and the cell to the left
        - Base cases:
            - If m or n is 0, there are no unique paths
            - If m or n is 1, there is only one unique path i.e. a 1 x 1 grid has only one unique path
    """
    def solution(m: int, n: int, memo):
        key = f'{m}, {n}'
        if key in memo:
            return memo[key]

        if not m or not n:
            return 0
        if m == 1 and n == 1:
            return 1
        memo[key] = solution(m - 1, n, memo) + solution(m, n - 1, memo)
        return memo[key]
    return solution(m, n, {})


def uniquePathsTabulation(m: int, n: int) -> int:
    """
    - Dynamic programming problem
    - Time complexity: O(n.m) - n is the number of rows and m is the number of columns
    - Space complexity: O(n.m)
    - Approach: Dynamic programming - Tabulation
        - Use a table to store the number of unique paths to reach a cell
        - Add the number of unique paths to reach the cell above and the cell to the left
        - Base case:
            - If m or n is 1, there is only one unique path i.e. a 1 x 1 grid has only one unique path
        - Return the number of unique paths to reach the bottom right cell
    """
    table = [[0] * (n + 1) for _ in range(m + 1)]
    table[1][1] = 1

    for r in range(m + 1):
        for c in range(n + 1):
            if r < m:
                table[r + 1][c] += table[r][c]
            if c < n:
                table[r][c + 1] += table[r][c]
    return table[m][n]
