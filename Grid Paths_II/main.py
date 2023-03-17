"""
Consider an n×n grid whose squares may have traps. It is not allowed to move to a square with a trap.

Your task is to calculate the number of paths from the upper-left square to the lower-right square.

You can only move right or down.

Input
    The first input line has an integer n: the size of the grid.
    After this, there are n lines that describe the grid. Each line has n characters: . denotes an empty cell, and * denotes a trap.

Output
    Print the number of paths modulo 10^9+7.

Constraints
    1≤n≤1000

Example
    Input:
    4
    ....
    .*..
    ...*
    *...

Output: 3
"""

if __name__ == '__main__':
    n = int(input())
    A = [input() for _ in range(n)]

    if A[0][0] == '*':
        print(0)
        exit()

    dp = [[0] * n for _ in range(n)]
    mod = 10**9 + 7
    dp[0][0] = 0 if A[0][0] == 1 else 1

    for i in range(1, n):
        dp[0][i] = 0 if A[0][i] == '*' else dp[0][i - 1]

    for i in range(1, n):
        dp[i][0] = 0 if A[i][0] == '*' else dp[i - 1][0]

    for i in range(1, n):
        for j in range(1, n):
            if A[i][j] == '*':
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % mod

    print(dp[n - 1][n - 1] % mod)
