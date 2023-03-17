"""
You have n coins with certain values. Your task is to find all money sums you can create using these coins.

Input

The first input line has an integer n: the number of coins.

The next line has n integers x1,x2,…,xn: the values of the coins.

Output

First print an integer k: the number of distinct money sums. After this, print all possible sums in increasing order.

Constraints
1≤n≤100
1≤xi≤1000
Example

Input:
4
4 2 5 2

Output:
9
2 4 5 6 7 8 9 11 13
"""

if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().split()))
    total = sum(A)
    dp = [False] * (total + 1)
    dp[0] = True
    for coin in A:
        for w in range(total, coin - 1, -1):
            dp[w] = dp[w] or dp[w - coin]
    res = [w for w in range(1, total + 1) if dp[w]]
    print(len(res))
    print(" ".join(map(str, sorted(res))))
