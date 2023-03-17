"""
There is a list of n numbers and two players who move alternately.

On each move, a player removes either the first or last number from the list,
and their score increases by that number.

Both players try to maximize their scores.

What is the maximum possible score for the first player when both players play optimally?

Input

The first input line contains an integer n: the size of the list.

The next line has n integers x1,x2,…,xn: the contents of the list.

Output

Print the maximum possible score for the first player.

Constraints
1≤n≤5000
−109≤xi≤109
Example

Input:
4
4 5 1 3

Output:
8
"""
from functools import lru_cache

if __name__ == '__main__':
    # Top-Down solution
    def fn(lo, hi):
        if lo > hi:
            return 0
        if lo == hi:
            return A[lo]
        if dp[lo][hi] is not None:
            return dp[lo][hi]
        left = A[lo] + min(fn(lo + 1, hi - 1), fn(lo + 2, hi))
        right = A[hi] + min(fn(lo + 1, hi - 1), fn(lo, hi - 2))
        dp[lo][hi] = max(left, right)
        return dp[lo][hi]
    n = int(input())
    A = list(map(int, input().split()))
    dp = [[None for i in range(n + 1)] for j in range(n + 1)]
    x = fn(0, n - 1)
    print(x)

    # Bottom-Up DP solution
    dp = [[0] * n for _ in range(n)]

    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if i == j:
                dp[i][j] = A[i]
            else:
                dp[i][j] = max(A[i] - dp[i + 1][j], A[j] - dp[i][j - 1])

    total = sum(A)
    print((total + dp[0][n - 1]) // 2)
