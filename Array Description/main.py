"""
You know that an array has n integers between 1 and m, and the absolute difference between two adjacent values is at most 1.

Given a description of the array where some values may be unknown, your task is to count the number of arrays that match the description.

Input

The first input line has two integers n and m: the array size and the upper bound for each value.

The next line has n integers x1,x2,…,xn: the contents of the array. Value 0 denotes an unknown value.

Output

Print one integer: the number of arrays modulo 109+7.

Constraints
1≤n≤105
1≤m≤100
0≤xi≤m
Example

Input:
3 5
2 0 2

Output:
3

Explanation: The arrays [2,1,2], [2,2,2] and [2,3,2] match the description.




"""

if __name__ == '__main__':
    n, limit = list(map(int, input().split()))
    A = list(map(int, input().split()))
    mod = 10 ** 9 + 7
    dp = {}
    if A[0] == 0:
        for k in range(1, limit + 1):
            dp[(0, k)] = 1
    else:
        dp[(0, A[0])] = 1
    # dp[i][k] = dp[i-1][k-1] + dp[i-1][k] + dp[i-1][k+1]
    for i in range(1, len(A)):
        if A[i] == 0:
            for k in range(1, limit + 1):
                dp[(i, k)] = dp.get((i - 1, k - 1), 0) + dp.get((i - 1, k), 0) + dp.get((i - 1, k + 1), 0)
                dp[(i, k)] %= mod
        else:
            dp[(i, A[i])] = dp.get((i - 1, A[i] - 1), 0) + dp.get((i - 1, A[i]), 0) + dp.get((i - 1, A[i] + 1), 0)
            dp[(i, A[i])] %= mod
    res = 0
    for k in range(1, limit + 1):
        res += dp.get((n - 1, k), 0)
        res %= mod
    print(res)
