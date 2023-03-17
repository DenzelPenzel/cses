"""
Your task is to build a tower whose width is 2 and height is n. You have an unlimited supply of blocks whose width and height are integers.

For example, here are some possible solutions for n=6:

Given n, how many different towers can you build? Mirrored and rotated towers are counted separately if they look different.

Input

The first input line contains an integer t: the number of tests.

After this, there are t lines, and each line contains an integer n: the height of the tower.

Output

For each test, print the number of towers modulo 109+7.

Constraints
1≤t≤100
1≤n≤106
Example

Input:
3
2
6
1337

Output:
8
2864
640403945
"""

if __name__ == '__main__':
    def fn(n: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[0] * 8 for _ in range(n)]

        for j in range(8):
            dp[0][j] = 1

        for i in range(1, n):
            for num in range(8):
                if num in [0, 2, 3, 4, 5]:
                    dp[i][num] = dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][3] + dp[i - 1][4] + dp[i - 1][5]
                else:
                    dp[i][num] = dp[i - 1][2] + dp[i - 1][6] + dp[i - 1][7]
                dp[i][num] %= mod

        return (dp[n - 1][3] + dp[n - 1][7]) % mod


    n = int(input())
    A = []
    for _ in range(n):
        A.append(int(input()))

    for x in A:
        print(fn(x))
