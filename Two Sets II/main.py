"""
Your task is to count the number of ways numbers 1,2,…,n can be divided into two sets of equal sum.

For example, if n=7, there are four solutions:
{1,3,4,6} and {2,5,7}
{1,2,5,6} and {3,4,7}
{1,2,4,7} and {3,5,6}
{1,6,7} and {2,3,4,5}
Input

The only input line contains an integer n.

Output

Print the answer modulo 109+7.

Constraints
1≤n≤500
Example

Input:
7

Output:
4
"""

if __name__ == '__main__':
    n = int(input())
    total = (n * (n + 1)) // 2

    if total % 2 != 0:
        print(0)
    else:
        target = total >> 1
        mod = 10 ** 9 + 7
        dp = [0] * (target + 1)
        dp[0] = 1
        for coin in range(1, n + 1):
            for w in range(target, coin - 1, -1):
                dp[w] = dp[w] + dp[w - coin]
        res = dp[target]//2
        print(res % mod)
