"""
Given an a×b rectangle, your task is to cut it into squares.
On each move you can select a rectangle and cut it into two rectangles in such a way that all side lengths remain integers.

What is the minimum possible number of moves?

Input

The only input line has two integers a and b.

Output

Print one integer: the minimum number of moves.

Constraints
1≤a,b≤500
Example

Input:
3 5

Output:
3

"""

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    inf = float('inf')
    dp = [[inf] * (m + 1) for _ in range(n + 1)]

    for j in range(m + 1):
        dp[0][j] = 0
    for i in range(n + 1):
        dp[i][0] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == j:
                dp[i][j] = 0
            else:
                min_steps = inf
                for k in range(1, i):
                    a, b = i - k, i - (i - k)
                    min_steps = min(min_steps, dp[a][j] + dp[b][j] + 1)
                for k in range(1, j):
                    a, b = j - k, j - (j - k)
                    min_steps = min(min_steps, dp[i][a] + dp[i][b] + 1)
                dp[i][j] = min_steps

    print(dp[n][m])
